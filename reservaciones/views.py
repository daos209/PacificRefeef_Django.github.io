# reservaciones/views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Reservation
from .forms import ReservationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Verifica si el usuario es administrador
def admin_check(user):
    return user.is_superuser

# Vista de registro de usuario
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'reservaciones/registro.html', {'form': form})

# Crear reserva (con manejo de errores)
@login_required
def make_reservation(request):
    room_type = request.GET.get('roomType')
    room_number = request.GET.get('roomNumber')
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_success')
        else:
            # Manejo de errores de formulario
            return render(request, 'reservaciones/make_reservation.html', {'form': form, 'room_type': room_type, 'room_number': room_number})
    else:
        form = ReservationForm(initial={'room_type': room_type, 'room_number': room_number})
    return render(request, 'reservaciones/make_reservation.html', {'form': form, 'room_type': room_type, 'room_number': room_number})

# Vista de éxito de reserva (opcional: mostrar detalles)
def reservation_success(request):
    # Puedes mostrar detalles de la reserva creada aquí
    return render(request, 'reservaciones/success.html')

# Editar reserva (con manejo de errores)
@user_passes_test(admin_check)
def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
        else:
            # Manejo de errores de formulario
            return render(request, 'reservaciones/edit_reservation.html', {'form': form})
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservaciones/edit_reservation.html', {'form': form})

# Panel de administración (añade filtrado o paginación como mejora)
@user_passes_test(admin_check)
def admin_dashboard(request):
    reservations = Reservation.objects.all()  # Recupera todas las reservas
    # Puedes filtrar o paginar las reservas aquí como mejora
    return render(request, 'reservaciones/admin_dashboard.html', {'reservations': reservations})