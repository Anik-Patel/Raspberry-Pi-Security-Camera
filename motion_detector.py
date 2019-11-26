# USAGE
# python motion_detector.py
# python motion_detector.py --video videos/example_01.mp4

# import the necessary packages

import argparse
import datetime
from mail import mail
import time
import cv2
from convert import convert
import os
import glob
def grab_contours(cnts):

    # if the length the contours tuple returned by cv2.findContours

    # is '2' then we are using either OpenCV v2.4, v4-beta, or

    # v4-official

    if len(cnts) == 2:

        cnts = cnts[0]



    # if the length of the contours tuple is '3' then we are using

    # either OpenCV v3, v4-pre, or v4-alpha

    elif len(cnts) == 3:

        cnts = cnts[1]



    # otherwise OpenCV has changed their cv2.findContours return

    # signature yet again and I have no idea WTH is going on

    else:

        raise Exception(("Contours tuple must have length 2 or 3, "

            "otherwise OpenCV changed their cv2.findContours return "

            "signature yet again. Refer to OpenCV's documentation "

            "in that case"))



    

    return cnts




vs = cv2.VideoCapture(0)
time.sleep(2)
# initialize the first frame in the video stream
for i in range(50):
    ret, img = vs.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    firstFrame = cv2.GaussianBlur(gray, (21, 21), 0)
    
    if cv2.waitKey(30) == 27:
        break
    
firstframe = gray
    
count = 0
# loop over the frames of the video
while True:
	count += 1
    
	ret, frame = vs.read()
    
	text = "Unoccupied"

    
	if frame is None:
		break

    # resize the frame, convert it to grayscale, and blur it
    
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

   
    

    # compute the absolute difference between the current frame and
    # first frame
	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

    # dilate the thresholded image to fill in holes, then find contours
    # on thresholded image
	thresh = cv2.dilate(thresh, None, iterations=2)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
	cnts = grab_contours(cnts)
    
    
    

    # loop over the contours
	for c in cnts:
        # if the contour is too small, ignore it
        
        # compute the bounding box for the contour, draw it on the frame,
        # and update the text
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		text = "Occupied"
		cv2.imwrite('C:/Path/Images/Security_Update{}.jpg'.format(count), frame)
        
		firstframe = gray
        
    # draw the text and timestamp on the frame
	
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    # show the frame and record if the user presses a key
	cv2.imshow("Security Feed", frame)
	if (count % 500) == 0:
		convert()
		mail('project.avi')
		for filename in glob.glob('D:/Path/Images/*.jpg'):
			os.remove(filename)
			print('done')
			count = 1

	key = cv2.waitKey(1) & 0xFF

    # if the `q` key is pressed, break from the lop
	if key == ord("q"):
		break

# cleanup the camera and close any open windows
vs.release()
cv2.destroyAllWindows()

