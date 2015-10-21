

class Motob:
    #How to interact with motors
    def __init__(self, motors):

        self.motors = motors
        self.value = None

    def update(self, recommendation):
        #Gets a new recommendation
        self.operationalize(motor_recommendation)
        #Sets as previous recommendation
        self.value = recommendation

    def operationalize(self, motor_recommendation):
        pass
