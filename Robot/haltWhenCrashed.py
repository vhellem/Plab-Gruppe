__author__ = 'edvardvb'

class HaltWhenCrashed:


    def __init__(self, sensor, pri=1000):
        self.sensor = sensor
        self.weight = pri
        self.match = 0
        self.active = True
        self.range = 3


    def setRange(self, r):
        self.range = r

    def updateSensorValues(self):
        return self.sensor.distance

    def sense_and_act(self):
        print('HaltWhenCrashed sensing')
        dist = self.updateSensorValues()
        print('dist = ', dist)
        if dist>=self.range:
            self.weight = 0
            self.recommendation= []
        else:
            self.recommendation= [0, 0, True]
