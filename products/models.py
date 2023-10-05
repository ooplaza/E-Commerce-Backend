from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    class ProductStatusChoices(models.TextChoices):
        draft = "draft", "Draft"
        published = "published", "Published"

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    price = models.IntegerField(default=0)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=ProductStatusChoices.choices)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["-published"]
