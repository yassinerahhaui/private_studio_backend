from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order, Time, Coupe
from .serializers import OrderSer, TimeSer, CoupeSer
from rest_framework import status

@api_view(['GET','POST'])
def create_order(request):
  if request.method == 'GET':
    obj = Order.objects.all()
    serializer = OrderSer(obj,many=True)
    return Response(serializer.data)
  
  if request.method == 'POST':
    serializer = OrderSer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
