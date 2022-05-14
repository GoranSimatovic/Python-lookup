# -*- coding: utf-8 -*-
"""
Created on Sat May 14 17:48:24 2022

@author: Goran
"""
import math
import random

def input_an_integer():
    return int(input('Please input an integer:'))

def test_if_prime(x):
        
    if x<3:
        return True
    elif x%2==0:
        return False
    elif x<=7:
        return True
    else:
        for i in range(3,math.floor(x/2.0),2):
            if x%i==0:
                return False
    
    return True

list_size = int(input('How long is the list of integers\n'))
   
list_min =  int(input('What is the smallest possible random integer?\n'))
list_max =  int(input('What is the largest possible random integer?\n'))

a = [random.randint(list_min, list_max) for x in range(1,list_size)]

print('We have generated the following list:\n', a, '\n')

primes = set([x for x in a if test_if_prime(x)])

print('The following numbers of this list are primes:\n', [x for x in primes])

    
    