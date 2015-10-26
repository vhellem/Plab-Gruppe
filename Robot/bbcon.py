import time

from BeScared import BeScared
from attackRed import AttackRed
from stayInMap import StayInMap
from camera import Camera
from arbitrator import Arbitrator
from motob import Motob
from camultrasob import CamUltra
from wander import Wander
from ReflectanceSob import ReflectanceSob

__author__ = 'magber'


class Bbcon:

    def __init__(self):
        cam = CamUltra()
        ref = ReflectanceSob()
        self.sensobs = [cam, ref]
        self.active_behaviours = [AttackRed(cam), BeScared(cam), StayInMap(ref), Wander()]
        self.motobs = [Motob(self)]
        self.arbitrator = Arbitrator(self)
        #self.active_behaviours = []
        self.inactive_behaviours = []

    def activate_behaviour(self, behaviour):
        if behaviour not in self.active_behaviours:
            self.active_behaviours.append(behaviour)
        if behaviour in self.inactive_behaviours:
            self.inactive_behaviours.remove(behaviour)

    def deactivate_behaviour(self, behaviour):
        if behaviour in self.active_behaviours:
            self.active_behaviours.remove(behaviour)
        if behaviour not in self.inactive_behaviours:
            self.inactive_behaviours.append(behaviour)

    def r(self):
        while True:
            print('Updating sensors')
            for sensob in self.sensobs:
                sensob.update()
            print('Updating behaviours')
            for behaviour in self.active_behaviours:
                behaviour.sense_and_act()
            recommendations = self.arbitrator.choose_action()
            print('Updating motobs')
            for motob in self.motobs:
                motob.update(recommendations)
            if recommendations[-1] == False:
                print('=== HALTING ===')
                break
            print('=============')
            print('Step complete')
            print('=============')
            # for sensob in self.sonsobs:
            #     sensob.reset()