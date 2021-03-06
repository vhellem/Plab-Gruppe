
class StayInMap():
    def __init__(self, refl ,max_pri=9):
        self.sensor = refl
        self.priority = max_pri
        self.active = True
        self.treshold = 150
        self.about_to_crash = False
        self.values = [self.sensor.max_val for _ in range(5)]


    def get_weight(self):
        self.about_to_crash = False
        self.values = self.sensor.value
        for reading in self.values:
            if reading <= self.treshold:
                self.about_to_crash = True
                self.weight = self.priority
            self.weight =  0

    def get_motor_recommendation(self):
        if self.about_to_crash:
            l, r = self.compute_turn()
            self.recommendation = [l, r, False]
        else:
            self.recommendation = []

    def compute_turn(self):
        direction = 0
        for i in range(0, 5):
            if self.values[i] <= self.treshold:
                direction += i
        return [1/direction, -1/direction]

    def sense_and_act(self):
        print('StayInMap senses and acts')
        self.get_weight()
        self.get_motor_recommendation()