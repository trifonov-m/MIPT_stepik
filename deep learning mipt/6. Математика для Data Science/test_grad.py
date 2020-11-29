import numpy as np


def grad_descent_v1(func, deriv, start=None, callback=None):
    """
    Реализация градиентного спуска для функций с одним локальным минимумом,
    совпадающим с глобальным. Все тесты будут иметь такую природу.
    :param func: float -> float — функция
    :param deriv: float -> float — её производная
    :param start: float — начальная точка
    """
    if start is None:
        # Если точка не дана, сгенерируем случайную
        # из стандартного нормального распределения.
        # При таком подходе начальная точка может быть
        # любой, а не только из какого-то ограниченного диапазона
        np.random.seed(179)
        start = np.random.randn()

    if deriv(start) > 0:
        epsilon = -0.001
    else:
        epsilon = 0.001

    x = start
    F_der = deriv(x)
    while abs(F_der) != 10*(-2):
        x += epsilon
        F_der = deriv(x)
        callback(x, func(x))  # не забывайте логировать шаги!
    return x