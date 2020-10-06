#coding:utf-8
import numpy as np
import json
import math
from util import *
from args import *
from math import sqrt
import datetime
def nearest():
    # Get arguments
    args = parse_args()

    t0=datetime.datetime.now()
    # Use the corresponding data file
    initial = readfile()
    coordinates,unchange_coordinates=randomise(initial)
    num_location = coordinates.shape[0]
    costs=[]
    costs.append(0)
    if coordinates.shape[0] == 0:
        return []
    current = coordinates[0]
    nnpoints=np.zeros(shape=(1,2))
    nnpoints=np.vstack((nnpoints,current))
    nnpoints=np.delete(nnpoints,0,0)
    coordinates=np.delete(coordinates,0,0)
    while coordinates.shape[0] > 0:
        next=coordinates[0]
        count=0
        inter_count=0
        for coordinate in coordinates:
            count+=1
            if dist(current,coordinate)<dist(current ,next):
                inter_count+=1
                next=coordinate
                del_count=count-1
        costs.append(costs[-1]+dist(current,coordinate))
        if inter_count==0:
            del_count=0
        nnpoints=np.vstack((nnpoints,next))
        coordinates=np.delete(coordinates,del_count,0)
        current=next

    print("x=",nnpoints[-1][0],"y=",nnpoints[-1][1])
    plot_nearest(nnpoints, costs,unchange_coordinates,t0)
    export2js(nnpoints,"nearest")
def dist(a,b):
    a_temp=a*111000
    b_temp=b*111000
    dist1=np.linalg.norm(a_temp - b_temp)
    return dist1


if __name__ == "__main__":
    nearest()

