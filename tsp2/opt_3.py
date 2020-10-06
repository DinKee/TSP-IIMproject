#coding:utf-8
import numpy as np
import json
import math
from datetime import datetime
from util import *
from args import *
from math import sqrt
def opt_3():
    # Get arguments
    args = parse_args()
    t0=datetime.datetime.now()
    # Use the corresponding data file
    
    initial = readfile()
    coordinates,unchange_coordinates=randomise(initial)

    num_location = coordinates.shape[0]
    costs=[]
    #costs.append(0)
    if len(coordinates) == 0:
        return []
    for i in range(len(coordinates) - 1):
        for j in range(i + 2, len(coordinates) - 1):
            for k in range(j + 2, len(coordinates) - 1):
                way = 0
                #print("i=",i,"j=",j,"k=",k)
                current = dist(coordinates[i], coordinates[i+1]) + dist(coordinates[j], coordinates[j+1]) + dist(coordinates[k], coordinates[k+1])
                if current >  dist(coordinates[i], coordinates[i+1]) + dist(coordinates[j], coordinates[k]) + dist(coordinates[j+1], coordinates[k+1]):
                    current = dist(coordinates[i], coordinates[i+1]) + dist(coordinates[j], coordinates[k]) + dist(coordinates[j+1], coordinates[k+1])
                if current >  dist(coordinates[i], coordinates[j]) + dist(coordinates[i+1], coordinates[j+1]) + dist(coordinates[k], coordinates[k+1]):
                    current = dist(coordinates[i], coordinates[j]) + dist(coordinates[i+1], coordinates[j+1]) + dist(coordinates[k], coordinates[k+1])
                    way = 2
                if current >  dist(coordinates[i], coordinates[j]) + dist(coordinates[i+1], coordinates[k]) + dist(coordinates[j+1], coordinates[k+1]):
                    current = dist(coordinates[i], coordinates[j]) + dist(coordinates[i+1], coordinates[k]) + dist(coordinates[j+1], coordinates[k+1])
                    way = 3
                if current >  dist(coordinates[i], coordinates[j+1]) + dist(coordinates[k], coordinates[i+1]) + dist(coordinates[j], coordinates[k+1]):
                    current = dist(coordinates[i], coordinates[j+1]) + dist(coordinates[k], coordinates[i+1]) + dist(coordinates[j], coordinates[k+1])
                    way = 4
                if current >  dist(coordinates[i], coordinates[j+1]) + dist(coordinates[k], coordinates[j]) + dist(coordinates[i+1], coordinates[k+1]):
                    current = dist(coordinates[i], coordinates[j+1]) + dist(coordinates[k], coordinates[j]) + dist(coordinates[i+1], coordinates[k+1])
                    way = 5
                if current >  dist(coordinates[i], coordinates[k]) + dist(coordinates[j+1], coordinates[i+1]) + dist(coordinates[j], coordinates[k+1]):
                    current = dist(coordinates[i], coordinates[k]) + dist(coordinates[k], coordinates[i+1]) + dist(coordinates[j], coordinates[k+1])
                    way = 6
                if current >  dist(coordinates[i], coordinates[k]) + dist(coordinates[j+1], coordinates[j]) + dist(coordinates[i+1], coordinates[k+1]):
                    current = dist(coordinates[i], coordinates[k]) + dist(coordinates[j+1], coordinates[j]) + dist(coordinates[i+1], coordinates[k+1])
                    way = 7
                
                if way == 1:
                    coordinates[j+1:k+1] = np.flipud(coordinates[j+1:k+1])
                elif way == 2:
                    coordinates[i+1:j+1]= np.flipud(coordinates[i+1:j+1])
                elif way == 3:
                    coordinates[i+1:j+1]= np.flipud(coordinates[i+1:j+1])
                    coordinates[j+1:k+1] = np.flipud(coordinates[j+1:k+1])

                elif way == 4:
                    temp1=coordinates[:i+1]
                    temp2=coordinates[j+1:k+1]
                    temp3=coordinates[i+1:j+1]
                    temp4=coordinates[k+1:]
                    temp5=np.vstack((temp1,temp2))
                    temp5=np.vstack((temp5,temp3))
                    temp5=np.vstack((temp5,temp4))
                    coordinates = temp5
                    
                elif way == 5:
                    temp = np.vstack((coordinates[:i+1] , coordinates[j+1:k+1]))
                    temp =np.vstack((temp, np.flipud(coordinates[i+1:j+1])))
                    temp =np.vstack((temp, coordinates[k+1:]))
                    coordinates = temp
 
                elif way == 6:
                    temp = coordinates[:i+1]
                    temp =np.vstack((temp, np.flipud(coordinates[j+1:k+1])))
                    temp =np.vstack((temp, coordinates[i+1:j+1]))
                    temp =np.vstack((temp, coordinates[k+1:]))
                    coordinates = temp

                elif way == 7:
                    temp = coordinates[:i+1]
                    temp =np.vstack((temp,np.flipud(coordinates[j+1:k+1])))
                    temp = np.vstack((temp,np.flipud(coordinates[i+1:j+1])))
                    temp =np.vstack((temp, coordinates[k+1:]))
                    coordinates = temp
                distance=0
                for l in range(coordinates.shape[0] - 1):
                    distance += dist(coordinates[l], coordinates[l + 1])
                costs.append(distance)
               
                
                   
    plot_nearest(coordinates, costs,unchange_coordinates,t0)
    export2js(coordinates,"opt_3")
def dist(a,b):
    a_temp=a*111000
    b_temp=b*111000
    dist1=np.linalg.norm(a_temp - b_temp)
    return dist1


if __name__ == "__main__":
    opt_3()

