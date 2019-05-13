"""
===============
Sample 3d facade plots in Matplotlib
===============

An introduction to 3d facade plots in the pyplot interface.

"""

###############################################################################
# :mod:`matplotlib.pyplot` is a collection of command style functions
# that make matplotlib work like MATLAB.
# :mod:`mpl_toolkits.mplot3d` is a collection of command style functions
# that are used to generate 3D plots.
#
# The only required parameter of :func:`~matplotlib.pyplot.projection_plot`
# command is as follows: an array for the projection options and an array
# specifying the bounds for the x-axis, y-axis, and z-axis respectively.
#
# An empty graph can be generated with added x-, y-, and z-axis arrows
# through origin with arrow pointing towards positive direction by only
# specifying the axes limits. The axes would be labeled X, Y and Z
# automatically.
#
#
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


plt.projection_plot([[-1, 1], [-2, 2], [-3, 3]])

plt.show()

###############################################################################
# :func:`~matplotlib.pyplot.projection_plot` is a versatile command, and will take
# # an arbitrary number of arguments. For example, if you provide an array of
# coordinates to the :func:`~matplotlib.pyplot.projection_plot` command as
# an optional parameter (points), matplotlib assumes it is a sequence of x, y and z
# values. Each subarray will be plotted as a separate point.
#
#
plt.projection_plot([[-3, 3], [-3, 3], [-3, 3]], points=[[2, 2, 2]])

plt.show()

###############################################################################
# If you provide an array of projection options for each point to the
# :func:`~matplotlib.pyplot.projection_plot` command as an optional parameter
# (projection_line_options), matplotlib assumes it is in the order of [
# <dashed/solid>, <color>, <quiver:boolean>].
#
#
plt.projection_plot([[-3, 3], [-3, 3], [-3, 3]], points=[[2, 2, 2]], projection_line_options=[["solid", "red", True]])

plt.show()

###############################################################################
# To plot a line instead of points, you can issue the command with the
# following optional parameter:
#
#
plt.projection_plot([[-3, 3], [-3, 3], [-3, 3]], line_equation="<x,y,z>=<0,0,0>+t<1,1,1>")

plt.show()

###############################################################################
# Line options for the drawn line can be provided in as an optional parameter
# (line_options), as an array. For example, you can issue the command to
# generate a dashed red line:
#
#
plt.projection_plot([[-3, 3], [-3, 3], [-3, 3]], line_equation="<x,y,z>=<0,0,0>+t<1,1,1>", line_options=["dashed", "red"])

plt.show()