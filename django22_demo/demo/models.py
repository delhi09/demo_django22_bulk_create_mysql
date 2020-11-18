from django.db import models


class Example(models.Model):
    class Meta:
        db_table = "example"

    fizz = models.CharField(max_length=200)
    buzz = models.IntegerField()
    fizzbuzz = models.DateTimeField("date published")

class Food(models.Model):
    class Meta:
        db_table = "menu"
    name=models.CharField(max_length=64)
    price = models.IntegerField()
