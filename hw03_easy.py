print('Прудников В. В.')

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print('Задача №1')

def my_round(number, ndigits):
    num = number * (10 ** (ndigits + 1))
    if num % 10 >= 5:
        num = (num // 10 + 1) / (10 ** ndigits)
    else:
        num = (num // 10) / (10 ** ndigits)
    return num


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

print('Задача №2')
def lucky_ticket(ticket):
    if len(str(ticket)) != 6:
        return 'Не может быть счастливым'
    suml = sum([int(i) for i in str(ticket)[:3]])
    #print(suml)
    sumr = sum([int(i) for i in str(ticket)[3:]])
    #print(sumr)
    if suml == sumr:
        return 'lucky'
    else:
        suml != sumr
        return 'not lucky'

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436752))
