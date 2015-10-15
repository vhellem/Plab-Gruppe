import bbcon.py
import random

class Arbitrator():

    def __init__(self, bbcon):
        self.bbcon = bbcon

    def choose_action(self):
        recommendations = []
        weights = []
        """ Store data from behaviours """
        for behaviour in bbcon.behaviours:
            if behaviour.active:
                recommendations.append(behaviour.recommendation)
                weights.append(behaviour.weight)

        """ Create stochastic weighting scale """
        total = 0
        cumulative = []
        for w in weights:
            total += w
            cumulative.append(total)

        """ Select behaviour based on weighting """
        choice = random.randrange(0,total)
        for index in range(len(cumulative)):
            if choice <= cumulative[index]:
                chosen_recommendation = recommendations[index]

        #FIGURE OUT HOW MOTORS ARE HANDLED, AND PUSH RECOMMENDATIONS
        #TO CORRECT MOTORS




