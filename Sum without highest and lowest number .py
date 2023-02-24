import codewars_test as test
from solution import sum_array

def sum_array(arr):
    if arr == None or 3 > len(arr):
        return(0)
    arr.remove(max(arr))
    arr.remove(min(arr))
    return (sum(arr))

test.assert_equals(sum_array([-6, -20, -1, -10, -12]), -28)

"""
import codewars_test as test
from solution import sum_array

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('None or Empty')
    def basic_test_cases():
        test.assert_equals(sum_array(None), 0)
        test.assert_equals(sum_array([]), 0)

    @test.it("Only one Element")
    def one_test_cases():
        test.assert_equals(sum_array([3]), 0)
        test.assert_equals(sum_array([-3]), 0)

    @test.it("Only two Element")
    def two_test_cases():
        test.assert_equals(sum_array([3, 5]), 0)
        test.assert_equals(sum_array([-3, -5]), 0)

    @test.it("Real Tests")
    def real_test_cases():
        test.assert_equals(sum_array([6, 2, 1, 8, 10]), 16)
        test.assert_equals(sum_array([6, 0, 1, 10, 10]), 17)
        test.assert_equals(sum_array([-6, -20, -1, -10, -12]), -28)
        test.assert_equals(sum_array([-6, 20, -1, 10, -12]), 3) """