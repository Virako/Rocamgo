#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cv import *

# for detect stone
def clip_image_(image,rect):
"""cut the interesting region of image
   To make the rectangle using function cvRect(int x, int y, int width, int height)     
"""
    
    
    """cvSetImageROI( IplImage* img, CvRect rect )"""
    cvSetImageROI(image,rect)
    """create destination image
       Note that cvGetSize will return the width and the height of ROI 
    """
    img2 = cvCreateImage(cvGetSize(image), image.depth, image.nChannels)

    cvCopy(image, img2, NULL)

    cvResetImageROI(image)
    
    return img2
    
    
    
def search_circle_in_image(image, goban):
    

    #spent the image in grayscale
    gray = cvCreateImage(cvSize(image.width, image.height), IPL_DEPTH_8U, 1)
    cvCvtColor(image, gray, CV_BGR2GRAY)
  
    #create 2 images for pass de filter
    gray_aux = cvCreateImage(cvSize(gray.width, gray.height), gray.depth, \
     gray.nChannels)
     
    gray_aux_2 = cvCreateImage(cvSize(gray.width, gray.height), gray.depth, \
     gray.nChannels)
     
    #pass the filter    
    cvCanny(gray, gray_aux_2, 50,55,3)
    cvSmooth(gray_aux_2, gray_aux, CV_GAUSSIAN, 5, 5)
    
    #¿update goban for the square?   
    circles = cvHoughCircles( gray_aux, storage, CV_HOUGH_GRADIENT, dp, \
     goban.square[0]/2, 50, 55, goban.square[0]/4,  goban.square[0] ) 
    
    return circles
    
def detected_colour_black_or_white_in_pixel_array(pixelarray):
    #in rgb the black is 0,0,0 and white is 255,255,255
    #in opencv the order of chanels colours is    
    pass
    

    
def look_for_areas_where_there_are_differences():
    pass
       
