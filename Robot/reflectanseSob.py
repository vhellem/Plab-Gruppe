from reflectance_sensors import ReflectanceSensors

__author__ = 'Vegard'


class reflectanceSob:
    def __init__(self):
        self.sensor = ReflectanceSensors(auto_calibrate=True)

    def update(self):
        print('reflectance sensor updates')
        self.sensor.update()
        self.value = self.sensor.value
    def reset(self):
        self.sensor.reset()