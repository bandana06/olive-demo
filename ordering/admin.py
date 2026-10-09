from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, MenuItem, Table, Order, PromoOffer

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(MenuItem)
class MenuItemAdmin(ModelAdmin):
    list_display = ['name', 'category', 'dietary_preference', 'price', 'is_available', 'is_featured']
    list_filter = ['category', 'dietary_preference', 'is_available', 'is_featured']
    list_editable = ['price', 'is_available', 'is_featured', 'dietary_preference']

@admin.register(Table)
class TableAdmin(ModelAdmin):
    list_display = ['number', 'capacity', 'is_booked']
    list_editable = ['is_booked']

@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ['id', 'customer_name', 'phone_number', 'table', 'total_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    list_editable = ['status']
    
@admin.register(PromoOffer)
class PromoOfferAdmin(ModelAdmin):
    list_display = ['name', 'is_active', 'probability_weight']
    list_editable = ['is_active', 'probability_weight']
    list_filter = ['is_active']
