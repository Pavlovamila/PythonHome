#Семинар 1.
#1 Напишите программу кот принимает на вход 2 числа и проверяет явл ли одно число квалратом др

#a = int(input())
#b = int(input())

#if a == b**2 or b == a**2:
#    print('ДА')

#else:
#    print('НЕТ')

#Напишите программу кот принимает на вход 5 чисел и находит максимальное из них
#a, b, c, d, e = int(input()), int(input()), int(input())

#print(f'Максимальное число:{max(a,b,c,d,e)}')

#Дано 3-значное число, найти сумму 3 чисел
a = int(input())

print((a % 100 // 10) + (a % 10) + (a // 100))






#Домашнее задание. 
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет
#day = int(input('Введите день недели 1-7: '))
#if day > 7 or day < 1:
#     print('Введите с 1-7')
#elif day == 6 or day == 7:
#    print("Да, это выходной")
#else:
#     print("Нет, это не выходной")