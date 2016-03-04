import numpy as np
import glob
import os
import cv2
import cPickle as pickle


## Code starts from here ##
class Features: 
      def __init__(self,bins):
      # Self stores the number of bins for the histogram
       self.bins = bins
      
      def describe(self,image):
       #image = cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
       hist = cv2.calcHist([image],[0,1,2],None,self.bins,[0,256,0,256,0,256]) # Get the BGR histogram
       hist = cv2.normalize(hist) # Normalize the histogram to achieve invariance to scale
       return hist.flatten() # Return the flattened 1-D histogram
       
os.chdir('/home/raghuram/Desktop/Computer Vision Projects/coil-100')
file_list = glob.glob('*.png')
#print type(file_list)

index = {}
'''
for name in file_list:
    I = cv2.imread(name)
    #cv2.imshow('Image',I)
    #cv2.waitKey(0)
    obj = Features([8,8,8])
    histogram = obj.describe(I)
    name = str(name)
    index[name] = histogram # Store the index
    print name

f = open('index.csv',"w")
pickle.dump(index,f)
f.close()  
'''

class Search_Histogram:
     def __init__(self,index):
          self.index = index
   
     def search(self,queryHistogram):
         result = {} # Dictionary of results 
         for (k,histogram) in self.index.items(): # The method items() returns a list of dict's (key, value) tuple pairs
             d = self.comparison(histogram,queryHistogram)
             result[k] = d # Store the distance using the image name as key in results dictionary   
        #Sort the results to obtain the most relevant results
         result = sorted([v,k] for(k,v) in result.items())
         result = result[::-1]   
         result = result[0:5] # Store only the top five results
         return result

     def comparison(self,indexed_image_hist,query_hist):
         distance = cv2.compareHist(indexed_image_hist,query_hist,cv2.cv.CV_COMP_INTERSECT)
         return distance  	
