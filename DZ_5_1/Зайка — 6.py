n = int(input())
count = 0
for i in range(n):
    description = input()
    if 'зайка' in description.lower():
        count += 1
print(count)