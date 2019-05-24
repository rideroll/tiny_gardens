from django.db import models
from django.core.validators import MinValueValidator

from accounts.models import ProfileUser


class Theme(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return f'{self.name}\n {self.description}'


class Elements(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return f'{self.name}\n {self.description}'


class Jewellery(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=200)
    elements = models.ManyToManyField('Elements', blank=True)
    price = models.PositiveIntegerField(validators=[MinValueValidator(5)])
    image_url = models.URLField()
    description = models.TextField()
    color = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.description}'