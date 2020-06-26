import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
d = {'key':'value'}
m = {'key':'value'}
c = {'key':'value'}

cnt = 0
selfile=''
selparent=''

def orb_compute(file1,file2,cnt):

    img1 = cv2.imread(file1,0) # queryImage
    img2 = cv2.imread(file2,0) # trainImage

    # Initiate ORB detector
    orb = cv2.ORB_create()
    # find the keypoints and descriptors with ORB
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    file = os.path.basename(file2)
    parent=os.path.basename(os.path.dirname(file2))
    m[file]= matches
    c[file]= parent
    cnt = len(matches)
    #if(len(matches)>= cnt ):
    #    cnt=len(matches)
    #    selfile=file
    #    selcategory=parent
    return cnt