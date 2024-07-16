import sys

import psutil
from pywinauto import mouse
from pywinauto.application import Application


def get_pid(processName):
    """
    根据进程名获取进程 id
    :param processName: 进程名
    :return:
    """
    for proc in psutil.process_iter():
        try:
            if proc.name() == processName:
                return proc.pid
        except psutil.NoSuchProcess:
            pass
    return -1


def getApp(startPath, processName):
    """
    获取app
    :param startPath: app启动文件路径
    :param processName: app进程名
    :return:
    """
    if get_pid(processName) == -1:
        # 启动
        Application(backend='uia').start(startPath)
    # 连接
    app = Application(backend='uia').connect(process=get_pid(processName))
    return app


if __name__ == '__main__':
    # 单击：默认左键
    # mouse.click(button="left", coords=(930, 28))
    # mouse.right_click(coords=(1000, 120))
    # mouse.double_click(button="left", coords=(170, 45))
    # 鼠标中间键
    # mouse.wheel_click( coords=(170, 45))
    # 按住鼠标
    # mouse.press(button="left",coords=(1425,30))
    #  释放鼠标
    # mouse.release(button="left",coords=(1300,30))
    # 滑动鼠标滚轮,默认往上滚动，wheel_dist  负数则往下滚动
    # mouse.scroll(coords=(1300,200),wheel_dist=-3)
    # 移动鼠标位置
    mouse.move(coords=(100,100))
    # sys.exit()
