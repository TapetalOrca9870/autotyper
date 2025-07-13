from tkinter import *
from tkinter import ttk
import pyautogui
import  time

def write(write_time, x, y, language, text, auto_enter):
    time.sleep(2)
    pyautogui.FAILSAFE = False
    pyautogui.click(int(x), int(y))
    if language == 'ru':   
        pyautogui.hotkey("shift", "alt")
        pyautogui.write(text, interval=write_time)
        pyautogui.hotkey("shift", "alt")
        if auto_enter:
            pyautogui.press('enter')
    elif language == 'en':
        pyautogui.write(text, interval=write_time)
        if auto_enter:
            pyautogui.press('enter')

tk = Tk()
tk.title('autotyper')
tk.geometry('550x250')
label = Label(tk, text='write interval (s):', font=("Arial", 24))
label.place(x = 1, y = 1)
entry = Entry(tk)
entry.place(x=240, y=15)

label2 = Label(tk, text='x, y:', font=("Arial", 24))
label2.place(x = 1, y = 35)
entry2 = Entry(tk, width=5)
entry2.place(x=75, y=50)
entry2_1 = Entry(tk, width=5)
entry2_1.place(x=120, y=50)

label4 = Label(tk, text='language:', font=("Arial", 24))
label4.place(x = 1, y = 70)
entry4 = Entry(tk)
entry4.place(x=145, y=85)

label5 = Label(tk, text='text:', font=("Arial", 24))
label5.place(x = 1, y = 110)
entry5 = Entry(tk)
entry5.place(x=80, y=125)

label6 = Label(tk, text='auto send:', font=("Arial", 24))
label6.place(x = 1, y = 150)
entry6 = Entry(tk)
entry6.place(x=155, y=164)

write_time = entry.get()   # time to type
x = entry2.get()           # coordinates by x gride
y = entry2_1.get()         # coordinates by y gride
language = entry4.get()    # en or ru
text = entry5.get()        # a some text
auto_enter = entry6.get()  # True or Enter

button = Button(tk, text='start', command=lambda: write(entry.get(), entry2.get(), entry2_1.get(), entry4.get(), entry5.get(), entry6.get()),  width=50, height=2)
button.place(x = 30, y = 200)


tk.mainloop()