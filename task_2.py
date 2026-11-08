import random


def f(x):
    return x ** 2


def monte_carlo_integral(a, b, points):
    # Для x² найбільше значення на відрізку буде на одному з його кінців.
    height = max(f(a), f(b))
    rectangle_area = (b - a) * height
    under_curve = 0

    for _ in range(points):
        x = random.uniform(a, b)
        y = random.uniform(0, height)
        if y <= f(x):
            under_curve += 1

    return rectangle_area * under_curve / points


if __name__ == "__main__":
    a = 0
    b = 2
    points = 100_000

    # Однакове початкове значення дає повторюваний результат.
    random.seed(42)
    estimate = monte_carlo_integral(a, b, points)
    exact = (b ** 3 - a ** 3) / 3

    print(f"Кількість точок: {points}")
    print(f"Метод Монте-Карло: {estimate:.6f}")
    print(f"Точне значення: {exact:.6f}")
    print(f"Абсолютна похибка: {abs(estimate - exact):.6f}")
