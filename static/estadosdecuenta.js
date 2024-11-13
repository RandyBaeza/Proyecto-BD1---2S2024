document.addEventListener('DOMContentLoaded', function () {
    // Verifica si hay un mensaje de error
    const errorMessage = document.getElementById('errorMessage');
    if (errorMessage) {
        alert(errorMessage.value);  // Muestra la alerta con el mensaje de error
        window.location.href = '/';  // Redirige al index.html
    }
    const idTF = document.getElementById('idTF').value;
    const userId = document.getElementById('userId').value;
    const TipoTC = document.getElementById('TipoTC').value;
    //const buscar = document.getElementById('buscar').value;
    console.log(`Fetching empleados for userId: ${userId}, ${idTF}, ${TipoTC} `);


    fetch(`/listar_EC/${userId}/${idTF}/${TipoTC}`)
        .then(response => response.json())
        .then(empleados => {
            const tbody = document.getElementById('ecTableBody');
            tbody.innerHTML = '';  // Limpiar la tabla antes de agregar nuevos datos

            empleados.forEach(empleado => {
                const row = document.createElement('tr');

                row.innerHTML = `
                    <td>${empleado.Fecha}</td>
                    <td>${empleado.Saldo}</td>
                    <td>${empleado.InteresCorriente}</td>
                    <td>${empleado.InteresMoratorio}</td>
                    <td>${empleado.OperacionesATM}</td>
                    <td>${empleado.OperacionesVentanilla}</td>
                    <td>
                        <button onclick="window.location.href='/movimientos/${empleado.Id}/${'TCM'}'">Movimientos</button>
                    </td>
                `;
                tbody.appendChild(row);
            });
        })
        .catch(error => {
            //alert('Error fetching employee list.');
            console.error('Error fetching employee list:', error);
        });
});


