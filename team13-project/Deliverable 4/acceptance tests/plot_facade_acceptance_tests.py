import matplotlib.pyplot as plt

# plot a single point with no projection lines from the axes
#plt.projection_plot([[-2,2],[-2,2],[-2,2]], points=[[1,1,1]], projection_line_options=[["None","",""]])

# plot a single point with dashed black projection lines from the axes
# plt.projection_plot([[-2,2],[-2,2],[-2,2]], points=[[1,1,1]], projection_line_options=[["dashed","black",False]])

# plot two points, one with solid red projection lines and one with dashed blue projection lines and arrowheads from the axes
# plt.projection_plot([[-2,2],[-2,2],[-2,2]], points=[[1,1,1],[-1,-1,-1]], projection_line_options=[["solid","red",False],["dashed", "blue", True]])

# plot a dashed black 3d line given as a string 
# plt.projection_plot([[-3,3],[-3,3],[-3,3]], line_equation="<x,y,z>=<0,0,0>+t<1,1,1>", line_options=["solid", "black"])

# plot a solid green 3d line given as a string, and add projection lines two two points on that line, where one is dashed red and the other is solid black with arrowheads
#plt.projection_plot([[-3,3],[-3,3],[-3,3]], points=[[2,2,2],[-2,-2,-2]], projection_line_options=[["dashed","red",False],["solid", "black", True]], line_equation="<x,y,z>=<0,0,0>+t<1,1,1>", line_options=["dashed","green"])

plt.show()