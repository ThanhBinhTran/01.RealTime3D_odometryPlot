from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import matplotlib.pyplot as plt
from device_drone import *
from device_platform import *
import math

###########################################
# Curve to geometry twist
###########################################
fig = plt.figure("curve to geometry twist")
ax = fig.gca()

###########################################
# Curve function
###########################################

data_size = 20
# sample data for drone (denote: dx, dy, dz)
# just generate sample data for drawing drone
x = np.linspace(-10, 10, data_size)
y = x**2 
x_data = []
y_data = []
x_linear = []
x_angular = []
linear = 0
angular = 0
past_angle = -math.pi/2
def cal_angle(v1, v2):
    unit_vector_1 = v1 / np.linalg.norm(v1)
    unit_vector_2 = v2 / np.linalg.norm(v2)
    print ("unit V1", unit_vector_1)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)
    print ("angle ", angle)
    return angle

past_pose = [x[0], y[0]]
for i in range (len(x)):
    
    ''' whenever receiving new data, update pose and tracjectory then draw them '''
    
    # clear plot
    #plt.cla()
    ax.cla()
    
    # get current pose and calcualte linear and angluar for x
    cur_pose = [x[i], y[i]]
    linear = math.dist(cur_pose, past_pose)
    direction = np.subtract(cur_pose, past_pose)
    angle = cal_angle(direction, [1, 0])
    print (angle)
    angular = angle - past_angle
    x_linear.append(linear)
    x_angular.append(angular)

    # update past pose
    past_pose = cur_pose
    past_angle = angle

#print (x_linear)
#print (x_angular)
    x_data.append(x[i])
    y_data.append(y[i])
    if True:
        plt.plot(x_data, y_data, label='Platform', color='blue', marker = '.',
                linewidth=1, markersize=2)
    #plt.text(cur_pose[0], cur_pose[1], linear)
        plt.text(cur_pose[0], cur_pose[1]-0.5, math.degrees(angular))
        # add legend and some informations
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        ax.set_title('Realtime 3D Coorindate of Drone and Platform')
        plt.xlim([-12, 12])
        #plt.ylim([0, 5])
        ax.legend()
        #pause every 0.5 second
        plt.pause(1)

plt.show()
