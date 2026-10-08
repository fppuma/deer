import unittest

from backpack import BackPack


class TestBackPack(unittest.TestCase):

    def test_new_backpack_is_empty(self):
        backpack = BackPack()
        self.assertEqual(backpack.items, [])

    def test_each_backpack_has_its_own_items(self):
        # Si items fuera un atributo de clase, b también tendría "book".
        a = BackPack()
        b = BackPack()
        a.items.append("book")
        self.assertEqual(a.items, ["book"])
        self.assertEqual(b.items, [])


if __name__ == "__main__":
    unittest.main()
