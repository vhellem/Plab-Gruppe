__author__ = 'Vegard'
from .behaviour import Behaviour
from .imager2 import Imager
class AttackRed(Behaviour):

    def sense_and_act(self):
        s = 1
        im = Imager(image=self.sensor.update()).scale(s,s)
        if im.red():
            pass
        else:
