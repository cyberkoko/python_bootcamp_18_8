from Zjazd3.zad2pro import Employee


class PremiumEmployee(Employee):

    def __init__(self, name='Jan', lastname='Kowalski', wage=500, bonus=0):
        super().__init__(name, lastname, wage)
        self.bonus = bonus

    def give_bonus(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        sal = super(PremiumEmployee, self).pay_salary()  # super().pay_salary <---tez zadziala
        sal += self.bonus
        self.bonus = 0
        return sal

    @classmethod
    def create_hero(cls):
        return PremiumEmployee('pracownik', 'miesiaca', 0, 0)

    @classmethod
    def emp_from_string(cls, str_param):
        list_param = str_param.split(';')
        return PremiumEmployee(list_param(0), list_param(1), list_param(2))
    @staticmethod
    def say_hello():
        return 'Hello'



def test_import_from_text():
    param = 'Henryk', 'Zdun', '50'
    emp = PremiumEmployee.emp_from_string(param)
    assert emp.name == 'Hanryk'
    assert emp.lastname == 'Zdun'
    assert emp.wage == 50


def test_create():
    emp = PremiumEmployee('Jan', 'Nowak', 100, 2000)
    assert emp.name == 'Jan'
    assert emp.lastname == 'Nowak'
    assert emp.wage == 100
    assert emp.bonus == 2000


def test_register():
    emp = PremiumEmployee('Jan', 'Nowak', 100)
    emp.register_time(5)
    emp.give_bonus(1000)
    emp.give_bonus(400)
    assert emp.bonus == 1400
    assert emp.pay_salary() == 1900


def test_employee_of_the_month():
    emp = PremiumEmployee.create_hero()
    assert emp.pay_salary() == 0
