import unittest
from .fifth_ass import Device, Smartphone, Laptop, Tablet, Cart
class TestDevice(unittest.TestCase):
    def test_device_availability(self):
        d = Device("Test Device", 1000, 5, 12)
        self.assertTrue(d.is_available(3))
        self.assertFalse(d.is_available(6))

    def test_reduce_stock(self):
        d = Device("Test Device", 1000, 5, 12)
        result = d.reduce_stock(2)
        self.assertTrue(result)
        self.assertEqual(d.stock, 3)

    def test_apply_discount(self):
        d = Device("Test Device", 1000, 5, 12)
        d.apply_discount(10)
        self.assertEqual(d.price, 900)


class TestDerivedClasses(unittest.TestCase):
    def test_smartphone(self):
        phone = Smartphone("Phone", 800, 5, 12, 6.1, 20)
        self.assertIn("Screen", phone.display_info())
        self.assertEqual(phone.make_call(), "Calling from Phone...")

    def test_laptop(self):
        laptop = Laptop("Laptop", 1200, 3, 24, 16, 3.2)
        self.assertIn("RAM", laptop.display_info())
        self.assertEqual(laptop.run_program(), "Running software on Laptop...")

    def test_tablet(self):
        tablet = Tablet("Tablet", 600, 4, 12, "2048x1536", 450)
        self.assertIn("Resolution", tablet.display_info())
        self.assertEqual(tablet.browse_internet(), "Browsing on Tablet...")


class TestCart(unittest.TestCase):
    def test_add_device(self):
        cart = Cart()
        phone = Smartphone("Phone", 800, 5, 12, 6.1, 20)
        message = cart.add_device(phone, 2)
        self.assertEqual(message, "Added 2 x Phone to cart.")
        self.assertEqual(cart.items[phone], 2)

    def test_remove_device(self):
        cart = Cart()
        phone = Smartphone("Phone", 800, 5, 12, 6.1, 20)
        cart.add_device(phone, 2)
        message = cart.remove_device(phone, 1)
        self.assertEqual(message, "Removed 1 x Phone from cart.")
        self.assertEqual(cart.items[phone], 1)

    def test_get_total_price(self):
        cart = Cart()
        phone = Smartphone("Phone", 800, 5, 12, 6.1, 20)
        cart.add_device(phone, 2)
        self.assertEqual(cart.get_total_price(), 1600)

    def test_checkout(self):
        cart = Cart()
        phone = Smartphone("Phone", 800, 5, 12, 6.1, 20)
        cart.add_device(phone, 2)
        receipt = cart.checkout()
        self.assertIn("Final Total: $1600.00", receipt)
        self.assertEqual(phone.stock, 3)
        self.assertEqual(len(cart.items), 0)

if __name__ == "__main__":
    unittest.main()
