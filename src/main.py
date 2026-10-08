from person import Person

# Creamos dos objetos (instancias) a partir de la misma clase.
ana = Person("Ana", 30)
luis = Person("Luis", 25)

print(ana.greet())
print(luis.greet())

ana.have_birthday()
print(ana.greet())
