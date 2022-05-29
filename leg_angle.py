# -*- coding: utf-8 -*-
"""
Created on Sat May 28 20:05:56 2022

@author: Goran
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import ndimage

img = mpimg.imread('./noga.jpg')
img = ndimage.rotate(img, -90)
fig, axe = plt.subplots()

plt.imshow(img)

a = np.asarray(plt.ginput(3, timeout=-1))

hip_relative = a[0]-a[1]
foot_relative = a[2]-a[1]

hip_angle = 180*math.atan(hip_relative[0]/hip_relative[1])/math.pi
foot_angle = 180*math.atan(foot_relative[0]/foot_relative[1])/math.pi

plt.plot([a[0][0], a[1][0]],
         [a[0][1], a[1][1]],
         marker = 'o',
         color = 'green')


plt.plot([a[1][0], a[2][0]],
         [a[1][1], a[2][1]],
         marker = 'o',
         color = 'green')


text = f'The knee is bent at {round(180-hip_angle+foot_angle,1)} degrees'

plt.title(text)
plt.show()

#axe.text((a[2][0]+a[0][0])/2,
#         (a[2][1]+a[0][1])/2, text, {'color': 'C0', 'fontsize': 20})

