from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('send_email/', views.send_email, name='send_email'),  # Define the URL pattern for sending email
]
