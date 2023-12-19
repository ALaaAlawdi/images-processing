# Page 70 in book
import cv2

img = cv2.imread('./galaxy_leader.jpg', 1)
print(img[0, 0])  # return the color [Red,Green,blue]
print(img[0, 0, 0])  # return Red
print(img[0, 0, 1])  # return green
print(img[0, 0, 2])  # return blue

# change Pixel Color, The Pixel 100,100 his color will be 0 red , 0 green 255 blue
for i in range(10):
    # img[i,i] = [0, 0,255]

    # Pixel 10,10 RED  new value 255
    img.itemset((i, i, 2), 255)


print(img[100, 100])
#حجم الصورة وعدد القنوات اللونية
print(img.shape)
#عدد البكسلات
print(img.size)
#نوع البيانات
print(img.dtype)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyWindow()
