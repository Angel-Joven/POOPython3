# JOVEN JIMENEZ ANGEL CRISTIAN

from cosas import *

def main():
    per1 = Persona("Angel", 21)
    print(per1)
    print(Persona.descripcion)
    print("----- Herencia Alumno ------")
    al1 = Alumno("Angel", 21, "0123456789", "ICO")
    print(al1)
    print(Alumno.descripcion)
    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()
    print("------ Herencia Profesor ------")
    profe1 = Profesor("Jesus", 30 + 16, 363565, "Ingenieria de Software")
    print(profe1)
    profe1.dormir()
    print("------ Herencia Ayudante - Profesor ------")
    ayudante = AyudanteProfesor("Adrian", 20, "25254", "ICO", 232323, "Ing. de Software", 4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.dar_clase("POO")

main()