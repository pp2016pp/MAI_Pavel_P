n = int(input())
products = set(input() for _ in range(n))

m = int(input())
recipes = {}
for _ in range(m):
  dish = input()
  required_products = set(input().split()[1:])
  recipes[dish] = required_products

can_cook = set()
for dish, required_products in recipes.items():
  if required_products.issubset(products):
    can_cook.add(dish)

if not can_cook:
  print("Готовить нечего")
else:
  print("\n".join(sorted(can_cook)))
