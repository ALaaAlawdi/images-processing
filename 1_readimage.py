import cv2

# Read the image
img = cv2.imread('./galaxy_leader.jpg', -1)


# Display the original and resized images
cv2.imshow('Galaxy leader', img)


# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
