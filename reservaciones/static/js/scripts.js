document.addEventListener('DOMContentLoaded', function() {
    const floorSelect = document.getElementById('floor');
    const roomSelect = document.getElementById('roomNumber');
    const roomTypeSelect = document.getElementById('roomType');
    
    // Función para generar números de habitación según el tipo y piso
    function generateRoomNumbers(floor, roomType) {
        let rooms = [];
    
        if (roomType === 'estandar') {
            if (floor >= 1 && floor <= 5) {
                rooms = Array.from({ length: 6 }, (_, i) => `${floor}0${i + 1}`);
            }
        } else if (roomType === 'deluxe') {
            if (floor === 6 || floor === 7) {
                rooms = Array.from({ length: 4 }, (_, i) => `${floor}0${i + 1}`);
            }
        }
    
        return rooms;
    }

    // Función para actualizar las opciones de pisos según el tipo de habitación
    function updateFloors(roomType) {
        let floors = [];
    
        if (roomType === 'estandar') {
            floors = Array.from({ length: 5 }, (_, i) => i + 1); // Pisos 1 a 5
        } else if (roomType === 'deluxe') {
            floors = [6, 7]; // Pisos 6 y 7
        }
    
        // Limpiar opciones anteriores
        floorSelect.innerHTML = '<option value="">Seleccione un Piso</option>';
    
        // Añadir nuevas opciones
        floors.forEach(function(floor) {
            const option = document.createElement('option');
            option.value = floor;
            option.textContent = 'Piso ' + floor;
            floorSelect.appendChild(option);
        });
    
        // Resetear selección de piso y habitación
        floorSelect.value = '';
        roomSelect.innerHTML = '<option value="">Seleccione una Habitación</option>';
    }

    // Función para actualizar las opciones de habitaciones
    function updateRooms(floor, roomType) {
        const rooms = generateRoomNumbers(floor, roomType);
    
        // Limpiar opciones anteriores
        roomSelect.innerHTML = '<option value="">Seleccione una Habitación</option>';
    
        // Añadir nuevas opciones
        rooms.forEach(function(room) {
            const option = document.createElement('option');
            option.value = room;
            option.textContent = 'Habitación ' + room;
            roomSelect.appendChild(option);
        });
    }

    // Actualiza pisos disponibles cuando se cambia el tipo de habitación
    roomTypeSelect.addEventListener('change', function() {
        const roomType = this.value;
        if (roomType) {
            updateFloors(roomType);
            // Resetear selección de habitación cuando se cambia el tipo de habitación
            roomSelect.innerHTML = '<option value="">Seleccione una Habitación</option>';
        }
    });
    
    floorSelect.addEventListener('change', function() {
        const floor = parseInt(this.value, 10); // Convertir a número entero
        const roomType = roomTypeSelect.value;
        if (floor && roomType) {
            updateRooms(floor, roomType);
        }
    });

    // Inicializar valores si están preseleccionados
    const initialRoomType = roomTypeSelect.value;
    const initialRoomNumber = roomSelect.value;
    if (initialRoomType) {
        updateFloors(initialRoomType);
        if (initialRoomNumber) {
            const initialFloor = parseInt(initialRoomNumber.charAt(0), 10);
            updateRooms(initialFloor, initialRoomType);
            floorSelect.value = initialFloor;
        }
    }
});