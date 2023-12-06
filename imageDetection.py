import cv2
import easyocr
import matplotlib.pyplot as plt

import rgbOperations as rgbO

image_path = "math12-20-4-x-16-article-386w.png"

img =  cv2.imread(image_path)

print("size:",img.shape)

reader = easyocr.Reader(['en'])

allowList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

readText = reader.readtext(img)

imgScale = int(1*img.shape[0]/400) + 2

for textRow in readText:
    print(textRow)
    
    bbox, text, score = textRow

    scoreColor = rgbO.BlendBetweenColorsWithWeight((255,0,0),(0,255,0),score)

    cv2.rectangle(img, bbox[0],bbox[2],scoreColor,imgScale)

    cv2.putText(img, text, bbox[0],cv2.FONT_HERSHEY_COMPLEX,imgScale,scoreColor,imgScale)





plt.imshow(img)
plt.show()