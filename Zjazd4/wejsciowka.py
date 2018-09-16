class Animal:
    def __init__ (self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def anima_sound(cls):
        return ('sound')

class Dog:
    def __init__(self,dog_sound):
        self.dog_sound = dog_sound


class Cat:
    def __init__(self, cat_sound):
        self.cat_sound = cat_sound



"""
animal = Animal("Strange something", 1000)
animal.name
"Strange something"
animal.age
1000
animal.sound()
"knock knock"
   #  Stwórz klasy Dog i Cat, które dziedziczą po Animal i przeciążają metodę sound tak, że:

cat = Cat("Albert", 5)
dog = Dog("Nina", 6)
dog.sound()
 "how how"
cat.sound()
"... (sorry - that's cat!)"
        # Przeciaż operator >  tak by, można było porównywać wiek:
 cat > dog
 True
 >>> dog > animal
 False
"""