from tkinter import NO
import pyodbc

class MssqlConnection:
    def __init__(self):
        self.connection_string = (
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=mssql-181428-0.cloudclusters.net,19997;'
            'DATABASE=BD_Proyecto;'
            'UID=Randy;'
            'PWD=Randy1010'
        )

    def connect_mssql(self):
        try:
            return pyodbc.connect(self.connection_string)
        except pyodbc.Error as ex:
            print(f"Connection error: {ex}")
            raise
    
    # Listar las Tarjetas
    def listarTarjetas(self, idUsuario, buscar = ""): 
        connect = self.connect_mssql()
        cursor = connect.cursor()       
        #idUsuario = 0
        cursor.execute("EXECUTE [dbo].[ListarTarjetas] @inidUsuario=?, @OutResult=0;"
                       , (idUsuario)) 
        result = cursor.fetchall()[0][0]
        if result == 0: 
            cursor.nextset()
            empleados = cursor.fetchall()   
            connect.commit()
            cursor.close()
            connect.close()
            print('Empleados: ', empleados)
            return [{'Id': row[0], 'NumeroTarjeta': row[1], 'Activo': row[2]
                     , 'TipoTC': row[3], 'FechaVencimiento': row[4].strftime("%m/%Y")} for row in empleados]
        else:   # Error en la BD
            cursor.close()
            connect.close()
            return result    

    def consultarEC(self, IdTF): 
        connect = self.connect_mssql()
        cursor = connect.cursor()       
        cursor.execute("EXECUTE [dbo].[ListarECTCM] @inIdTF=?, @OutResult=0;"
                       , (IdTF)) 
        result = cursor.fetchall()[0][0]
        if result == 0: 
            cursor.nextset()
            empleados = cursor.fetchall()   
            connect.commit()
            cursor.close()
            connect.close()
            print('Empleados: ', empleados)
            return [{'Id': row[0], 'Fecha': row[1].strftime("%d-%m-%Y"), 'Saldo': round(row[2], 2)
                     , 'InteresCorriente': round(row[3], 2), 'InteresMoratorio': round(row[4], 2)
                     , 'OperacionesATM': row[5], 'OperacionesVentanilla': row[6]} for row in empleados]
        else:   # Error en la BD
            cursor.close()
            connect.close()
            return result    

    def consultarSEC(self, IdTF): 
        connect = self.connect_mssql()
        cursor = connect.cursor()       
        cursor.execute("EXECUTE [dbo].[ListarSECTCA] @inIdTF=?, @OutResult=0;"
                       , (IdTF)) 
        result = cursor.fetchall()[0][0]
        if result == 0: 
            cursor.nextset()
            empleados = cursor.fetchall()   
            connect.commit()
            cursor.close()
            connect.close()
            print('Empleados: ', empleados)
            return [{'Id': row[0], 'Fecha': row[1].strftime("%d-%m-%Y")
                     , 'OperacionesATM': row[2], 'OperacionesVentanilla': row[3]
                     , 'Compras': row[4], 'SumaCompras': round(row[5], 2)
                     , 'Retiros': row[6], 'SumaRetiros': round(row[7], 2)} for row in empleados]
        else:   # Error en la BD
            cursor.close()
            connect.close()
            return result    

    # Lista los movimientos
    def listarMovimientos(self, idEC, TipoTC): 
        connect = self.connect_mssql()
        cursor = connect.cursor()       
        cursor.execute("EXECUTE [dbo].[ListarMovimientos] @inIdEC=?, @inTipoTC=?, @OutResult=0;", (idEC, TipoTC))
        result = cursor.fetchall()[0][0]
        if result == 0: 
            cursor.nextset()
            movimientos = cursor.fetchall()        
            cursor.close()
            connect.close()
            print('Movimientos: ', movimientos)
            return [{'Fecha': row[0].strftime("%d-%m-%Y"), 'TipoMovimiento': row[1]
                     , 'Descripcion': row[2], 'Referencia': row[3]
                     , 'Monto': round(row[4], 2), 'Saldo': round(row[5], 2)} for row in movimientos]
        else:   # Error en la BD
            cursor.close()
            connect.close()
            return result
        
 

  

    # Login, recibe el nombre de usuario y contrasena
    def login(self, username, password): 
        connect = self.connect_mssql()
        cursor = connect.cursor()       
        cursor.execute("EXECUTE [dbo].[Login] @inUsername=?, @inPassword=?, @OutResult=0;"
                       , (username, password))    
        result = cursor.fetchall()
        connect.commit()
        cursor.close()
        connect.close()
        print(result)
        return result
        # Login exitoso: return [(0, IdUsuario)] o [(1, IdUsuario)] o [(-1,)]


  


if __name__ == '__main__':
    # Ejemplo de uso
    x = MssqlConnection()
    nombre = 'vcvc'

    #x.listarEmpleados(1)
    #x.listarEmpleados(1, nombre)
    #x.consultarEC(2)
    #x.listarMovimientos(1)
    #x.login('test', '1234')
    #x.listarTarjetas(1)
    #x.logout(1)
    
