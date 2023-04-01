numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares = {x for x in numbers if (int(x**0.5))**2 == x}
print(squares)  # выведет {1, 4, 9, 16, 25, 36, 49, 64, 81, 100}
