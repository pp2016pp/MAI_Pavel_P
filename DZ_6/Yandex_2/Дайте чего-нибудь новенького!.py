n = int(input())
menu = set(input() for _ in range(n))
week = set()
for _ in range(int(input())):
  week.update(input().split()[1:])
uncooked = menu - week
if not uncooked:
  print("Готовить нечего")
else:
  print("\n".join(sorted(uncooked)))
