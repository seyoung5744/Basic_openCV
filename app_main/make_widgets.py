import tkinter as tk
import cv2
import os

c_serv = None # 서비스 객체 전역 변수
s_serv = None

def btn1_clicked():
    c_serv.preview()


def btn2_clicked(app):
    fname = app.ent.get()
    print(fname)
    c_serv.capture(fname)

def btn3_clicked(app):
    fname = app.ent.get()
    c_serv.write_avi(fname)

def btn4_clicked():
    c_serv.stop()

def btn5_clicked(app):
    fname = app.ent.get()
    c_serv.view_video(fname)

def slide_start():
    s_serv.start()

def slide_stop():
    s_serv.stop()

def make(app, service=None):
    global c_serv, s_serv
    c_serv, s_serv = service[0], service[1]
    print(type(s_serv))
    app.ent = tk.Entry(app.sub_fr, width=60)
    app.btn1 = tk.Button(app.sub_fr, width=10, font=10, text='preview')
    app.btn2 = tk.Button(app.sub_fr, width=10, font=10, text='사진저장')
    app.btn3 = tk.Button(app.sub_fr, width=10, font=10, text='영상촬영')
    app.btn4 = tk.Button(app.sub_fr, width=10, font=10, text='영상촬영종료')
    app.btn5 = tk.Button(app.sub_fr, width=10, font=10, text='동영상보기')
    app.btn6 = tk.Button(app.sub_fr, width=10, font=10, text='사진슬라이드시작')
    app.btn7 = tk.Button(app.sub_fr, width=10, font=10, text='사진슬라이드종료')


    app.ent.grid(row=0, column=0, columnspan=3)
    app.btn1.grid(row=1, column=0)
    app.btn2.grid(row=1, column=1)
    app.btn3.grid(row=2, column=0)
    app.btn4.grid(row=2, column=1)
    app.btn5.grid(row=2, column=2)
    app.btn6.grid(row=3, column=0)
    app.btn7.grid(row=3, column=1)

    app.btn1['command'] = btn1_clicked
    app.btn2['command'] = lambda: btn2_clicked(app)
    app.btn3['command'] = lambda: btn3_clicked(app)
    app.btn4['command'] = btn4_clicked
    app.btn5['command'] = lambda: btn5_clicked(app)
    app.btn6['command'] = slide_start
    app.btn7['command'] = slide_stop
