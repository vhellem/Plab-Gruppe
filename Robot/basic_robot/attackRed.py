__author__ = 'Vegard'
from .behaviour import Behaviour
from .imager2 import Imager
class AttackRed(Behaviour):


    def __init__(self, bbcon, sensor, motor=[0, 0], pri=10):
        super().__init__(bbcon, sensor, motor, pri)

    def sense_and_act(self):
        s = 1
        im = Imager(image=self.sensor.update()).scale(s,s)
        if im.red():
            return []
