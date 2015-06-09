from ..com_interface import Communication
import math
import numpy as np
from ..position import Position


class FakeRobot(Communication):
    def __init__(self):
        self.current = Position()
        self.velocity = np.zeros(2)  # velocity of the robot's wheels mm/s
        self.accel = np.zeros(2)  # acceleration of the wheels mm/s2
        self.rotation_friction = np.zeros(2)  # friction due to rotation N
        self.cmd = np.zeros(2)  # cmds of the 2 motors (in [-255, 255])
        self.inter_wheels_distance = 200  # distance in mm between the wheels
        self.motorg = Motor()
        self.motord = Motor()
        self.weight = 5.0  # weight of the robot in kg
        self.J = 1.0  # inertia momentum of the robot
        self.wheel_radius = 28  # radius of the wheels in mm

    def simulate(self, dt):
        torque_d = (self.motord.simulate_cmd(self.cmd[0]))
        torque_g = (self.motorg.simulate_cmd(self.cmd[1]))
        self.accel = np.array([torque_d, torque_g]) / self.wheel_radius
        self.velocity += self.accel * dt
        self.current.x += math.cos(self.current.cap) * self.velocity.mean()
        self.current.y += math.sin(self.current.cap) * self.velocity.mean()
        dv = (self.velocity[0] - self.velocity[1])
        self.current.cap += dv / (self.inter_wheels_distance / 2)

    def run(self):
        self.simulate()


class Motor():
    # TODO add correct values
    def __init__(self, r=1.0, lv=1.0, lc=1.0, vbat=24.0, reductor=20.):
        """
        U = r * i + lv * w
        C = lc * i """
        # parameters
        self.r = r
        self.lv = lv
        self.lc = lc
        self.vbat
        self.w = 0
        self.reductor = reductor

    def simulate_cmd(self, cmd):
        """ return C
            cmd is between -255 and 255"""
        U = self.vbat * cmd * 1.0 / 255
        i = U - self.lv * self.w
        return self.lc * i * self.reductor

    def read_w_wheel(self, w_wheel):
        """ read the speed of a wheel and store the speed of the rotor """
        self.w = w_wheel * self.reductor

