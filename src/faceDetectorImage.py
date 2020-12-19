import numpy as np
#import argparse
import cv2
'''
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, help = "Input Imagepath")
args = vars(ap.parse_args())
'''
caffeModel = "res10_300x300_ssd_iter_140000.caffemodel"
prototextPath = "deploy.prototxt.txt"

print("loading the model...")
net = cv2.dnn.readNetFromCaffe(prototextPath,caffeModel)

#image = cv2.imread(args.get('image'))
image = cv2.imread("C:/Users/KIIT/Desktop/1.jpeg")
h,w = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image,(300,300)),1.0,(300,300),(104.0, 177.0, 123.0))

net.setInput(blob)
detections = net.forward()

for i in range(0,detections.shape[2]):
    confidence = detections[0,0,i,2]
    
    print(confidence)
    if confidence > 0.5:
        box= detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        
        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(image, (startX, startY), (endX, endY),
                      (0, 0, 255), 2)
        cv2.putText(image, text, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

cv2.imshow("Output", image)
cv2.waitKey(0)
