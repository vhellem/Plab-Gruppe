
class Wander():


    def __init__(self, pri=1):
        self.active = True
        self.weight = pri


    def sense_and_act(self):
        print('Wander senses and acts')
        mrec = self.random_step()
        self.recommendation = mrec



    def random_step(self):
        from random import uniform
        left = uniform(-1, 1)
        right = uniform(-1, 1)
        return [left, right, False]