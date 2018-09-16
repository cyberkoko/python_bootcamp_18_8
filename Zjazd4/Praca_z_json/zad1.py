import json

baza_employees = ["Imie","Nazwisko","Rok urodzenia"]

# zapis do pliku

with open("employees.json", "w") as f:
    json.dump(baza_employees, f)

# otwarcie pliku
with open("employees.json") as f:

    baza_employees = input("Co chcesz zrobić ? ")
    if baza_employees == 'd':

        input("Imie ")
        input("Nazwisko ")
        input("Rok urodzenia ")
        input("Pensja ")

    if baza_employees == "w":

        print("Lista pracowników jest pusta")


with open("employees.json") as f:
    list = json.load( f)
    print(list)

print(list)

with open("employees.json", 'w') as f:
    json.dump(list, f)




