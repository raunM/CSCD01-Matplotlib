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


def test_projection_plot_invalid_params():
    with pytest.raises(Exception) as excinfo:
        projection_plot([[1,1,1], [1,-1,1]],[["dashed","black",False]], [[-2,2],[-2,2],[-2,2]])
    excinfo.match(r'Number of projection line options different than number of plotted points'')

def test_projection_plot_invalid_params2():
    with pytest.raises(ValueError) as excinfo:
        projection_plot([[1,1,1], [1,-1,1]],[["dashed","black",False], ["dashed","black",False], ["dashed","black",False]], [[-2,2],[-2,2],[-2,2]])
    excinfo.match(r'Number of projection line options different than number of plotted points'')
    
def test_projection_plot_fail_invalid_params():
    # Missing axis limit
    with pytest.raises(ValueError) as excinfo:
        projection_plot([[1,1,1], [1,-1,1]],[["dashed","black",False]], [[-2,2],[-2,2]])
    excinfo.match(r'Invalid axis limit.')

@pytest.mark.mpl_image_compare(baseline_dir='baseline_images', filename='dashed_projection_lines.png')
def test_dashed_projection_lines():
    # Simple case with multiple points dashed black projection lines
    projection_plot([[1,1,1], [1,-1,1], [-1,1,-1]],[["dashed","black",False], ["dashed","black",False], ["dashed","black",False]], [[-2,2],[-2,2],[-2,2]])

@pytest.mark.mpl_image_compare(baseline_dir='baseline_images', filename='solid_red_arrow_projection_lines.png')
def test_solid_red_arrow_projection_lines():
    # Simple case with multiple points dashed black projection lines
    projection_plot([[1,-1,1], ["solid","red",True]], [[-2,2],[-2,2],[-2,2]])

@pytest.mark.mpl_image_compare(baseline_dir='baseline_images', filename='dashed_line.png')
def test_dashed_line():
    projection_plot([],[], [[-2,2],[-2,2],[-2,2]], "<x,y,z>=<0,0,0>+t<1,1,2>", ["dashed", "black"])

@pytest.mark.mpl_image_compare(baseline_dir='baseline_images', filename='solid_line_blue.png')
def test_solid_line_blue():
    projection_plot([],[], [[-2,2],[-2,2],[-2,2]], "<x,y,z>=<0,0,0>+t<2,2,2>", ["solid", "blue"])

@pytest.mark.mpl_image_compare(baseline_dir='baseline_images', filename='line_with_projection.png')
def test_projection_line_with_line():
    projection_plot([[1,1,1], [-1,-1,-1]],[["dashed","red",False], ["solid","black",True]], [[-2,2],[-2,2],[-2,2]], 
    "<x,y,z>=<0,0,0>+t<1,1,1>", ["solid", "green"])