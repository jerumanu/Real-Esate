from django.db import models
from django.forms import CharField, ImageField, IntegerField




class Detail(models.Model):
    title=CharField(max_length=50)
    detail_descrip=CharField(max_length=50)
    image= ImageField()
    bedRooms= IntegerField()
    bathRoom=ImageField()


    def __str__(self):
        return self.title

class post(models.Model):
    name=CharField(max_length=50)
    phone_no= IntegerField()
