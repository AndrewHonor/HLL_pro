2. Створити frange ітератор. Який буде працювати з float or Decimal.

class frange:
    pass

for i in frange(1, 100, 3.5):
    print(i)

має вивести

1
4.5
8.0
...


Перед здачею перевірти тести чи проходять:

assert(list(frange(5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])

print('SUCCESS!')

3. Створити context manager який буде фарбувати колір виведеного тексту

https://www.skillsugar.com/how-to-print-coloured-text-in-python

Приклад:

print('\033[93m', end='')
print('aaa')
print('bbb')
print('\033[0m', end='')
print('ccc')

with colorizer('red'):
    print('printed in red')
print('printed in default color')
