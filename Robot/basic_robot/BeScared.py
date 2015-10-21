from .behaviour import Behaviour

class BeScared(Behaviour):

    range = 0.3
    def __init__(self, bbcon, sensor, motor, pri=1):
        super().__init__(bbcon, sensor, motor, pri)


    def setRange(self, r):
        self.range = r
    def updateSensorValues(self):
        return self.sensor.update()

    def sense_and_act(self):
        dist = self.updateSensorValues()
        if dist>=self.range:
            self.setMatchDegree(0)
        else:
            self.setMatchDegree(dist/self.range)
        #Kaller bbcon sin oppdateringsfunksjon? Med motorrekommendasjoner og prioritet
        return [self.motor, self.setWeight(), 1)]
