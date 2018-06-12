from django.urls import path
from .views import *
    
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]