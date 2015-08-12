from PIL import Image
import os

failed = 0
small = 0
sizex = 3200
sizey = 2000
smalldir = "small"
gooddir = "good"
brokendir = "broken"

for file in os.listdir("."):
    if file.endswith(".jpg") or file.endswith(".jpeg"):
        try:
          im = Image.open(file)
          im.verify()
          if (im.size[0] < sizex) or (im.size[1] < sizey):
            os.rename(file,"./" + smalldir + "/" + file)
          else:
            os.rename(file,"./" + gooddir + "/" + file)
        except:
          failed += 1
          os.rename(file,"./" + brokendir + "/" + file)
