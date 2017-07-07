from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class userpro(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(u'姓名', max_length=30)

    def __str__(self):
        return self.name


class 访问量(models.Model):
    Day = models.CharField(max_length=100)
    PV = models.IntegerField()
    UV = models.IntegerField()

    def __str__(self):
        return self.Day


class 时间轴(models.Model):
    Day = models.CharField(max_length=100)
    val = models.FloatField()

    def __str__(self):
        return self.Day
