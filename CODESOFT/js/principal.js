// Simulación de acciones
function agregarEquipo() {
    alert("Función para agregar equipo.");
}

function editarEquipo() {
    alert("Función para editar equipo.");
}

function eliminarEquipo() {
    alert("Función para eliminar equipo.");
}

function generarReporte() {
    alert("Función para generar reporte.");
}

// Filtro en la tabla
document.getElementById('search').addEventListener('keyup', function() {
    let input = this.value.toLowerCase();
    let rows = document.querySelectorAll('#inventory-table tbody tr');
    
    rows.forEach(row => {
        const cells = row.querySelectorAll('td');
        const rowText = Array.from(cells).map(cell => cell.textContent.toLowerCase()).join(' ');
        
        if (rowText.includes(input)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
});

// Verificar si el usuario está logueado
window.onload = function() {
    const user = JSON.parse(localStorage.getItem('user'));
    
    if (!user) {
        // Si no hay sesión, redirigir al login
        window.location.href = 'login.html';
    } else {
        // Mostrar el nombre del usuario en el dashboard
        document.getElementById('user-info').textContent = `Bienvenido, ${user.username}`;
    }
};

// Función para cerrar sesión
function logout() {
    localStorage.removeItem('user');  // Eliminar la sesión
    window.location.href = 'login.html';  // Redirigir al login
}

