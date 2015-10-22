from Robot.basic_robot.Behaviours.BeScared import BeScared
from Robot.basic_robot.Behaviours.attackRed import AttackRed
from Robot.basic_robot.Behaviours.stayInMap import StayInMap

from Robot.basic_robot.Sensors.camera import Camera

from Robot.basic_robot.arbitrator import Arbitrator
from Robot.basic_robot.motob import Motob

import time

__author__ = 'magber'


class Bbcon:

    def __init__(self):
        self.behaviors = [AttackRed(), BeScared(), StayInMap()]
        self.sensobs = [Camera()]
        self.motobs = [Motob(self)]
        self.arbitrator = Arbitrator(self)
        self.active_behaviors = []
        self.inactive_behaviors = []

    def activate_behavior(self, behavior):
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)
        if behavior in self.inactive_behaviors:
            self.inactive_behaviors.remove(behavior)

    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)
        if behavior not in self.inactive_behaviors:
            self.inactive_behaviors.append(behavior)

    def run_one_timestep(self):
        for sensob in self.sensobs:
            sensob.update()
        for behavior in self.behaviors:
            behavior.update()
        recommendations = self.arbitrator.choose_action()
        for motob in self.motobs:
            motob.update(recommendations)
        time.sleep(0.5)
        # for sensob in self.sonsobs:
        #     sensob.reset()