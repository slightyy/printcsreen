import cv2
import mss
import numpy as np

with mss.mss() as sct:
    # 设置截取区域，此处为整个屏幕
    monitor = sct.monitors[0]

    while True:
        # 截取屏幕图像
        img = sct.grab(monitor)

        # 将截取的图像数据转换为numpy数组
        img = np.array(img)

        # 在窗口中显示图像
        cv2.imshow("Real-time Screenshot", img)

        # 按下 ESC 键退出循环
        if cv2.waitKey(1) == 27:
            break

cv2.destroyAllWindows()
#macos 需要截取当前屏幕的话要在设置里面允许pycharm录制屏幕
