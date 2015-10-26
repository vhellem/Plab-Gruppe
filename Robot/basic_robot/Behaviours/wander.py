from Robot.basic_robot.Behaviours.behaviour import Behaviour

class Wander(Behaviour):



    def __init__(self, pri=1):
        self.active = True
        self.weight = pri


    def sense_and_act(self):
        mrec = self.random_step()
        self.recommendation = mrec



    def random_step(self):
        from random import uniform
        left = uniform(-1, 1)
        right = uniform(-1, 1)
        return [left, right, False]