# %%
from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
from myDef import preprocessing
# %%
image,_=preprocessing(6)
car_no='36서 9478'
df=pd.read_csv('./info.csv',encoding='cp949')
cols=['car_info', 'Patient_Id','Gender','age','exp1', 'exp2', 'exp3']
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
            globals()["label{}".format(i[0])]=Label(master=frame,relief='solid',bd=1,width=15,height=2,text=cols[i[0]],bg='white')
            globals()["label{}".format(i[0])].grid(row=i[0],column=0)
        
        for i in enumerate(df_list):
            globals()["label{}".format(i[0])]=Label(master=frame,relief='ridge',bd=1,width=15,height=2,text=df_list[i[0]],bg='white')
            globals()["label{}".format(i[0])].grid(row=i[0],column=1)

    else:
        label_none=Label(master=window,text='차량 정보 없음')
        label_none.pack(side='top')
        
    window.mainloop()
# %%
open_window()