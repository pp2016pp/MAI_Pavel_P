n = int(input())
headers = []
for i in range(n):
    headers.append(input())

search_query = input().lower()
for header in headers:
    if header.lower().find(search_query) != -1:
        print(header)
