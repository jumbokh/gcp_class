import requests
import cv2
import time
import re

base = 'https://westcentralus.api.cognitive.microsoft.com/vision/v2.0'
recog_url = f'{base}/recognizeText?mode=Printed'
key = '7fff44ff719f4c6eb1a027d19426ebf2'
headers = {'Ocp-Apim-Subscription-Key': key}                            # 查看結果的請求標頭
headers_stream = {'Ocp-Apim-Subscription-Key': key,                     # 辨識的請求標頭
                  'Content-Type': 'application/octet-stream'}  
def get_license(img):
    img_encode = cv2.imencode('.jpg', img)[1]       # 將 img 編碼為 jpg 格式，[1]返回資料, [0]返回是否成功
    img_bytes = img_encode.tobytes()                # 再將資料轉為 bytes, 此即為要傳送的資料
    r1 = requests.post(recog_url,            # 發出 POST 
                              headers = headers_stream, 
                              data = img_bytes)
    if r1.status_code != 202:                # 202 代表接受請求
        print(r1.json())
        return '請求失敗'
    #--↓↓辨識請求成功↓↓--#
    result_url = r1.headers['Operation-Location'] # 取得查看結果的請求路徑
    r2 = requests.get(result_url, headers = headers) # 發出 GET 請求
    while r2.status_code == 200 and r2.json()['status'] != 'Succeeded':
        r2 = requests.get(result_url, headers = headers)    # 繼續發出 GET
        time.sleep(0.5)
        print('status: ', r2.json()['status'])      # 顯示辨識狀態
    #--↓↓辨識完成↓↓--#
    carcard = ''  # 紀錄車牌
    lines = r2.json()['recognitionResult']['lines']
    for i in range(len(lines)):
        text = lines[i]['text'] # 取得辨識文字
        m = re.match(r'^[\w]{2,4}[-. ][\w]{2,4}$', text)    # 匹配是否為車牌格式
        if m != None:   # 匹配成功
            carcard = m.group()
            return carcard
    if carcard == '':   # 無匹配結果
        return '找不到車牌'
#----------------------------------------------------------#
try:
    img = cv2.imread('car.jpg') # 讀取圖片
    print('status:  Start')
    text = get_license(img)     # 辨識圖片中的車牌
    print('車牌：', text)
    cv2.imshow('Frame', img)    # 顯示圖片
    cv2.waitKey(0)              # 等待
    cv2.destroyAllWindows()     # 關閉視窗
except:
    print('讀取圖片失敗')






