__author__ = 'Vegard'


class AttackRed():


    def __init__(self, cam, pri=10):
        self.sensor = cam
        self.weight = 0
        self.active = True

    def sense_and_act(self):
        print('AttackRed updating')
        s = 1
        im = self.sensor.image
        print('Photo taken in AttackRed')
        if im:
            print('Photo exists')
            im.dump_image("test.jpeg")
            if im.red():
                self.recommendation = [1, 1, False]
                self.weight = 10
            else:
                self.recommendation = []
                self.weight = 0
        else:
            print('Photo does not exist')
            self.recommendation = []
            self.weight = 0
