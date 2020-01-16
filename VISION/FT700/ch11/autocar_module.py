import cv2
import numpy as np

def get_edge(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 灰階處理
    blur = cv2.GaussianBlur(gray, (13, 13), 0)        # 高斯模糊
    canny = cv2.Canny(blur, 50, 150)                # 邊緣偵測
    return canny

def get_roi(img):
    mask = np.zeros_like(img)          # 全黑遮罩
    points = np.array([[[146, 539],     # 建立多邊形座標
                        [781, 539],
                        [515, 417],
                        [296, 397]]])
    cv2.fillPoly(mask, points, 255)    # 多邊三角形
    roi = cv2.bitwise_and(img, mask)
    return roi

def draw_lines(img, lines):                 # 建立自訂函式
    for line in lines:
        points = line.reshape(4,)       # 降成一維 shape = (4,)
        x1, y1, x2, y2 = points         # 取出直線座標
        cv2.line(img,                   # 繪製直線
                 (x1, y1), (x2, y2),
                 (0, 0, 255), 3)
    return img

def get_avglines(lines):
    if lines is None:                   # 如果有找到線段
        print('偵測不到直線線段')
        return None
    #-----↓先依斜率分到左組或右組↓
    lefts = []
    rights = []
    for line in lines:
        points = line.reshape(4,)
        x1, y1, x2, y2 = points
        slope, b = np.polyfit((x1, x2), (y1, y2), 1)  # y = slope*x + b
        # print(f'y = {slope} x + {b}')  #若有需要可將斜率與截距印出
        if slope > 0:   # 斜率 > 0, 右邊的直線函數
            rights.append([slope, b])  # 以 list 存入
        else:       # 斜率 < 0, 左邊的直線函數
            lefts.append([slope, b])  # 以 list 存入

    #-----↓再計算左組與右組的平圴線↓
    if rights and lefts:     # 必須同時有左右兩邊的直線函數
        right_avg = np.average(rights, axis=0)    # 取得右邊的平均直線
        left_avg = np.average(lefts, axis=0)      # 取得左邊的平均直線
        return np.array([right_avg, left_avg])
    else:
        print('無法同時偵測到左右邊緣')
        return None

def get_sublines(img, avglines):
	sublines = []					# 用於儲存線段座標
	for line in avglines:		# 一一取出所有直線函數
		slope, b = line		    # y = slope*x + b
		y1 = img.shape[0]		# 影像高度 (即影像的最底部位
		y2 = int(y1*(3/5))		# 取影像高度的 3/5 位置為線段
		x1 = int((y1 - b) / slope)	# x = (y-b/m), 取得線段 x 座標
		x2 = int((y2 - b) / slope)
		sublines.append([x1, y1, x2, y2])	# 座標存入串列中
	return np.array(sublines)		# 將串列轉為陣列回傳
