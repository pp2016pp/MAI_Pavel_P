class Human:
    def __init__(self, name):
        self.name = name


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    Eva = Woman('Eva')
    Adam = Man('Adam')
    return [Eva, Adam]
# paradise = God()
# test.assert_equals(isinstance(paradise[0], Man), True, "First object are a man")