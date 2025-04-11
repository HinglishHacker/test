from django.urls import path
from .views import register_view, login_view, logout_view
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('allauth.urls')),  # добавь все URL для allauth
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
