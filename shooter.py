import numpy as np
import random
from matplotlib import pyplot
class Guy:
    error = 1.5
    rangee = .1
    def __init__(self, gen, num, ang, dist):
        self.generation = gen
        self.number = num
        self.angle = ang
        self.distance = dist
        self.hit = 0
    def shoot(self):
        hits = 0
        for i in range(100):
            guess = np.random.normal(self.angle, Guy.error, 1)[0]
            if (guess > -1*Guy.rangee and guess < Guy.rangee):
                hits += 1
        self.hit = hits
        return hits
    
l1 = []
l2 = [Guy(0, 1, 3, 1)]
gen = 0
def makeGuys():
    global gen, l1, l2
    l1 = []
    gen+=1
    for i in range(100):
        l1.append(Guy(gen, 1, np.random.normal(l2[0].angle, .03, 1)[0], 1))
        


def mainf():
    global l1, l2, gen
    makeGuys()
    l2 = []
    l2.append(l1[0])
    for i in l1:
        if(i.shoot()>l2[0].hit):
            l2[0] = i
    if (l2[0].generation%10 == 0):
        #print(l2[0].angle)
        pyplot.plot(1, 2)
        
    


for i in range(10000):
    mainf()

    

