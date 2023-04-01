n = int(input())  # ввод количества местностей
objects = set()  # создание пустого множества, где будут храниться объекты

# обработка каждой местности
for i in range(n):
    description = input().split()
    for word in description:
        if word.istitle() and word.isalpha():  # проверка, является ли слово объектом
            objects.add(word)

print('\n'.join(sorted(objects)))  # вывод объектов, разделяя их переносом строки и сортируя алфавитном порядке
