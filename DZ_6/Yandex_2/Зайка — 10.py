objects = set()

while True:
    line = input().strip()
    if not line:
        break
    words = line.split()
    if 'зайка' in words:
        # Find the index of the word "зайка"
        index = words.index('зайка')

        # If possible, add the object to the left of "зайка"
        if index > 0:
            objects.add(words[index-1])

        # If possible, add the object to the right of "зайка"
        if index < len(words) - 1:
            objects.add(words[index+1])

print(*sorted(objects), sep='\n')
