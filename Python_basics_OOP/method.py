class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"Product name is {self.name} and price is {self.price}")

    @classmethod
    def get_total_product(cls):
        print(f"Total product = {cls.count}")

    @staticmethod
    def calc_price(price, discount):
        f_price = price - (price * discount / 100)
        print(f"Discounted price is = {f_price}")


p2 = Product("Mobile", 100000)
p1 = Product("Tab", 120000)
p3 = Product("Laptop", 300000)

p1.calc_price(p1.price, 10)
p2.get_info()

Product.get_total_product()