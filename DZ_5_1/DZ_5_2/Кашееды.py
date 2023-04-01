n, m = map(int, input().split())
set_manna = {input() for i in range(n)}
set_oatmeal = {input() for i in range(m)}

obj_intersection = set_manna.intersection(set_oatmeal)
if obj_intersection:
    print(len(obj_intersection))
else:
    print("Таких нет")
