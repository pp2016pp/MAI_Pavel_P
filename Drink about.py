"""def array_madness(a,b):
    for i in range(len(a)):
        a[i]=a[i]**2
    for i in range(len(b)):
        b[i]=b[i]**3
    if sum(a)>sum(b):
        return True
    else:
        return False

import codewars_test as test
from solution import array_madness

@test.describe("Array Madness")
def fixed_tests():
    @test.it('Simple Test Cases')
    def simple_test_cases():
        test.assert_equals(array_madness([4, 5, 6], [1, 2, 3]),True)
        test.assert_equals(array_madness( [1, 2, 3],[4, 5, 6]),False)"""


"""Дети пьют пунш.
Подростки пьют кока-колу.
Молодые люди пьют пиво.
Взрослые пьют виски.

Дети младше 14 лет.
Подростки младше 18 лет.
Молодые люди в возрасте до 21 года.
У взрослых их 21 или больше."""


"""drinks_dict = {
    "14": "toddy",
    "18": "coke",
    "21": "beer",
    "22": "whisky"
}"""


def drink(age):
    if age < 14:
        print("drink toddy") # В задаче print меняем на return
    elif age < 18:
        print("drink coke")
    elif age < 21:
        print("drink beer")
    else:
        print("drink whisky")

drink(13)
drink(17)
drink(18)
drink(20)
drink(30)



