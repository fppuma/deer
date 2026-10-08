class Person:
    """Una clase es un molde para crear objetos."""

    def __init__(self, name, age):
        # __init__ se ejecuta al crear el objeto.
        # self es el propio objeto; aquí guardamos sus atributos.
        self.name = name
        self.age = age

    def greet(self):
        # Un método es una función que pertenece a la clase.
        return f"Hola, soy {self.name} y tengo {self.age} años."

    def have_birthday(self):
        self.age += 1
