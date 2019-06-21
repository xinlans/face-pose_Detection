#-*- coding: utf-8 -*-

import cv2
import sys
import gc


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Usage: %s camera_id\r\n" % (sys.argv[0]))
		sys.exit(0)

	
	#框住人脸的矩形边框颜色
	color = [(255, 0, 0), (0, 255 ,0), (0, 0, 255)]
	
	#捕获指定摄像头的实时视频流
	cap = cv2.VideoCapture(int(sys.argv[1]))
	
	#人脸识别分类器本地存储路径
	cascade_path =[ './haarcascade_frontalface_alt_tree.xml',
					'./haarcascade_profileface.xml',
					'./lbpcascade_frontalcatface.xml'
					]
	cascade = []
	# 使用人脸识别分类器，读入分类器
	for i in cascade_path:
		cascade.append(cv2.CascadeClassifier(i))
	while True:
		#读取视频流中一帧图像
		isread, frame =cap.read()
		if isread:
			#图像灰度化，降低计算复杂度
			frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			for j in cascade:
				faceRects = j.detectMultiScale(frame_gray,scaleFactor = 1.2, minNeighbors = 3, minSize = (32,32))
				if len(faceRects) > 0:
					for faceRect in faceRects:
						x, y, w, h = faceRect

						cv2.rectangle(frame, (x, y), (x + w, y + h), color[cascade.index(j)], 2)


			#cv2.imshow("快把朕找出来啊",frame)
			cv2.imshow(r"识别本大爷",frame)
		
		k = cv2.waitKey(10)
		if k & 0xFF ==  ord('q'):
			break
			
	cap.release()
	cv2.destroyAllWindows()

					
		
		
