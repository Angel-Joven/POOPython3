# JOVEN JIMENEZ ANGEL CRISTIAN

class Autor:
    def __init__(self, nom, pseudo):
        self.__nombre = nom
        self.__pseudonimo = pseudo

    # GETs

    @property
    def nombre(self):
        return self.__nombre

    @property
    def pseudonimo(self):
        return self.__pseudonimo

    # SETs

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    @pseudonimo.setter
    def pseudonimo(self, pseudo):
        self.__pseudonimo = pseudo

    # Metodo Tostring

    def __str__(self):
        return f"\n        |     Nombre: {self.__nombre}\n        |     Pseudonimo: {self.__pseudonimo}"

    # Metodos de uso general

    def escribir(self):
        print(f"{self.__pseudonimo} esta escribiendo su siguiente obra.")

class Libro:
    def __init__(self, titu, aut, an, ed):
        self.__titulo = titu
        self.__autor = aut
        self.__año = an
        self.__editorial = ed

    # GETs

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def año(self):
        return self.__año

    @property
    def editorial(self):
        return self.__editorial

    # SETs

    @titulo.setter
    def titulo(self, titu):
        self.__titulo = titu

    @autor.setter
    def autor(self, aut):
        self.__autor = aut

    @año.setter
    def año(self, an):
        self.__año = an

    @editorial.setter
    def editorial(self, ed):
        self.__editorial = ed

    # Metodo Tostring

    def __str__(self):
        return f"""
        -----------------------------------------------------------
        | Nombre del libro: {self.__titulo} 
        | Autor: {self.__autor}
        | Año de publicacion: {self.__año}
        | Editorial: {self.__editorial}
        -----------------------------------------------------------
        """

    # Classmethod

    @classmethod
    def libro_planeta(cls, titulo, autor, año):
        return cls(titulo, autor, año, "Planeta")

    # Metodos de uso general

    def leer(self, minutos):
        print(f"Leyendo por {minutos} minutos")

class Persona:
    def __init__(self, nom, eda):
        self.__nombre = nom
        self.__edad = eda

    # GETs

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    # SETs

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    @edad.setter
    def edad(self, eda):
        self.__edad = eda

class Alumno(Persona):
    def __init__(self, nom, eda, nume_cuenta, carr, prome):
        super().__init__(nom, eda)
        self.__numero_cuenta = nume_cuenta
        self.__carrera = carr
        self.__promedio = prome




