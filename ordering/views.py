from django.shortcuts import render
from .models import Category, MenuItem

def menu(request):
    categories = Category.objects.prefetch_related('items').all()
    # Also fetch all available items for a "All" view if needed
    menu_items = MenuItem.objects.filter(is_available=True)
    return render(request, 'ordering/menu.html', {
        'categories': categories,
        'menu_items': menu_items
    })

def cart(request):
    return render(request, 'ordering/cart.html')

def checkout(request):
    return render(request, 'ordering/checkout.html')
