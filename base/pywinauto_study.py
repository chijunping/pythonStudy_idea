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
    from pywinauto.timings import Timings

    # Timings.defaults()  # 默认等待时间
    # Timings.slow()  # 等待时间加倍
    # Timings.fast()  # 等待时间减半
    startPath = r"C:\Program Files (x86)\PremiumSoft\Navicat Premium\navicat.exe"
    processName = "navicat.exe"
    app = getApp(startPath=startPath, processName=processName)
    # ========== 连接已经打开的软件
    # print(app)

    # 通过窗口句柄连接已经打开的软件
    # app = Application(backend='uia').connect(handle=395542)
    # print(app)

    # ======= 获取窗口窗口
    # 方式一：app["类名或标题"]；方式二：app.窗口类名或标题
    # 使用类名来选择窗口
    dlg = app["Navicat Premium"]
    # 使用标题来选择窗口
    # 打印窗口中所有的控件
    # dlg.print_control_identifiers()
    # 窗口最大化，最小化
    # dlg.maximize()
    # dlg.restore()
    # dlg.minimize()
    # status = dlg.get_show_state()
    # print(status)
    # sleep(1)
    # dlg.close()
    # 获取当前窗口显示的坐标
    # rect = dlg.rectangle()
    # print(rect)
    # menu = dlg.Menu
    menu = dlg["Menu"]
    # 不对的获取方式，会报异常
    # file = dlg["Menu"]["文件"]
    # file = menu.child_window(title="文件", control_type="MenuItem")
    file = menu.child_window(title="文件")
    # dlg.print_control_identifiers()

    # 查看对象所属的类型
    # print(dlg.wrapper_object())
    # print(menu.wrapper_object())
    # print(file.wrapper_object())
    # 查案对象所支持的方法
    # print(dir(dlg.wrapper_object()))
    # print(dir(menu.wrapper_object()))
    # print(dir(file.wrapper_object()))
    # 控件文本内容的获取
    # print(file.texts())
    # 获取窗口的子元素
    # print(dlg.children())
    # # 获取菜单的子元素
    # print(menu.children())
    # # 获取文件的子元素
    # print(file.children())
    # 获取控件类名
    # print(dlg.class_name())
    # 获取控件的属性
    # print(dlg.get_properties())
    # 截图
    # pic=menu.capture_as_image()
    # pic.save("03.png")
    # print(pic)
    # 获取子菜单
    # print(menu.items())
    # print(menu.item_by_index(0))
    # print(menu.item_by_path("文件"))
    # print(menu.item_by_path("文件->新建连接"))
    # 菜单项的操作方法
    # 获取子菜单项
    # print(file.items())
    # 点击菜单:需要逐层菜单点击
    # file.click_input()
    menu.item_by_path("文件").click_input()
    menu.item_by_path("文件->新建连接").click_input()
    menu.item_by_path("文件->新建连接->MySQL...").click_input()
    # 选择新建连接的窗口
    new_dlg = app["MySQL - 新建连接"]
    # 等待“新建连接”窗口处于打开/可见状态
    # print(new_dlg)
    new_dlg.wait(wait_for="ready", timeout=10, retry_interval=1)
    print("新建窗口已处于可见状态！")
    new_dlg.wait_not(wait_for_not="ready", timeout=10, retry_interval=1)
    print("新建窗口已处于不可见状态！")

    sys.exit()
