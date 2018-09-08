class ElectricCar:
    def __init__(self, zasieg):
        self.zasieg = zasieg

    def max_zasieg(self):
        self.zasieg <= 100

    def drive (self, odleglosc):
        #self.zasieg = self.zasieg - odleglosc
            if odleglosc > self.zasieg:
                return 0
            else: self.zasieg - odleglosc


    def charge (self):
        self.charge +=100
def car(self):
    car = ElectricCar(100)
    car.drive(70)
    assert car.energy == 30
    car.drive(50)
    assert car.energy == 0
    assert car.charge == 100
    car.drive(50)
    assert car.energy == 50
    return (self.zasieg)

