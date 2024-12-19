from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class PotentialUser(models.Model):
    email = models.EmailField(primary_key=True, unique=False)
    os = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    tier = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(4)])

    def __str__(self):
        return self.email

    @classmethod
    def create(cls, email,os,tier):
        if cls.objects.filter(email=email).exists():
            raise ValueError("Email already exists")
        return cls(email=email, os=os, tier=tier)