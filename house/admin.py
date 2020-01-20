from django.contrib import admin
from house import models as house_models


admin.site.register(house_models.House)
admin.site.register(house_models.Room)
admin.site.register(house_models.HouseRoom)
admin.site.register(house_models.Photo)
admin.site.register(house_models.Accommodation)
admin.site.register(house_models.HouseType)
admin.site.register(house_models.NearBuilding)
admin.site.register(house_models.Rule)
admin.site.register(house_models.Favourite)
admin.site.register(house_models.BlockedDateInterval)
