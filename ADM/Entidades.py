#import mysql_connector
#import PyQt5

class Persona():
    
    def __init__(self, ID_persona, rut, nombre, apePat, apeMat, nombre_2, direccion, telefono, correo, cargo):
        self.ID_persona = ID_persona
        self.rut = rut
        self.nombre = nombre
        self.nombre_2 = nombre_2
        self.apePat = apePat
        self.apeMat = apeMat
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.cargo = cargo


    def mostrarDatos(self):
        txt = "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}"
        return txt.format(self.ID_persona , self.rut, self.nombre, self.nombre_2, self.apePat, self.apeMat, self.direccion, self.telefono, self.correo, self.cargo)

class Jefe_RR_HH(Persona):

    def __init__(self, ID_persona, rut, nombre, apePat, apeMat, nombre_2, direccion, telefono, correo, cargo, ID_ADM):
        super().__init__(ID_persona, rut, nombre, apePat, apeMat, nombre_2, direccion, telefono, correo, cargo)

        self.ID_ADM = ID_ADM
    
    def addADM(self, account):
        pass
        
        
ent_priv= Jefe_RR_HH(1, 221456456-6,"Juan", "Gutierrez", "Salazar", "Sebastian", "Linea-1", 981457345, "@gmail.com", "ADMNISTRADOR", 111)

prs = Persona(1, 901456456-6,"Luis", "Enrique", "Baltazar", "Jorge", "Linea-2", 917777345, "@gmail.com","EMPLEADO")

print(ent_priv.mostrarDatos())

adm = input('''''')






        
















