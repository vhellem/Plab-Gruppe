class BeScared:


    def __init__(self, sensor, pri=1):
        self.sensor = sensor
        self.weight = pri
        self.match = 0
        self.active = True
        self.range = 30


    def setRange(self, r):
        self.range = r
    def updateSensorValues(self):
        return self.sensor.distance

    def sense_and_act(self):
        print('BeScared sensing')
        dist = self.updateSensorValues()
        print('dist = ', dist)
        if dist>=self.range:
            self.weight = 0
        else:
            self.weight = 6

        self.recommendation= [-1, -1, False]
