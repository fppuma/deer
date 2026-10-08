# Atributos de instancia: la clase `BackPack` y su campo `items`

Notas comparando Python con Java, a partir de [src/backpack.py](../src/backpack.py):

```python
class BackPack:
    def __init__(self):
        self.items = []
```

`self.items = []` crea un **atributo de instancia**, el equivalente a un campo en Java, y le asigna una lista vacía. Hay tres diferencias importantes con Java.

## 1. El campo se crea al asignarlo, sin declaración previa

En Java declaras el campo en el cuerpo de la clase y lo inicializas en el constructor:

```java
public class BackPack {
    private List<Object> items;          // declaración

    public BackPack() {
        this.items = new ArrayList<>();  // inicialización
    }
}
```

En Python no existe la declaración. El campo **empieza a existir en el momento en que lo asignas** con `self.items = ...`, y por eso los campos se crean en `__init__`.

- `__init__` cumple el papel del constructor.
- `self` es el equivalente a `this`, pero Python te obliga a escribirlo: es el primer parámetro de cada método y siempre tienes que usarlo para acceder a los campos (`self.items`, nunca solo `items`).

## 2. `[]` es una lista, parecida a un `ArrayList`

`[]` crea una `list` vacía. Es lo mismo que escribir `list()`, pero más corto, y es la forma habitual.

| Java | Python |
|---|---|
| `new ArrayList<>()` | `[]` |
| `items.add(x)` | `items.append(x)` |
| `items.get(0)` | `items[0]` |
| `items.size()` | `len(items)` |
| `items.remove(x)` | `items.remove(x)` |
| `items.contains(x)` | `x in items` |
| `for (Object x : items)` | `for x in items:` |

Python tiene **tipado dinámico**: la lista no tiene un tipo genérico y acepta cualquier cosa, como un `List<Object>`. Si quieres documentar el tipo, puedes añadir una anotación (*type hint*). Python no la comprueba al ejecutar, pero el editor sí la usa para ayudarte:

```python
from typing import List   # en Python 3.8 hace falta este import

class BackPack:
    def __init__(self):
        self.items: List[str] = []
```

## 3. Es público, y el "privado" es solo una convención

Python no tiene `private`. Desde fuera puedes hacer `backpack.items` directamente. La convención es poner un guion bajo delante (`self._items`) para indicar "esto es interno, no lo toques desde fuera". Python no lo impide; es un acuerdo entre programadores.

## Error típico viniendo de Java: atributo de clase vs. atributo de instancia

En Java, un campo inicializado en su declaración (`private List<Object> items = new ArrayList<>();`) se crea **por cada objeto**. En Python, si pones la asignación en el cuerpo de la clase, fuera de `__init__`, pasa algo muy distinto:

```python
class BackPack:
    items = []   # ¡atributo de CLASE, compartido, como un static!
```

Con esa versión, todas las mochilas comparten **la misma lista**: si añades un objeto a una, aparece en todas. Al asignarla en `__init__`, cada mochila recibe su propia lista nueva:

```python
a = BackPack()
b = BackPack()
a.items.append("book")
print(a.items)  # ['book']
print(b.items)  # []  → cada mochila tiene su propia lista
```

El test `test_each_backpack_has_its_own_items` de [tests/test_backpack.py](../tests/test_backpack.py) comprueba justamente esto.

### Un error parecido: listas como valor por defecto

No uses una lista como valor por defecto de un parámetro. Ese valor por defecto se crea **una sola vez** y lo comparten todas las llamadas:

```python
# Mal: todas las mochilas creadas sin argumento comparten la misma lista
def __init__(self, items=[]):
    self.items = items

# Bien: crear una lista nueva en cada llamada
def __init__(self, items=None):
    if items is None:
        items = []
    self.items = items
```

## Estilo: indentación

La guía de estilo oficial de Python (**PEP 8**) recomienda **4 espacios** de indentación. Con 2 espacios el código también funciona, pero en casi todo el código Python verás 4.
