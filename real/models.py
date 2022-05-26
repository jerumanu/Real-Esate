from django.db import models






class Detail(models.Model):
    title=models.CharField(max_length=50)
    detail_descripe=models.CharField(max_length=50)
    photos= models.ImageField()
    bedroom_no=  models.IntegerField()
    bathroom_no=models.IntegerField()


    def __str__(self):
        return self.title

class Post(models.Model):
    name=models.CharField(max_length=50)
    phone_no= models.IntegerField()
    email=models.EmailField()


class Estate(models.Model):
    locations= models.CharField(max_length=20)
    price=models.IntegerField()
    image=models.ImageField()

class Amentitis(models.Model):
    security=models.CharField(max_length=10)
    parking=models.CharField(max_length=10) 
    power=models.CharField(max_length=10)
    pool=models.CharField(max_length=10)
    water=models.CharField(max_length=10) 

