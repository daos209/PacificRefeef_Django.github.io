from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    ROOM_TYPES = (
        ('estandar', 'Habitación Estándar'),
        ('deluxe', 'Habitación Deluxe'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona reserva con usuario
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    floor = models.IntegerField()
    room_number = models.CharField(max_length=3)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"Reserva de {self.user.username} - {self.room_type} - Piso {self.floor} - Habitación {self.room_number}"
