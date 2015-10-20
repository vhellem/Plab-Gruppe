__author__ = 'Vegard'

class Behaviour:
    active = False
    def __init__(self, bbcon, sensor, motor, pri=1):
        self.active = True
        self.sensor = sensor
        self.priority = pri
        self.motor = motor


    def sense_and_act(self):
        self.updateSensorValues()

    def weightProperty(self):
        return self.deg*self.priority

    def considerSwitchMode(self):
        if self.active:
            self.considerDeactivation()
        else:
            self.considerActivation()

    def considerDeactivation(self):
        pass

    def considerActivation(self):
        pass


    def setMatchDegree(self, d):
        self.deg = d


    def update(self):
        self.considerSwitchMode()
        if self.active:
            self.sense_and_act()

    def updateSensorValues(self):
        pass



