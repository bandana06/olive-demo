from django.shortcuts import render
from ordering.models import PromoOffer, MenuItem
from pages.models import InstagramPost

def home(request):
    # Fetch 4 random available menu items
    featured_items = MenuItem.objects.filter(is_available=True).order_by('?')[:4]
    # Fetch all active Instagram posts
    instagram_posts = InstagramPost.objects.filter(is_active=True)
    return render(request, 'pages/home.html', {
        'featured_items': featured_items,
        'instagram_posts': instagram_posts
    })

def about(request):
    return render(request, 'pages/about.html')

def team(request):
    return render(request, 'pages/team.html')

def blog(request):
    return render(request, 'pages/blog.html')

def contact(request):
    return render(request, 'pages/contact.html')

def policy(request):
    return render(request, 'pages/policy.html')

def complain(request):
    return render(request, 'pages/complain.html')

def wheel(request):
    # Get active offers, we need exactly 6 for the wheel to look right, 
    # but we will handle less than 6 on the frontend by showing "coming soon"
    active_offers = PromoOffer.objects.filter(is_active=True)
    return render(request, 'pages/wheel.html', {'offers': active_offers})
