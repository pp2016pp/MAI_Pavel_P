class Dog ():
  def __init__(self, breed):
    self.breed = breed
    

snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")

scoobydoo.bark = lambda: "Woof"

# Tests
# --------------------------
import codewars_test as test
from solution import snoopy, scoobydoo

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(snoopy.bark(), "Woof")
        test.assert_equals(scoobydoo.bark(),"Woof")