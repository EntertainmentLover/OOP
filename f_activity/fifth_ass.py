class Device:
    def __init__(self, name, price, stock, warranty):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty

    def display_info(self):
        return f"{self.name} | Price: ${self.price:.2f} | Stock: {self.stock} | Warranty: {self.warranty_period} months"

    def __str__(self):
        return self.display_info()

    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            self.price -= self.price * (discount_percentage / 100)

    def is_available(self, amount):
        return amount > 0 and self.stock >= amount

    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount
            return True
        return False


class Smartphone(Device):
    def __init__(self, name, price, stock, warranty, screen_size, battery_life):
        super().__init__(name, price, stock, warranty)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def display_info(self):
        return f"{super().display_info()} | Screen: {self.screen_size}\" | Battery: {self.battery_life}h"

    def __str__(self):
        return f"Smartphone -> {self.display_info()}"

    def make_call(self):
        print(f"Calling from {self.name}...")

    def install_app(self):
        print(f"Installing app on {self.name}...")


class Laptop(Device):
    def __init__(self, name, price, stock, warranty, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def display_info(self):
        return f"{super().display_info()} | RAM: {self.ram_size}GB | CPU: {self.processor_speed}GHz"

    def __str__(self):
        return f"Laptop -> {self.display_info()}"

    def run_program(self):
        print(f"Running software on {self.name}...")

    def use_keyboard(self):
        print(f"Typing on {self.name}...")


class Tablet(Device):
    def __init__(self, name, price, stock, warranty, screen_resolution, weight):
        super().__init__(name, price, stock, warranty)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def display_info(self):
        return f"{super().display_info()} | Resolution: {self.screen_resolution} | Weight: {self.weight}g"

    def __str__(self):
        return f"Tablet -> {self.display_info()}"

    def browse_internet(self):
        print(f"Browsing on {self.name}...")

    def use_touchscreen(self):
        print(f"Using touchscreen on {self.name}...")


class Cart:
    def __init__(self):
        self.items = {}

    def add_device(self, device, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
        current_amount = self.items.get(device, 0)
        if device.stock >= current_amount + amount:
            self.items[device] = current_amount + amount
            print(f"Added {amount} x {device.name} to cart.")
        else:
            print(f"Insufficient stock for {device.name}!")

    def remove_device(self, device, amount):
        if device not in self.items:
            print(f"{device.name} is not in the cart.")
            return
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
        if amount >= self.items[device]:
            del self.items[device]
            print(f"Removed {device.name} from cart.")
        else:
            self.items[device] -= amount
            print(f"Removed {amount} x {device.name} from cart.")

    def get_total_price(self):
        total = 0
        for device, amount in self.items.items():
            total += device.price * amount
        return total

    def print_items(self):
        if not self.items:
            print("Cart is empty.")
            return
        print("\n--- Cart Items ---")
        for i, (device, amount) in enumerate(self.items.items(), start=1):
            subtotal = device.price * amount
            print(f"{i}. {device.name} | Qty: {amount} | Unit Price: ${device.price:.2f} | Subtotal: ${subtotal:.2f}")
        print(f"Total Price: ${self.get_total_price():.2f}")

    def checkout(self):
        if not self.items:
            print("Nothing to checkout!")
            return
        for device, amount in self.items.items():
            if not device.is_available(amount):
                print(f"Checkout failed. Not enough stock for {device.name}.")
                return
        print("\n--- Receipt ---")
        for device, amount in self.items.items():
            device.reduce_stock(amount)
            print(f"{device.name} x {amount} = ${device.price * amount:.2f}")
        print(f"Final Total: ${self.get_total_price():.2f}")
        print("Thank you for your purchase!")
        self.items.clear()

def show_devices(inventory):
    print("\n--- Available Devices ---")
    for i, device in enumerate(inventory, start=1):
        print(f"{i}. {device}")

def create_inventory():
    return [
        Smartphone("iPhone 15", 999, 10, 12, 6.1, 20),
        Smartphone("Samsung Galaxy S24", 899, 8, 24, 6.2, 22),
        Smartphone("Google Pixel 8", 799, 7, 12, 6.2, 24),
        Smartphone("Xiaomi 14", 749, 11, 18, 6.36, 21),
        Smartphone("OnePlus 12", 829, 9, 12, 6.7, 23),
        Smartphone("Nothing Phone 2", 699, 6, 12, 6.7, 19),
        Smartphone("Sony Xperia 1 V", 1099, 4, 24, 6.5, 18),

        Laptop("MacBook Air M3", 1299, 5, 12, 16, 3.5),
        Laptop("Dell XPS 13", 1199, 6, 24, 16, 3.4),
        Laptop("HP Spectre x360", 1149, 5, 24, 16, 3.2),
        Laptop("Lenovo ThinkPad X1", 1399, 7, 36, 32, 3.6),
        Laptop("ASUS ROG Zephyrus", 1599, 4, 24, 32, 4.2),
        Laptop("Acer Aspire 5", 699, 10, 12, 8, 2.8),
        Laptop("MSI Modern 15", 849, 8, 12, 16, 3.1),

        Tablet("iPad Pro", 999, 9, 12, "2732x2048", 466),
        Tablet("Samsung Galaxy Tab S9", 849, 7, 24, "2560x1600", 498),
        Tablet("Xiaomi Pad 6", 499, 12, 12, "2880x1800", 490),
        Tablet("Lenovo Tab P12", 429, 8, 12, "2944x1840", 615),
        Tablet("Huawei MatePad 11", 549, 6, 12, "2560x1600", 485),
        Tablet("Amazon Fire Max 11", 299, 10, 12, "2000x1200", 490)
    ]

def cart_remove_menu(cart):
    if not cart.items:
        print("Cart is empty.")
        return
    cart_list = list(cart.items.items())
    print("\n--- Remove From Cart ---")
    for i, (device, amount) in enumerate(cart_list, start=1):
        print(f"{i}. {device.name} | Qty in cart: {amount}")
    choice = input("Enter item number to remove (or b to go back): ")
    if choice.lower() == "b":
        return
    if not choice.isdigit():
        print("Invalid input.")
        return
    idx = int(choice) - 1
    if 0 <= idx < len(cart_list):
        device, current_amount = cart_list[idx]
        qty = input(f"How many {device.name} do you want to remove? ")
        if qty.isdigit():
            cart.remove_device(device, int(qty))
        else:
            print("Invalid quantity.")
    else:
        print("Invalid item number.")

def add_to_cart_menu(inventory, cart):
    show_devices(inventory)
    choice = input("\nEnter device number to add to cart (or b to go back): ")
    if choice.lower() == "b":
        return
    if not choice.isdigit():
        print("Invalid input.")
        return
    idx = int(choice) - 1
    if 0 <= idx < len(inventory):
        qty = input(f"How many {inventory[idx].name} do you want to add? ")
        if qty.isdigit():
            cart.add_device(inventory[idx], int(qty))
        else:
            print("Invalid quantity.")
    else:
        print("Invalid device number.")

def main():
    inventory = create_inventory()
    cart = Cart()
    while True:
        print("\n=== Electronic Device Store ===")
        print("1. Show Devices")
        print("2. Show Cart")
        print("3. Remove Item From Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            add_to_cart_menu(inventory, cart)
        elif choice == "2":
            cart.print_items()
        elif choice == "3":
            cart_remove_menu(cart)
        elif choice == "4":
            cart.checkout()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
