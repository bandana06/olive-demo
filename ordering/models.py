from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    DIETARY_CHOICES = [
        ('veg', 'Veg'),
        ('nonveg', 'Non-Veg'),
        ('vegan', 'Vegan')
    ]

    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    dietary_preference = models.CharField(max_length=20, choices=DIETARY_CHOICES, default='veg')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_booked = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Table {self.number} (Capacity: {self.capacity})"

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending (Needs Call)'),
        ('verified', 'Verified & Preparing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]
    
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    items_summary = models.TextField(help_text="JSON or text summary of cart items")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"

class PromoOffer(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True, help_text="Is this offer currently available on the wheel?")
    probability_weight = models.IntegerField(default=10, help_text="Higher number means higher chance of winning")
    
    def __str__(self):
        return f"{self.name} (Active: {self.is_active})"
