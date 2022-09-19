import cv2
import numpy as np

input_img_path = 'D:/CVTest/Input/MyPicture.png'
output_img_directery = 'D:/CVTest/Output/'

# 读取
# 函数参数一： 需要读入图像的完整的路径
# 函数参数二： 标志以什么形式读入图像，可以选择一下方式：
# cv2.IMREAD_COLOR： 加载彩色图像。任何图像的透明度都将被忽略。它是默认标志
# cv2.IMREAD_GRAYSCALE：以灰度模式加载图像
# cv2.IMREAD_UNCHANGED：保留读取图片原有的颜色通道
origin_img = cv2.imread(input_img_path, cv2.IMREAD_UNCHANGED)


# 保存到本地
# 函数参数一： 保存的图像名称(字符串)
# 函数参数二： 图像对象，类型是numpy中的ndarray类型
cv2.imwrite(output_img_directery+'origin_img.png', origin_img)
