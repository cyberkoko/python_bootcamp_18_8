class Product:
    def __init__(self, id, name, price, discount):
        self._id = id
        self._name = name  # <-- teoretycznie jest to prywatne, i nie powinno sie tam zagladac jako niepisana zasada
        self.price = price  # <-- to jest calkowicie publiczne i dostepne dla wszystkich
        self._discount = 0

    @property
    def full_name(self):
        return 'Product: ' + self._name

    @property
    def discount_price(self):
        '''prices after discount'''
        return self.price * (1 - self.discount)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 3:
            self._name = value

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if type(value) == float or type(value) == int:

            if 0 <= value <= 0.3:
                self._discount = value

    @discount.deleter
    def discount(self):

        self._discount = 0


pr1 = Product(1, 'bułka', 10, 20)

print(pr1.price)
print(pr1._id)
print(pr1.full_name)
print(pr1.discount_price)
print(pr1.name)

# atrybut jest chroniony za pomocą property
pr1.name = 'ala ma kota'
print(pr1.name)
print(pr1._name)  # <---tak nie robimy
# nie spelnia property mialo byc dluzsze od 3
pr1.name = 'cos'
print(pr1.name)
print(pr1._name)
print(pr1._discount)
print(pr1.discount_price)

print(pr1.discount)
pr1.discount = 0.3
print(pr1.discount)

print(pr1.discount)

value = 0
print(type(value)) == float

help(Product.discount_price)  # <--- wypisuje co jest wstawione wyzej w potrojny cudzysłów
