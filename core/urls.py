from django.urls import path
from . import views
from bookings.views import BookingCreateView  # Import qilish


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('rooms/', views.RoomListView.as_view(), name='rooms'),
    path('api/room/<int:pk>/', views.room_detail_api, name='room_detail_api'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('staff/', views.StaffView.as_view(), name='staff'),
    path('services/', views.ServicesView.as_view(), name='services'),
    
    # Contact sahifasi — BookingCreateView ni ishlatamiz
    path('contact/', BookingCreateView.as_view(), name='contact'),
]