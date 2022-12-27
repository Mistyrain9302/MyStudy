# %%
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import pandas as pd
from opencv import img_ori,plate_chars
# %%
image=np.array(img_ori)
car_no=plate_chars[0]
df=pd.read_csv('./info.csv',encoding='cp949')
cols=['차량 정보', '환자 ID','성별','나이','진료과1', '진료과2', '진료과3']
# %%
def df_finder(car_no,df):
    if sum(df['car_info']==car_no) >=1:
        idx=df[df['car_info']==car_no].index.tolist()[0]
        car=df.loc[idx,'car_info']
        P_id = df.loc[idx,'Patient_Id']
        gender = df.loc[idx,'Gender']
        age = df.loc[idx,'Age']
        exp1 = df.loc[idx,'exp1']
        exp2 = df.loc[idx,'exp2']
        exp3 = df.loc[idx,'exp3']
        data_list=[car,P_id,gender,age,exp1,exp2,exp3]

        return data_list
    else:
        print('일치하는 차량 번호 없음')
        return None
# %%
def open_window():
    window=Tk()

    window.title("차량 정보")
    window.resizable(1,1)
    df_list=df_finder(car_no,df)
    if df_list is not None:    
        img2=Image.fromarray(image)
        image_tk = ImageTk.PhotoImage(img2,master=window)

        img_label= Label(window,image=image_tk)
        img_label.configure(image=image_tk)
        img_label.grid(row=0,column=0)

        frame=Frame(window,relief='raised',bd=2,background='white',padx=2,pady=2)
        frame.grid(row=0,column=1)
        
        for i in enumerate(cols):
            globals()["label{}".format(i[0])]=Label(master=frame,relief='solid',
                                                    bd=1,width=15,height=2,
                                                    text=cols[i[0]],bg='white')
            globals()["label{}".format(i[0])].grid(row=i[0],column=0)
        
        for i in enumerate(df_list):
            globals()["label{}".format(i[0])]=Label(master=frame,relief='ridge',
                                                    bd=1,width=15,height=2,
                                                    text=df_list[i[0]],bg='white')
            globals()["label{}".format(i[0])].grid(row=i[0],column=1)

    else:
        window.geometry('640x640')
        label_none=Label(master=window,text='일치하는 차량 정보 없음',
                         font=("궁서체",40),fg='red')
        label_none.pack(side='top')
        
    window.mainloop()
# %%
open_window()
# %%
