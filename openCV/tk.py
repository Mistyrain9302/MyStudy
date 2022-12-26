# %%
from tkinter import *
from tkinter import ttk
from tksheet import Sheet
import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
import cv2
import numpy as np
from myDef import preprocessing, find_candidates,color_candidate_img,rotate_plate
# %%
root = tk.Tk()

# Load the JPG file
img_house = Image.open(r"sample.png")

# Convert the JPG image to a PhotoImage instance that tkinter can use.
image_tk = ImageTk.PhotoImage(img_house)

# Define columns
column_names = ("dwelling_type_column", "location_column")

# Pass the column names when we make the treeview.
treeview_places = ttk.Treeview(columns=column_names)

# Create the column texts that the user will see.
treeview_places.heading("dwelling_type_column", text="차량 번호")
treeview_places.heading("location_column", text="Location")


treeview_places.insert(parent="",
                     index="end",
                     image=image_tk,
                     values=("12바1234", "Fantasy Land"))


treeview_places.pack(expand=True, fill=tk.BOTH)

root.mainloop()
# %%
window=Tk()
image_car=Image.open(r'sample.png')
image_tk = ImageTk.PhotoImage(image_car)
# %%
def checkImg(car_no):    
    image,morph = preprocessing(car_no)
    candidates=find_candidates(morph)

    fills = [color_candidate_img(image,size) for size,_,_ in candidates]
    new_candis = [find_candidates(fill) for fill in fills]
    new_candis = [cand[0] for cand in new_candis if cand]
    candidate_imgs = [rotate_plate(image,cand) for cand  in new_candis]

    for i,img in enumerate(candidate_imgs):
        cv2.polylines(image,[np.int32(cv2.boxPoints(new_candis[i]))],True,(0,225,255),2)
        cv2.imshow('candidate_img'+str(i),img)

    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# %%
image,morph = preprocessing(7)
# %%
window=Tk()

window.title("차량 정보")
window.geometry("640x640")
window.resizable(1,1)

backFrame = tk.Frame(master=window,
                    width=640,
                    height=640,
                    bg='white')
#backFrame.pack()
backFrame.propagate(0)

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
