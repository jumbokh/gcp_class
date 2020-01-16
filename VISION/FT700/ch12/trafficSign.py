import cv2

img = cv2.imread('pic_turnR.jpg')
detector = cv2.CascadeClassifier('haar_turnR.xml')
signs = detector.detectMultiScale(img, 
                                  scaleFactor=1.1, 
                                  minNeighbors=2, 
                                  minSize=(30, 30))    
if len(signs) > 0 :
    for (x, y, w, h) in signs:          
        cv2.rectangle(img, 
                      (x, y), (x+w, y+h), 
                      (0, 0, 255), 2)  
else:
    print('nothing')

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()