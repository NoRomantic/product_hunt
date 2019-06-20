
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='注册页面'),
]
