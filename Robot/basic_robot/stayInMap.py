from Robot.basic_robot.behaviour import Behaviour
from Robot.basic_robot.reflectance_sensors import ReflectanceSensors


class StayInMap(Behaviour):
    def __init__(self, max_pri=9):
        self.sensor = ReflectanceSensors(auto_calibrate=True)
        self.priority = max_pri

        self.treshold = 150
        self.about_to_crash = False
        self.values = [self.sensor.max_val for _ in range(5)]


    def get_weight(self):
        self.about_to_crash = False
        self.updateSensorValues()
        for reading in self.values:
            if reading <= self.THRESHHOLD:
                self.about_to_crash = True
                self.weight = self.priority
            self.weight =  0

    def get_motor_recommendation(self):
        if self.about_to_crash:
            l, r = self.compute_turn()
            self.recommendation =  [l, r]
        else:
            self.recommendation = False

    def compute_turn(self):
        direction = 0
        for i in range(0, 5):
            if self.values[i] <= self.THRESHHOLD:
                direction += i
            return [1/direction, -1/direction]

    def sense_and_act(self):
        self.get_weight()
        self.get_motor_recommendation()