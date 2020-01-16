import cv2                      # 匯入 cv2 套件

capture = cv2.VideoCapture(0)   # 建立攝影機物件
if capture.isOpened():          
    while True:
        sucess, img = capture.read()        # 讀取影像
        if sucess:
            cv2.imshow('Frame', img)        # 顯示影像
        k = cv2.waitKey(100)                # 等待按鍵輸入
        if k == ord('s') or k == ord('S'):  # 按下 S(s)
            cv2.imwrite('shot.jpg', img)    # 儲存影像
            print('稍後在此加入車牌辨識功能')   
            
        if k == ord('q') or k == ord('Q'):  # 按下 Q(q) 結束迴圈
            print('exit')
            cv2.destroyAllWindows()         # 關閉視窗
            capture.release()               # 關閉攝影機
            break
else:
    print('開啟攝影機失敗')

 



