from random import uniform


class Arbitrator:
    def __init__(self, bbcon):
        self.bbcon = bbcon

    def choose_action(self):
        print('Choosing action')
        recommendations = []
        weights = []
        """ Store data from behaviours """
        for behaviour in self.bbcon.active_behaviours:

            if behaviour.active and len(behaviour.recommendation) > 0:
                recommendations.append(behaviour.recommendation)
                weights.append(behaviour.weight)
                print(behaviour)
        print(recommendations)
        print(weights)
        return self.scale_and_select(recommendations, weights)

    def scale_and_select(self, recommendations, weights):
        print('Scaling and selecting')
        """ Create stochastic weighting scale """
        total = 0
        cumulative = []
        for w in weights:
            total += w
            cumulative.append(total)

        """ Select behaviour based on weighting """
        choice = uniform(0, total)
        for index in range(len(cumulative)):
            if choice <= cumulative[index]:
                chosen_recommendation = recommendations[index]
                break
        """Assumes recommendations are a tuple with the following data:
            [0] Rec. for motob 1
            [1] Rec. for motob 2
            [2...] Rec for motob [3...]
            [n] Halt flag (boolean, must be set t/f in behaviour
        """
        print(chosen_recommendation)
        return chosen_recommendation
        # HOW ARE RECOMMENDATIONS FORMATTED? NEED TO PULL 1 FOR
        # EACH MOTOB AND A BOOLEAN FOR THE HALT FLAG

        # FIGURE OUT HOW MOTORS ARE HANDLED, AND PUSH
        # RECOMMENDATIONS TO CORRECT MOTORS
