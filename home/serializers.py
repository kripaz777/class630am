from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item
# Serializers define the API representation.
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title','price','discounted_price','description','category','image','label','status']