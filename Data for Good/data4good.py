#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:20:07 2020

@author: leemshari
"""

import matplotlib.pyplot as plt

#This will plot a bar graph of the voter data gathered 
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
#Each generation should be specified for clarity
groups = ['Millenials', 'Millenials\nVoted', 'Baby Boomers', 'Baby Boomers\nVoted']
population = [72.06,31.3,72.56,48.1]
plt.xlabel('Age Groups')
plt.ylabel('Population\n(in millions)')
voters = ax.bar(groups,population)
#The audience should be able to quickly recognize the bar that refers to them
voters[1].set_color('r')
plt.show()


print("Data was gathered after the 2016 election")
print("With a population of 72.06 million if",48.1-31.3,"million more millenials voted they \n would have voted at the same rate as the most influential voting demographic")