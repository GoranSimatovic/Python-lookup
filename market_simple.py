# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:09:37 2022

Simple model of going long on SP500 with regular buyins

@author: Goran
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


years_on_market = 50
self_money = np.zeros(1+years_on_market*12)

#intervals between buyins in months
months_between_buys = 1
#buyins value
buy_in_sum = 1000

for i in range(len(self_money)):
    if np.mod(i,months_between_buys)==0:
        self_money[i]=+buy_in_sum

#initial investment        
self_money[0]=7000

money_table = pd.DataFrame(columns = ['input_money', 'invested_money', 'discounted projected growth', 'result', 'total_projected_gain'])
money_table['input_money'] = self_money
money_table['invested_money'] = np.cumsum(self_money)
money_table['result'] = 0
money_table['result'][0] = money_table['input_money'][0]

#Assuming stable ECB/FED promissed rates 2%/3%
inflation = 0.025
#Average SP500 growth rate
annual_growth = 0.105
money_table['discounted projected growth'] = np.power(1+annual_growth-inflation,1/12)

for i in money_table.index[:-1]:
    money_table['result'].loc[i+1] = (money_table['result'].loc[i]+money_table['input_money'].loc[i+1])*money_table['discounted projected growth'].loc[i]

money_table['total_projected_gain'] = money_table['result']/money_table['invested_money']
money_table['effective_profit'] = money_table['result'] - money_table['invested_money']
print(money_table[['total_projected_gain', 'effective_profit']])

years_for_observation = range(30+1)
gains_overview = pd.DataFrame(columns = ['invested money', 'relative gain', 'profit'], index = years_for_observation)

for i in gains_overview.index:
    gains_overview['invested money'].loc[i] = money_table.loc[12*i,['invested_money']].values[0]
    gains_overview['relative gain'].loc[i] = money_table.loc[12*i,['total_projected_gain']].values[0]
    gains_overview['profit'].loc[i] = money_table.loc[12*i,['effective_profit']].values[0]
    
gains_overview['diff'] =gains_overview['profit'].diff()
print(gains_overview)

gains_overview['profit'].plot( label = str(buy_in_sum))

plt.legend()
plt.show()

