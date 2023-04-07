n = int(input())
toys = {}
for i in range(n):
    line = input().split(': ')
    name = line[0]
    toys_list = line[1].split(', ')
    for toy in toys_list:
        if toy in toys:
            toys[toy].add(name)
        else:
            toys[toy] = {name}

unique_toys = [toy for toy, children in toys.items() if len(children) == 1]
unique_toys.sort()

for toy in unique_toys:
    print(toy)

