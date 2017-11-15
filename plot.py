import Dynamics
from Main.Robot import Robot

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.ion()
class PlotArm(object):

    def __init__(self):
        """
        create class variable for plot
        """
        self.fig = plt.figure()
        self.ax = self.fig.gca(projection = '3d')
        self.lines = self.ax.plot([],[],[])
        #self.figure, self.ax = plt.axes(projection='3d')
        #self.lines, = self.ax.plot3D([],[],[])
        #self.figure, self.ax = plt.subplots()
        #self.lines, = self.ax.plot([],[],'=')
        self.ax.set_autoscaley_on(True)
        self.ax.grid()
        pose_1 = [1,2,3]
        pose_2 = [2,3,9]
        pose_3 = [7,9,2]


    def update(self, p_1,p_2,p_3):


                #self.lines.set_zdata(zdata)
        xdata = [ p_1[0], p_2[0], p_3[0] ]
        ydata = [p_1[1], p_2[1], p_3[1]]
        #zdata = [p_1[1], p_2[1], p_3[1]]

        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)
        #self.lines.set_zdata(zdata)

        self.ax.relim()
        self.ax.autoscale_view()

        # We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()



xdata = []
ydata = []
#zdata = []
ploter = PlotArm()
for i in range(100):
    import time
    p_1 = (i, 0, 1,)
    p_2 = (0, 1, 3,)
    p_3 = (0, 2, 6,)
    time.sleep(1)
    ploter.update(p_1,p_2,p_3)




