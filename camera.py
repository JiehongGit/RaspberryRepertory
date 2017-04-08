# -*- coding: UTF-8 -*- 
# 导入必要的软件包
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# 初始化相机并抓取原始相机捕获的引用
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# 让摄像头进行热身
time.sleep(0.1)

# 从摄像头捕捉帧
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
          # 抓住原NumPy数组表示的图像，然后初始化时间戳
    image = frame.array

          # 展示frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

          # 在准备下一帧时清除流
    rawCapture.truncate(0)

          # 按q退出frame
    if key == ord("q"):
        break