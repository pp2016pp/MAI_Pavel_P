def array_madness(a,b):
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
        test.assert_equals(array_madness( [1, 2, 3],[4, 5, 6]),False)