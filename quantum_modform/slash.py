from sage.all import *


def construct_multiplier(N, values_on_gens):
    """
    For given values on generators of Gamma_0(N), return the corresponding multiplier system.
    It does not check the compatibility of the values.
    The values should be given as elements of the `UniversalCyclotomicField`.
    """
    F = Gamma0(N).farey_symbol()
    assert len(F.generators()) == len(values_on_gens)
    def multiplier(gamma):
        assert gamma in Gamma0(N)
        exps = F.word_problem(gamma, output='syllables')
        r = 1
        for idx, exp in exps:
            r *= values_on_gens[idx] ** exp
        return r
    return multiplier


def slash(f, k, chi, gamma):
    """Slash action of a function with weight k and a multiplier system chi"""
    m_const = 1 / chi(gamma)
    a, b, c, d = gamma[0][0], gamma[0][1], gamma[1][0], gamma[1][1]
    def f_gamma(x):
        gamma_x = (a * x + b) / (c * x + d)
        return m_const * abs(c * x + d) **(-k) * f(gamma_x)
    return f_gamma


def error(f, k, chi, gamma):
    return lambda x: f(x) - slash(f, k, chi, gamma)(x)
