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

Consulta()

def Eliminar():
    id = int(input('Ingrese el número del id que desea eliminar: '))

    res = conn.cursor()
    sql = ('DELETE FROM usuarios WHERE id={}').format(id)
    res.execute(sql)

    conn.commit()
    row = res.rowcount

    print(f'Registro eliminado {row}')

# Eliminar()