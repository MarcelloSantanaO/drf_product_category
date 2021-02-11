from django.db import models
from django.db.models import CharField, TextField, FloatField, ManyToManyField


class Category(models.Model):
    name = CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = CharField(max_length=50, null=False)
    description = TextField(max_length=255, null=True)
    price = FloatField(null=False)
    categories = ManyToManyField(Category)

    def __str__(self):
        return f"name: {self.name}, description: {self.description}," \
               f" price: {self.price}"
