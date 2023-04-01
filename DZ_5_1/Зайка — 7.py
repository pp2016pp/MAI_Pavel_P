n = int(input())
for i in range(n):
    description = input()
    index = description.lower().find('заяц')
    if index != -1:
        print(index + 1)
    else:
        print("NO")