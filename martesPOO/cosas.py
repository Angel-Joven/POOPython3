# JOVEN JIMENEZ ANGEL CRISTIAN

class Alumno: #Clase Alumno
    facultad = "Fes Aragon"

    def __init__(self, nom, ed, carr): #Declara el constructor de la clase Alumno
        #print("constructor")
        #print(type(self))
        #pass #Evita que genere un error a esta funcion vacia
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = carr

#al1 = Alumno()
#al1.edad = 999

#print(al1.edad)