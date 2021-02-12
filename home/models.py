from django.db import models
from django.urls import reverse
LABEL = (('new','new'),('hot','hot'),('','default'))
STATUS = (('active','active'),('','default'))
STOCK = (('in','IN Stock'),('out','Out of stock'))
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 300)
    slug = models.CharField(max_length = 300)
    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length = 300)
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    image = models.TextField(blank = True)
    description = models.TextField(blank = True)
    label = models.CharField(choices = LABEL,max_length = 100,blank = True)
    slug = models.CharField(max_length= 200)
    status = models.CharField(max_length = 300,choices = STATUS,blank = True)
    stock = models.CharField(max_length = 300,choices = STOCK)

    def __str__(self):
        return self.title

    def get_item_url(self):
        return reverse("home:product",kwargs = {'slug':self.slug})

class Slider(models.Model):
    name = models.CharField(max_length = 500)
    image = models.TextField()
    text = models.TextField()
    rank = models.IntegerField()
    status = models.CharField(max_length = 200,choices = STATUS,blank = True)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length = 400)
    image = models.TextField()
    rank = models.IntegerField()
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length = 300)
    subject =models.TextField()
    email = models.CharField(max_length = 200,blank = True)
    message = models.TextField()

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length = 400)
    image = models.TextField()
    rank = models.IntegerField()

    def __str__(self):
        return self.name

