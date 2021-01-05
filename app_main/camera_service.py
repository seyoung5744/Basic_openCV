import threading
import cv2

def preview_th(stop, app):
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 400)
    while stop(): # 외부에서 쓰레드 종료.동기화 처리
        # 굳이 함수로 하는 이유는 동기화 문제 때문에.
        # mainloop랑 동시 실행되는 쓰레드이기 때문에 공유자원인 flag값을
        # 직접적으로 사용하기엔 위험이 따름
        # 임계 영역.
        ret, frame = cam.read()
        if ret:
            app.change_img(frame)
        cv2.waitKey(100) # 0.1 s
    cam.release()

def video_write_th(stop, app, fname):
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    codec = cv2.VideoWriter_fourcc(*'DIVX')
    # 동영상 작성자 객체 생성
    path = './video/'+fname + '.avi'
    out = cv2.VideoWriter(path, codec, 25.0, (640,480)) # 초당 프레임 수 25.0
    while stop():
        ret, frame = cam.read()
        if ret:
            frame = cv2.resize(frame, (640, 400))
            out.write(frame)
            app.change_img(frame)
        else:
            break
        cv2.waitKey(100) # 0.1 s
    cam.release()

def video_read_th(stop, app, fname):
    path = './video/' + fname + '.avi'
    cap = cv2.VideoCapture(path)
    while cap.isOpened() and stop(): # 동영상 파일이 정상 오픈이면
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (640, 400))
            app.change_img(frame)
        else:
            break
        cv2.waitKey(100)
    cap.release()

class CameraService:
    def __init__(self, app):
        self.cam = None
        self.app = app # main_ui 에서 만든 ui 창. AppWindow 객체
        self.flag = True # 쓰레드 종료 flag

    def stop(self):
        self.flag = False

    def preview(self):
        self.flag = True
        cam_th = threading.Thread(target=preview_th, args=(lambda:self.flag, self.app))
        cam_th.start()

    def capture(self, fname):
        print(fname,"gg")
        self.stop() # preview_th 먼저 종료
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 640)
        self.cam.set(4, 400)
        ret, frame = self.cam.read()
        self.app.change_img(frame) # 레이블을 현재 영상으로 바꾸고
        cv2.imwrite('img/'+fname, frame) # 마지막 이미지를 저장.
        self.cam.release()

    def write_avi(self, fname):
        self.flag = True
        cam_th = threading.Thread(target=video_write_th,
                                  args=(lambda: self.flag, self.app, fname))
        cam_th.start()

    def view_img(self, fname):
       pass


    def view_video(self, fname):
        self.flag = True
        cam_th = threading.Thread(target=video_read_th,
                                  args=(lambda: self.flag, self.app, fname))
        cam_th.start()