from Robot.basic_robot.Behaviours.behaviour import Behaviour
from Robot.basic_robot.Sensors.reflectance_sensors import ReflectanceSensors


class StayInMap(Behaviour):
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
            if reading <= self.THRESHHOLD:
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
            if self.values[i] <= self.THRESHHOLD:
                direction += i
            return [1/direction, -1/direction]

    def sense_and_act(self):
        self.get_weight()
        self.get_motor_recommendation()