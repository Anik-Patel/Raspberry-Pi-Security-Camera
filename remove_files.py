import os 
import glob

for filename in glob.glob('D:/basic-motion-detection/Images/*.jpg'):
			os.remove(filename)