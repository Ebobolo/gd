st = list(map(int, input("Введите элементы списка через пробел: ").split()))
num = int(input("Введите число для подсчета: "))
print("Число {} присутствует {} раз(а) в списке".format(num, st.count(num)))