# اقتصاص الصورة
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('./color-schemes.png')
print(img.shape)
#[y1:y2,x1:x2]

part = img[125:240, 110:230]
for i in range(120,600,120):
    # img[0:115, 0:i] = part
    img[0:115, 0:120] = part
# img[0:115, 120:240] = part
# img[0:115, 240:360] = part
# img[0:115, 360:480] = part
# img[0:115, 480:600] = part



plt.imshow(img)
# plt.xticks([])
# plt.yticks([])
plt.show()
