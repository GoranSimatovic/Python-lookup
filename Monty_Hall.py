# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:18:59 2021

@author: Goran
"""
import numpy as np

success_counter = np.zeros(2)
number_of_trials = 100000
for i in range(number_of_trials):
    
    car_id = np.random.choice(3, 1)[0]
    player_first_choice = np.random.choice(3, 1)[0]
    
    #here the player does not switch
    if car_id == player_first_choice:
        success_counter[0] += 1
        
    # here the player switches
    elif car_id != player_first_choice:
        success_counter[1] += 1

print('Switching success rate:',success_counter[1]/number_of_trials)
print('Not switching success rate:',success_counter[0]/number_of_trials)
