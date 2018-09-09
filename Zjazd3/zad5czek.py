class Product:
    def __init__(self, id, name, price):
        self._id = id

        self._name = name

        self.price = price

        self._discount = 0

        def print_info(self):

        prod = f'"{self._name}", id: {self._id}, cena: {self.price} PLN, znizka: {self._discount}%'

        print(prod) \

@property
def full_name(self):
    return 'Product: ' + self._name


@property
def discount_price(self):
    return self.price * self._discount / 100


@property
def name(self):
    return self._name

@name.setter
def name(self, value):
    if len(value) > 3:
        self.name = value


@property
def discount(self):
    return self._discount


@discount.setter
def discount(self, discount):
    if 0 < discount <= 30:
        self._discount = discount
        def test_discount():


product = Product(1, 'Woda', 10.00)

product.print_info()

product.discount = 30

assert product.discount == 30

assert product.discount_price == 3

product.discount = 40

assert product.discount == 30

assert product.discount_price == 3

product.print_info()
