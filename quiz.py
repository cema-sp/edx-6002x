import random

def drawing_without_replacement_sim(numTrials):
        '''
        Runs numTrials trials of a Monte Carlo simulation
        of drawing 3 balls out of a bucket containing
        4 red and 4 green balls. Balls are not replaced once
        drawn. Returns a float - the fraction of times 3 
        balls of the same color were drawn in the first 3 draws.
        '''
        balls = ['r','r','r','r','g','g','g','g']
        same = 0
        for i in xrange(numTrials):
            a, b, c = random.sample(balls, 3)
            if a == b and b == c:
                same = same + 1

        return float(same)/numTrials

