import cv2
import autocar_module as m
import numpy as np

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

#-------------------------------------------------------------#
img = cv2.imread('road.jpg')            # 讀取圖片
edge = m.get_edge(img)                  # 邊緣偵測
roi = m.get_roi(edge)                   # 取得 ROI
lines = cv2.HoughLinesP(image=roi,      # Hough 轉換取得線段座標陣列
                        rho=3,
                        theta=np.pi/180,
                        threshold=60,
                        minLineLength=40,
                        maxLineGap=50)
avglines = get_avglines(lines)          # 取得左右 2 條平均線方程式
if avglines is not None:
    lines = get_sublines(img, avglines) # 取得要畫出的左右 2 條線段
    img = m.draw_lines(img, lines)      # 畫出線段
    cv2.imshow('Line', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

