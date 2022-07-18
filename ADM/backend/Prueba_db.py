import mysql.connector


conectar = mysql.connector.connect(
    user="root",
    password="diego2015",
    host="localhost",
    database="correo_yury",
    port="3306"

)

print(conectar)