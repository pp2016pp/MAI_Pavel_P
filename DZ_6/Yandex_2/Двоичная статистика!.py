numbers = input().strip().split()

result = []

for num in numbers:
    num = int(num)
    binary = bin(num)[2:]
    num_of_digits = len(binary)
    num_of_ones = binary.count('1')
    num_of_zeros = num_of_digits - num_of_ones
    result.append({
        'digits': num_of_digits,
        'ones': num_of_ones,
        'zeros': num_of_zeros
    })

print(result)

