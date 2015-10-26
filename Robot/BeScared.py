class BeScared:

    range = 30
    def __init__(self, sensor, pri=1):
        self.sensor = sensor
        self.weight = pri
        self.match = 0
        self.active = True


    def setRange(self, r):
        self.range = r
    def updateSensorValues(self):
        return self.sensor.distance

    def sense_and_act(self):
        dist = self.updateSensorValues()
        if dist>=self.range:
            self.weight = 0
        else:
            self.weight = (dist/self.range)

        self.recommendation= [-1, -1, False]
