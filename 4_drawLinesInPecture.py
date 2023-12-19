import numpy
import cv2
img = numpy.zeros((512,512,3),numpy.uint8)
#512 , 512 The size
#3 Color as RGB
#numpy.uint8 -> تحديد نوع الارقام صحيحة او عشرئية الخ..

# cv2.line(img,(0,0),(511,511),(0,0,255),5)

# cv2.line(img,(0,0),(511,0),(0,255,255),5)
# cv2.line(img,(511,0),(511,511),(255,0,255),5)
# cv2.line(img,(511,511),(0,511),(255,0,0),5)
# cv2.line(img,(0,0),(0,511),(255,255,255),5)

cv2.rectangle(img , (10,10),(500,500),(255,0,255),5)


#img -> الصورة الي يرسم عليها
#(0,0) starting point
#(511,511) ending point
#color
#thick line

# lets see
cv2.imshow('show image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()