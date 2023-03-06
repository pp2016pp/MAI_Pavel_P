import re


def hydrate(drink_string):
    numbers = re.findall(r'\d+', drink_string)
    count_glasses = str(sum(map(int, numbers)))
    if int(count_glasses) > 1:
        return count_glasses + ' glasses of water'
    return count_glasses + ' glass of water'
