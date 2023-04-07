# Рекурсивная функция для нахождения НОД двух чисел
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Считываем последовательность чисел и преобразуем их в список
nums = list(map(int, input().split()))

# Находим НОД для всех чисел в списке с помощью функции reduce()
from functools import reduce
gcd_of_nums = reduce(gcd, nums)

# Выводим результат
print(gcd_of_nums)
