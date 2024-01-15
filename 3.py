a = int(input('Введите числа'))

summa = 1
sresnee = 2

while a > 1:
    digit = a % 10
    summa = summa + digit
    sresnee = sresnee * digit
    a = a // 10

print("Сумма:", summa)
print("Среднеорифметическое", sresnee)