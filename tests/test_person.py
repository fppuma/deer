import unittest

from person import Person


class TestPerson(unittest.TestCase):
    """Cada método que empieza con test_ es una prueba."""

    def test_create_person(self):
        ana = Person("Ana", 30)
        self.assertEqual(ana.name, "Ana")
        self.assertEqual(ana.age, 30)

    def test_greet(self):
        ana = Person("Ana", 30)
        self.assertEqual(ana.greet(), "Hola, soy Ana y tengo 30 años.")

    def test_have_birthday(self):
        ana = Person("Ana", 30)
        ana.have_birthday()
        self.assertEqual(ana.age, 31)


if __name__ == "__main__":
    unittest.main()
