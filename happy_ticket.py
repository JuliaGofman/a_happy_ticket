ticket = list(map(int, list(input())))
if sum(ticket[:3]) == sum(ticket[3:]):
    print('Счастливый')
else:
    print('Обычный')