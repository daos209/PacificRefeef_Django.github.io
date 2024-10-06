# reservaciones/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL para la página de inicio
    path('login/', views.user_login, name='login'),  # URL para el inicio de sesión
    path('select_room_type/', views.select_room_type, name='select_room_type'),  # URL para la preselección de tipo de habitación
    path('make_reservation/', views.make_reservation, name='make_reservation'),  # URL para hacer la reserva
    path('reservation_success/', views.reservation_success, name='reservation_success'),
    path('edit_reservation/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('delete_reservation/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
]