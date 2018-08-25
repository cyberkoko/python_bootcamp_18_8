#skarbonka
skarb=0
while skarb < 100:   
    wpłata = int(input('Ile wpłacasz ?'))
    skarb += wpłata
    print(f'Po wpłaceniu {wpłata} zł w skarbonce jest {skarb} zł')
print(f'Udało sie uzbierać {skarb} zł')
