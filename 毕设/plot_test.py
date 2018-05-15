import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.contour import ContourSet

try:
    import tkinter as Tk
except ImportError:
    # Backward compat for Python 2
    import Tkinter as Tk

import sys
import numpy as np

class Model(object):
    pass

class Controller(object):
    pass


class View(object):
    """Test docstring. """
    def __init__(self, root):
        f = Figure()
        ax = f.add_subplot(111)
        ax.set_xticks([])
        ax.set_yticks([])
        # ax.set_xlim((x_min, x_max))
        # ax.set_ylim((y_min, y_max))
        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.show()
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        canvas.mpl_connect('button_press_event', self.onclick)
        toolbar = NavigationToolbar2TkAgg(canvas, root)
        toolbar.update()
        # self.controllbar = ControllBar(root, controller)
        self.f = f
        self.ax = ax
        self.canvas = canvas
        # self.controller = controller
        self.contours = []
        self.c_labels = None
        # self.plot_kernels()

class ControllBar(object):
    def __init__(self, root, controller):
        fm = Tk.Frame(root)
        bspline_group = TK.Frame(fm)
        
        Tk.Radiobutton(kernel_group, text="均匀", variable=controller.kernel,
                       value=0, command=controller.refit).pack(anchor=Tk.W)
        Tk.Radiobutton(kernel_group, text="准", variable=controller.kernel,
                       value=1, command=controller.refit).pack(anchor=Tk.W)
        Tk.Radiobutton(kernel_group, text="分段", variable=controller.kernel,
                       value=2, command=controller.refit).pack(anchor=Tk.W)
        kernel_group.pack(side=Tk.LEFT)



def main(argv):
    root = TK.Tk()
    root.wm_title("Bspline")
    view = View(root)
    Tk.maninloop()

if __name__ == "__main__":
    P = np.array([[9.036145, 21.084337, 37.607573, 51.893287, 61.187608],
                  [51.779661, 70.084746, 50.254237, 69.745763, 49.576271]])

    n = 4


    # plt.plot(P[0, 0: n+1 ], P[1, 0: n + 1],
    #      'o', 'LineWidth', 1,
    #      'MarkerEdgeColor', 'k',
    #      'MarkerFaceColor', 'g',
    #      'MarkerSize', 6)
    # plt.figure(1)
    # plt.plot(P[0, 0: n+1 ], P[1, 0: n + 1],
    #     'bo')

    fig = Figure()
    ax = fig.add_subplot(111)
    ax.set_title("OO")
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.show()
    

    
    
