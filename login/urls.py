# accounts/urls.py
from django.urls import path
from .views import login_view
from django.contrib import admin

urlpatterns = [
    path('login_next/', login_view),
    path('admin/', admin.site.urls),
]
