class player:
def __init__(self,n):
self.name = n
self.score = 0
#methods
def increaseScore(self,s):
self.score = self.score + s
def decreaseScore(self,s):
self.score = self.score - s
