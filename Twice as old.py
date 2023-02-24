def twice_as_old(dad_years_old, son_years_old):
    twice_as_old = dad_years_old - son_years_old * 2
    if twice_as_old < 0:
        twice_as_old = twice_as_old * (-1)
    return twice_as_old


import codewars_test as test
from solution import twice_as_old

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(twice_as_old(36,7) , 22)
        test.assert_equals(twice_as_old(55,30) , 5)
        test.assert_equals(twice_as_old(42,21) , 0)
        test.assert_equals(twice_as_old(22,1) , 20)
        test.assert_equals(twice_as_old(29,0) , 29)
