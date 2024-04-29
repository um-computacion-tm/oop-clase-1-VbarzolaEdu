class Persona:

    def __init__ (self, nombre: str = 'john', apellido: str ='doe', dni: int = 123456):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__dni__ = dni
    
    def __str__(self):                  
        return f'Mis datos son nombre = {self.__nombre__} apellido = {self.__apellido__} documento = {self.__dni__}'