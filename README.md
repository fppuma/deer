# Aprendiendo POO con Python

Proyecto de práctica para aprender programación orientada a objetos (clases, objetos, atributos y métodos).

## Estructura

```
deer/
├── README.md        # este archivo
├── docs/            # mis notas de aprendizaje
│   ├── tests-en-python.md
│   └── atributos-de-instancia.md
├── src/             # código fuente
│   ├── person.py    # la clase Person
│   ├── backpack.py  # la clase BackPack
│   └── main.py      # programa que usa las clases
└── tests/           # pruebas automáticas
    ├── test_person.py
    └── test_backpack.py
```

## Requisitos

Python 3.8 o superior. No hace falta instalar nada más: las pruebas usan `unittest`, que viene incluido con Python.

## Ejecutar el programa

Desde la carpeta `deer/`:

```bash
python3 src/main.py
```

## Ejecutar las pruebas

Desde la carpeta `deer/`:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

`PYTHONPATH=src` le indica a Python que busque los módulos (como `person`) dentro de `src/`.

Más detalles en [docs/tests-en-python.md](docs/tests-en-python.md).

## Agregar una clase nueva

1. Crea el archivo en `src/`, por ejemplo `src/dog.py`.
2. Úsala en `src/main.py` con `from dog import Dog`.
3. Crea sus pruebas en `tests/test_dog.py` (el nombre debe empezar con `test_`).
