import cv2
import matplotlib.pyplot as plt	  # 匯入 pyplot
import autocar_module as m	    # 匯入自訂模組

img = cv2.imread('road.jpg')    # 讀取圖片
edge = m.get_edge(img)       # 取得邊緣圖
plt.imshow(edge)            # 顯示邊緣圖及座標
plt.show()					     # 顯示