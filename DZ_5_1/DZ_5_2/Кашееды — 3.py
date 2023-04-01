n, m = map(int, input().split())
set_manna = {input() for i in range(n)}
set_oatmeal = {input() for i in range(m)}

obj_intersection = set_manna.intersection(set_oatmeal)
obj_difference = set_manna.symmetric_difference(set_oatmeal)
obj_difference.difference_update(obj_intersection)

if obj_difference:
    print('\n'.join(sorted(obj_difference)))
else:
    print("Таких нет")

