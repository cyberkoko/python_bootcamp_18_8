import tkinter


def spalanie():
    a = int(a_entry.get())
    b = int(b_entry.get())
    c = int(c_entry.get())
    koszt = (c_label / 100) * a_label * b_label

    wynik_label.configure(text=koszt)

    root = tkinter.Tk()
    root.columnconfigure(3, weight=3)
    root.title("Kosztorys przejazdu")

    a_label = tkinter.Label(master=root, text="Podaj spalanie")
    a_label.grid(row=0, column=0)
    a_entry = tkinter.Entry(master=root)
    a_entry.grid(row=0, column=1)
    b_label = tkinter.Label(master=root, text="Podaj cene paliwa")
    b_label.grid(row=1, column=0)
    b_entry = tkinter.Entry(master=root)
    b_entry.grid(row=1, column=1)
    c_label = tkinter.Label(master=root, text="Podaja odległość")
    c_label.grid(row=2, column=0)
    c_entry = tkinter.Entry(master=root)
    c_entry.grid(row=2, column=1)

    dodaj_button = tkinter.Button(master=root, text="Koszt", command=spalanie)
    dodaj_button.grid(row=3, column=1)

    wynik_label = tkinter.Label(master=root, text="Wynik: - ")
    wynik_label.grid(row=4, column=3)

    root.mainloop()
