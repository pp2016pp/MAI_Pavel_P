n = int(input())
employees = {}

for i in range(n):
    surname = input().strip()
    if surname not in employees:
        employees[surname] = 0
    employees[surname] += 1

count = 0
for surname in sorted(employees.keys()):
    if employees[surname] > 1:
        count += 1
        print(surname + ': ' + str(employees[surname]))

if count == 0:
    print('Однофамильцев нет')
