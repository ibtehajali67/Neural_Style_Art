import cv2
from PIL import Image
import numpy
def changeImageSize(maxWidth,maxHeight,image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


img = Image.open("input_image/9.png") # get 
overlay = changeImageSize(125, 125, img)
           
cap = cv2.VideoCapture('in_video/555.mp4')
print (cap.grab())
out = cv2.VideoWriter('out_video/45.mp4',cv2.VideoWriter_fourcc(*'mp4v'),10, (125, 125))

bands = list(overlay.split())
print(bands)
if len(bands) == 4:
    # Assuming alpha is the last band
    bands[3] = bands[3].point(lambda x: x*0.8)
overlay = Image.merge(overlay.mode, bands)
while(True):
    ret, frame = cap.read()
    print(frame)
    base = Image.fromarray(frame) 
    base = changeImageSize(125, 125, base)
    base.paste(overlay, (1,1), overlay)
    base=numpy.array(base)
    #base = cv2.cvtColor(base,cv2.COLOR_BGR2RGB) 
    out.write(base)
    if cv2.waitKey(20) & 0xFF == 27:
        break
print("Done")
cap.release()
cv2.destroyAllWindows()

