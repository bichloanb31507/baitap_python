import math

def tinhToan(first, x, mu):
    return first + (((mu + 1) * (mu + 2)) / 2) * x**mu * (-1)**mu

print("Nhập x:")
x = float(input())
print("Nhập k:")
k = int(input())

mu = 1
first = 1
second = tinhToan(first, x, mu)

while math.fabs(first - second) > 10**(-k):
    mu = mu + 1
    first = second
    second = tinhToan(first, x, mu)
    
print(f'{first:.3f}')