from __future__ import absolute_import, unicode_literals
from akv.celery import app
from reservation.models import Reservation
from django.core.mail import send_mail
from time import sleep
from celery import shared_task


@app.task
def set_reservation_as_inactive(reservation_id):
    """
    This celery task sets the 'status' flag of the reservation object 
    to 2 in the database after the reservation end time has elapsed.
    """

    reservation = Reservation.objects.get(pk=reservation_id)
    if reservation.status == 3:
        reservation.status = 6
        reservation.save()


@app.task
def set_reservation_as_inactive_after_approve(reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    if reservation.status == 1:
        reservation.status = 6
        reservation.save()


@app.task
def set_reservation_as_inactive_after_request(reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    if reservation.status == 0:
        reservation.status = 6
        reservation.save()


@app.task
def send_reservation_notification(reservation_id):
    """
    This celery task sets the 'status' flag of the reservation object 
    to 2 in the database after the reservation end time has elapsed.
    """
    reservation = Reservation.objects.get(pk=reservation_id)
    reservation.status = 2
    reservation.save()


@app.task
def send_email_task(house, guest, owner, owner_email, reservation_id):
    send_mail('Новая бронь на AKV',
              f'Здравствуйте, {owner}. Ваш дом {house} забронировал пользователь {guest}!',
              'webmaster@localhost',
              [owner_email],
              fail_silently=False)
    return None
