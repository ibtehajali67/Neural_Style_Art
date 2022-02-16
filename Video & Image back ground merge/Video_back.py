import cv2
from PIL import Image
import numpy

x,y=[],[]
img = Image.open("input_image/11.jpg") # get image
pixels = img.load() # create the pixel map
con=0
for i in range(img.size[0]): # for every pixel:
    for j in range(img.size[1]):
        if pixels[i,j] != (0,0,0,0):
            y.append(j)
            x.append(i)
            con+=1
x=numpy.array(x)
y=numpy.array(y)
img2=cv2.imread("input_image/11.jpg")
#img=numpy.array(img)               
img_height,img_width,_=img2.shape
print(img_height,img_width)

cap = cv2.VideoCapture('in_video/20.mp4')
print (cap.grab())
if cap.isOpened():
    frame_width  = int(cap.get(3))
    frame_height = int(cap.get(4))
                               

size = (frame_width, frame_height)
print(size)
a = (int(.5 *frame_width)-int(.5 *img_width))
b = (int(.5 * frame_height)-int(.5 *img_height))
out = cv2.VideoWriter('out_video/43.mp4', 
                         cv2.VideoWriter_fourcc(*'mp4v'),
                         10, size)
print(a)
print(b)
count=0
while(True):
    ret, frame = cap.read()
    frame[y+b, x+a]=img2[y,x]  
    cv2.resize(frame,size)
    out.write(frame)
    count+=1
    if cv2.waitKey(20) & 0xFF == 27:
        break
print("Done")
cap.release()
cv2.destroyAllWindows()

