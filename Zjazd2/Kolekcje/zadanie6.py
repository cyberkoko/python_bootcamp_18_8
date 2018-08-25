

"""

liczby = [5,2,1,4,3]

min_=None
max_=None

for i in range(len(liczby)):

    print (i, liczby[i])

"""
'''
min_=None
max_=None

liczby = [5,2,1,4,3]

for i in range(len(liczby)):
    if min_ is None or liczby[i] < liczby[min_]:
        min_ = i
    elif i > min_:
        min_ = i
print(min_)

for i in range(len(liczby)):
    if max_ is None or liczby[i]  liczby[min_]:
        max_ = i
    elif i < max_:
        max_ = i
print(max_)

x=min_
y=max_
poprawne na koncu

'''
min_=None
max_=None

liczby = [5,2,1,4,3]
print('liczby',liczby)
for i in range(len(liczby)):
    if min_ is None or liczby[i] < liczby[min_]:
        min_ = i
    if max_ is None or liczby[i] > liczby[max_]:
        max_ = i


tmp = liczby[min_]
liczby[min_] = liczby[max_]
liczby[max_] = tmp

print('liczby', liczby)