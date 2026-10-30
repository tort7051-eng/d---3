class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(f"{self.name} - {self.price} грн. В наявності: {self.quantity}")


class Cart:
    def __init__(self):
        self.products = []

    #Додавання товару
    def add_product(self, product, amount=1):
        if product.quantity >= amount and amount > 0:
            self.products.append((product, amount))
            product.quantity -= amount
            print(f"{product.name} додано до кошика!")
        else:
            print("Недостатньо товару на складі!")

    #Видалення товару
    def remove_product(self, product):
        for item in self.products:
            if item[0] == product:
                self.products.remove(item)
                product.quantity += item[1]
                print(f"{product.name} видалено з кошика!")
                return
        print("Товар не знайдено!")

    #Підрахунок загальної вартості
    def total_price(self):
        total = sum(product.price * amount
                    for product, amount in self.products)
        return total

    #Показ кошика
    def show_cart(self):
        print("\n--- Ваш кошик ---")
        if not self.products:
            print("Кошик порожній")
        else:
            for product, amount in self.products:
                print(f"{product.name} x {amount} = {product.price * amount} грн")
            print(f"Загальна вартість: {self.total_price()} грн")


#Створення товарів
phone = Product("Телефон", 10000, 5)
laptop = Product("Ноутбук", 25000, 3)
mouse = Product("Мишка", 500, 10)

#Створення кошика
cart = Cart()

#Показ товарів
print("--- Товари магазину ---")
phone.show_info()
laptop.show_info()
mouse.show_info()

#Додавання товарів
cart.add_product(phone, 1)
cart.add_product(mouse, 2)
cart.add_product(laptop, 1)

#кошика
cart.show_cart()

#Видалення товару
cart.remove_product(mouse)

#Оновлений кошик
cart.show_cart()