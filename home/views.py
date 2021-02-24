from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.
from .models import *

class Baseview(View):
    view = {}


class HomeView(Baseview):
    def get(self,request):
        self.view['categories'] =  Category.objects.all()
        self.view['sliders'] = Slider.objects.all()
        self.view['items'] = Item.objects.all()
        self.view['new'] = Item.objects.filter(label = 'new')
        self.view['hot'] = Item.objects.filter(label='hot')
        self.view['brands'] = Brand.objects.all()
        self.view['rank_one'] = Ad.objects.filter(rank = 1)
        self.view['rank_two'] = Ad.objects.filter(rank=2)
        self.view['rank_three'] = Ad.objects.filter(rank=3)
        self.view['rank_four'] = Ad.objects.filter(rank=4)
        self.view['rank_five'] = Ad.objects.filter(rank=5)
        self.view['rank_six'] = Ad.objects.filter(rank=6)
        self.view['rank_seven'] = Ad.objects.filter(rank=7)
        self.view['rank_eight'] = Ad.objects.filter(rank=8)
        return render(request,'index.html',self.view)

class ItemDetailView(Baseview):
    def get(self,request,slug):
        self.view['detail_product'] = Item.objects.filter(slug=slug)
        self.view['philips_brand'] = Brand.objects.filter(name = "philips").count()


        return render(request,'product-detail.html',self.view)

class CategoryListView(Baseview):
    def get(self,request,slug):
        self.view['category_product'] = Item.objects.filter(category = slug)
        return render(request,'product-list.html',self.view)

class SearchView(Baseview):
    def get(self, request):
        if request.method == 'GET':
            search = request.GET['query']
            self.view['search_product'] = Item.objects.filter(
                title__icontains = search
            )
            self.view['searched_for'] = search
        else:
            return redirect('/')
        return render(request, 'search.html', self.view)


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request,'This username already exists')
                return redirect("home:account")
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'This email already exists')
                return redirect("home:account")
            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password =password,
                    first_name = first_name,
                    last_name = last_name
                )
                user.save()
                messages.success(request, 'Successfully signedup.You may login now.')
                return redirect("home:account")
        else:
            messages.error(request, 'password does not match')
            return redirect("home:account")

    return render(request,'login.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.error(request,"Username and password do not match.")
            return redirect("home:account")
    return redirect("home:account")

class ViewCart(Baseview):
    def get(self,request):
        self.view['carts'] = Cart.objects.filter(user = request.user.username)
        return render(request,'cart.html',self.view)

def cart(request,slug):
    if Cart.objects.filter(slug = slug,user = request.user.username).exists():
        quantity = Cart.objects.get(slug = slug,user = request.user.username).quantity
        quantity = quantity +1
        Cart.objects.filter(slug = slug,user = request.user.username).update(quantity = quantity)

    else:
        username = request.user.username
        data = Cart.objects.create(
            user = username,
            slug = slug,
            item = Item.objects.filter(slug = slug)[0]

        )
        data.save()

    return redirect('home:viewcart')

def deletecart(request,slug):
    if Cart.objects.filter(slug = slug,user = request.user.username).exists():
        Cart.objects.filter(slug=slug, user=request.user.username).delete()
        messages.success(request, "The product is deleted.")
    return redirect('home:viewcart')

