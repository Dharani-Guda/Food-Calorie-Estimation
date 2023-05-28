# import OpenCV and pyplot
from audioop import avg
import cv2 as cv
from matplotlib import pyplot as plt

def volume(images):
# read left and right images
	imgR = cv.imread(images, 0)
	imgL = cv.imread(images, 0)

	# creates StereoBm object
	stereo = cv.StereoBM_create(numDisparities = 16,
								blockSize = 15)

	# computes disparity
	disparity = stereo.compute(imgL, imgR)
	print(imgR.ravel())
	depth=abs(max(imgR.ravel())//disparity)
	return depth[0][0]
