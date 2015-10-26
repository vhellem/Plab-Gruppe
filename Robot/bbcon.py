import time

from BeScared import BeScared
from attackRed import AttackRed
from stayInMap import StayInMap
from camera import Camera
from arbitrator import Arbitrator
from motob import Motob
from camultrasob import CamUltra
from reflectanseSob import ReflectanceSob
from wander import Wander

__author__ = 'magber'


class Bbcon:

    def __init__(self):
        cam = CamUltra()
        ref = ReflectanceSob()
        self.sensobs = [cam, ref]
        self.behaviors = [AttackRed(cam), BeScared(cam), StayInMap(ref), Wander()]
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

    def r(self):
        for sensob in self.sensobs:
            sensob.update()
        for behavior in self.behaviors:
            behavior.sense_and_act()
        recommendations = self.arbitrator.choose_action()
        for motob in self.motobs:
            motob.update(recommendations)
        time.sleep(0.5)
        # for sensob in self.sonsobs:
        #     sensob.reset()