from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.mail import send_mail
from django.template.loader import render_to_string
import os


@api_view(['GET', 'POST'])
def welcome_email(request):
    if request.method == 'GET':
        try:
            email = Token.objects.get(key=request.GET['key']).user
        except:
            return Response("invalid input", status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            email = request.data['email']
        except:
            return Response("invalid input", status=status.HTTP_400_BAD_REQUEST)
    subject = "Welcome to FindMyWorks"
    message = "Welcome to FindMyWorks."
    html_message = render_to_string('welcome_email.html')
    email_from = os.getenv("EMAIL_HOST_USER")
    recipient_list = [email]
    try:
        send_mail(subject, message, email_from, recipient_list, html_message=html_message)
        return Response({"message": "sent!!"}, status=status.HTTP_200_OK)
    except:
        return Response("email sending failed", status=status.HTTP_400_BAD_REQUEST)
