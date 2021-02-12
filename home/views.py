from django.shortcuts import render
from django.views.generic import View
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


        return render(request,'product-detail.html',self.view)