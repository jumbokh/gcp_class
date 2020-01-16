import cv2
import autocar_module as m
import numpy as np

img = cv2.imread('road.jpg')        
edge = m.get_edge(img)              # 邊緣偵測
mask = np.zeros_like(edge)          # 全黑遮罩
points = np.array([[[146, 539],     # 建立多邊座標
                    [781, 539], 
                    [515, 417],
                    [296, 397]]]) 
cv2.fillPoly(mask, points, 255)     # 繪製三角形
cv2.imshow('Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()