import cv2
import autocar_module as m
import numpy as np

def get_roi(img):
    mask = np.zeros_like(img)           # 全黑遮罩
    points = np.array([[[146, 539],     # 建立多邊形座標
                        [781, 539], 
                        [515, 417],
                        [296, 397]]]) 
    cv2.fillPoly(mask, points, 255)     # 繪製多邊形
    roi = cv2.bitwise_and(img, mask)
    return roi
#---------------------------------------------------#
img = cv2.imread('road.jpg')        # 讀取圖片
edge = m.get_edge(img)              # 邊緣偵測
roi = get_roi(edge)                 # 取得 ROI 
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()