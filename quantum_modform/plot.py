from bisect import bisect

from sage.all import *

from .utils import rats


def divide_list(ls, points=[]):
    """Divide a sorted list `ls` into several lists, where the division points are given by `points`."""
    result = []
    prev_index = 0
    for point in points:
        index = bisect(ls, point)
        result.append(ls[prev_index:index])
        prev_index = index
    if prev_index < len(ls):
        result.append(ls[prev_index:])
    return result


def plot_func(func, N=100, low=-1, high=1, real_or_imag="both", singular=[], exclude=[], join_points=True):
    """
    Plot a function (error function of a quantum modular form) defined on (a subset of) the rational numbers.

    Args:
        func: a function to plot
        N (int): denominator for the rational numbers
        low (float): lower bound of the domain
        high (float): upper bound of the domain
        real_or_imag (str): "real", "imag", or "both"
        singular (list): a list of singular points where the function is not defined.
            Domain of the plot will be divided by these points, and the function will be plotted on each subdomain.
        exclude (list): a list of additional points to exclude
        join_points (bool): whether to join the adjacent points or not
    """
    rs = rats(N, low=low, high=high, exclude=exclude+singular)
    singular = sorted(singular)
    rs_divided = divide_list(rs, points=singular)
    if real_or_imag in ["both", "real"]:
        scp_real_combined = None
        for rs_sub in rs_divided:
            pts_real = [(x, float(func(x).real())) for x in rs_sub]
            if join_points:
                if scp_real_combined is None:
                    scp_real = list_plot(pts_real, plotjoined=True, markersize=1, color="blue", legend_label="real")
                else:
                    scp_real = list_plot(pts_real, plotjoined=True, markersize=1, color="blue")
            else:
                scp_real = scatter_plot(pts_real, markersize=1, facecolor="blue", edgecolor="blue")
            if scp_real_combined is None:
                scp_real_combined = scp_real
            else:
                scp_real_combined += scp_real
    if real_or_imag in ["both", "imag"]:
        scp_imag_combined = None
        for rs_sub in rs_divided:
            pts_imag = [(x, float(func(x).imag())) for x in rs_sub]
            if join_points:
                if scp_imag_combined is None:
                    scp_imag = list_plot(pts_imag, plotjoined=True, markersize=1, color="red", legend_label="imag")
                else:
                    scp_imag = list_plot(pts_imag, plotjoined=True, markersize=1, color="red")
            else:
                scp_imag = scatter_plot(pts_imag, markersize=1, facecolor="red", edgecolor="red")
            if scp_imag_combined is None:
                scp_imag_combined = scp_imag
            else:
                scp_imag_combined += scp_imag
    
    if real_or_imag == "real":
        return scp_real_combined
    if real_or_imag == "imag":
        return scp_imag_combined
    if real_or_imag == "both":
        return scp_real_combined + scp_imag_combined
