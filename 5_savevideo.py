# حفظ الفيديو

# import cv2
# from matplotlib import pyplot
# import numpy

# capture = cv2.VideoCapture(0) #تحديد أي كاميرا
# while(True):
#     #capture frame by frame
#     #ret->0->لا تلتقط صورة
#     #ret->1->التقط صورة

#     ret,frame = capture.read()

#     #our operation on the frame here
#     # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
#     #display the result
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) == ord('q'):
#         break

# capture.release()
# cv2.destroyAllWindows()


import cv2

# Define the video codec, output file name, FPS, and frame size
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = 'output.mp4'
fps = 30.0  # Frames per second
frame_size = (640, 480)  # Frame size

# Create a VideoWriter object to save the video
video_writer = cv2.VideoWriter(output_file, fourcc, fps, frame_size)

# Open the video capture
capture = cv2.VideoCapture(0)  # Specify the camera index

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()

    # Our operation on the frame here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Write the frame to the VideoWriter object
    video_writer.write(gray)

    # Display the resulting frame
    cv2.imshow('frame', gray)

    # Check for the 'q' key press to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture and VideoWriter objects
capture.release()
video_writer.release()

# Destroy any remaining windows
cv2.destroyAllWindows()
