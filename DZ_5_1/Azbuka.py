n = int(input())
words = [input() for i in range(n)]
first_letters = set(['а', 'б', 'в'])
for word in words:
    if word[0] not in first_letters:
        print("NO")
        break
else:
    print("YES")