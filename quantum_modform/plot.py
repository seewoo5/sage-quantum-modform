from sage.all import *

from .utils import rats


def plot_func(func, N=100, real_or_imag="both", exclude=[]):
    rs = rats(N, exclude=exclude)
    if real_or_imag in ["both", "real"]:
        pts_S_real = [(x, float(func(x).real())) for x in rs]
        scp_S_real = scatter_plot(pts_S_real, markersize = 10, facecolor="blue")
    if real_or_imag in ["both", "imag"]:
        pts_S_imag = [(x, float(func(x).imag())) for x in rs]
        scp_S_imag = scatter_plot(pts_S_imag, markersize = 10, facecolor="red")
    
    if real_or_imag == "real":
        return scp_S_real
    if real_or_imag == "imag":
        return scp_S_imag
    if real_or_imag == "both":
        return scp_S_real + scp_S_imag
