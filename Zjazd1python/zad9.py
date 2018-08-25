import datetime

# z modułu datetime pobieram klase o tej samej nazwie datetime, 
# dalej idac pobieram z tego klase year aby miec konkretny rok z datetime 


rok_urdzenia = int(input('Podaj rok urodzenia: '))
rok = datetime.datetime.today(). year
if rok-rok_urdzenia >= 18:
    print ('Jesteś pełnoletni!')
else:
    print ('Jesteś niepełnoletni!')
	
#uproscic aby byl rok 2000	

#rok_biezacy = 2018
#wiek = rok_biezacy - liczba

#from datetime import datetime* <-- z modułu pobieram datetime  




