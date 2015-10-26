
class StayInMap():
    def __init__(self, refl ,max_pri=9):
        self.sensor = refl
        self.priority = max_pri
        self.active = True
        self.treshold = 0.4
        self.about_to_crash = False
        self.values = [self.sensor.max_val for _ in range(5)]


    def get_weight(self):
        self.about_to_crash = False
        self.values = self.sensor.value
        self.weight =  0
        print('IR-sensor: ', self.values)
        for reading in self.values:
            if reading <= self.treshold:
                self.about_to_crash = True
                self.weight = self.priority


    def get_motor_recommendation(self):
        if self.about_to_crash:
            l, r = self.compute_turn()
            self.recommendation = [l, r, False]
        else:
            self.recommendation = []

    def compute_turn(self):
        if self.values[0]<= self.treshold or self.values[1]<=self.treshold:
            return (0.9, -0.6)

        else:
            return (-0.6, -0.9)


    def sense_and_act(self):
        print('StayInMap senses and acts')
        self.get_weight()
        self.get_motor_recommendation()