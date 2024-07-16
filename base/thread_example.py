import threading
import time


def listen_music(name):
    while True:
        time.sleep(1)
        print(name, "正在播放音乐")


def download_music(name):
    while True:
        time.sleep(2)
        print(name, "正在下载音乐")


if __name__ == '__main__':
    p1 = threading.Thread(target=listen_music, args=("网易云音乐",))
    p2 = threading.Thread(target=download_music, args=("网易云音乐",))
    p1.start()
    p2.start()
