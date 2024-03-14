from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    category_description = models.TextField(blank=True, null=True)
    category_created_at = models.DateTimeField(auto_now_add=True)
    category_updated_at = models.DateTimeField(auto_now=True)
    category_icon = models.ImageField(upload_to='categories/icons/', blank=True, null=True)

    def __str__(self):
        return self.category_name

