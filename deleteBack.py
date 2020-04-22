import numpy as np 
import cv2 
import glob
import os
from PIL import Image  
from resizeimage import resizeimage

path1 = "D:/Giao Trinh/Nam4/Ki2/HTDPT/Flower_DataSet/Buttercup"
path2 = "D:/Giao Trinh/Nam4/Ki2/HTDPT/Flower_DataSet/Buttercup2"

filenames = glob.glob(path1+"/*.jpg")
images = [cv2.imread(img) for img in filenames]
i=0
# for imgo in images:
while(i<len(images)):
	
	imgo=images[i]
	height, width = imgo.shape[:2] 
	#Create a mask holder 
	mask = np.zeros(imgo.shape[:2],np.uint8) 

	#Grab Cut the object 
	bgdModel = np.zeros((1,65),np.float64) 
	fgdModel = np.zeros((1,65),np.float64) 
	print(i)
		#Hard Coding the Rect The object must lie within this rect. 
	rect = (10,10,width-30,height-30) 
	cv2.grabCut(imgo,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT) 
	mask = np.where((mask==2)|(mask==0),0,1).astype('uint8') 
	img1 = imgo*mask[:,:,np.newaxis] 

		#Get the background 
	background = imgo - img1 

		#Change all pixels in the background that are not black to white 
	background[np.where((background > [0,0,0]).all(axis = 2))] = [0,0,0] 

		#Add the background and the image 
	final = background + img1 
	                # need to do some more processing here             
	cv2.imwrite(path2+"/"+os.path.basename(filenames[i]),final)
	i=i+1




