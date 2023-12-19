import cv2
import numpy as np


img2 = cv2.imread("./galaxy_leader.jpg",1)
img1 = cv2.imread("./yahya.jpg",1)


img1 = cv2.resize(img1,(750,600))
img2 = cv2.resize(img2,(750,600))
git remote add origin https://github.com/your-username/your-repository.git

rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]


# Now create a mask of LOGO and create its inverse mask also
img2gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:c