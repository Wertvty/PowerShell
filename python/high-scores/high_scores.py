class HighScores(object):
    scores = []
    def __init__(self, n):
        self.scores = n
    
    
    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        return sorted(self.scores, reverse = True)[0:3]

    def latest(self):
        return self.scores[len(self.scores)-1]