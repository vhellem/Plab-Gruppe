from Robot.basic_robot.behaviour import Behaviour
from Robot.basic_robot.camera import Camera
from Robot.basic_robot.imager2 import Imager
__author__ = 'Vegard'


class AttackRed(Behaviour):


    def __init__(self, pri=10):
        self.sensor = Camera()
        self.weight = 0

    def sense_and_act(self):
        s = 1
        im = Imager(image=self.sensor.update()).scale(s,s)
        if im.red():
            self.recommendation = [1, 1, False]
            self.weight = 10
        else:
            self.recommendation = []
            self.weight = 0
