from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .helpers import send_otp_to_phone
from .models import User

# Create your views here.

@api_view(['POST'])
def send_otp(request):
    data = request.data

    if data.get('phone_number') is None:
        return  Response(
            {
                'status' : 400,
                'message' : 'phone_number is Required'
            }
        )
    
    if data.get('password') is None:
        return  Response(
            {
                'status' : 400,
                'message' : 'password is Required'
            }
        )

    user = User.objects.create(

        phone_number = data.get('phone_number'),
        otp = send_otp_to_phone(data.get('phone_number'))

    )

    user.set_password = data.get('set_password')

    user.save()

    return Response(
        {
            'status' : 200,
            'message' : 'OTP Sent'
        }
    )