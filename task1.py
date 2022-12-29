#1
num = int(input('Введите номер дня недели: '))
if num == 6 or num ==7:
    print('Выхдной день')
elif num >=1 and num <=5:
    print('Будний день')
else:
    print('Неверный ввод')
