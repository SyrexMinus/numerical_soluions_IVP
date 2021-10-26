from numpy import arange


def y_prime(x, y_):
    try:
        return (y_ ** 2 - y_) / x
    except OverflowError:
        return float("inf")


def y(x):
    if x == 0:
        raise Exception(f"Function does not exist at point x={x}")
    try:
        return 1 / (abs(x) + 1)
    except OverflowError:
        return float("inf")


class y_i:
    def __init__(self, step, f, y0, x0):
        self.step = step
        self.f = f
        self.value = y0
        self.x = x0

    def next(self):
        raise NotImplementedError


class y_i_euler(y_i):
    def next(self):
        self.value = self.value + self.step * self.f(self.x, self.value)
        self.x += self.step
        return self.value


class y_i_imp_euler(y_i):
    def next(self):
        self.value = self.value + self.step / 2 * (self.f(self.x, self.value) + self.f(self.x + self.step,
                                                                                       self.value + self.step * self.f(
                                                                                           self.x, self.value)))
        self.x += self.step
        return self.value


class y_i_runge_kutta(y_i):
    def next(self):
        k1 = self.f(self.x, self.value)
        k2 = self.f(self.x + self.step / 2, self.value + self.step * k1 / 2)
        k3 = self.f(self.x + self.step / 2, self.value + self.step * k2 / 2)
        k4 = self.f(self.x + self.step, self.value + self.step * k3)
        self.value = self.value + self.step / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        self.x += self.step
        return self.value


def truncation_error(actual, approximate):
    return abs(actual - approximate)


def get_solutions_info(x0, y0, X, step_number):
    x0_ = x0
    y0_ = y0
    X_ = X
    step = (X_ - x0_) / step_number
    if 0.0 in arange(x0_, X_ + step, step):
        x0_ += 0.00001
        X_ += 0.00001
    my_y_i_euler = y_i_euler(step, y_prime, y0_, x0_)
    my_y_i_imp_euler = y_i_imp_euler(step, y_prime, y0_, x0_)
    my_y_i_RK = y_i_runge_kutta(step, y_prime, y0_, x0_)
    xs = [x0_]
    exact_ys = [y0_]
    euler_ys = [y0_]
    imp_euler_ys = [y0_]
    RK_ys = [y0_]
    euler_LTEs = [0]
    imp_euler_LTEs = [0]
    RK_LTEs = [0]
    euler_GTEs = [0]
    imp_euler_GTEs = [0]
    RK_GTEs = [0]

    current_x = round(x0_ + step, 5)
    while current_x <= X_:
        prev_x = xs[len(xs) - 1]
        prev_exact_y = exact_ys[len(exact_ys) - 1]
        current_y = y(current_x)

        current_euler_y = my_y_i_euler.next()
        current_imp_euler_y = my_y_i_imp_euler.next()
        current_RK_y = my_y_i_RK.next()

        local_euler_y = y_i_euler(step, y_prime, prev_exact_y, prev_x).next()
        local_imp_euler_y = y_i_imp_euler(step, y_prime, prev_exact_y, prev_x).next()
        local_RK_y = y_i_runge_kutta(step, y_prime, prev_exact_y, prev_x).next()

        euler_LTE = truncation_error(current_y, local_euler_y)
        imp_euler_LTE = truncation_error(current_y, local_imp_euler_y)
        RK_LTE = truncation_error(current_y, local_RK_y)

        euler_GTE = truncation_error(current_y, current_euler_y)
        imp_euler_GTE = truncation_error(current_y, current_imp_euler_y)
        RK_GTE = truncation_error(current_y, current_RK_y)

        xs.append(current_x)
        exact_ys.append(current_y)
        euler_ys.append(current_euler_y)
        imp_euler_ys.append(current_imp_euler_y)
        RK_ys.append(current_RK_y)
        euler_LTEs.append(euler_LTE)
        imp_euler_LTEs.append(imp_euler_LTE)
        RK_LTEs.append(RK_LTE)
        euler_GTEs.append(euler_GTE)
        imp_euler_GTEs.append(imp_euler_GTE)
        RK_GTEs.append(RK_GTE)
        current_x = round(current_x + step, 5)

    exact_d = {'x': xs, 'y(exact)': exact_ys}
    euler_d = {'x': xs, 'y(exact)': exact_ys, 'y(Euler)': euler_ys, 'LTE': euler_LTEs,
               'GTE': euler_GTEs}
    imp_euler_d = {'x': xs, 'y(exact)': exact_ys, 'y(ImpEuler)': imp_euler_ys, 'LTE': imp_euler_LTEs,
                   'GTE': imp_euler_GTEs}
    RK_d = {'x': xs, 'y(exact)': exact_ys, 'y(RK)': RK_ys, 'LTE': RK_LTEs,
            'GTE': RK_GTEs}
    return exact_d, euler_d, imp_euler_d, RK_d


def calculate_total_errors(x0, y0, X, step_range_start, step_range_end):
    ns = [i for i in range(step_range_start, step_range_end + 1)]
    euler_total_errors = []
    imp_euler_total_errors = []
    RK_total_errors = []
    for step_number in ns:
        exact_d, euler_d, imp_euler_d, RK_d = get_solutions_info(x0=x0, y0=y0, X=X, step_number=step_number)
        euler_total_errors.append(max(euler_d['GTE']))
        imp_euler_total_errors.append(max(imp_euler_d['GTE']))
        RK_total_errors.append(max(RK_d['GTE']))

    euler_return = {'ns': ns, 'TE': euler_total_errors}
    imp_euler_return = {'ns': ns, 'TE': imp_euler_total_errors}
    RK_return = {'ns': ns, 'TE': RK_total_errors}
    return euler_return, imp_euler_return, RK_return
