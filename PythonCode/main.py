from AdminPage import *
from SearchBook import *
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from UserPage import *

import pymysql
# Add your own database name and password here to reflect in the code
mypass = "S@nde780yepuri"
mydatabase="libpos"
print('before')
con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
print('after')
cur = con.cursor()

root = Tk()
root.title("Login")
root.geometry("600x480")

def calladmin():
    usern = username_box.get()
    passw = password_box.get()
    if usern == "" or passw == "":
        messagebox.showinfo("Error", "All fields are required")
    else:
        try:
            cur.execute("select * from user2 where user_name=%s and user_password=%s", (usern, passw))
            op = cur.fetchone()
            print(op[1])
            if op == None:
                messagebox.showinfo("Error", "Invalid Username or Password")
            else:
                root.destroy()
                mainmenu()


        except EXCEPTION as es:
            messagebox.showerror("Error"f"Error Due to: {str(es)}")


def callUser():
    usern = username_box.get()
    passw = password_box.get()
    if usern == "" or passw == "":
        messagebox.showinfo("Error", "All fields are required")
    else:
        try:
            cur.execute("select * from user2 where user_name=%s and user_password=%s", (usern, passw))
            op = cur.fetchone()
            # print(op)
            if op == None:
                messagebox.showinfo("Error", "Invalid Username or Password")
            else:
                root.destroy()
                mainmenu1(op[0])


        except EXCEPTION as es:
            messagebox.showerror("Error"f"Error Due to: {str(es)}")


bg = ImageTk.PhotoImage(file="CMS-Home-Image.jpg")
bg_image = Label(root, image=bg).grid()

del_frame = Frame(root, bd=4, relief=RIDGE, bg="#BBD8FF")
del_frame.place(x=100, y=60, width=400, height=180)

# Label for username and password
username = Label(del_frame, text="USERNAME", bg="#BBD8FF", fg="black", font=15)
username.grid(row=12, column=0, sticky=W, padx=10, pady=10)
password = Label(del_frame, text="PASSWORD", bg="#BBD8FF", fg="black", font=15)
password.grid(row=14, column=0, sticky=W, padx=10, pady=10)

# Text boxes for username and password
global username_box
username_box = Entry(del_frame, font=15, bd=5, relief=GROOVE)
username_box.grid(row=12, column=1, pady=10, padx=10, sticky="w")

global password_box
password_box = Entry(del_frame, font=15, bd=5, relief=GROOVE)
password_box.grid(row=14, column=1, pady=10, padx=10, sticky="w")

usern = username_box.get()
passw = password_box.get()

# Login Button for student and admin
adminlogin = Button(del_frame, text="Admin Login", bg="white", fg="black", font=15, command=calladmin)
adminlogin.grid(row=20, column=0, pady=10, padx=10)

studentlogin = Button(del_frame, text="User Login",bg="white", fg="black", font=15, command=callUser)
studentlogin.grid(row=20, column=1, pady=10, padx=10)

root.mainloop()

