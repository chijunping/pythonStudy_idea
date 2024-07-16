from pywinauto.application import Application
app = Application(backend="uia").start('notepad.exe')
# 查到这个记事本的控件树
dlg_spec = app['无标题 - 记事本']
dlg_spec.print_control_identifiers()