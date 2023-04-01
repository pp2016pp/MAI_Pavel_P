n = int(input())
employees = {}

for i in range(n):
    surname = input().strip()
    if surname not in employees:
        employees[surname] = 0
    employees[surname] += 1

count = 0
for surname, occur in employees.items():
    if occur > 1:
        count += 1

print(count)
