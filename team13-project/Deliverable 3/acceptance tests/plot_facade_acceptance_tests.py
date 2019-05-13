# plot a single point with no projection lines from the axes
# projection_plot([[1,1,1]],[["none","",""]], [[-2,2],[-2,2],[-2,2]])

# plot a single point with dashed black projection lines from the axes
# projection_plot([[1,1,1]],[["dashed","black",False]], [[-2,2],[-2,2],[-2,2]])

# plot two points, one with solid red projection lines and one with dashed blue projection lines and arrowheads from the axes
# projection_plot([[1,1,1],[-1,-1,-1]],[["solid","red",False],["dashed", "blue", True]], [[-2,2],[-2,2],[-2,2]])

# plot a dashed black 3d line given as a string 
# projection_plot([],[], [[-3,3],[-3,3],[-3,3]], "<x,y,z>=<0,0,0>+t<1,1,1>", ["solid", "black"])

# plot a solid green 3d line given as a string, and add projection lines two two points on that line, where one is dashed red and the other is solid black with arrowheads
# projection_plot([[2,2,2],[-2,-2,-2]],[["dashed","red",False],["solid", "black", True]], [[-3,3],[-3,3],[-3,3]], "<x,y,z>=<0,0,0>+t<1,1,1>", ["dashed","green"])