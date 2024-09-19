import math


def my_pi(desired_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    a = 1
    b = 1 / (math.sqrt(2))
    t = 1 / 4
    p = 1

    while True:
        a_n1 = (a + b) / 2
        b_n1 = math.sqrt(a * b)
        t_n1 = t - (p * (math.pow((a_n1 - a), 2)))
        p_n1 = 2 * p

        a = a_n1
        b = b_n1
        t = t_n1
        p = p_n1

        pi_estimate = (math.pow((a_n1 + b_n1), 2)) / (4 * t_n1)
        if abs(math.pi - pi_estimate) < desired_error:
            return pi_estimate



desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
