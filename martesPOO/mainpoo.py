# JOVEN JIMENEZ ANGEL CRISTIAN

from cosas import Alumno

def main():
    """
    al1 = Alumno()
    print(al1) #No hay nada que imprimir, sin embargo, se ha creado el objeto
    al2 = Alumno()
    print(al1.facultad) #Para solo al1
    print(al2.facultad)
    print(Alumno.facultad)
    print("-----------------------------")
    #Nuevo atribudo de instancia SOBRE 'al1'
    al1.facultad = "Fes Aragon EDOMEX"
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    print("----- Un vistazo a los objetos -----")
    print(vars(al1))
    print(vars(al2))
    Alumno.facultad = "Fes Aragon EDOMEX" #Para todas las instancias (valor de la variable de la clase)
    print("------ Modificar atrubutos publicos ------")
    al1.edad = 999
    print(vars(al1))
    print(vars(al2))
    """

    al1 = Alumno("Angel", 21, "ICO")
    al2 = Alumno("Montse", 20, "Derecho")
    print(vars(al1))
    al1.__edad = 333
    print(al1.__edad)
    print(vars(al1))

main()