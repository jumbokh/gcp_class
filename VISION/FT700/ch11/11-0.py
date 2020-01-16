import cv2

img = cv2.imread('road.jpg')    # 讀取圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 灰階處理
blur = cv2.GaussianBlur(gray, (3, 3), 0)        # 高斯模糊
cv2.imshow('Normal', img)   # 顯示原始圖片
cv2.imshow('Gray', gray)    # 顯示灰階圖片
cv2.imshow('Blur', blur)    # 顯示高斯模糊圖片
cv2.waitKey(0)
cv2.destroyAllWindows()