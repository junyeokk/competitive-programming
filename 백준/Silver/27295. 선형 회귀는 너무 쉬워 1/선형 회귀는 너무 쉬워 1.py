from fractions import Fraction

n, b = map(int, input().split())

sx, sy = 0, 0

for i in range(n):
    x, y = map(int, input().split())
    sx += x
    sy += y

if sx == 0:
    print("EZPZ")
else:
    num = sy - n * b
    den = sx
    f = Fraction(num, den)
    if f.denominator == 1:
        print(f.numerator)
    else:
        print(f"{f.numerator}/{f.denominator}")
