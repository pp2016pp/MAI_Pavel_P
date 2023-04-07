n = int(input())
points = []
for i in range(n):
    points.append(tuple(map(int, input().split())))

f = [1] * n
for i in range(1, n):
    for j in range(i):
        if ((points[i][0] - points[j][0]) % 10 == 0 and
            (points[i][1] - points[j][1]) % 10 == 0):
            f[i] = max(f[i], f[j] + 1)

print(max(f))
