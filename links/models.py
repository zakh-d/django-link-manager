import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Collection(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)
    holder = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="my_collections")

    def get_absolute_url(self):
        return reverse('collection_detail', args=[self.id])


class Link(models.Model):

    name = models.CharField(max_length=255, blank=True)
    url = models.URLField()
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="links")

    def __str__(self):
        if self.name:
            return self.name
        return self.url


class Subscription(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="my_subscriptions")
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
