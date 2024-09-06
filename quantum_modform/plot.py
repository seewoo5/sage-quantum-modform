from sage.all import *

from .utils import rats


def plot_func(func, N=100, low=-1, high=1, real_or_imag="both", exclude=[], join_points=True):
    rs = rats(N, low=low, high=high, exclude=exclude)
    if real_or_imag in ["both", "real"]:
        pts_S_real = [(x, float(func(x).real())) for x in rs]
        if join_points:
            scp_S_real = list_plot(pts_S_real, plotjoined=True, markersize=1, color="blue", legend_label="real")
        else:
            scp_S_real = scatter_plot(pts_S_real, markersize=1, facecolor="blue", edgecolor="blue")
    if real_or_imag in ["both", "imag"]:
        pts_S_imag = [(x, float(func(x).imag())) for x in rs]
        if join_points:
            scp_S_imag = list_plot(pts_S_imag, plotjoined=True, markersize=1, color="red", legend_label="imag")
        else:
            scp_S_imag = scatter_plot(pts_S_imag, markersize=1, facecolor="red", edgecolor="red")
    
    if real_or_imag == "real":
        return scp_S_real
    if real_or_imag == "imag":
        return scp_S_imag
    if real_or_imag == "both":
        return scp_S_real + scp_S_imag
