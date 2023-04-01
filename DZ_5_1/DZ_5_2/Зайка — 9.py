seen = {}

while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if not line:
        break

    words = line.split()

    for word in words:
        if word not in seen:
            seen[word] = 0
        seen[word] += 1

for item in seen.items():
    print(item[0], item[1])
