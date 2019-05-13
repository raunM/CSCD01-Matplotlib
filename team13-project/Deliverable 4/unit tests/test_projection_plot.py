import pytest

from mpl_toolkits.mplot3d import Axes3D, axes3d, proj3d, art3d
from matplotlib import cm
from matplotlib import path as mpath
from matplotlib.testing.decorators import image_comparison, check_figures_equal
from matplotlib.cbook.deprecation import MatplotlibDeprecationWarning
from matplotlib.collections import LineCollection, PolyCollection
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import numpy as np

baseline_dir_local = 'baseline_images/test_projection_plot';
def test_projection_plot_invalid_params():
    with pytest.raises(Exception) as excinfo:
        plt.projection_plot([[-2,2],[-2,2],[-2,2]], points=[[1,1,1], [1,-1,1]], projection_line_options=[["dashed","black",False]])
    excinfo.match(r'Number of projection line options different than number of plotted points.')

def test_projection_plot_invalid_params2():
    with pytest.raises(Exception) as excinfo:
        plt.projection_plot([[-2,2],[-2,2],[-2,2]], points=[[1,1,1], [1,-1,1]], projection_line_options=[["dashed","black",False], ["dashed","black",False], ["dashed","black",False]])
    excinfo.match(r'Number of projection line options different than number of plotted points.')
    
def test_projection_plot_fail_invalid_params():
    # Missing axis limit
    with pytest.raises(Exception) as excinfo:
        plt.projection_plot([[-2,2],[-2,2]], points=[[1,1,1], [1,-1,1]], projection_line_options=[["dashed","black",False]])
    excinfo.match(r'Please provides limits for X, Y and Z axes.')

@pytest.mark.mpl_image_compare(baseline_dir=baseline_dir_local, filename='dashed_projection_lines.png')
def test_dashed_projection_lines():
    # Simple case with multiple points dashed black projection lines
    plt.projection_plot([[-2,2],[-2,2],[-2,2]], points=[[1,1,1], [1,-1,1], [-1,1,-1]], projection_line_options=[["dashed","black",False], ["dashed","black",False], ["dashed","black",False]])
    return plt.gcf()

@pytest.mark.mpl_image_compare(baseline_dir=baseline_dir_local, filename='solid_red_arrow_projection_lines.png')
def test_solid_red_arrow_projection_lines():
    # Simple case with multiple points dashed black projection lines
    plt.projection_plot([[-2,2],[-2,2],[-2,2]], points=[[1,-1,1]], projection_line_options=[["solid","red",True]])
    return plt.gcf()

@pytest.mark.mpl_image_compare(baseline_dir=baseline_dir_local, filename='dashed_line.png')
def test_dashed_line():
    plt.projection_plot([[-2,2],[-2,2],[-2,2]], line_equation="<x,y,z>=<0,0,0>+t<1,1,2>", line_options=["dashed", "black"])
    return plt.gcf()

@pytest.mark.mpl_image_compare(baseline_dir=baseline_dir_local, filename='solid_line_blue.png')
def test_solid_line_blue():
    plt.projection_plot([[-2,2],[-2,2],[-2,2]], line_equation="<x,y,z>=<0,0,0>+t<2,2,2>", line_options=["solid", "blue"])
    return plt.gcf()

@pytest.mark.mpl_image_compare(baseline_dir=baseline_dir_local)
def test_projection_line_with_line():
    plt.projection_plot([[-2,2],[-2,2],[-2,2]], points=[[1,1,1], [-1,-1,-1]], projection_line_options=[["dashed","red",False], ["solid","black",True]], 
    line_equation="<x,y,z>=<0,0,0>+t<1,1,1>", line_options=["solid", "green"])
    return plt.gcf()

@pytest.mark.mpl_image_compare(baseline_dir=baseline_dir_local)
def test_empty_figure():
    plt.projection_plot([[-2,2],[-2,2],[-2,2]])
    return plt.gcf()

@pytest.mark.mpl_image_compare(baseline_dir=baseline_dir_local)
def test_zero_size_plot():
    with pytest.warns(UserWarning):
        plt.projection_plot([[0,0],[0,0],[0,0]], points=[[1,1,1], [-1,-1,-1]], projection_line_options=[["dashed","red",False], ["solid","black",True]],  
        line_equation="<x,y,z>=<0,0,0>+t<1,1,1>", line_options=["solid", "green"])
    return plt.gcf()

@pytest.mark.mpl_image_compare(baseline_dir=baseline_dir_local)
def test_invalid_equation():
    plt.projection_plot([[-2,2],[-2,2],[-2,2]], line_equation="<x,y,z>=<0,0,0+t<1,1,1>", line_options=["solid", "green"])
    return plt.gcf()

def test_invalid_equation():
    with pytest.raises(Exception) as excinfo:
        plt.projection_plot([[-2,2],[-2,2],[-2,2]], line_equation="<x,y,=<0,0,0+t<1,1,1>", line_options=["solid", "green"])
    excinfo.match(r'given string representing line does not begin with <x,y,z>=')

@pytest.mark.mpl_image_compare(baseline_dir=baseline_dir_local)
def test_reversed_bounds():
    plt.projection_plot([[2,-2],[2,-2],[2,-2]], points=[[1,1,1], [-1,-1,-1]], projection_line_options=[["dashed","red",False], ["solid","black",True]])
    return plt.gcf()

