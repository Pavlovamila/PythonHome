# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

day = int(input('Введите день недели 1-7: '))
if day > 7 or day < 1:
     print('Введите с 1-7')
elif day == 6 or day == 7:
    print("Да, это выходной")
else:
     print("Нет, это не выходной")