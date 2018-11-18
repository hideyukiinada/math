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
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Configurable parameters
IMAGE_WIDTH = 1280  # px
IMAGE_HEIGHT = 720  # px
DPI = 100  # Change image size if you change this.

BASE_TEXT_FONT = 'serif'
TITLE_COLOR = '#111111'
TITLE_FONT_SIZE = 16

NO_DATA_POINTS = 100  # Number of data points to plot


class PlotHelper():
    @staticmethod
    def plot(f,
             plot_title="",
             x_coord_min=-5,
             x_coord_max=5,
             y_coord_min=-1,
             y_coord_max=10):
        """
        Plot the function using matplotlib

        Parameters
        ----------
            f: function
                Function to plot
            plot_title: str
                Title of the plot.  TeX notation is supported.
            x_coord_min: int
                Minimum value of x-coordinate
            x_coord_max: int
                Maximum value of x-coordinate
            y_coord_min: int
                Minimum value of y-coordinate
            y_coord_max: int
                Maximum value of y-coordinate
        """
        # Set up Tex to use in title and text.
        plt.rc('text', usetex=True)
        plt.rc('font', family=BASE_TEXT_FONT)

        fig = plt.figure(figsize=(IMAGE_WIDTH / DPI, IMAGE_HEIGHT / DPI),
                         dpi=DPI)  # fig size is in inch

        ax = fig.add_subplot(111,  # 1 row high, 1 col wide at index #1
                             aspect='equal',
                             autoscale_on=False,
                             xlabel='x',
                             ylabel='y')

        plt.title(plot_title, fontsize=TITLE_FONT_SIZE, color=TITLE_COLOR)

        plt.xlim(x_coord_min, x_coord_max)
        plt.ylim(y_coord_min, y_coord_max)

        plt.xticks(np.arange(x_coord_min, x_coord_max + 1, 1)) # Interval is 1. Add 1 to include the end point.
        plt.yticks(np.arange(y_coord_min, y_coord_max + 1, 1))
        plt.grid()

        x = np.linspace(x_coord_min, x_coord_max, NO_DATA_POINTS)
        y = f(x)

        ax.axhline(color='#000000') # draw x-axis in black
        ax.axvline(color='#000000') # draw y-axis in black

        plt.plot(x, y)

        plt.show()
