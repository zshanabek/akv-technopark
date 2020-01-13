from account.models import User
from django.db.models import (
    Model, TextField, DateTimeField, ForeignKey, CASCADE)
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def deserialize_user(user):
    return {
        'id': user.id, 'email': user.email,
        'first_name': user.first_name, 'last_name': user.last_name
    }


class TrackableDateModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MessageModel(TrackableDateModel):
    user = ForeignKey(User, on_delete=CASCADE, verbose_name='user',
                      related_name='from_user', db_index=True)
    recipient = ForeignKey(User, on_delete=CASCADE,
                           verbose_name='recipient', related_name='to_user', db_index=True)
    body = TextField(max_length=2000)

    def __str__(self):
        return '{} {}'.format(self.id, self.body)

    def to_json(self):
        return {'text': self.body, 'id': self.id, 'created_at': str(self.created_at), 'updated_at': str(self.updated_at)}

    def characters(self):
        return len(self.body)

    def notify_ws_clients(self):
        """
        Inform client there is a new message.
        """
        notification = {
            'type': 'recieve_group_message',
            'user': deserialize_user(self.user),
            'message': self.to_json()
        }

        channel_layer = get_channel_layer()
        print("sender: {}; {}; {}".format(self.user.id,
                                          self.user.email, self.user.full_name()))
        print("receive {}; {}; {}".format(self.recipient.id,
                                          self.recipient.email, self.recipient.full_name()))

        async_to_sync(channel_layer.group_send)(
            "{}".format(self.user.id), notification)
        async_to_sync(channel_layer.group_send)(
            "{}".format(self.recipient.id), notification)

    def save(self, *args, **kwargs):
        """
        Trims white spaces, saves the message and notifies the recipient via WS
        if the message is new.
        """
        new = self.id
        self.body = self.body.strip()  # Trimming whitespaces from the body
        super(MessageModel, self).save(*args, **kwargs)
        if new is None:
            self.notify_ws_clients()

    # Meta
    class Meta:
        app_label = 'core'
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ('-created_at',)