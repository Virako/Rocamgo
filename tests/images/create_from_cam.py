
from cv import CaptureFromCAM
from cv import CaptureFromFile
from cv import QueryFrame
from cv import ShowImage
from cv import SaveImage
from cv import WaitKey


# Create images from video or file. 4 photos per seconds. 
# DANGER with the image's names. 
#capture = CaptureFromCAM(0)
capture = CaptureFromFile('../videos/capture1.avi')

num = 12
while 1:
    num += 1
    img = QueryFrame(capture)
    key = WaitKey(250)
    if not img:
        break
    SaveImage('img%04d.png' %num, img)

