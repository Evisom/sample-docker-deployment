class SampleClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return SampleClass(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return SampleClass(self.x - other.x, self.y - other.y)