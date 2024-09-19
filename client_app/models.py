import random

from django.db import models

from accounts.models import User
from app.models import BaseModel


class StaffUser(BaseModel):
    class RoleChoices(models.TextChoices):
        TEACHER = "Teacher"
        DEPUTY = "Deputy Principal"
        PRINCIPAL = "Principal"
        BURSAR = "Bursar"
        LIBRARIAN = "Librarian"
        OTHER = "Other"

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="staff_user", null=True, blank=True
    )
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    id_number = models.CharField(max_length=10)
    staff_number = models.CharField(max_length=8, null=True, blank=True)
    image = models.ImageField(upload_to="staff-profiles", null=True, blank=True)
    role = models.CharField(
        choices=RoleChoices.choices, default=RoleChoices.TEACHER, max_length=30
    )

    def save(self, *args, **kwargs):
        if not self.staff_number:
            self.staff_number = self.generate_staff_number()
        super().save(*args, **kwargs)

    def generate_staff_number(self):
        """
        Generate a unique 8-character numeric staff number.
        """
        while True:
            staff_number = "".join(random.choices("0123456789", k=8))
            if not StaffUser.objects.filter(staff_number=staff_number).exists():
                return staff_number
