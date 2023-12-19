#العمليات الحسابية على الصور
import cv2
import numpy as np
from matplotlib import pyplot as plt
x = np.uint8([250])
y = np.uint8([10])

#الجمع cv2
print (cv2.add(x,y)) # 250+10 = 260 => 255
#الجمع np
print (x+y) # 250+10 = 260 % 256 = 4



img1 = cv2.imread("./galaxy_leader.jpg",1)
img2 = cv2.imread("./yahya.jpg",1)

img2 = cv2.resize(img2,(750,600))
img1 = cv2.resize(img1,(750,600))

res = cv2.addWeighted(img1,0.7,img2,0.3,0)
plt.imshow(res)
plt.xticks([]),plt.yticks([])
plt.show()
