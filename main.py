from typing import SupportsComplex
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

segmentor=SelfiSegmentation()
fpsreader=cvzone.FPS()

# imgBg=cv2.imread("Images/night.jpg")

listimg=os.listdir("Images")
print(listimg)

imglist=[]

for imgPath in listimg:
    img=cv2.imread(f'Images/{imgPath}')
    imglist.append(img)
print(len(imglist))

indeximg=0

while True:
    success,img= cap.read()
    
    imgOut= segmentor.removeBG(img, imglist[indeximg], threshold=0.8)    

    imageStacked= cvzone.stackImages([img, imgOut], 2,1)
    _, imageStacked= fpsreader.update(imageStacked, color=(0,0,255))
    
    cv2.imshow("Image", imageStacked)
    #cv2.imshow("Image", img)
    #cv2.imshow("Image Out", imgOut)
    key= cv2.waitKey(1)
    
    if key == ord('a'):
        if indeximg > 0:
                indeximg -= 1
    elif key == ord('d'):
        if indeximg<len(imglist)-1:
                indeximg += 1
    elif key == ord('q'):
        break