from django.urls import path
from .views import *

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(),name = 'index'),
    path('product/<slug>', ItemDetailView.as_view(),name = 'product'),
    path('category/<slug>', CategoryListView.as_view(),name = 'category'),
    path('search', SearchView.as_view(),name = 'search'),
    path('account', signup,name = 'account'),
    path('login',login,name='login'),
    path('viewcart',ViewCart.as_view(),name = 'viewcart'),
    path('add-to-cart/<slug>',cart,name = 'add-to-cart'),
    path('delete-cart/<slug>', deletecart, name='delete-cart'),
    path('delete-single-cart/<slug>',remove_single_item, name='delete-single-cart'),
    path('contact',contact, name='contact'),

]
