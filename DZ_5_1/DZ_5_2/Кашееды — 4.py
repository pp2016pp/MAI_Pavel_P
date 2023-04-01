n = int(input())
kasha_dict = {}
for i in range(n):
    line = input().split()
    name = line[0]
    kashas = set(line[1:])
    for kasha in kashas:
        if kasha in kasha_dict:
            kasha_dict[kasha].add(name)
        else:
            kasha_dict[kasha] = {name}

target_kasha = input()
if target_kasha in kasha_dict:
    for name in sorted(kasha_dict[target_kasha]):
        print(name)
else:
    print("Таких нет")
