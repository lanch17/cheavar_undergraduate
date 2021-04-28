import os
import time
import math
import numpy as np
import numpy.linalg as npla
import scipy
from scipy import linalg as spla
import scipy.sparse
import scipy.sparse.linalg
from scipy import integrate
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from collections import Counter 

%matplotlib inline
#%matplotlib tk

np.set_printoptions(precision = 4)


######################
#This function returns an array of numbers in seconds,
#based on length of the array and the frames per second
######################
def get_timearray(arr,fps):
    length = arr.size;
    time = np.zeros(length);
    #create time based on frame index and frames per second
    for i in range(length):
        time[i]=(i)/fps;
    return time;
    
    
########################
#This function takes in an array of amplitudes and the fps in order to
#create the plot of amplitude vs time
# arr = array of amplitudes 
# fps = frames per second
########################
def create_plot(arr,fps):
    #Calls get_timearray first to plot time in the x-axis and amplitude in the y-axis
    time = get_timearray(arr,fps)
    plt.plot(time, arr)
    plt.title('Amplitude vs Time(seconds)')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude (a.u)')
    plt.show()
    return time,arr

##################################################
# This function takes in four parameters, in order to extract a smaller plot
# with a start and ending amplitude, the array of amplitudes and the frames per second
# start = starting amplitude
# end = ending amplitude
# arr = array of amplitudes
# fps = frames per second
##################################################

def smaller_plotGivenAmplitude(start,end,arr,fps):
    #Find at which index the arr contains start and end amplitude
    result1 = np.where(arr == start)
    result2 = np.where(arr == end)
    startindex = result1[0][0];
    endindex = result2[0][0];
    print("starting index",startindex);
    print("end index",endindex);
    print("starting time", time[startindex]);
    print("ending time",time[endindex]);
    #get the time array
    time = get_timearray(arr,fps);
    #Index the time and amplitude array at the specific start and ending index
    newtime = (time[startindex:endindex])
    newamplitude = (arr[startindex:endindex])
    #plt.plot(newtime, newamplitude)
    return newtime,newampitude


##################################################
# This function takes in four parameters, in order to extract a smaller plot
# with a start time and ending time in seconds, the array of amplitudes and the frames per second
# start = starting time
# end = ending time
# arr = array of amplitudes
# fps = frames per second
##################################################

def smaller_plotGivenTime(start,end,arr,fps):
    res = [] 
    res1 = []
    time = get_timearray(arr,fps);
    #Find the index at which the time array is greater than start time 
    for idx in range(0, len(time)) : 
        if time[idx] > start: 
            res.append(idx) 
    #Find the index at which the time array is greater than the end time
    print("starting index",res[0])
    for idx in range(0, len(time)) : 
        if time[idx] > end: 
            res1.append(idx) 
    print("ending index",res1[0])
    startindex = res[0];
    endindex = res1[0];
    #Create new array of time and new amplitude
    newtime = (time[startindex:endindex])
    newamplitude = (arr[startindex:endindex])
    plt.plot(newtime, newamplitude)
    plt.title('Amplitude vs Time(seconds)')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude (a.u)')
    plt.show()
    return newtime,newamplitude
    
    
 def norm(data):
    return (data)/np.linalg.norm(data)
    
    
#############################
    #The following code block creates the plot given the file pathname
    # granted that there is only one cell analyzed in the txt file
    #
    # Change the parameter to be only path, instead of path = "mouseheart.txt' and then call the function with 
    # a given path
#############################
def createPlotFromFile(path = 'mouseheart.txt'):

    
    #In the first parameter, put the txt file path name
    h = open(path, 'r') 

    # Reading from the file 
    content = h.readlines() 

    #arraycontent extracts the array of numbers from the txt file
    #it is on the 3rd line
    arraycontent = content[2][20:-3];
    #x is an array of string numbers, no longer a string of numbers separated by commas
    x = arraycontent.split(",")
    #Convert the array of string numbers into an array of float numbers
    A = np.array([])
    for number in x:
        A = np.append(A, float(number))

    #Extract the fps from the txt file
    fpsindexend = content[0].find("fps");
    fpsindexbeg = 0;
    for n in range(fpsindexend,0,-1):
        if (content[0][n:n+1] == '('):
            print (n);
            fpsindexbeg = n+1;
            break;
    print(content[0][fpsindexbeg:fpsindexend])
    #Convert the string into a float     
    fps = float(content[0][fpsindexbeg:fpsindexend])
    #Call create_plot given the array of amplitdues and the fps
    create_plot(A,fps);   