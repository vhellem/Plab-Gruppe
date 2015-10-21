from .behaviour import Behaviour

class Wander(Behaviour):



    def __init__(self, bbcon, sensor, motor, pri=1):
        super().__init__(bbcon, sensor, motor, pri)

    def sense_and_act(self):
        mrec = self.random_step()
        self.bbcon.getUpdates(mrec, self.priority, 2)


    def random_step(self):
        from random import choice
        left = choice([-0.5, -0.25, 0,  0.25, 0.5])
        right = choice([-0.5, -0.25, 0 ,0.25, 0.5])
        return [left, right]