from camera import Camera
from ultrasonic import Ultrasonic
from imager2 import Imager

class CamUltra():

    def __init__(self):
        self.camera = Camera()
        self.range = 30
        self.ultrasensor = Ultrasonic()

    def update(self):
        print('Updating CamUltra')
        self.distance = self.ultrasensor.update()
        print('dist = ', self.distance)
        if self.distance<self.range:
            print('Taking a picture in CamUltra')
            s = 1
            self.image = Imager(image=self.camera.update()).scale(s,s)
        else:
            self.image = False

    def reset(self):
        self.ultrasensor.reset()
        self.camera.reset()