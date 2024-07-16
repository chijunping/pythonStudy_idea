from time import sleep

import psutil
from pywinauto.application import Application
import io
import sys
from pywinauto import mouse
from pywinauto.keyboard import send_keys
from pywinauto.win32functions import SetFocus
from pywinauto import mouse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


# 获取进程id
def get_pid(processName):
    for proc in psutil.process_iter():
        try:
            if (proc.name() == processName):
                print(proc.name())
                print(str(proc.pid))
                return proc.pid
        except psutil.NoSuchProcess:
            pass
    return -1


def __get_element_postion(self, element):
    """获取元素的中心点位置"""
    # 元素坐标
    element_position = element.rectangle()
    # 算出中心点位置
    center_position = (int((element_position.left + element_position.right) / 2),
                       int((element_position.top + element_position.bottom) / 2))
    return center_position


def start(self):
    # 1、获取左侧【聊天】切换元素
    chat_list_element = self.weixin_pc_window.child_window(title="聊天", control_type="Button")
    # 2、点击进入到聊天列表
    mouse.click(button='left',
                coords=self.__get_element_postion(chat_list_element))


def teardown(self):
    """释放资源"""
    # 结束进程，释放资源
    self.app.kill()


if __name__ == '__main__':
    procId = get_pid("WeChat.exe")

    if (procId == -1):
        print("WeChat.exe  is not running")

    app = Application(backend='uia').connect(process=procId).start('C:\Program Files (x86)\Tencent\WeChat\WeChat.exe')
    # 获取窗口对象
    # 通过title及ClassName获取窗体对象
    weixin_pc_window = app.window(title="微信", class_name="WeChatMainWndForPC")

    weixin_pc_window.set_focus()

    # 3、点击【文件传输助手】进入到聊天页面
    file_helper_element = weixin_pc_window.child_window(title="文件传输助手", control_type="ListItem")

    mouse.click(button='left',
                coords=__get_element_postion(file_helper_element))
    # 4、获取输入框元素，模拟输入
    edit_element = weixin_pc_window.child_window(title=r"输入", control_type="Edit")

    sleep(2)
    # 输入内容
    edit_element.type_keys("星安果")
    # 使用键盘模拟回车，即：发送
    send_keys('{ENTER}')
