def runge_kutta_4(f, x0, y0, x_end, h):
    x = x0
    y = y0
    while x < x_end:
        if x + h > x_end:
            h = x_end - x
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
    return y

def f(x, y):
    return 2 * x

x0 = 0
y0 = 1
x_end = 1
h = 0.1

rk4_result = runge_kutta_4(f, x0, y0, x_end, h)

analytic_result = x_end**2 + 1

print("Метод Рунге-Кутта 4 порядка: y(1) =", rk4_result)
print("Аналитическое решение: y(1) =", analytic_result)
print("Погрешность:", abs(rk4_result - analytic_result))