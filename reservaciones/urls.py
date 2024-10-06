from django.urls import path
from . import views

urlpatterns = [
    path('make_reservation/', views.make_reservation, name='make_reservation'),
    path('reservation_success/', views.reservation_success, name='reservation_success'),
    path('edit_reservation/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('delete_reservation/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
]
