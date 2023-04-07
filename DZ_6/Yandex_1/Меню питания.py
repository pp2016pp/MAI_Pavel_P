n = int(input())
cereals = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
schedule = []
for i in range(n):
    cereal = cereals[i % len(cereals)]
    schedule.append(cereal)
print(schedule)
