#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 20:20:18 2020

@author: leemshari
"""
import sqlite3
import matplotlib.pyplot as plt

#Connecting to DB that I created on the command line
conn = sqlite3.connect('Visualization')

c = conn.cursor()
#Data in DB changed from strings to ints
def getInts(a_list):
    
    for i in range(0, len(a_list)): 
        a_list[i] = int(a_list[i])
        
    return(a_list)
#Plotting graphs in matplotlib (title, labels, datapoints, ranges)
def thePlot(a_list,b_list,str):
#Size of the graph needs to support 42 x axis data points    
    fig = plt.figure(figsize=(18, 5))
    ax = fig.add_subplot(111)
#Title for graph needs to be at the top of the graph
    plt.title(str, fontsize = 15)
#Labels for the x and y axis
    plt.xlabel("Date", fontsize = 12)
    plt.ylabel("Score \n(1 worst to 5 best)", fontsize = 12)
#Data on y axis only ranges from 1-5, using 0-6 to include everything
    plt.ylim(0,6)
#42 x axis data points needed to fit so rotating provided more space
    ax.xaxis.set_tick_params(rotation = 50)
    ax.plot(a_list,b_list)
    print(ax)


def main():
#Query statement to focus on data from specific column    
    c.execute("SELECT date FROM daily")
#Getting data from specific column which 
    d = c.fetchall()
#List comprehension to get data points from nested tuple to simple list
    day = [item for t in d for item in t]
    
    c.execute("SELECT commute FROM daily")
    
    q1 = c.fetchall()
    commute = [item for t in q1 for item in t]
#Call for items in now simple list to be changed into ints
    getInts(commute)
    
    c.execute("SELECT alertness FROM daily")
    
    q2 = c.fetchall()
    alertness = [item for t in q2 for item in t]
    getInts(alertness)
    
    c.execute("SELECT completion FROM daily")
    
    q3= c.fetchall()
    completion = [item for t in q3 for item in t]
    getInts(completion)
    
    c.execute("SELECT diet FROM daily")
    
    q4 = c.fetchall()
    diet = [item for t in q4 for item in t]
    getInts(diet)
    
    c.execute("SELECT homework FROM daily")
    
    q5 = c.fetchall()
    homework = [item for t in q5 for item in t]
    getInts(homework)
    
    c.execute("SELECT calendar FROM daily")
    
    q6 = c.fetchall()
    calendar = [item for t in q6 for item in t]
    getInts(calendar)
    
    c.execute("SELECT sleep FROM daily") 
    
    q7 = c.fetchall()
    sleep = [item for t in q7 for item in t]
    getInts(sleep)

#This graph will be a bit different because it will be a multi line graph
    fig2 = plt.figure(figsize=(18, 5))
    plt.title('Calendar/Completion Comparison', fontsize = 15) 
    plt.ylim(0,6)
    fig2.autofmt_xdate(rotation=40)
    plt.xlabel("Date", fontsize = 12)
    plt.ylabel("Score \n(1 worst to 5 best)", fontsize = 12)
#This will allow me plot a graph with 2 lines and compare calendar list with ompletion list
#Line colors should be red and blue    
    comple_comp = plt.plot(day,completion,"-b",label = 'completion')
    calen_comp = plt.plot(day,calendar, "-r", label = 'calendar')
#Legend needed to distinguish between lines on the graph
    plt.legend(loc = "upper right") 
    print(comple_comp,calen_comp)
    
#Calls to plot the 7 individual graphs created from the data gathered from survery    
    thePlot(day,commute,'Commute')
    thePlot(day,alertness,'Alertness')
    thePlot(day,completion,'Completion')
    thePlot(day,diet,'Diet')    
    thePlot(day,homework,'Homework')    
    thePlot(day,calendar,'Calendar')
    thePlot(day,sleep,'Sleep')

main()

conn.commit()
conn.close()