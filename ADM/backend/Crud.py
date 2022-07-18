from Conectar import Connect


class Usuario:
    def __init__(self, rut, nombre, apePat, apeMat, segundo_nombre, direccion , telefono, correo, Cargo) -> None:
        self.rut = rut
        self.nombre = nombre
        self.apePat = apePat
        self.apeMat = apeMat
        self.segundo_nombre = segundo_nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.cargo = Cargo
        self.conectar = Connect()

    def actualizarDatos(self):
        sql = f"UPDATE nombre, apellido_paterno, apellido_materno, segundo_nombre, direccion, telefono, correo, Cargo SET rut = {self.nombre, self.apePat, self.apeMat, self.segundo_nombre, self.direccion, self.telefono, self.correo, self.cargo}"
        msj = self.conectar.ejecutar(sql)

        if msj == 1:
            return "Datos Actualizados"
        if msj == 0:
            return "Error. Verifique si lo datos esten bien. o contacte con su administrador!"

        return msj
    
    def mostrarDatos(self):
        sql = f"SELECT * FROM persona WHERE rut = {self.rut}"
        msj = self.conectar.listarTodos(sql)

        if msj == 1:
            return "Successfully exit!."
        if msj == 0:
            return "Error. Verifique si lo datos esten bien. o contacte con su administrador!"



        

