import numpy as np
from PIL import Image
from Definition import *

# 在draw.py文件中
width, height = 800, 600  # 定义画布的宽度和高度
# Define frame_buf as a 2D array filled with zeros
frame_buf = np.zeros((height, width, 3), dtype=np.uint8)

# 调用draw_line函数时，传递width和height作为参数
#draw_line(np.array([0, 0, 1.0]), np.array([800, 600, 1.0]))

# 将NumPy数组转换为图像
img = Image.fromarray(frame_buf)

# 显示图像
img.show()