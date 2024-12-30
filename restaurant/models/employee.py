from django.db import models
from custom_auth.models import Role
import uuid

class RestaurantEmployee(models.Model):
    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70, unique=True)
    country_code = models.CharField(max_length=3, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.RESTAURANT_STAFF)
    unit = models.ForeignKey(
        'restaurant.RestaurantUnit',
        on_delete=models.CASCADE,
        related_name='employees',
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["first_name", "last_name", "email"], name="restaurant_employee_idx")
        ]
        db_table = 'restaurant_employee'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"