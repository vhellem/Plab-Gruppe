from reflectance_sensors import ReflectanceSensors

__author__ = 'Vegard'


class ReflectanceSob:
    def __init__(self):
        self.sensor = ReflectanceSensors(auto_calibrate=False)
        self.max_val = self.sensor.max_val

    def update(self):
        self.sensor.update()
        self.value = self.sensor.value
    def reset(self):
        self.sensor.reset()