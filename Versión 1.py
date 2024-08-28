


class Persona():
    def __init__(self):
        self.nombre = ""
        self.id = 0
        self.genero = ""

    def SetName(self,nombre):
            self.nombre = nombre
    def SetId(self,id):
            self.id = id
    def SetGen(self,genero):
            self.genero = genero
    
    def GetName(self):
          return self.nombre
    def GetId(self):
          return self.id
    def GetGen(self):
          return self.genero

class Paciente(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.servicio = ""
        
    def SetService(self,servicio):
        self.servicio = servicio

    def GetService(self,servicio):
        return self.servicio
        
class Enfermera(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.turno = ""
        self.rango = ""

    def SetTurn(self,turno):
         self.turno = turno
    def SetRange(self,rango):
        self.turno = rango

    def GetTurn(self,turno):
         return self.turno
    def GetRange(self,rango):
         return self.rango
    
class Medico(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.turno = ""
        self.rango = ""

    def SetTurn(self,turno):
         self.turno = turno
    def SetEspecialidad(self,especialidad):
        self.especialidad = especialidad

    def GetTurn(self,turno):
         return self.turno
    def GetEspecialidad(self,especialidad):
         return self.especialidad

#Hola
    