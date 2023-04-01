rle = [('a', 2), ('b', 3), ('c', 1), ('d', 2)]
string = "".join(char * count for char, count in rle)
print(string)  # выведет "aabbbcd"

