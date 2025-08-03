from django.contrib import admin
from app.models import *
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Farm)
admin.site.register(Irrigation)
admin.site.register(Fertilizer)
admin.site.register(PestControl)
admin.site.register(Notification)