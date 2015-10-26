from camera import Camera
from ultrasonic import Ultrasonic
from imager2 import Imager

class CamUltra():

    def __init__(self):
        self.camera = Camera()
        self.range = 300
        self.ultrasensor = Ultrasonic()

    def update(self):
        self.distance = self.ultrasensor.update()
        if self.distance<self.range:
            s = 1
            self.image = Imager(image=self.camera.update()).scale(s,s)
        else:
            self.image = False

    def reset(self):
        self.ultrasensor.reset()
        self.camera.reset()