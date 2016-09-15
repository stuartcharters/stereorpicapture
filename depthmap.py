import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('left-ir-2.jpg',0)
imgR = cv2.imread('right-ir-2.jpg',0)

#stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
stereo = cv2.StereoBM(cv2.STEREO_BM_BASIC_PRESET,ndisparities=64, SADWindowSize=7)
disparity = stereo.compute(imgL,imgR)
cv2.imwrite('depthmap.jpg',disparity)
#plt.imshow(disparity,'gray')
#plt.show()
