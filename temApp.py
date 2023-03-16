from db import get_connection

# try:
#     connection=get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute('call consulta_alumnos()')
#         resultset=cursor.fetchall()
#         for row in resultset:
#             print(row)
#         connection.close()
# except Exception as ex:
#     print(ex)

try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call agregar_alumno(%s, %s, %s)',
                       ('Ivan', 'Ornelas', 'Meza', 'ivan@gmail.com'))
        resultset=cursor.fetchall()
        for row in resultset:
            print(row)
        connection.close()
except Exception as ex:
    print(ex)
