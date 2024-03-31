"""Задание 2

Написать функцию check_phone, которая будет принимать строку и проверять,
что она соответствует шаблону:
1. код страны +375
2. код оператора 29, 33, 44, 25 в скобках
3. три цифры
4. тире
5. две цифры
6. тире
7 две цифры

"""


#Код программы
from re import fullmatch
def check_phone():
    while True:
        phone_number = input(str("Enter your phone number +375(##)###-##-##: "))
        if fullmatch(
            r"\+[3][7][5][(][2][5,9][)]\d\d\d[-]\d\d[-]\d\d|\+[3][7][5][(][3][3][)]\d\d\d[-]\d\d[-]\d\d|\+[3][7][5][(][4][4][)]\d\d\d[-]\d\d[-]\d\d", phone_number
            ):
            print(f"Your phone >>{phone_number}<<")
            break
        else:
            print("Invalid input, please enter again!")
    return phone_number
    
    
check_phone()
