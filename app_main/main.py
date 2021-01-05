import tkinter as tk
import app_main.main_ui as win
import app_main.make_widgets as mkw
import app_main.service as s
import app_main.camera_service as cs
import app_main.slide_service as ss

def main():
    img_path = 'img/a.jpg'
    root = tk.Tk()
    app = win.AppWindow(root, '650x700+100+100', img_path)
    service = [cs.CameraService(app), ss.SlideService(app)]
    mkw.make(app,service)
    # s.service() #ui 이벤트와 상관없이 수행해야하는 기능
    app.mainloop()

main()
