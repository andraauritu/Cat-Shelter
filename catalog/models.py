from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone



# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=100)
    ADOPTION_STATUS = (
        ('available', 'Available'),
        ('adopted', 'Adopted'),
        ('pending', 'Adoption Pending'),
    )
    adoption_status = models.CharField(
        max_length=10,
        choices=ADOPTION_STATUS,
        default='available',
    )
    picture = models.ImageField(upload_to='cats/')
    bio = models.TextField()
    arrived_date = models.DateField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = (
        ('staff', 'Staff'),
        ('adopter', 'Adopter'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='adopter')

    def __str__(self):
        return self.user.username

class Adoption(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    adopter = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    adoption_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.adopter.user.username} adopted {self.cat.name}"


class MedicalRecord(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='medical_records')
    procedure = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"{self.cat.name} - {self.procedure} on {self.date}"

class Visit(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='visits')
    visitor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='scheduled_visits')
    full_name = models.CharField(max_length=255)
    visit_date = models.DateField()
    visit_time = models.TimeField(default=timezone.now)  # Add this line for visit time

    def __str__(self):
        return f"Visit for {self.cat.name} by {self.full_name} on {self.visit_date} at {self.visit_time}"
