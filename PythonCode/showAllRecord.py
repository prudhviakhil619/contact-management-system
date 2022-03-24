from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.ttk import Treeview
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "S@nde780yepuri"
mydatabase = "CMS_db"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()


def showAll(userId):
    class A(Frame):
        def __init__(self, parent):
            Frame.__init__(self, parent)
            self.CreateUI()
            self.LoadTable()
            self.grid(sticky=(N, S, W, E))
            parent.grid_rowconfigure(0, weight=1)
            parent.grid_columnconfigure(0, weight=1)

        def CreateUI(self):
            tv = Treeview(self)
            tv['columns'] = ('user_id', 'user_name', 'user_mobile', 'user_email', 'user_address', 'role_id')
            tv.heading('#0', text='user_id', anchor='center')
            tv.column('#0', anchor='center')
            tv.heading('#1', text='user_name', anchor='center')
            tv.column('#1', anchor='center')
            tv.heading('#2', text='user_mobile', anchor='center')
            tv.column('#2', anchor='center')
            tv.heading('#3', text='user_email', anchor='center')
            tv.column('#3', anchor='center')
            tv.heading('#4', text='user_address', anchor='center')
            tv.column('#4', anchor='center')
            tv.heading('#5', text='role_id', anchor='center')
            tv.column('#5', anchor='center')
            tv.grid(sticky=(N, S, W, E))
            self.treeview = tv
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)

        def LoadTable(self):
            Select = "select u.user_id, u.user_name, u.user_mobile, u.user_email, u.user_address, u.role_id from user u inner join userContacts uc1 on uc1.contact_user_id = u.user_id  where uc1.parent_user_id  = %s"
            cur.execute(Select, userId)
            result = cur.fetchall()
            user_id = ""
            user_name = ""
            user_mobile = ""
            user_email = ""
            user_address = ""
            role_id = ""
            for i in result:
                user_id = i[0]
                user_name = i[1]
                user_mobile = i[2]
                user_email = i[3]
                user_address = i[4]
                role_id = i[5]
                self.treeview.insert("", 'end', text=user_id,
                                     values=(user_name, user_mobile, user_email, user_address, role_id))

    root = Tk()
    root.title("Your contacts")
    A(root)
