import os
import cv2
import threading

def preview_th(stop, app):
    flist = os.listdir('./img')
    i = 0
    while stop(): # 외부에서 쓰레드 종료.동기화 처리
        print(flist[i%len(flist)])
        img = cv2.imread('./img/' + flist[i%len(flist)])
        app.change_img(img)
        cv2.waitKey(1000)
        i += 1

class SlideService:
    def __init__(self, app):
        self.app = app # main_ui 에서 만든 ui 창. AppWindow 객체
        self.flag = True # 쓰레드 종료 flag

    def stop(self):
        self.flag = False

    def start(self):
        self.flag = True
        cam_th = threading.Thread(target=preview_th, args=(lambda: self.flag, self.app))
        cam_th.start()


