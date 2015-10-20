__author__ = 'Vegard'

class Behaviour:
    active = False
    def __init__(self, bbcon, sensor, motor, pri=1):
        self.active = True
        self.sensor = sensor
        self.priority = pri
        self.motor = motor


    def weight(self):

    def switchMode(self):
        if self.active:
            self.active = False
        else:
            self.active = True


    def setMatchDegree(self, d):
        self.deg = d
