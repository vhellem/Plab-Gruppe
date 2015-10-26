from Robot import motors

__author__ = 'edvardvb'


class Motob:
    def __init__(self, bbcon):
        self.motors = motors.Motors()
        self.value = 0
        self.bbcon = bbcon

    def update(self, recommendation):
        self.value = recommendation
        self.operationalize()

    def operationalize(self):
        if self.value[-1] == True:  # If halt_request flag is true
            self.motors.stop()
            """ Probably do something in bbcon as well, unsure where to handle this """
        if self.value[0] == 0 and self.value[1] == 0:
            self.motors.stop()  # Unsure if stop completely halts the run or just stops motors momentarily.

        """ More assumptions, needs more work if recommendations are formatted as (L, 45) """
        val = [self.value[0], self.value[1]]
        self.motors.set_value(val)
