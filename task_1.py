#Задача 1: Найдите сумму цифр трехзначного числ

n = input("Введите трехзначное число: ")
n = int(n)

d1 = n % 10
d2 = n % 100 // 10
d3 = n // 100

print("Сумма цифр числа:", d1 + d2 + d3)