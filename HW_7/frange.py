from decimal import Decimal


class frange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            stop = start
            start = 0
        self.start = Decimal(start)
        self.stop = Decimal(stop)
        self.step = Decimal(step)

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        current = self.current
        self.current += self.step
        return float(current)


# Приклад використання
for i in frange(1, 100, 3.5):
    print(i)

###
assert (list(frange(5)) == [0, 1, 2, 3, 4])
assert (list(frange(2, 5)) == [2, 3, 4])
assert (list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert (list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert (list(frange(1, 5)) == [1, 2, 3, 4])
assert (list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert (list(frange(0, 0)) == [])
assert (list(frange(100, 0)) == [])

print('SUCCESS!')
