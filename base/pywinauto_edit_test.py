import sys

import psutil
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
    # Timings.defaults()  # 默认等待时间
    # Timings.slow()  # 等待时间加倍
    # Timings.fast()  # 等待时间减半
    startPath = r"C:\Windows\System32\notepad.exe"
    processName = "notepad.exe"
    app = getApp(startPath=startPath, processName=processName)
    dlg = app["无标题 - 记事本"]
    # dlg.print_control_identifiers()
    dlg["Edit"].type_keys("python来了")
    dlg.menu_select("编辑->替换(R)")
    dlg_r=dlg.child_window(title="替换", control_type="Window")
    dlg_r.print_control_identifiers()
    dlg_r.child_window(title="查找内容(N):", auto_id="1152", control_type="Edit").type_keys("python")
    dlg_r.child_window(title="替换为(P):", auto_id="1153", control_type="Edit").type_keys("python-java")
    dlg_r.child_window(title="全部替换(A)", auto_id="1025", control_type="Button").click()
    # dlg_r["Button3"].click()
    sys.exit()
