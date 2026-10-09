from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import SiteConfiguration, InstagramPost

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(ModelAdmin):
    pass

@admin.register(InstagramPost)
class InstagramPostAdmin(ModelAdmin):
    list_display = ('url', 'is_active', 'order', 'created_at')
    list_editable = ('is_active', 'order')
    search_fields = ('url',)
    list_filter = ('is_active',)

