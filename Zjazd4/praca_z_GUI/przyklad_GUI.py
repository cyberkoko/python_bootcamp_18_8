import tkinter


def zlacz_napisy():
    a=a_entry.get()
    b=b_entry.get()
    wynik_labe.configure(text=f"Wynik:{a+b}")

def czysc_napisy():
    print(locals())
    print(globals())
    wynik_labe.configure(text="wynik")


root = tkinter.Tk()
root.title("Prosty kalkulator")

a_label = tkinter.Label(master=root, text="a")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()
b_label = tkinter.Label(master=root, text="b")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()



wynik_labe = tkinter.Label(master=root,text="wynik: -")
wynik_labe.pack()


dodaj_butto=tkinter.Button(master=root,text="Dodaj",command=zlacz_napisy)
dodaj_butto.pack()


czysc_napisy=tkinter.Button(master=root,text="Czysc",command=czysc_napisy)
czysc_napisy.pack()



root.mainloop()


