__author__ = 'Vegard'

class Behaviour:
    active = False
    def __init__(self, bbcon, sensor, motor=[0, 0], pri=1):
        self.active = True
        self.sensor = sensor
        self.priority = pri
        self.motor = motor


    def sense_and_act(self):
        self.updateSensorValues()

    def setWeight(self):
        return self.deg*self.priority

    def considerSwitchMode(self, m):
        if self.active:
            self.considerDeactivation(m)
        else:
            self.considerActivation(m)

    def considerDeactivation(self, m):
        if m =="D":
            self.active = False

    def considerActivation(self, m):
        if m=="A":
            self.active = True


    def setMatchDegree(self, d):
        self.deg = d


    def update(self):
        message = self.bbcon.checkForMessage()
        self.considerSwitchMode(message)
        if self.active:
            self.sense_and_act()

    def updateSensorValues(self):
        pass



