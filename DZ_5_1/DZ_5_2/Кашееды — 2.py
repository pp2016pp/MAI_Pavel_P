n, m = map(int, input().split())
set_manna = {input() for i in range(n)}
set_oatmeal = {input() for i in range(m)}

obj_difference = set_manna.symmetric_difference(set_oatmeal)
count = 0
for obj in obj_difference:
    if obj in set_manna or obj in set_oatmeal:
        count += 1

if count:
    print(count)
else:
    print("Таких нет")
