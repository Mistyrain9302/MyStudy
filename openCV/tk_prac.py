# %%
from tkinter import *
from tksheet import Sheet
import pandas as pd
from PIL import ImageTk,Image

# %%
class demo(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title('THIS IS WINDOWS')
        self.geometry("1560x600+100+100")
        image=ImageTk.PhotoImage(Image.open('./sample.png'))
        label= Label(self,image=image)
        label.pack()        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frame = Frame(self)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.sheet = Sheet(
            self.frame,
            data=pd.read_csv('./train.csv').values.tolist(),
        )
        self.sheet.enable_bindings()
        self.frame.grid(row=0, column=0, sticky="nswe")
        self.sheet.grid(row=0, column=0, sticky="nswe")
# %%
app = demo()
app.mainloop()
# %%
window=Tk()
# %%
root = Tk()
root.title('사진불러오기')
root.geometry('800x600')
 
img = ImageTk.PhotoImage(Image.open('./sample.png'))
label = Label(image=img)
label.pack()
 
quit = Button(root, text='종료하기', command=root.quit)
quit.pack()
 
root.mainloop()

# %%
window=Tk()
window.title("사진보여주기")
window.geometry("800x600")

img = ImageTk.PhotoImage(Image.open('./sample.png'))
label = Label(image=img)
label.pack()

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)
window.frame = Frame(window)
window.frame.grid_columnconfigure(0, weight=1)
window.frame.grid_rowconfigure(0, weight=1)
window.sheet = Sheet(
    window.frame,
    data=pd.read_csv('./train.csv').values.tolist(),
)
window.sheet.enable_bindings()
window.frame.grid(row=0, column=0, sticky="nswe")
window.sheet.grid(row=0, column=0, sticky="nswe")

window.mainloop()
# %%
import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
root.geometry('500x500')
tree = ttk.Treeview(root, column=('A','B'), selectmode='browse', height=10)
tree.grid(row=0, column=0, sticky='nsew')
tree.heading('#0', text='Pic directory', anchor='center')
tree.heading('#1', text='A', anchor='center')
tree.heading('#2', text='B', anchor='center')
tree.column('A', anchor='center', width=100)
tree.column('B', anchor='center', width=100)
img = ImageTk.PhotoImage(Image.open('./sample.png'))
tree.insert('', 'end', text="#0's text", image=img,value=("Something", "Another Thing"))
root.mainloop()
# %%
import tkinter as tk
from tkinter import ttk, PhotoImage


root = tk.Tk()

# PNG image path
img_canada_flag = ImageTk.PhotoImage(Image.open('./sample.png'))

# Define columns
column_names = ("country_column", "capital_city_column")

# Pass the column names when we make the treeview.
treeview_country = ttk.Treeview(columns=column_names)

# Create the column texts that the user will see.
treeview_country.heading("country_column", text="Country")
treeview_country.heading("capital_city_column", text="Capital")

treeview_country.insert(parent="",
                     index="end",
                     image=img_canada_flag,
                     values=("Canada", "Ottawa"))

treeview_country.pack(expand=True, fill=tk.BOTH)

root.mainloop()