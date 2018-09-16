




class Animal:
    def __init__(self, name, age, sound= "knock knock"):
        self.name = name
        self.age = age
        self.sound = sound
    def sound (self):
        return self.sound



def test_animal():
    animal = Animal('Strange somthings',1000)
    assert animal.name =="Strange somthings"
    assert animal.age == 1000
    assert animal.sound() == "knock knock"






