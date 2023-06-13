from django.contrib import admin

from .models import Activity, Item , Place

admin.site.register(Activity)
admin.site.register(Place)
admin.site.register(Item)
