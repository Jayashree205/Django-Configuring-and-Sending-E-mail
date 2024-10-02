# ex4/urls.py
from django.contrib import admin
from django.urls import path
from emailapp import views  # Import your views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('admin/', admin.site.urls),
    path('emailapp/send_email/', views.send_email, name='send_email'),  # Email sending URL
]
