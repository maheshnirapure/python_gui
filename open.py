import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('Software')

name_label=ttk.Label(win,text='enter you name:')
name_label.grid(row=0,column=0,sticky=tk.W)

age_label=ttk.Label(win,text='enter you age:')
age_label.grid(row=1,column=0,sticky=tk.W)

email_label=ttk.Label(win,text='enter you email:')
email_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text='select your gender:')
gender_label.grid(row=3,column=0,sticky=tk.W)



#CREATE ENTRY BOX
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=1,column=1)

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=16,textvariable=email_var)
email_entrybox.grid(row=2,column=1)

#creat combobox

gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=14,textvariable=gender_var,state='readonly')
gender_combobox['value']=('male','female','other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

#radio button add there
usertype=tk.StringVar()
radiobtn1=ttk.Radiobutton(win,text='student',value='Student',variable=usertype)
radiobtn1.grid(row=4,column=0)

radiobtn2=ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=usertype)
radiobtn2.grid(row=4,column=1)

#chek button
chekbtn_var=tk.IntVar()
chekbtn=ttk.Checkbutton(win,text='chek if you want to subcribe this buttin',variable=chekbtn_var)

chekbtn.grid(row=5,columnspan=3)

def action():
    user_name=name_var.get()
    user_age=age_var.get()
    user_email=email_var.get()
    print(f'{user_name}is {user_age} year old,{user_email}')
    user_type=usertype.get()
    user_gender=gender_var.get()

    if chekbtn_var.get()==0:
        subcribed='No'
    else:
        subcribed='yes'
    print(user_gender,user_type,subcribed)
    with open('file.txt','a')as f:
        f.write(f'{user_name},{user_age},{user_email},{user_gender},{user_type},{subcribed}\n')
submit_button =ttk.Button(win,text='Submit',command=action())
submit_button.grid(row=6,column=0)

win.mainloop()