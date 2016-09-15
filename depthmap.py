import numpy as np
    2 import cv2
    3 from matplotlib import pyplot as plt
    4
    5 imgL = cv2.imread('tsukuba_l.png',0)
    6 imgR = cv2.imread('tsukuba_r.png',0)
    7
    8 stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    9 disparity = stereo.compute(imgL,imgR)
   10 plt.imshow(disparity,'gray')
   11 plt.show()
