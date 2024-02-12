from django.contrib import admin
from .models import *

from django.db.models import F, Case, When, BooleanField

admin.site.register(HotelShortIntro)
admin.site.register(FoodCategory)
admin.site.register(MenuList)


@admin.register(Contact)
class ContactAdminView(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'read']
    list_editable = ['read']
    ordering = ['read']

    def get_readonly_fields(self, request, obj=None):
        """Make the existing objects field readonly except for read field"""
        if obj is None:
            return []
        return [field.name for field in self.model._meta.fields if field.name != 'read']


@admin.register(HotelContactInfo)
class HotelContactInfo(admin.ModelAdmin):
    list_display = ['address', 'email', 'phone_number']


admin.site.register(Testimonial)
admin.site.register(BannerImage)
admin.site.register(History)
admin.site.register(VisionAndGoal)
