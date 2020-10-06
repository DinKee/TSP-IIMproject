#coding:utf-8
import numpy as np
import json
import math
from datetime import datetime
from util import *
from args import *
from math import sqrt
def opt_2():
    # Get arguments
    args = parse_args()
    t0=datetime.datetime.now()
    # Use the corresponding data file
    
    initial = readfile()
    coordinates,unchange_coordinates=randomise(initial)

    num_location = coordinates.shape[0]
    costs=[]

    # States: New, Current and Best
    # sol_new, sol_current, sol_best = (np.arange(num_location), ) * 3
    # cost_new, cost_current, cost_best = (float('inf'), ) * 3

    #costs.append(0)
    for i in range(coordinates.shape[0]-1):
        for j in range(i+2,coordinates.shape[0]-1):
            if dist(coordinates[i], coordinates[i+1]) + dist(coordinates[j], coordinates[j+1]) > dist(coordinates[i], coordinates[j]) + dist(coordinates[i+1], coordinates[j+1]):
                        coordinates[i+1:j+1] = np.flipud(coordinates[i+1:j+1])
            distance=0
            for i in range(num_location - 1):
                distance += dist(coordinates[i], coordinates[i + 1])
            costs.append(distance)
    plot_nearest(coordinates, costs,unchange_coordinates,t0)
    #export2csv(coordinates)
    export2js(coordinates,"opt_2")

def dist(a,b):
    a_temp=a*111000
    b_temp=b*111000
    dist1=np.linalg.norm(a_temp - b_temp)
    return dist1


if __name__ == "__main__":
    opt_2()

