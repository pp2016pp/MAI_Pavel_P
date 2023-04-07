n = int(input())
l = int(input())
title = ""
for i in range(n):
  s = input().strip()
  if len(title) + len(s) > l:
    title = title.strip()
    break
  else:
    title += s + " "
title = title.strip()
if len(title) < len(s):
  title += "..."
print(title)
