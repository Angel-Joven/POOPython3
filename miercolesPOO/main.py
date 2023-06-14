# JOVEN JIMENEZ ANGEL CRISTIAN

from cosas import Alumno, Perro

def main():
    al1 = Alumno("Angel", 21, "ICO")
    print(vars(al1))
    al1.__nombre = "Diego"
    print(vars(al1))
    al1.set_nombre("Maria")
    print(vars(al1))
    print("--------- To String ---------")
    print(al1)
    al1.set_edad(999)
    print(al1)
    al1.estudiar(4)
    print("------ Aqui empieza perro ------")
    perro1 = Perro("Poddle", 2, 0.35)
    print(vars(perro1))
    perro1.raza = "De la calle" #Set en notacion Pythonic
    print(vars(perro1))
    perro1.__raza = "Otra"
    print(vars(perro1))
    print(perro1)
    perro1.edad = 12
    perro1.estatura = 0.45
    print(perro1)
    cachorro = Perro.es_cachorro(perro1.edad)
    print(cachorro)
    Perro.dormir()
    danes = Perro.perro_grande(0.8)
    print(danes)

"""
+ Publico
- Privado
# Protected
~ Friendly (relacion de clases con paquetes)

@property -> Get
@(nombre del atributo).setter -> Set
@staticmethod -> Evita crear otro objeto para hacerlo llamar (acceso estatico)
@classmethod -> Crea un metodo de clase que tiene acceso a los atributos de la CLASE 
                (acceso estatico / Sirve para contructores sobrecargados)

"""

main()