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

    def get_category_url(self):
        return reverse("home:category",kwargs = {'slug':self.id})

class Item(models.Model):
    title = models.CharField(max_length = 300)
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    image = models.ImageField(upload_to = 'media')
    description = models.TextField(blank = True)
    label = models.CharField(choices = LABEL,max_length = 100,blank = True)
    slug = models.CharField(max_length= 200,unique = True)
    status = models.CharField(max_length = 300,choices = STATUS,blank = True)
    stock = models.CharField(max_length = 300,choices = STOCK)
    category =models.ForeignKey(Category,on_delete = models.CASCADE,null = True)

    def __str__(self):
        return self.title

    def get_item_url(self):
        return reverse("home:product",kwargs = {'slug':self.slug})

    def get_cart_url(self):
        return reverse("home:add-to-cart",kwargs = {'slug':self.slug})


class Slider(models.Model):
    name = models.CharField(max_length = 500)
    image = models.ImageField(upload_to = 'media')
    text = models.TextField()
    rank = models.IntegerField()
    status = models.CharField(max_length = 200,choices = STATUS,blank = True)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length = 400)
    image = models.ImageField(upload_to='media')
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
    image = models.ImageField(upload_to = 'media')
    rank = models.IntegerField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    item = models.ForeignKey(Item,on_delete = models.CASCADE,null = True)
    slug = models.CharField(max_length = 200,blank = True)
    quantity = models.IntegerField(default = 1)
    user = models.CharField(max_length = 200)
    date = models.DateTimeField(null = True)
    total = models.IntegerField(default = 0)
    def __str__(self):
        return self.user

    def delete_cart_url(self):
        return reverse("home:delete-cart", kwargs={'slug': self.slug})

