print('str - napis')

s = 'Ala ma kota'
s2 = 'Ola ma psa'
print(s[4])
print(s[4:6])
print(s + s)
print(s + s2)
print(10 * s)
print(s * 5)
# print(s * s2) - niepoprawne

print('int - liczba całkowita')
i = 7
print(7 + 4)
print(7 / 4) # dzielenie z ułamkiem
print(7 // 4) # dzielenie całkowitoliczbowe
print(-7 // 4) # zawsze w dół (w kierunku minus nieskończoności)
print(7 % 4) # reszta z dzielenia
print(-7 % 4)
# print(i[3]) - niepoprawne

print(10000 ** 1000)
# operatory opisane w podręczniku

print('float - liczba "zmiennoprzecikowa" (floating point)')
# float w Pythonie = double z Javy / C
print(3 * 1.2)

# Dla pieniędzy w Pythonie profesjonalnie używamy klasy Decimal

print('bool - wartość logiczna')
b = True
print(b)
b = False
print(b)

x = 123
b = x > 100
print(b) # True
b = 2*x > 500
print(b) # False

x = 5
b = bool(x)
print(b)

b = x != 0
print(b)

x = 7
print(1 < x < 10)
print(1 < x and x < 10)
