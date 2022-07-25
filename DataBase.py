import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='123456789',
            db='correo_yury'
        )
        
        self.cursor = self.connection.cursor()
    
    def show_log_action(self):
        query = "SELECT * FROM log_action"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
    
    def user_exist(self, username, password):
        query = f"SELECT * FROM employee WHERE rut = '{username}' AND pass = '{password}'"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchone() != None
        except Exception as e:
            print(e)
    
    def user_type(self, username, password):
        query = f"SELECT rh FROM employee WHERE rut = '{username}' AND pass = '{password}'"
        try:
            if self.user_exist(username, password):
                self.cursor.execute(query)
                return self.cursor.fetchone()[0]
            else:
                return None
        except Exception as e:
            print(e)

if __name__ == '__main__':
    database = DataBase()

    # for element in database.show_log_action():
    #     print(f"id: {element[0]}, description: {element[1]}")
    print(database.user_exist('123', '321'))