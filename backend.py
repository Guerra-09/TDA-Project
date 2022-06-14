import mysql.connector


class Connect:

    def __init__(self) -> None:
    
        self.__database = mysql.connector.connect(
                    host = 'localhost',
                    user = 'root',
                    password = '123456789',
                    database = 'guerra'
                )  

        self.__cursor = self.__database.cursor()
    

    def ejecutar(self, sql):
            try:
                self.__cursor.execute(sql)
                self.__database.commit()
                resul = self.__cursor.rowcount
                return resul
            except mysql.connector.Error as e:
                return "Error" + str(e)


    def listarTodos(self, sql):
        try:
            self.__cursor.execute(sql)
            lista = self.__cursor.fetchall()
            return lista
        except mysql.connector.Error as e:
            return "Error" +str(e)


    def listarUno(self, sql):
        try:
            self.__cursor.execute(sql)
            lista = self.__cursor.fetchone()
            return lista
        except mysql.connector.Error as e:
            return "Error" +str(e)