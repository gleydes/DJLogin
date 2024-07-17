from django.urls import path
from .views import login_view, register_view, welcome_view, logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('welcome/', welcome_view, name='welcome'),
    path('logout/', logout_view, name='logout'),
]