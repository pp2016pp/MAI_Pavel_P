numbers = [3, 7, 2, 5, 2, 8, 7, 1]
result = " ".join(str(x) for x in sorted(set(numbers)))
print(result)  # выведет "1 2 3 5 7 8"


