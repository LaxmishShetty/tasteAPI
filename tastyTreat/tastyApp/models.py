from django.db import models

# Create your models here.


class Taste(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=40)
    tasteOfDish = models.ForeignKey(Taste, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PersonName(models.Model):
    name = models.CharField(max_length=50)
    heCanEat = models.ManyToManyField(Dish)

    def __str__(self):
        return self.name

