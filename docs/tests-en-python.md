# Tests en Python con `unittest`

Un **test** es código que ejecuta tu código y comprueba que el resultado es el esperado. En lugar de mirar a ojo lo que imprime el programa, Python hace la comprobación y te avisa si algo falla.

`unittest` viene incluido con Python, así que no hay que instalar nada.

## 1. Cómo se escribe un test

Ejemplo basado en [tests/test_person.py](../tests/test_person.py):

```python
import unittest                  # (1) módulo de tests incluido en Python

from person import Person        # (2) el código que queremos probar


class TestPerson(unittest.TestCase):     # (3) una clase que hereda de TestCase

    def test_have_birthday(self):        # (4) cada método test_... es un test
        ana = Person("Ana", 30)          #     Preparar
        ana.have_birthday()              #     Actuar
        self.assertEqual(ana.age, 31)    #     Comprobar
```

1. **`import unittest`** carga la herramienta de tests.
2. **Importar lo que vas a probar**, en este caso la clase `Person`.
3. **Una clase que hereda de `unittest.TestCase`.** Es POO: la clase de tests recibe de `TestCase` todos los métodos `assert...`.
4. **Cada método cuyo nombre empieza con `test_` es un test.** Python los encuentra y los ejecuta automáticamente. Si el nombre no empieza con `test_`, ese método se ignora.

### El patrón Preparar, Actuar y Comprobar

| Paso | Qué hace | En el ejemplo |
|---|---|---|
| **Preparar** | Crea los objetos que necesitas | `ana = Person("Ana", 30)` |
| **Actuar** | Ejecuta lo que quieres probar | `ana.have_birthday()` |
| **Comprobar** | Verifica el resultado | `self.assertEqual(ana.age, 31)` |

## 2. Las comprobaciones (asserts) más usadas

```python
self.assertEqual(a, b)        # a == b
self.assertNotEqual(a, b)     # a != b
self.assertTrue(x)            # x es verdadero
self.assertFalse(x)           # x es falso
self.assertIn(item, lista)    # item está en lista
self.assertIsNone(x)          # x es None
```

Para comprobar que el código lanza un error cuando corresponde:

```python
def test_negative_age_raises_error(self):
    with self.assertRaises(ValueError):
        Person("Ana", -5)
```

## 3. `setUp`: código común a todos los tests

Si todos los tests crean el mismo objeto, puedes crearlo una sola vez en `setUp`. Python ejecuta `setUp` antes de **cada** test, así que cada test recibe un objeto nuevo y los tests no se afectan entre sí:

```python
class TestPerson(unittest.TestCase):

    def setUp(self):
        self.ana = Person("Ana", 30)

    def test_greet(self):
        self.assertEqual(self.ana.greet(), "Hola, soy Ana y tengo 30 años.")

    def test_have_birthday(self):
        self.ana.have_birthday()
        self.assertEqual(self.ana.age, 31)
```

## 4. Cómo se ejecutan

Siempre desde la carpeta raíz del proyecto (`deer/`):

```bash
# Todos los tests de la carpeta tests/
PYTHONPATH=src python3 -m unittest discover -s tests -v

# Solo un archivo
PYTHONPATH=src python3 -m unittest tests/test_person.py -v

# Solo un test concreto
PYTHONPATH=src python3 -m unittest test_person.TestPerson.test_greet -v
```

| Parte | Significado |
|---|---|
| `-m unittest` | Ejecuta el módulo de tests |
| `discover` | Busca automáticamente los archivos cuyo nombre empieza con `test` |
| `-s tests` | Indica que busque dentro de la carpeta `tests/` |
| `-v` | *Verbose*: muestra el nombre y el resultado de cada test |
| `PYTHONPATH=src` | Hace que `from person import ...` encuentre los archivos de `src/` |

El tercer comando (un solo test) puede fallar si Python no encuentra `test_person` desde la carpeta en la que estás. Si te pasa, usa el de un solo archivo.

## 5. Cómo leer el resultado

Si todo va bien:

```
test_greet (test_person.TestPerson) ... ok
Ran 3 tests in 0.000s
OK
```

Si algo falla, verás uno de estos dos resultados:

- **`FAIL`**: el código se ejecutó, pero una comprobación no se cumplió. Python te muestra qué esperaba y qué obtuvo:
  ```
  AssertionError: 30 != 31
  ```
- **`ERROR`**: el código lanzó una excepción antes de llegar a la comprobación. Puede ser un error de escritura en el código, un atributo que no existe, etc.

## 6. Convenciones

- Archivos: `test_<lo_que_pruebas>.py`, por ejemplo `test_dog.py`.
- Clases: `Test<Clase>`, por ejemplo `TestDog`.
- Métodos: `test_<qué_comprueba>`, con un nombre descriptivo como `test_bark_returns_woof`.
- Cada test comprueba **una sola cosa**. Así, cuando uno falla, sabes enseguida qué se rompió.

## 7. ¿Qué es `PYTHONPATH`?

Es una variable de entorno estándar de Python ([documentación oficial](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)).

Cuando escribes `import person`, Python busca `person.py` en una lista de carpetas llamada `sys.path`. Puedes verla así:

```bash
python3 -c "import sys; print(sys.path)"
```

Esa lista incluye, en este orden:

1. La carpeta del script que ejecutas. Por eso `python3 src/main.py` encuentra `person.py` sin ayuda.
2. Las carpetas que pongas en `PYTHONPATH`.
3. Las carpetas de la biblioteca estándar y de los paquetes instalados con `pip`.

Los tests están en `tests/`, así que Python no mira dentro de `src/` por sí solo. Con `PYTHONPATH=src` añades esa carpeta a la lista solo mientras dura ese comando.

En proyectos profesionales se suele usar en su lugar un archivo `pyproject.toml` con `pip install -e .`, o pytest con `pythonpath = src` configurado. Así no hace falta escribir `PYTHONPATH` en cada comando.

## 8. Más adelante: pytest

**pytest** es una herramienta muy popular que hay que instalar aparte. Permite escribir tests más cortos, con un `assert ana.age == 31` simple y sin necesidad de clases. Los conceptos son los mismos que con `unittest`.
