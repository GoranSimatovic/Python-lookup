# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:51:22 2020

Dice game simulator, player is sensible, gambler goes for it all

@author: Goran
"""


import numpy as np
import pandas as pd

def make_decision(results):
    dice_count = []
    for i in range(1,7):
        dice_count.append((results == i).sum())
    
    if dice_count == [1,1,1,1,1,1]:
        return 0, 1500
    
    dice_count = pd.Series(dice_count)
    
    if (dice_count[0]==0) & (dice_count[4] == 0) & ((dice_count>=3).sum()==0):
        return 0,0
    
    keep = []
    score = 0
    
    doubling = pd.Series(dice_count >= 3)
    
    if (doubling).sum()>0:
        for j in dice_count.index.values:
            if dice_count.loc[j]>=3:
                keep = np.concatenate((keep,(j+1)*np.ones(dice_count[j])))
                score = score + (j+1)*100*(2**(dice_count.loc[j]-3))
                dice_count[j]=0
                
        if dice_count[0] + dice_count[4] == dice_count.sum():
            score = score + 100*dice_count[0] + 50*dice_count[4]
            dice_count = np.zeros(6)
    else:
        
        if dice_count[0] + dice_count[4] == dice_count.sum():
            score = score + 100*dice_count[0] + 50*dice_count[4]
            dice_count = np.zeros(6)
        
        if dice_count[0]>0:
            score = score + 100
            dice_count[0] = dice_count[0]-1
        elif dice_count[4]>0:
            score = score + 50
            dice_count[4] = dice_count[4]-1
        
    if score == 0:
        dice_count = np.zeros(6)
        
    if dice_count.sum() ==2:
        if dice_count[0]>0:
            score = score + 100
            dice_count[0] = dice_count[0]-1
        elif dice_count[4]>0:
            score = score + 50
            dice_count[4] = dice_count[4]-1
        

        
    return dice_count.sum(), score



def player_run(p_n_dice, p_score):
    print('Conservative player turn',p_n_dice, p_score)
    new_score = p_score

    while ((p_n_dice>2) & (new_score >0)) | ((p_n_dice==6) & (new_score ==0)) |((p_n_dice<3) & (new_score >1600)):
        p_results = np.random.randint(1,7, size = p_n_dice)
        print(p_results)
        returned_dice, new_score = make_decision(p_results) 
        
        if new_score == 0:
            p_score = 0
            break
        p_score = p_score + new_score
        p_n_dice = returned_dice
        if p_n_dice == 0:
            p_n_dice = 6
        print(returned_dice, new_score)
    return p_n_dice, p_score






def gambler_run(p_n_dice, p_score):
    
    print('Twan turn',p_n_dice, p_score)
    new_score = p_score

    while True:
        
        p_results = np.random.randint(1,7, size = p_n_dice)
        print('Dice toss:',p_results)
        returned_dice, new_score = make_decision(p_results) 
        print('Leftover dice:', returned_dice, '  New Score:', new_score)
        
        if (new_score == 0):
            p_score = 0
            break
        
        p_score = p_score + new_score
        p_n_dice = returned_dice
        if p_n_dice == 0:
            p_n_dice = 6
            
        if (p_n_dice<3) & (p_score >800):
            break
        
        if (p_n_dice==1) & (p_score >450):
            break
        
    print('Returned dice:',p_n_dice,'Final score:', p_score)
    return p_n_dice, p_score








def play_dice():
    
    p1_score = 0
    p2_score = 0
    
    dice_in_play = 6
    returned_dice = 6
    score = 0
    while (p1_score < 10000) & (p2_score<10000):
         

        if (returned_dice <3) & (score>1000):
             print('Start score:',p2_score)
             dice_in_play = returned_dice
             returned_dice, score = gambler_run(dice_in_play, score)
             p2_score = p2_score + score
             print('End score:',p2_score)
                
        else:
            dice_in_play = 6
            print('Start score:',p2_score)
            returned_dice, score = gambler_run(dice_in_play, 0)
            p2_score = p2_score + score
            print('End score:',p2_score)
            
                   
        if (returned_dice <3) & (score>1000):
             print('Start score:',p1_score)
             dice_in_play = returned_dice
             returned_dice, score = player_run(dice_in_play, score)
             p1_score = p1_score + score
             print('End score:',p1_score)
                
        else:
            dice_in_play = 6
            print('Start score:',p1_score)
            returned_dice, score = player_run(dice_in_play, 0)
            p1_score = p1_score + score
            print('End score:',p1_score)
 
        
    if p1_score>=10000:
        return 1
    else:
        return 0
    

n_player1_wins = 0
for i in range(100):
    n_player1_wins = n_player1_wins + play_dice()