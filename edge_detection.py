# Author: Endri Dibra

# importing the required libraries
import cv2
import numpy as np

# getting camera of the device(e.x pc, laptop)
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)


while True:

    # reading the input of the camera (video)
    success, frame = camera.read()

    if success:

        # displaying the camera(video)
        cv2.imshow("Camera", frame)

        # applying laplacian filter and displaying it
        laplacian = cv2.Laplacian(frame, cv2.CV_64F)
        laplacian = np.uint8(laplacian)
        cv2.imshow("Laplacian", laplacian)

        # applying canny filter (for edges) and displaying it
        edges = cv2.Canny(frame, 100, 100)
        cv2.imshow("Canny", edges)

        # unless the milliseconds run out or user press keyboard
        # for interruption the cameras will be displayed
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

# releasing and closing all the open cameras
camera.release()
cv2.destroyAllWindows()