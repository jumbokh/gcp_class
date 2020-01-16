import cv2

try:
    img = cv2.imread('car.jpg')             # 讀取圖片
    img_small = cv2.resize(img, (300, 100)) # 改變尺寸
    cv2.imshow('Frame1', img)               # 顯示原圖
    cv2.imshow('Frame2', img_small)         # 顯示新圖
    cv2.waitKey(0)                          # 等待
    cv2.destroyAllWindows()                 # 關閉視窗
    try:
        cv2.imwrite('small.jpg', img_small) # 儲存影像
        print('saved')
    except:
        print('Error：write')
except:
    print('Error：read')