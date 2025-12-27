import uuid
import qrcode
from io import BytesIO
from django.db import models
from django.contrib.auth.models import User
from django.core.files.base import ContentFile

from django.db import models
import uuid


class Item(models.Model):
    # Existing fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='items/')
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # --- NEW COLUMNS ---
    CATEGORY_CHOICES = [
        ('ELECTRONICS', 'Electronics'),
        ('FURNITURE', 'Furniture'),
        ('DOCUMENTS', 'Important Documents'),
        ('VEHICLES', 'Vehicles'),
        ('OTHER', 'Other'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    serial_number = models.CharField(max_length=100, blank=True, null=True, help_text="Manufacturer serial number")
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    warranty_expiry = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True, help_text="Physical storage location")

    def __str__(self):
        return self.name

    # ... keep your existing save() method for QR generation here ...