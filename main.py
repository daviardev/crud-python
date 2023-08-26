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