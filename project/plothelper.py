#!/usr/bin/env python
"""
Plot helper class to set up various parameters for matplotlib.
This allows the caller to only define the function instead of worrying about setting up various parameters for plotting.

__author__ = "Hide Inada"
__copyright__ = "Copyright 2018, Hide Inada"
__license__ = "The MIT License"
__email__ = "hideyuki@gmail.com"
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

# Configurable parameters
IMAGE_WIDTH = 1280  # px
IMAGE_HEIGHT = 720  # px
DPI = 100  # Change image size if you change this.

BASE_TEXT_FONT = 'serif'
TITLE_COLOR = '#111111'
TITLE_FONT_SIZE = 16

NO_DATA_POINTS = 100  # Number of data points to plot
NO_DATA_POINTS_3D = 50  # Number of data points to plot per coordinate. This number will be squared to make a mesh


class PlotHelper():
    @staticmethod
    def plot(f,
             plot_title="",
             x_coord_min=-5,
             x_coord_max=5,
             y_coord_min=-1,
             y_coord_max=10,
             dimensions=2):
        """
        Plot the function using matplotlib.

        You can pass a function or a list of functions.  Type check is done internally to determine
        the data type of the first argument and plots multiple graphs if a list of functions are passed.

        Parameters
        ----------
            f: function or list
                Function to plot, or a list of functions
            plot_title: str
                Title of the plot.  TeX notation is supported
            x_coord_min: int
                Minimum value of x-coordinate
            x_coord_max: int
                Maximum value of x-coordinate
            y_coord_min: int
                Minimum value of y-coordinate
            y_coord_max: int
                Maximum value of y-coordinate
            dimensions: int
                Dimension of the plot.  Only 2 and 3 are supported.


        Raises
        ------
            NotImplementedError
                If a value other than 2 or 3 is specified in dimensions.
        """

        if dimensions not in (2, 3):
            raise NotImplementedError("Only 2-D and 3-D plots are supported")

        # Set up Tex to use in title and text.
        plt.rc('text', usetex=True)
        plt.rc('font', family=BASE_TEXT_FONT)

        fig = plt.figure(figsize=(IMAGE_WIDTH / DPI, IMAGE_HEIGHT / DPI),
                         dpi=DPI)  # fig size is in inch

        if dimensions == 3:
            ax = fig.add_subplot(111,
                                 xlabel='x',
                                 ylabel='y',
                                 zlabel='z',
                                 projection='3d')
            title_pad = 40  # adjust this if you still see your title overlapping the plot

        else:  # 2-D
            ax = fig.add_subplot(111,  # 1 row high, 1 col wide at index #1
                                 aspect='equal',
                                 autoscale_on=False,
                                 xlabel='x',
                                 ylabel='y')

            ax.axhline(color='#000000')  # draw x-axis in black
            ax.axvline(color='#000000')  # draw y-axis in black
            title_pad = 0

        plt.title(plot_title, fontsize=TITLE_FONT_SIZE, color=TITLE_COLOR, pad=title_pad)

        plt.xlim(x_coord_min, x_coord_max)
        plt.ylim(y_coord_min, y_coord_max)

        plt.xticks(np.arange(x_coord_min, x_coord_max + 1, 1))  # Interval is 1. Add 1 to include the end point.
        plt.yticks(np.arange(y_coord_min, y_coord_max + 1, 1))
        plt.grid()

        if dimensions == 3:
            x = np.linspace(x_coord_min, x_coord_max, NO_DATA_POINTS_3D)
            y = np.linspace(y_coord_min, y_coord_max, NO_DATA_POINTS_3D)

            x_mesh, y_mesh = np.meshgrid(x, y)

            # If a list of lambda is passed, plot for each function
            if isinstance(f, list):
                for actual_f in f:
                    z = actual_f(x_mesh, y_mesh)
                    ax.plot_surface(x_mesh, y_mesh, z)
            else:
                z = f(x_mesh, y_mesh)
                ax.plot_surface(x_mesh, y_mesh, z)

        else:  # 2-D
            x = np.linspace(x_coord_min, x_coord_max, NO_DATA_POINTS)

            # If a list of lambda is passed, plot for each function
            if isinstance(f, list):
                for actual_f in f:
                    y = actual_f(x)
                    plt.plot(x, y)
            else:
                y = f(x)
                plt.plot(x, y)

        plt.show()
