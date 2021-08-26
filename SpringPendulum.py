import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class SpringPendulum:
    def __init__(self, g, m, k, l, dis, disV, angle, angleV, dt, T, ax):
        self.g = g
        self.m = m
        self.k = k
        self.l = l
        self.dis = dis
        self.disV = disV
        self.angle = angle
        self.angleV = angleV
        self.dt = dt
        self.T = T
        self.t_points = np.arange(0.0, self.T, self.dt)
        self.line, = ax.plot([],[], '-', c="#B80000", lw=1, alpha=0.5)
        self.spring, = ax.plot([],[], 'o-', c="#0000FF", lw=3, markersize=12)

    def calculation(self):
        self.angle_points = np.zeros(len(self.t_points))
        self.dis_points = np.zeros(len(self.t_points))
        self.angle_points[0] = self.angle
        self.dis_points[0] = self.dis
        for i in range(1,len(self.t_points)):
            disA = (self.dis * self.angleV ** 2.0) + (self.g * np.cos(self.angle)) - self.k / self.m * (self.dis - self.l)
            angleA = -(2 * self.disV * self.angleV + self.g * np.sin(self.angle)) / self.dis
            self.disV += disA*self.dt
            self.dis += self.disV*self.dt
            self.angleV += angleA*self.dt
            self.angle += self.angleV*self.dt
            self.dis_points[i] = self.dis
            self.angle_points[i] = self.angle
        self.x_points = self.dis_points * np.sin(self.angle_points)
        self.y_points = -1 * self.dis_points * np.cos(self.angle_points)

    def animetion(self, i):
        self.line.set_data(self.x_points[:i], self.y_points[:i])
        self.spring.set_data([0, self.x_points[i]], [0, self.y_points[i]])
        return self.spring, self.line

if __name__ == '__main__':
    fig, ax = plt.subplots()
    ax.set_xlim((-6, 6))
    ax.set_ylim((-10, 2.5))
    sp1 = SpringPendulum(1, 1, 10, 5, 4, 0.0, np.pi/6, 0.0, 0.05, 50, ax) # set sp1 = initial SpringPendulum (not compute)
    sp1.calculation() # compute the trajectory line of sp1
    animetion = FuncAnimation(fig, sp1.animetion, np.arange(1, len(sp1.t_points)), interval=int(1000*sp1.dt), blit=True)
    plt.show()
