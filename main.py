from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="grey",fg="black")
        title.pack(side=TOP,fill=X)


        #AllVariables......
        self.Roll_No_var= StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Contact_var = StringVar()
        self.Gender_var = StringVar()
        self.College_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()


        #Manage_Frame.......
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="grey")
        Manage_Frame.place(x=20,y=100,width=450,height=560)

        m_title = Label(Manage_Frame,text="Manage Students",font=("times new roman",30,"bold"),bg="grey")
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame,text="Roll No.",font=("times new roman",20,"bold"),bg="grey")
        lbl_roll.grid(row=1,column=0,padx=20,sticky="w")

        txt_roll = Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", font=("times new roman", 20, "bold"), bg="grey")
        lbl_name.grid(row=2, column=0, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame,textvariable=self.Name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email", font=("times new roman", 20, "bold"), bg="grey")
        lbl_email.grid(row=3, column=0, padx=20, sticky="w")

        txt_email = Entry(Manage_Frame, textvariable=self.Email_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, padx=20, sticky="w")

        lbl_contact = Label(Manage_Frame, text="Contact No.", font=("times new roman", 20, "bold"), bg="grey")
        lbl_contact.grid(row=4, column=0, padx=20, sticky="w")

        txt_contact = Entry(Manage_Frame, textvariable=self.Contact_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=4, column=1, padx=20, sticky="w")

        lbl_clg = Label(Manage_Frame, text="College", font=("times new roman", 20, "bold"), bg="grey")
        lbl_clg.grid(row=5, column=0, padx=20, sticky="w")

        txt_clg = Entry(Manage_Frame, textvariable=self.College_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_clg.grid(row=5, column=1, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender", font=("times new roman", 20, "bold"), bg="grey")
        lbl_gender.grid(row=6, column=0, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("times new roman", 14, "bold"),state="readonly")
        combo_gender["values"]=["Male","Female","Other"]
        combo_gender.grid(row=6, column=1, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address", font=("times new roman", 20, "bold"), bg="grey")
        lbl_address.grid(row=7, column=0, padx=20, sticky="w")

        self.txt_address= Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_address.grid(row=7,column=1,padx=20,sticky="w")


        #ButtonFrame......
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="grey")
        btn_Frame.place(x=15, y=400, width=410)

        Addbtn =  Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=1,padx=10,pady=10)
        Updatebtn = Button(btn_Frame, text="Update", width=10,command=self.update_data).grid(row=0, column=2, padx=10, pady=10)
        Deletebtn = Button(btn_Frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=3, padx=10, pady=10)
        Clearbtn = Button(btn_Frame, text="Clear", width=10,command=self.clear).grid(row=0, column=4, padx=10, pady=10)

        #Detail_Frame......
        Detail_Frame= Frame(self.root,bd=4,relief=RIDGE,bg="grey")
        Detail_Frame.place(x=500,y=100,width=820,height=560)

        lbl_search = Label(Detail_Frame, text="Search By", font=("times new roman", 20, "bold"), bg="grey")
        lbl_search.grid(row=0, column=0, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by,width=10,  font=("times new roman", 14, "bold"), state="readonly")
        combo_search["values"] = ["Roll_no", "Name", "Gender" , "College"]
        combo_search.grid(row=0, column=1, padx=20, sticky="w")

        txt_search = Entry(Detail_Frame,textvariable=self.search_txt, width=20,font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, padx=20, sticky="w")

        Searchbtn = Button(Detail_Frame, text="Search", width=10,pady=5,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        Showallbtn = Button(Detail_Frame, text="Show All", width=10,pady=5,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        #TableFrame....
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="grey")
        Table_Frame.place(x=10, y=70, width=785, height=465)

        scroll_x= Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,columns=("roll","Name","Email","Gender","Contact","College","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("Name", text="Name")
        self.Student_table.heading("Email", text="Email")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("Contact", text="Contact")
        self.Student_table.heading("College", text="College")
        self.Student_table.heading("Address", text="Address")

        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("Name", width=110)
        self.Student_table.column("Email", width=100)
        self.Student_table.column("Gender", width=100)
        self.Student_table.column("Contact", width=100)
        self.Student_table.column("Address", width=150)
        self.Student_table.column("College", width=100)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_students(self):
        if self.Roll_No_var.get()=="" or self.Name_var.get()=="" or self.College_var.get()=="" or self.Gender_var.get()=="" or self.Contact_var.get()=="" or self.Email_var.get()=="" or self.txt_address=="":
            messagebox.showerror("Error","All fields are required!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("Insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                            self.Name_var.get(),
                                                                             self.Email_var.get(),
                                                                             self.Gender_var.get(),
                                                                             self.Contact_var.get(),
                                                                             self.College_var.get(),
                                                                             self.txt_address.get('1.0',END)
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted.")
    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("Select * from students")
        rows= cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.Roll_No_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Contact_var.set("")
        self.College_var.set("")
        self.Gender_var.set("")
        self.txt_address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row = self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Contact_var.set(row[4])
        self.College_var.set(row[5])
        self.Gender_var.set(row[3])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END,row[6])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("Update students set name= %s,email=%s,gender=%s,contact=%s,college=%s,address=%s where roll_no=%s", (
                                                                          self.Name_var.get(),
                                                                          self.Email_var.get(),
                                                                          self.Gender_var.get(),
                                                                          self.Contact_var.get(),
                                                                          self.College_var.get(),
                                                                          self.txt_address.get('1.0', END),
                                                                          self.Roll_No_var.get()
                                                                          ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students where " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
        rows= cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()


root = Tk()
ob = Student(root)
root.mainloop()