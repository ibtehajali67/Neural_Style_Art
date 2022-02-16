import cv2
import numpy as np
import os
import glob
from u2net_test import main
import argparse
parser = argparse.ArgumentParser(description="Process some integer.")
parser.add_argument('-m','--mask_dir',type=str , help="path of mask of image")
parser.add_argument('-st','--style_output_dir',type=str , help="path of mask of image")
parser.add_argument('-inn','--image_dir',type=str , help="path of image")
# parser.add_argument('-mk','--mask',type=str , help="path of image")
parser.add_argument('-o','--out_dir',type=str , help="path of mask of image")
args=parser.parse_args()
main(args.image_dir,args.mask_dir)
mask=args.mask_dir+"/*.png"
def object_style(n,img,forg,bkg,out):
  f=((os.path.basename(forg)).split("_")[1]).split(".")[0]
  b=(os.path.basename(bkg)).split("_")[1]
  img=cv2.imread(img) #input image mask
  forg=cv2.imread(forg) #forground_styled result image
  bkg=cv2.imread(bkg) #background_styled result image 
  h,w,_=forg.shape
  img=cv2.resize(img,(w,h))
  bkg=cv2.resize(bkg,(w,h))
  y,x =np.where(np.all(img ==[0,0,0], axis=-1))
  forg[y,x]=bkg[y,x]
  # bkg[y,x]=forg[y,x]
  cv2.imwrite(out+n+"_"+f+"_"+b,forg)
def main():
    for x in glob.glob(mask):
      name=os.path.basename(x)
      name=name.split(".")[0]
      print(name)
      for forg in glob.glob(args.style_output_dir):
        s=os.path.basename(forg)
        if s.split("_")[0]==name:
            f=forg
            for back in glob.glob(args.style_output_dir):
                s=os.path.basename(back)
                if s.split("_")[0]==name:
                    if back != f:
                        b=back
                        object_style(name,x,f,b,args.out_dir)
    print("done")
if __name__ == "__main__":
    main()
    