def poch(a, q, n):
    # Compute the Pochhammer symbol (a; q)_n.
    p = 1
    for i in range(n):
        p *= 1 - a * q**i
    return p

def rats(N, exclude=[]):
    # list of rationals of denominator <= N, in [-1, 1]
    return [m/N for m in range(-N, N + 1) if m/N not in exclude]
