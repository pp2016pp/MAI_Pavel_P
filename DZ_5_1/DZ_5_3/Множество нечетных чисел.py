numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds = {x for x in numbers if x%2==1}
print(odds)  # выведет {1, 3, 5, 7, 9}
