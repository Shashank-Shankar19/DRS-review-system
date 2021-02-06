import cv2
from cv2 import cvtColor, imread
import tkinter
import PIL.Image
import PIL.ImageTk
from functools import partial
import threading
import time
import imutils  # pip install imutils


def playNextFast(speed):
    print(f"You are mad {speed}")


def Exiter():
    pass


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player out ho gaya hai. Use ground se nikal do")


def notOut():
    print("Player not out hai. Bechare ko khelne do")


def ext():
    exit()


SET_WIDTH = 650
SET_HEIGHT = 368

window = tkinter.Tk()
window.title("CoreTouch DRS Review System")
cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()
# Playback buttons

btn = tkinter.Button(window, text="<< reverse play (fast)",
                     width=50, bg="yellow", command=partial(playNextFast, -15))
btn.pack()


btn = tkinter.Button(
    window, text="<< reverse play (slow)", width=50, bg="cyan", command=partial(playNextFast, -25))
btn.pack()

btn = tkinter.Button(window, text=">> forward play (fast)",
                     width=50, bg="orange", command=partial(playNextFast, 15))
btn.pack()

btn = tkinter.Button(
    window, text=">> forward play (slow)", width=50, bg="blue", command=partial(playNextFast, 10))
btn.pack()

btn = tkinter.Button(window, text="! Give Out", width=50,
                     bg="red", command=out)
btn.pack()

btn = tkinter.Button(window, text=":) Give not out", width=50,
                     bg="green", command=notOut)
btn.pack()

btn = tkinter.Button(window, text="Exit", width=50,
                     bg="black", fg='white', command=ext)
btn.pack()


window.mainloop()
