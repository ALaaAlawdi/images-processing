#تحسين طريقة عرض الصورة
import numpy
from matplotlib import pyplot 
import cv2


img = cv2.imread('./galaxy_leader.jpg')
pyplot.imshow(img , cmap='gray',interpolation='bicubic')

#اخفاء تدرجات محور x , y
pyplot.xticks([])
pyplot.yticks([])

pyplot.show()