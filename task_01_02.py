plates = int(input())
cleanser = float(input())
dose = 0.5
counter = 0

while cleanser and plates:
    plates -= 1
    cleanser -= dose
    counter += 1
if not plates and not cleanser:
    print('Все тарелки вымыты, моющее средство закончилось')
elif not plates:
    print('Все тарелки вымыты. Осталось', cleanser, 'ед. моющего средства')
else:
    print('Моющее средство закончилось. Осталось', plates, 'тарелок')