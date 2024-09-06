from math import ceil


def poch(a, q, n):
    # Compute the Pochhammer symbol (a; q)_n.
    p = 1
    for i in range(n):
        p *= 1 - a * q**i
    return p

def rats(N, low=-1, high=1, exclude=[]):
    # list of rationals of denominator <= N, in [low, high)
    m_low = int(ceil(low * N))
    m_high = int(ceil(high * N))
    return [m/N for m in range(m_low, m_high) if m/N not in exclude]
