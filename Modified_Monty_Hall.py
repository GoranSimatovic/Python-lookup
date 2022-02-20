# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:43:35 2021

Variation on the Monty Hall problem with n possible doors
Test runs trials and compares to theoretical prediction

@author: Goran
"""

import numpy as np
import pandas as pd
import random
from scipy.stats import norm
import matplotlib.pyplot as plt

def mont__switch_prob(n):
   return pd.Series([(n-1)/n * 1/(n-2), 1/n])



number_of_doors = 3
number_of_trials = 400
number_of_iterations = 500


rates_per_iteration= pd.DataFrame(np.zeros((number_of_iterations,2)),columns = ['Switch success rate', 'Not switching success rate'])



for i in range(number_of_iterations):

    success_counter = np.zeros(2)

    for j in range(number_of_trials):
        
        car_id = np.random.choice(number_of_doors, 1)[0]
        player_first_choice = np.random.choice(number_of_doors, 1)[0]
        
        Monty_door = list(range(number_of_doors))
        Monty_door.remove(car_id)
        if player_first_choice != car_id:
            Monty_door.remove(player_first_choice)
        Monty_door = random.sample(Monty_door,1)[0]
        
        #here the player does not switch
        if car_id == player_first_choice:
            success_counter[0] += 1
            
        # here the player switches
        else:
            other_doors = list(range(number_of_doors))
            other_doors.remove(player_first_choice)
            other_doors.remove(Monty_door)
    
            player_second_choice = random.sample(other_doors,1)[0]
            if player_second_choice == car_id:
                success_counter[1] += 1
    
        switch_success= success_counter[1]/number_of_trials
        not_switch_success = success_counter[0]/number_of_trials
    
#    print('Swithching success rate:',switch_success)
#    print('Not swithching success rate:',not_switch_success)
    rates_per_iteration.loc[i] = [switch_success,not_switch_success]



data = rates_per_iteration['Switch success rate']
mu, std = norm.fit(data)

# Plot the histogram.
plt.hist(data, bins=25, density=True, alpha=0.6, color='g')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
plt.vlines(x=mu, ymin=0, ymax=max(p), color='blue', zorder=2, label = r'Fitted $\mu$')
plt.vlines(x=mont__switch_prob(number_of_doors)[0], ymin=0, ymax=norm.pdf(mont__switch_prob(number_of_doors)[0], mu, std), color='black', zorder=2, label = r'Theoretical distribution')
title = "Fit results: $N_{trials}$ = %.0f, mu = %.4f,  std = %.4f" % (number_of_trials, mu, std)
plt.legend()
plt.title(title)

plt.show()




#quick redo for no-switch option
data = rates_per_iteration['Not switching success rate']
mu, std = norm.fit(data)

# Plot the histogram.
plt.hist(data, bins=25, density=True, alpha=0.6, color='r')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
plt.vlines(x=mu, ymin=0, ymax=max(p), color='blue', zorder=2)
plt.vlines(x=mont__switch_prob(number_of_doors)[0], ymin=0, ymax=norm.pdf(mont__switch_prob(number_of_doors)[0], mu, std), color='black', zorder=2)
plt.title(title)

plt.show()

