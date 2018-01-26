import cv2
import numpy as np

# Run this script from the same directory as your Data folder

# Grab your webcam on local machine
cap = cv2.VideoCapture(0)

# Give image a name type
name_type = 'NotFruit_'

# Initialize photo count
number = 0

# Specify the name of the directory that has been premade and be sure that it's the name of your class
# Remember this directory name serves as your datas label for that particular class
set_dir = 'not_fruit'

print ("Photo capture enabled! Press esc to take photos!")

while True:
    # Read in single frame from webcam
    ret, frame = cap.read()

    # Use this line locally to display the current frame
    cv2.imshow('Color Picture', frame)

    # Use esc to take photos when you're ready
    if cv2.waitKey(10) & 0xFF == 27:

        # If you want them gray
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        # If you want to resize the image
        color_resize = cv2.resize(frame,(256,256), interpolation = cv2.INTER_NEAREST)

        # Save the image
        cv2.imwrite('Data/' + set_dir + '/' + name_type + "_" + str(number) + ".png", color_resize)

        print ("Saving image number: " + str(number))

        number+=1

    # Press q to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
