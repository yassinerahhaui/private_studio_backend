from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order, Time # , Coupe
from .serializers import OrderSer, TimeSer # , CoupeSer
from rest_framework import status
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import json

@api_view(['GET','POST'])
def create_order(request):
  if request.method == 'GET':
    obj = Order.objects.all()
    serializer = OrderSer(obj,many=True)
    return Response(serializer.data)
  
  if request.method == 'POST':
    serializer = OrderSer(data=request.data)
    if serializer.is_valid():
      name = request.data['name']
      email = request.data['email']
      phone = request.data['phone']
      time = request.data['time']
      coupe = request.data['coupe'].split(',')

      # send admin email
      html_content = render_to_string('admin_email.html', {
        'name':name,
        'email':email,
        'phone':phone,
        'time': time,
        'coupe': coupe
      })
      subject, from_email, to = "Hi Saîd New Service", "service.darkfade@gmail.com", "yassinerahhaoui12@gmail.com"
      text_content = f''
      msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
      msg.attach_alternative(html_content, "text/html")
      msg.send()

      # send client email
      html_content_client = render_to_string('client_email.html',{
        'name':name,
        'time': time,
        'coupe': coupe
      })
      subject2, from_email2, to2 = f'Hi {name} see you in PRIVATE_STUDIO', "service.darkfade@gmail.com", email
      text_content2 = f''
      msg2 = EmailMultiAlternatives(subject2, text_content2, from_email2, [to2])
      msg2.attach_alternative(html_content_client, "text/html")
      msg2.send()

      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
