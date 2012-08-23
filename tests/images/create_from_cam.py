
from cv import CaptureFromCAM
from cv import CaptureFromFile
from cv import QueryFrame
from cv import ShowImage
from cv import SaveImage
from cv import WaitKey


#capture = CaptureFromCAM(0)
capture = CaptureFromFile('../../prueba2.avi')

num = 7
while 1:
    num += 1
    img = QueryFrame(capture)
    key = WaitKey(30)
    if key != -1:
        SaveImage('img%d.png' %num, img)
    ShowImage("video", img)

