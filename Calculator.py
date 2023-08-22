#Комментарий
# Модули
from colorama import init
from colorama import Fore, Back, Style

# Переменные
print(Back.GREEN)
print(Fore.BLACK)
a = input("Первое число:\n")
op = input("Что делаем?(+,-,/,*)\n")
b = input("Второе число:\n")


# Проверка знака
if op == "+":
    c = float(a) + float(b)
elif op == "-":
    c = float(a) - float(b)
elif op == "/":
    c = float(a) / float(b)
elif op == "*":
    c = float(a) * float(b)
else:
    c = 0
print(Back.BLACK)
print(Fore.WHITE)
print("Ответ: " + str(c))

input()