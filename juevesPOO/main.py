# JOVEN JIMENEZ ANGEL CRISTIAN

#from cosas import *
from cosas import Libro, Autor, Alumno, Persona

def main():
    l1 = Libro.libro_planeta("El perfume", Autor("Patrik", "PS"), 1980)
    print(l1)
    # Codigo para cambiar el pseudonimo a lowercase dentro de l1
    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)
    print("------ Herencia ------")
    al2 = Alumno("Angel", 21, "318", "ICO", 9)
    print(vars(al2))
    al2.nombre = "Pepe"
    print(vars(al2))

main()