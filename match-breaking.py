import numpy as np
from random import randint
size = 100000
s = np.random.normal(0.5,0.1,size)

def tryit(p1,p2):
  legit = p1 > 0 and p1 < 1 and p1 != p2 and p2 > 0 and p2 < 1
  if legit:
    p3 = max(p1,p2) - min(p1,p2)
    return legit,  min(p1,p2) > 0.5 or max(p1,p2) < 0.5 or p3 > 0.5
  else:
    return legit, False

trials = 100000
legitTrials = trials
count = 0

for t in range(1,trials + 1):
  p1 = s[randint(0,size - 1)]
  p2 = s[randint(0,size - 1)]
  legit, result = tryit(p1,p2)
  if not legit:
    legitTrials = legitTrials - 1
  else:
    if result:
      count = count + 1

prop = count/legitTrials
print(legitTrials)
print(prop)
