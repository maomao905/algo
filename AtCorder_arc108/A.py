S, P = map(int, input().split())

def solv_quadratic_equation(a, b, c):
    D = (b**2 - 4*a*c) ** (1/2)
    x_1 = (-b + D) / (2 * a)
    x_2 = (-b - D) / (2 * a)

    return x_1, x_2

def ok(x):
    return x.is_integer() and x > 0

N,M = solv_quadratic_equation(1,-S,P)

print('Yes' if ok(N) and ok(M) else 'No')
