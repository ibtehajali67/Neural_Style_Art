# how Overlay 2 images by python => Pillow
# install: pip install Pillow
# from PIL import Image

from PIL import Image

#Function to resize the image
def changeImageSize(maxWidth,maxHeight,image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


#overlay = input("Enter The Image1 : ")

#base = input("Enter The Image2 : ")
overlay = "image1.png"
base = "image2.png"
# Open The overlay and base
overlay = Image.open(overlay)
base = Image.open(base)


# Take two images for blending them together
overlay = changeImageSize(400, 350, overlay)
base = changeImageSize(400, 350, base)

bands = list(overlay.split())

if len(bands) == 4:
    # Assuming alpha is the last band
    bands[3] = bands[3].point(lambda x: x*0.8)

overlay = Image.merge(overlay.mode, bands)
base.paste(overlay, (1, 1), overlay)

# Save Image
base.save('result.png')

# show The new Image
base.show()
