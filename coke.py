import os
import platform
import tkinter
from tkinter import messagebox
import ctypes


def get_drink():
    if platform.system() == 'Windows':
        print('Windows detected')

        ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)

    else:
        print('Thank god it\'s not windows')

        os.system('eject')


    messagebox.showinfo("coke.exe", "Here is your cup holder!")


root = tkinter.Tk()
root.withdraw()

result = messagebox.askquestion("coke.exe", "Do you want a drink?", icon='question')
if result == 'yes':
    print("You have a drink now")

    get_drink()
else:
    print("I guess you don't want one")
