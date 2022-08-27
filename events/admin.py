from django.contrib import admin
import events.models as models

# Register your models here.
admin.site.register(models.EventType)
admin.site.register(models.Tag)
admin.site.register(models.Event)
