"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.

Ввод: значение типа <int>
Вывод: единственное значение типа <bool> (True либо False)

Пример:
6
True

7
True

1
False
"""

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def checkNumber(num):
    if 6 <= num <= 7:
        print("True")
    elif 0 < num < 6:
        print("False")
    else:
        print("число вне пределов 7 дней")

num = InputNumbers("Введите число: ")
checkNumber(num)

"""
n = int(input("Введите день недели: ")) # на вход принимаем цифру, переводим ее в целое число
if n in range(1,6): # с помощью оператора if (если) полученное число n ,будет от 1 до 5 и range, который проверяет в диапазоне от 1 до 6, не включая 6
    print(n == range(1,6)) # на печать выведится False
else: # иначе
    print(n != range(1,6)) # на печать выведится True
"""
