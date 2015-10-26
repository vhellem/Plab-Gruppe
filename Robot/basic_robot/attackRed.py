from Robot.basic_robot.behaviour import Behaviour

__author__ = 'Vegard'


class AttackRed(Behaviour):


    def __init__(self, cam, pri=10):
        self.sensor = cam
        self.weight = 0
        self.active = True

    def sense_and_act(self):
        s = 1
        im = self.sensor.image
        if im:
            im.dump_image("test.jpeg")
            if im.red():
                self.recommendation = [1, 1, False]
                self.weight = 10
        else:
            self.recommendation = []
            self.weight = 0
