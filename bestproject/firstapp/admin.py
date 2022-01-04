from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Webpages)
admin.site.register(models.Topic)

admin.site.register(models.accessrecord)


admin.site.register(models.Users)

admin.site.register(models.Userprofile)