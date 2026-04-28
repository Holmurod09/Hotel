from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.BookingCreateView.as_view(), name='booking_create'),
    path('api/create/', views.booking_api_create, name='booking_api_create'),  # AJAX uchun
]