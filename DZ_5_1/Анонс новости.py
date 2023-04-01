n = int(input())
L = int(input())

for i in range(n):
    title = input().strip()
    title_words = title.split()
    shortened_title = ""
    for word in title_words:
        if len(shortened_title) + len(word) + 3 <= L:
            shortened_title += word + " "
        else:
            shortened_title = shortened_title.strip() + "..."
            break
    if len(shortened_title) < L:
        shortened_title = shortened_title.strip() + "..."
    print(shortened_title)
