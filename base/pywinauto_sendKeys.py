import sys
import time

import psutil
from pywinauto.application import Application
from pywinauto.keyboard import send_keys


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

    # send_keys("{LWIN}")
    # send_keys("cmd")
    # time.sleep(1)
    # send_keys("{ENTER}")
    # time.sleep(1)
    # send_keys("python")
    # time.sleep(1)
    #
    # send_keys("{ENTER}")
    # send_keys("^f")
    # 简写和修饰符：ctrl-> ^，shift->+，alt->%,举例："^s"代表 ctlr+s 保存快捷键
    # 查询：ctrl+f
    # send_keys("^f")
    # send_keys("%+{VK_F9}")

    # 全选
    send_keys("^a")
    # 复制
    send_keys("^c")
    # 粘贴
    send_keys("^v")
    # sys.exit()
