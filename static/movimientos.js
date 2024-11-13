document.addEventListener('DOMContentLoaded', function() {
    const IdEC = document.getElementById('idEC').value;
    //const TipoTC = document.getElementById('TipoTC').value;
    const urlSegments = window.location.href.split('/');
    const TipoTC = urlSegments[urlSegments.length - 1];
    console.log(`Fetching empleados for userId: ${IdEC}, ${TipoTC} `);


    // Obtener la lista de movimientos del empleado
    fetch(`/listar_movimientos/${IdEC}/${TipoTC}`)
        .then(response => response.json())
        .then(result => {
            const tbody = document.getElementById('movimientosTableBody');
            tbody.innerHTML = '';  // Limpiar la tabla antes de agregar nuevos datos

            // Comprobar si la respuesta es exitosa
            if (result.success) {
                // Si hay movimientos, agregar cada movimiento a la tabla
                result.movimientos.forEach(movimiento => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${movimiento.Fecha}</td>
                        <td>${movimiento.TipoMovimiento}</td>
                        <td>${movimiento.Descripcion}</td>
                        <td>${movimiento.Referencia}</td>
                        <td>${movimiento.Monto}</td>
                        <td>${movimiento.Saldo}</td>
                    `;
                    tbody.appendChild(row);
                });
            } else {
                // Si no hay movimientos, mostrar un mensaje
                alert('No hay movimientos.');
                //window.location.href = `/index/${userId}`; // Redirigir a la lista de empleados
            }
        })
        .catch(error => {
            console.error('Error fetching movimientos list:', error);
            alert('Error al obtener la lista de movimientos.');
        });
});
