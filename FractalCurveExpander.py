# -*- coding: utf-8 -*-
"""
￼￼
AUTHOR Harmanprit Tatla
VERSION 2015 - April - 9

PURPOSE: To plot expansions of a fractal curve.
"""
#imports
import time
import numpy as np
import matplotlib.pyplot as plt
from sys import path, stdout
from os import chdir

# Global constants (as part of CompareBooks program)
NUM_WORDS_TO_PRINT = 20

def peanoCurve(expansion):
    """Given a positive integer for expansion, the number of expansions to 
    perform on the Peano curve, displays a plot with the expansions."""

    print 'Plotting Peano curve. Please wait.' #prints out wait message.
    stdout.flush() 
    
    #Sequence of points for Peano curve after its first expansion.
    p_ = np.array([0+0j, 1+0j, 1+1j, 2+1j, 2+0j, 1+0j, 1-1j, 2-1j, 2+0j, 
                   3+0j]) / 3.
    zz = p_ #Holds sequence of points for Peano curve for each expansion
    
    plt.figure() 
   
    #subplot of first expansion of Peano curve 
    plt.subplot(1, expansion, 1) # 1 row, expansion columns, loc 1
    plt.plot(p_.real, p_.imag, 'k') # x-axis = real num, y-axis = imaginary num
    plt.title('Expanded Once', fontsize = 10)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    #To make space between curve and margins of subplot
    plt.xlim(-0.15, 1.15)
    plt.ylim(-0.6, 0.6)

    #Expands the Peano curve expansion times                         
    for num in range(expansion-1):
        #since num starts from 0, num+2 to get correct loc for subplot
        plt.subplot(1, expansion, num+2)
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        plt.xlim(-0.15, 1.15)
        plt.ylim(-0.6, 0.6) 
        
        #For each expansion, replaces line segment between consecutive points 
        #z1 and z2 by a path;(zz)[1:] used to get z2, the point next to each z1
        for z1, z2 in zip(zz, (zz)[1:]):
            #plots curve expansion by computing partial path between each z1 
            #and z2 then plotting it.
            plt.plot((z1 + p_ * (z2 - z1)).real, (z1 + p_ * (z2 - z1)).imag)
            
            #Appends each partial path to zz to make path for current expansion
            zz = np.append(zz, z1 + p_ * (z2 - z1)) 
            
            if num == 0: #if num==0 then plot title for second expansion.
                plt.title('Expanded Twice', fontsize = 10)
            else: #else num!=0; plot title for (num+2) expansion 
                  #since num starts at 0, +2 to get correct num for plot title
                plt.title('Expanded %d Times' % (num+2), fontsize = 10)
            
    plt.show()

peanoCurve(4) # call to get 4 expansions of Peano curve 




