import numpy as np


def numerical_derivative_2d(func, epsilon):
    """
    Функция для приближённого вычисления градиента функции двух переменных.
    :param func: np.ndarray -> float — произвольная дифференцируемая функция
    :param epsilon: float — максимальная величина приращения по осям
    :return: другая функция, которая приближённо вычисляет градиент в точке
    """

    def grad_func(x):
        """
        :param x: np.ndarray — точка, в которой нужно вычислить производную
        :return: приближённое значение производной в этой точке
        """
        y1_der = (func((x[0] + epsilon, x[1])) - func((x[0], x[1]))) / epsilon
        y2_der = (func((x[0], x[1] + epsilon)) - func((x[0], x[1]))) / epsilon
        return np.array([y1_der, y2_der])

    return grad_func


def grad_descent_2d(func, low, high, callback=None):
    """
    Реализация градиентного спуска для функций двух переменных
    с несколькими локальным минимумами, но известной квадратной окрестностью
    глобального минимума. Все тесты будут иметь такую природу.

    Обратите внимание, что здесь градиент функции не дан.
    Его нужно вычислять приближённо.

    :param func: np.ndarray -> float — функция
    :param low: левая граница интервала по каждой из осей
    :param high: правая граница интервала по каждой из осей
    """

    np.random.seed(179)
    start_x = np.random.uniform(low, high, 20)
    np.random.seed(178)
    start_y = np.random.uniform(low, high, 20)
    start = zip(start_x, start_y)

    max_iter = 10 ** 4  # максимальное количество итераций
    abs_tol = 1e-10  # требуемая точность
    base_step = 1  # шаг (к сожалению, выбирается эмпирически)
    epsilon = 10 ** (-10)
    min_list = []
    func_list = []

    for x in start:
        #callback(x, func(x))

        for k in np.arange(max_iter):

            #
            # Считаю необходимым здесь реализовать дробление шага, так как для каждой конкретной
            # функции подбирать свой base_step - это совсем никуда не годится.
            #
            #                     Цель этого дополнения:
            # Гарантировать, чтобы значение функции СТРОГО МОНОТОННО (!) убывало при итерациях.
            # Поможет при "зацикливании", так как автоматически измельчит шаг, если
            # base_step изначально выбран не очень удачно.
            #
            step = base_step
            while True:
                deriv = numerical_derivative_2d(func, epsilon)
                print(deriv(x))
                x_new = x - step * deriv(x)
                if func(x_new) < func(x) or x_new == x:
                    # Первая проверка гарантирует строгую монотонность ("<=" ставить нельзя, возможно "зацикливание")
                    # Вторая проверка позволяет выйти из цикла, если мы уже в локальном минимуме.
                    break
                step *= 0.5  # Параметр дробления можно уменьшить/увеличить. Но особого смысла в этом нет.

            #callback(x_new, func(x_new))

            # Критерий остановки предлагается самый простой:
            if abs(func(x_new) - func(x)) <= abs_tol:
                # print("abs_tol achieved")
                break
            x = x_new
        if x not in min_list:
            min_list.append(x)
            func_list.append(func(x))
    best_x = min_list[func_list.index(min(func_list))]
    return best_x


func = lambda x: (
            -1 / ((x[0] - 1)**2 + (x[1] - 1.5)**2 + 1)
            * np.cos(2 * (x[0] - 1)**2 + 2 * (x[1] - 1.5)**2))
low = -5
high = 5
print(grad_descent_2d(func, low, high, callback=None))
