from django.contrib.auth.models import User
from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Places"

    def __str__(self):
        return self.name


class Item(models.Model):
    activity = models.ForeignKey(Activity, related_name='items', on_delete=models.CASCADE)
    places = models.ForeignKey(Place, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name
