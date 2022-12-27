# %%
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import numpy as np
from myDef import preprocessing
# %%
image,_=preprocessing(6)
# %%
window=Tk()

window.title("차량 정보")
window.resizable(1,1)

img2=Image.fromarray(image)
image_tk = ImageTk.PhotoImage(img2,master=window)

label1= Label(window,image=image_tk)
label1.configure(image=image_tk)

label1.grid(row=0,column=0)

treeview=ttk.Treeview(columns=["name", "age", "grade"],
                      displaycolumns=["name", "age", "grade"],
                      master=window)
treeview.configure()

treeview.grid(row=0,column=1)


treeview.column("name", width=100, anchor="center")
treeview.heading("name", text="이름", anchor="center")

treeview.column("age", width=50, anchor="center")
treeview.heading("age", text="나이", anchor="center")

treeview.column("grade", width=50, anchor="center")
treeview.heading("grade", text="등급", anchor="center")

# 컬럼제목만 보이게함
treeview["show"] = "headings"

treeValueList = [("Aiden", 20, "A"),
                 ("Matthew", 19, "B"),
                 ("John", 21, "C")]

for i in range(len(treeValueList)):
    treeview.insert("", "end", text="", values=treeValueList[i], iid=i)

window.mainloop()
# %%
