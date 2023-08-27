import pyodbc

DATA_BASE = 'registros'
SERVER_NAME = 'DESKTOP-T7N9G51\SQLEXPRESS'

try:
    conn = pyodbc.connect (
        'DRIVER={SQL Server};'
        f'SERVER={SERVER_NAME};'
        f'DATABASE={DATA_BASE};'
        'Trusted_Connection=yes;'
    )
    print('Conexión exitosa', conn)
except Exception as err:
    print(f'Error de conexión {err}')

def Consulta():
    cur = conn.cursor()
    cur.execute('SELECT * FROM usuarios')
    row = cur.fetchall()

    for i in row:
        print(row)


def Eliminar():
    id = int(input('Ingrese el número del id que desea eliminar: '))

    res = conn.cursor()
    sql = ('DELETE FROM usuarios WHERE id={}').format(id)
    res.execute(sql)

    conn.commit()
    row = res.rowcount

    print(f'Registro eliminado {row}')

# Eliminar()

def Insertar():
    id = int(input('Ingrese un id válido: '))
    nombre = str(input('Ingrese un nombre: '))
    apellido = str(input('Ingrese un apellido: '))
    telefono = int(input('Ingrese un número de telefono: '))

    res = conn.cursor()
    res.execute(f"INSERT INTO usuarios(id, nombre, apellido, telefono) VALUES({id},'{nombre}', '{apellido}', {telefono})")
    conn.commit()

    row = res.rowcount
    print(f'{row} registro insertado')


def Editar():
    id = int(input('Seleccione el dato que quiere actualizar: '))
    nombre = str(input('Ingrese el nuevo nombre: '))
    apellido = str(input('Ingrese el nuevo apellido: '))
    telefono = int(input('Ingrese el nuevo número de teléfono: '))

    cur = conn.cursor()
    sql = 'UPDATE usuarios SET nombre=?, apellido=?, telefono=? WHERE id=?'

    cur.execute(sql, (nombre, apellido, telefono, id))
    conn.commit()

    row = cur.rowcount
    print(row)