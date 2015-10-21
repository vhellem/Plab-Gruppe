__author__ = 'Vegard'
from .behaviour import Behaviour
from .imager2 import Imager
class AttackRed(Behaviour):


    def __init__(self, bbcon, sensor, pri=10):
        super().__init__(bbcon, sensor, pri)

    def sense_and_act(self):
        s = 1
        im = Imager(image=self.sensor.update()).scale(s,s)
        if im.red():
            self.recommendation = [[1, 1], ]
        else:
            self.recommendation = [[], 0]
