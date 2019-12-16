# Raspberry-Pi-Security-Camera
I have created a repo that you can use to setup a Raspberry Pi security system.

##Setup
Change the info in `mail.py` to your info

Make a folder call `Images`

Change the `cv2.imwrite()` functions in `motion_detection.py` to the path of your folder

##Test
To test make sure your camera is in a place where the is no constant movement like a room. 
in the terminal type: python motion_detection.py
now your good to test
go into the room and walk around. Look for an email in your inbox

