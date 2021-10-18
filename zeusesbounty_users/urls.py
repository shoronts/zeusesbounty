from django.urls import path
from .views import ZeusesBountyUsers

urlpatterns = [
    path('', ZeusesBountyUsers.login, name='login'),
    path('register/', ZeusesBountyUsers.register, name='register'),
]
