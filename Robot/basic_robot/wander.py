from .behaviour import Behaviour

class Wander(Behaviour):



    def __init__(self, bbcon, sensor, pri=1):
        self.weight = pri
        super().__init__(bbcon, sensor, pri)

    def sense_and_act(self):
        mrec = self.random_step()
        self.recommendation = mrec



    def random_step(self):
        from random import uniform
        left = uniform(-1, 1)
        right = uniform(-1, 1)
        return [left, right]