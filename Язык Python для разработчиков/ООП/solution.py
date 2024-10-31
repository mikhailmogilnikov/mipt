class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if self.stock + quantity < 0:
            print(f"Ошибка: недостаточно товара '{self.name}' на складе.")
        else:
            self.stock += quantity


class Order:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if product.stock < quantity:
            print(f"Ошибка: недостаточно товара '{product.name}' на складе.")
        else:
            if product in self.products:
                self.products[product] += quantity
            else:
                self.products[product] = quantity
            product.update_stock(-quantity)

    def remove_product(self, product, quantity):
        if product in self.products:
            if self.products[product] < quantity:
                print(f"Ошибка: в заказе недостаточно товара '{product.name}'.")
            else:
                self.products[product] -= quantity
                product.update_stock(quantity)
                if self.products[product] == 0:
                    del self.products[product]
        else:
            print(f"Ошибка: товара '{product.name}' нет в заказе.")

    def return_product(self, product, quantity):
        if product in self.products:
            if self.products[product] < quantity:
                print(f"Ошибка: в заказе недостаточно товара '{product.name}' для возврата.")
            else:
                self.products[product] -= quantity
                product.update_stock(quantity)
                if self.products[product] == 0:
                    del self.products[product]
        else:
            print(f"Ошибка: товара '{product.name}' нет в заказе.")

    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.products.items())
        return total


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(f"{product.name}: цена - {product.price}, остаток - {product.stock}")

    def create_order(self):
        return Order()

if __name__ == "__main__":
    store = Store()

    product1 = Product("Ноутбук", 1000, 5)
    product2 = Product("Смартфон", 500, 10)

    store.add_product(product1)
    store.add_product(product2)

    store.list_products()

    order = store.create_order()

    order.add_product(product1, 2)
    order.add_product(product2, 3)

    total = order.calculate_total()
    print(f"Общая стоимость заказа: {total}")

    order.remove_product(product1, 1)

    order.return_product(product2, 2)

    store.list_products()

    total = order.calculate_total()
    print(f"Общая стоимость заказа после изменений: {total}")
