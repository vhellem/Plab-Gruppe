from Robot.basic_robot.camera import Camera
from Robot.basic_robot.ultrasonic import Ultrasonic
from Robot.basic_robot.imager2 import Imager

class CamUltra():

    def __init__(self):
        self.camera = Camera()
        self.range = 300
        self.ultrasensor = Ultrasonic()

    def update(self):
        self.distance = self.ultrasensor.update()
        if self.distance<self.range:
            s = 1
            self.image = Imager(image=self.sensor.update()).scale(s,s)
        else:
            self.image = False

    def reset(self):
        self.ultrasensor.reset()
        self.camera.reset()