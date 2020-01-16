import cv2
import autocar_module as m
import numpy as np

def draw_lines(img, lines):             # 建立自訂函式
    for line in lines:
        points = line.reshape(4,)       # 降成一維 shape = (4,)
        x1, y1, x2, y2 = points         # 取出直線座標
        cv2.line(img,                   # 繪製直線
                 (x1, y1), (x2, y2), 
                 (0, 0, 255), 3)   
    return img                          # 回傳繪製直線後的影像
#------------------------------------------------------------------#
img = cv2.imread('road.jpg')           # 讀取圖片
edge = m.get_edge(img)                 # 邊緣偵測
roi = m.get_roi(edge)                  # 取得 ROI 
lines = cv2.HoughLinesP(image=roi,     # Hough 轉換取得線段座標陣列
                        rho=3, 
                        theta=np.pi/180, 
                        threshold=60, 
                        minLineLength=40, 
                        maxLineGap=50)
print(lines)
if lines is not None:                   # 如果有找到線段
    img = draw_lines(img, lines)        # 在原圖繪製線段
else:
    print('偵測不到直線線段')
cv2.imshow('Line', img)
cv2.waitKey(0)
cv2.destroyAllWindows()