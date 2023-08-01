from rest_framework import serializers
from .models import Time, Order # Coupe

# class CoupeSer(serializers.ModelSerializer):
#   class Meta:
#     model = Coupe
#     fields = '__all__'

class TimeSer(serializers.ModelSerializer):
  class Meta:
    model = Time
    fields = '__all__'

class OrderSer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = '__all__'
