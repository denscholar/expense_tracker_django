from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Expense(models.Model):
    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.username + " " + "Expenses"

    class Meta:
        ordering = ["-date"]


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Category"

    def __str__(self):
        return self.name
