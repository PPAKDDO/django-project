from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# URLCOnf
urlpatterns = [
    path('page/', views.test_page),
    path('main/', views.main),
    path('main/json/', views.json, name='json'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
