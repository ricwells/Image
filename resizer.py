from PIL import ExifTags
import PIL.Image
from tkinter import *

import os

class resizer:
    EXTENSIONS = ['.jpg', '.png']
    ORIENTATION = 0

    def __init__(self):
        for self.ORIENTATION in ExifTags.TAGS.keys():
            if ExifTags.TAGS[self.ORIENTATION]=='Orientation':
                break

    def resize(self, inPath, factor, root):
        outPath = inPath + '\\' + "edited"
        items = os.listdir(inPath)
        if "edited" not in items:
            os.mkdir(outPath)

        i = 1
        for dirItem in  os.listdir(inPath):
            if dirItem[-4:] in self.EXTENSIONS:
                fullInPath = inPath + '\\' + dirItem
                img = PIL.Image.open(fullInPath)
                exif = img._getexif()
                if exif[self.ORIENTATION] == 6:
                    img = img.rotate(270, expand=True)
                elif exif[self.ORIENTATION] == 3:
                    img = img.rotate(180, expand=True)
                elif exif[self.ORIENTATION] == 8:
                    img = img.rotate(90, expand=True)

                w, h = img.size
                newImg = img.resize((round(w * factor), round(h * factor)))
                
                l = Label(root, text=f"({i}) saving {dirItem}, w,h: {w} {h}, orientation: { exif[self.ORIENTATION] }")
                l.pack()
                root.update()

                # print(f"({i}) saving {dirItem}, w,h: {w} {h}, orientation: { exif[self.ORIENTATION] }")
                newImg.save(outPath + '\\' + dirItem)
                i += 1