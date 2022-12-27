# %%
from tkinter import *
import pandas as pd
from PIL import ImageTk,Image

# %%
window=Tk()

window.title("기메의 생각")
window.resizable(1,1)
window.geometry("960x480")
img=Image.open('brain3.png')
image=ImageTk.PhotoImage(img,master=window)
img_label=Label(window,image=image)
img_label.pack(side='top')
label1=Label(master=window, text="계산 결과: 고기 빌런입니다.")
label1.pack(side='top')

    
window.mainloop()
# %%
