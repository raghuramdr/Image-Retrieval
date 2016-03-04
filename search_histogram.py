from matplotlib import pyplot as plt
import numpy as np
import cPickle as pickle
from cbir import Search_Histogram
import os
import sys
import cv2

os.chdir('/home/raghuram/Desktop/Computer Vision Projects/coil-100')
query_image_name = raw_input('Please enter the name of the image: ')
query_image_name = query_image_name+'.png'
print query_image_name
file_check = os.path.isfile(query_image_name)

if file_check==False:  
   print 'Please check the name of the file again'
   print 'Exiting program'
   sys.exit()
else:
   I = cv2.imread(query_image_name)
   cv2.imshow("QueryImage",I)
   cv2.waitKey(0)
   # Note: The query image is part of the original database. So, there is no need to index the query image
   # In case, the query image is an external image, it needs to be described and indexed.
   # Load the saved index 
   f = open('index.csv',"r")
   index = pickle.load(f)
   f.close()
   search_image = Search_Histogram(index) # Instantiate the Search_Histogram class
   # Now load the features of the query image
   query_feature = index[query_image_name]
   output = search_image.search(query_feature)
   D = {}
   # Convert the output list into a dictionary
   for i in range(0,len(output)):
       l = output[i]
       D[l[1]] = l[0]
   
   ctr = 1
   for (image_name,interesection_value) in D.items():
       I = cv2.imread(image_name)
       title = "Image number"+str(ctr)
       cv2.imshow(title,I)
       ctr+=1
  
   cv2.waitKey(0)
      
  
         
