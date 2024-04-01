"""Задание 1

Написать функцию check_login, которая будет принимать строку и проверять,
что она является логином, который соответствует следующим правилам:
1. Длина от 5 до 20 символов
2. Состоит из букв верхнего и нижнего регистра, цифр, знаков подчеркивания


"""

#Импортируем из модуля регулярок под модуль findall
from re import fullmatch
def check_login():
    login = input(str("Enter login: "))
    if fullmatch(r"\w{5,20}", login):                   #Регулярка на валидность по символам и нижнему "_" ([a-zA-Z0-9_]). Можно дополнить кириллицей [a-zA-ZА-ЯЁа-яё0-9_]
        print(f"Your login >>{login}<<")
    else:
        print("Invalid login, please enter again!")

    
check_login()


#Вариант 2 (где в функцию передаём строковое значение)
from re import fullmatch
def check_login(some_string: str):
    if fullmatch(r"\w{5,20}", some_string):                 
        print(f"Your login >>{some_string}<<")
    else:
        print("Invalid login, please enter again!")

    
check_login("Kifir_1992")

