import numpy as np
import random 
import math

def bernoulli(p):
    r = np.random.random()
    if r <= p:
        return 1
    else:
        return 0

def bernoulli_dist(p, size=1):
    sample = []
    
    for i in range(size):
        sample.append(bernoulli(p))
        
    return np.array(sample)



def binomial(n, p, size=1):
    sample = []
    
    for i in range(size):
        sample.append(bernoulli_dist(p, n).sum())
        
    return np.array(sample)


def poisson(l, size=1, n=1000):
    """
    Docstring: function to get the poisson
    input: l is lambda, size is the size of the sample, n times of exits
    output: an array that contains numbers that are the exits by each iteration of the for
    """
    p = l/n
    sample = []
    #for to repit the size
    for i in range(size):
        sample.append(binomial(n,p).sum())
        
    return np.array(sample)