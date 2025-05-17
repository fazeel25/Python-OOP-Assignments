class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

m = Multiplier(3)
print("Is m callable?", callable(m))
print("Result:", m(10))