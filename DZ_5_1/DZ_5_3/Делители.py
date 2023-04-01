numbers = {10, 15, 20}
divisors = {number: set(divisor for divisor in range(1, number+1) if number % divisor == 0) for number in numbers}
print(divisors)  # выведет {10: {1, 2, 5, 10}, 15: {1, 3, 5, 15}, 20: {1, 2, 4, 5, 10, 20}}
