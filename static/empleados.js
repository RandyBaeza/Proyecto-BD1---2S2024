document.addEventListener('DOMContentLoaded', function() {
    // Verifica si hay un mensaje de error
    const errorMessage = document.getElementById('errorMessage');
    if (errorMessage) {
        alert(errorMessage.value);  // Muestra la alerta con el mensaje de error
        window.location.href = '/';  // Redirige al index.html
    }
    const userId = document.getElementById('userId').value;
    const admin = document.getElementById('admin').value;
    //const buscar = document.getElementById('buscar').value;
    console.log(`Fetching empleados for userId: ${userId}`);
    console.log(`Fetching empleados for admin: ${admin}`);


    if (admin === '0') {
        fetch(`/listar_empleados/${admin}`)
            .then(response => response.json())
            .then(empleados => {
                const tbody = document.getElementById('employeeTableBody');
                tbody.innerHTML = '';  // Limpiar la tabla antes de agregar nuevos datos

                empleados.forEach(empleado => {

                    const row = document.createElement('tr');

                    let url = '';
                    if (empleado.TipoTC === 'TCM') {
                        url = `/consultar/${userId}/${empleado.Id}/${empleado.TipoTC}`;
                    } else {
                        url = `/consultarsub/${userId}/${empleado.Id}/${empleado.TipoTC}`; 
                    }

                    row.innerHTML = `
                        <td>${empleado.NumeroTarjeta}</td>
                        <td>${empleado.Activo}</td>
                        <td>${empleado.TipoTC}</td>
                        <td>${empleado.FechaVencimiento}</td>
                        <td>
                            <button onclick="window.location.href='${url}'">Estados de Cuenta</button>
                        </td>
                    `;
                    tbody.appendChild(row);

                });
            })
            .catch(error => {
                //alert('Error fetching employee list.');
                console.error('Error fetching employee list:', error);
            });
    }
    else {
        fetch(`/listar_empleados/${userId}`)
            .then(response => response.json())
            .then(empleados => {
                const tbody = document.getElementById('employeeTableBody');
                tbody.innerHTML = '';  // Limpiar la tabla antes de agregar nuevos datos

                empleados.forEach(empleado => {

                    const row = document.createElement('tr');

                    let url = '';
                    if (empleado.TipoTC === 'TCM') {
                        url = `/consultar/${userId}/${empleado.Id}/${empleado.TipoTC}`;
                    } else {
                        url = `/consultarsub/${userId}/${empleado.Id}/${empleado.TipoTC}`;
                    }

                    row.innerHTML = `
                        <td>${empleado.NumeroTarjeta}</td>
                        <td>${empleado.Activo}</td>
                        <td>${empleado.TipoTC}</td>
                        <td>${empleado.FechaVencimiento}</td>
                        <td>
                            <button onclick="window.location.href='${url}'">Estados de Cuenta</button>
                        </td>
                    `;
                    tbody.appendChild(row);

                });
            })
            .catch(error => {
                //alert('Error fetching employee list.');
                console.error('Error fetching employee list:', error);
            });
    }
});


