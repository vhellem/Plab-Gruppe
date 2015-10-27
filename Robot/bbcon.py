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
from zumo_button import Zumobutton
from haltWhenCrashed import HaltWhenCrashed

__author__ = 'magber'


class Bbcon:

    def __init__(self):
        cam = CamUltra()
        ref = ReflectanceSob()
        self.sensobs = [cam, ref]
        self.active_behaviours = [AttackRed(cam), BeScared(cam), StayInMap(ref), Wander(), HaltWhenCrashed(cam)]
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

    def one_timestep(self):
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
            return True
        print('=============')
        print('Step complete')
        print('=============')
        return False
            # for sensob in self.sonsobs:
            #     sensob.reset()

    def r(self):
        z = Zumobutton()
        z.wait_for_press()
        halted = False
        while not halted:
            halted = self.one_timestep()
        print('=== HALTED ===')

