import numpy as np
import random as rn

def flip_nuc(a):
    flip_a = [None]*len(a)
    for i in range(len(a)):
        if (a[i] == 'A'):
            flip_a[i] = np.random.choice(['C','G','T'])
        elif(a[i] == 'C'):
            flip_a[i] = np.random.choice(['A','G','T'])
        elif(a[i] == 'G'):
            flip_a[i] = np.random.choice(['C','A','T'])
        else: flip_a[i] = np.random.choice(['C','G','A'])
    return flip_a

