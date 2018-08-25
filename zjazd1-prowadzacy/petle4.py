x = 0

# Pętla wygląda jak nieskończona, ale jest przerywana za pomocą break
while True:
    x += 1
    print(f'x = {x}')
    if x == 50:
        print('Pętla zostaje przerwana')
        break
    print('Pętla działa dalej')
    
print('Koniec')
