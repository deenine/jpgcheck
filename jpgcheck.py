from PIL import Image
import os

#counters
failed = 0
small = 0
good = 0

# dimensions to define 'small' images
sizex = 320
sizey = 200

#directories
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
	  # On windows this throws an exception due to the file still being open from above,
          # too lazy to fix so just leaving broken files where they are for the moment 
          #os.rename(file,"./" + brokendir + "/" + file)

    if (failed + good + small) % 1000 == 0:
        print "Processed %d broken: %d small: %d good: %d" % ((failed + good + small), failed, small, good)


print "\nFinished\n------------\n Total: %d broken: %d small: %d good: %d" % ((failed + good + small), failed, small, good)

