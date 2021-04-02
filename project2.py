from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from cx_Oracle import *
import socket
import bs4
import requests
import matplotlib.pyplot as plt
import numpy as np

def f1():
	root.withdraw()
	adst.deiconify()

def f2():
	adst.withdraw()
	root.deiconify()

def f3():
	#stViewData.delete(1.0,END)
	root.withdraw()
	vist.deiconify()
	con=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="select *from studc_20"
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=""
		for d in data:
			msg=msg+" Roll no = "+str(d[0])+" Name = "+str(d[1])+" Marks = "+str(d[2])+ "\n"
		stViewData.config(state=NORMAL)
		stViewData.delete(1.0,END)
		stViewData.insert(INSERT,msg)
		stViewData.config(state=DISABLED)

	except DatabaseError as e:
		messagebox.showerror("Galat kiya ",e)

	finally:
		if con is not None:
			con.close()
def f4():
	vist.withdraw()
	root.deiconify()

def f5():
	rno= entAddRno.get()
	if not rno.isdigit() or rno==" " or int(rno)<1:
		messagebox.showerror("Wrong","Invalid Rno")
		entAddRno.delete(0,END)
		entAddRno.focus()
		return
	name=entAddName.get()
	if not name.isalpha() or len(name)<2 or name==" ":
		messagebox.showerror("Wrong","Invalid Name")
		entAddName.delete(0,END)
		entAddName.focus()
		return
	marks=entAddMarks.get()
	if not marks.isdigit() or marks==" " or int(marks)>100:
		messagebox.showerror("Wrong","Invalid Marks")
		entAddMarks.delete(0,END)
		entAddMarks.focus()
		return
		
	con =None	
	try:
		con=connect("system/abc123")
		#rno=int(entAddRno.get())
		#name=entAddName.get()
		#marks=int(entAddMarks.get())
		args=(int(rno),name,int(marks))
		cursor=con.cursor()
		sql="insert into studc_20 values('%d','%s','%d')"
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("Sahi kiya ",str(cursor.rowcount)+" rows inserted ")
	except DatabaseError as e:
		messagebox.showerror("Galat Kiya ",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		entAddRno.delete(0,END)
		entAddName.delete(0,END)
		entAddMarks.delete(0,END)
		entAddRno.focus()
def f6():
	root.withdraw()
	upst.deiconify()

def f7():
	upst.withdraw()
	root.deiconify()


def f8():
	rno=entUpRno.get()
	if not rno.isdigit() or rno == " " or int(rno) < 1:
		messagebox.showerror("Wrong ","Invalid Roll no")
		entUpRno.delete(0,END)
		entUpRno.focus()
		return
	
	name=entUpName.get()
	if len(name)<2 or not name.isalpha() or name == " ":
		messagebox.showerror("Wrong ","Invalid Name")
		entUpName.delete(0,END)
		entUpName.focus()
		return

	marks=entUpMarks.get()
	if not marks.isdigit() or marks == " " or int(marks) >100 or int(marks) <0 :
		messagebox.showerror("Wrong ","Invalid Marks")
		entUpMarks.delete(0,END)
		entUpMarks.focus()
		return
		
	con=None
	try:
		con=connect("system/abc123")
		rno=int(entUpRno.get())
		name=entUpName.get()
		marks=int(entUpMarks.get())
		cursor=con.cursor()
		args = (name,marks,rno)
		sql="update studc_20 set name = '%s',marks = '%d' where rno = '%d' "
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("Updated Successfully", str(cursor.rowcount) + " rows updated")
	except DatabaseError as e:
		messagebox.showerror("Error During Updation ",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		entUpRno.delete(0,END)
		entUpName.delete(0,END)
		entUpMarks.delete(0,END)
		entUpRno.focus()
		
def f9():
	root.withdraw()
	dst.deiconify()
	
def f10():
	dst.withdraw()
	root.deiconify()
	
	
def f11():
	rn=entDtRno.get()
	if not rn.isdigit() or rn == " " or int(rn) < 1:
		messagebox.showerror("Wrong ","Invalid Roll no")
		entDtRno.delete(0,END)
		entDtRno.focus()
		return
	con=None
	try:
		con=connect("system/abc123")
		rn=int(entDtRno.get())
		args=(rn)
		cursor=con.cursor()
		cursor.execute("Delete from studc_20 where rno=:rn",{'rn':(rn)})
		if cursor.rowcount>0:
			messagebox.showinfo("sahii kiya",str(cursor.rowcount)+" Record Deleted  ")
			print(cursor.rowcount,"Records deleted  ")
		else:
			messagebox.showinfo("Galat kiya",str(cursor.rowcount)+" Delete Operation Failed ")
			print("delete op failed ")
		con.commit()
		#print(cursor.rowcount,"Records deleted  ")
	except DatabaseError as e:
		print("issue",e)
		con.rollback()
	finally:
		if con is not None :
			con.close()
		entDtRno.delete(0,END)
		entDtRno.focus()
		
		print("Disconnected" )
		
"""web scrapping to obtain quotes from website brainyquote.com"""

res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")	
soup = bs4.BeautifulSoup(res.text,'lxml')	
quote = soup.find('img',{"class":"p-qotd"})
text = quote['alt']
mssg="Quote:-\t"+text
print(text)
	
	#entQuote.delete(0,END)
	#entQuote.insert(0,text)


""" fetching city name and using city name fetching temperature of that city using api from website openweathermap.com"""
try:
	#city="mumbai"
	socket.create_connection(("www.google.com", 80))
	res=requests.get("https://ipinfo.io")
	data=res.json()
	city=data['city']
	city1=city
	a1 = "https://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" +city1
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	api_address = a1 + a2 + a3
	res1 = requests.get(api_address)
	data = res1.json()
	main = data['main']
	temp = main['temp']
	print(temp)
	info=city+"\t"+str(temp)+"\u2103"
	
		#entTemp.insert(0, temp)

except OSError:
	print("Check network")

""" obtain graph of top 3 students scoring in marks """

def graph():
	name = []
	marks = []
	con = None 
	try :
		con = connect("system/abc123")
		cursor = con.cursor()
		sql = "select * from studc_20 order by marks desc"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data :
			marks.append(d[2])
			name.append(d[1])
		
		gmarks = [marks[0],marks[1],marks[2]]
		gname = [name[0],name[1],name[2]]
		x=np.arange(len(gname))
		plt.bar(x,gmarks,label="Marks out of 100")
		plt.xticks(x,gname)
		plt.xlabel('Names')
		plt.ylabel('Marks')
		plt.title("Marks of Top 3 Students")
		plt.legend()
		plt.show()
	except DatabaseError as e:
		messagebox.showerror("Error",e)
		con.rollback()
	except Exception as f:
		messagebox.showerror("Something is Wrong",f)
		con.rollback()
	finally :
		if con is not None :
			con.close()
				
		
	
		
#main


root=Tk()
root.title("Student Management System")
root.geometry("550x600+500+100")
root.configure(background='light green')


btnAdd=Button(root,text="Add",font=("Times New Roman",18,'bold italic'),width=10,command=f1)
btnView=Button(root,text="View",font=("Times New Roman",18,'bold italic'),width=10,command=f3)
btnUpdate=Button(root,text="Update",font=("Times New Roman",18,'bold italic'),width=10,command=f6)
btnDelete=Button(root,text="Delete",font=("TImes New Roman",18,'bold italic'),width=10,command=f9)
lblTemp=Label(root,text=info,font=("TImes New Roman",18,'bold italic'))
#entTemp=Entry(root,bd=2,width=3,font=("bracket serif",15,'italic'))
lblQuote=Label(root,text=mssg,font=("copperplate gothic light",18,' bold'),wraplength=500)
#entQuote=Entry(root,bd=7,width=70,font=("arial",10,'italic'))
#btnGetData=Button(root,text="Get Data",font=("arial",9,'bold'),width=7,command=f12)
btnGraph=Button(root,text="Graph",font=("Times New Roman",18,'bold italic'),width=10,command=graph)


btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)
lblTemp.pack(pady=20)
#entTemp.pack(pady=10)
lblQuote.pack(pady=20)
#entQuote.pack(pady=10)
#btnGetData.pack(pady=10)


#add student

adst=Toplevel(root)
adst.title("Add Student.")
adst.geometry("600x600+500+100")
adst.withdraw()

lblAddRno=Label(adst,text="Enter Roll No",font=("times",18,'bold'))
entAddRno=Entry(adst,bd=10,font=("arial",18,'bold'))
lblAddName=Label(adst,text="Enter Name",font=("times",18,'bold'))
entAddName=Entry(adst,bd=10,font=("arial",18,'bold'))
lblAddMarks=Label(adst,text="Enter Marks ",font=("times",18,'bold'))
entAddMarks=Entry(adst,bd=10,font=("arial",18,'bold'))
#lblAddBranch=Label(adst,text="Enter Branch ",font=("times",18,'bold'))
#entAddBranch=Entry(adst,bd=10,font=("arial",18,'bold'))
#lblAdd=Label(adst,text="Enter Address ",font=("times",18,'bold'))
#entAdd=Entry(adst,bd=10,font=("arial",18,'bold'))
#lblAddPhno=Label(adst,text="Enter Phone No ",font=("times",18,'bold'))
#entAddPhno=Entry(adst,bd=10,font=("arial",18,'bold'))
btnAddSave=Button(adst,text="Save",font=("Times New Roman",18,'bold italic'),width=5,background='cyan',command=f5)
btnAddBack=Button(adst,text="Back",font=("Times New Roman",18,'bold italic'),width=5,background='cyan',command=f2)



lblAddRno.pack(pady=6)
entAddRno.pack(pady=6)
lblAddName.pack(pady=6)
entAddName.pack(pady=6)
lblAddMarks.pack(pady=6)
entAddMarks.pack(pady=6)
#lblAddBranch.pack(pady=6)
#entAddBranch.pack(pady=6)
#lblAdd.pack(pady=6)
#entAdd.pack(pady=6)
#lblAddPhno.pack(pady=6)
#entAddPhno.pack(pady=6)
btnAddSave.pack(pady=6)
btnAddBack.pack(pady=6)

#view student 

vist=Toplevel(root)
vist.title("View Students Details")
vist.geometry("450x500+500+100")
vist.withdraw()
stViewData=scrolledtext.ScrolledText(vist,width=95,height=15)
btnViewBack=Button(vist,text="Back",font=("Times New Roman",18,'bold italic'),background='cyan',command=f4)
stViewData.pack(pady=10)
btnViewBack.pack(pady=10)


#Updatestudents

upst=Toplevel(root)
upst.title("Update Students Details")
upst.geometry("500x600+500+100")
upst.withdraw()

lblUpRno=Label(upst,text="Enter Roll No ",font=("times",18,'bold'))
entUpRno=Entry(upst,bd=10,font=("arial",18,'bold'))
lblUpName=Label(upst,text="Enter Name",font=("times",18,'bold'))
entUpName=Entry(upst,bd=10,font=("arial",18,'bold'))
lblUpMarks=Label(upst,text=" Enter Marks ",font=("times",18,'bold'))
entUpMarks=Entry(upst,bd=10,font=("arial",18,'bold'))
btnUpSave=Button(upst,text="Save",font=("Times New Roman",18,'bold italic '),background='cyan',command=f8)
btnUpBack=Button(upst,text="Back",font=("Times New Roman",18,'bold italic'),background='cyan',command=f7)

lblUpRno.pack(pady=10)
entUpRno.pack(pady=10)
lblUpName.pack(pady=10)
entUpName.pack(pady=10)
lblUpMarks.pack(pady=10)
entUpMarks.pack(pady=10)
btnUpSave.pack(pady=10)
btnUpBack.pack(pady=10)



#Delete students detail

dst=Toplevel(root)
dst.title("Delete Students Details ")
dst.geometry("500x400+500+100")
dst.withdraw()

lblDtRno=Label(dst,text="Enter Roll No ",font=("times",18,'bold'))
entDtRno=Entry(dst,bd=10,font=("arial",18,'bold'))
btnDtSave=Button(dst,text="Save",font=("Times New Roman",18,'bold italic '),background='cyan',command=f11)
btnDtBack=Button(dst,text="Back",font=("Times New Roman",18,'bold italic '),background='cyan',command=f10)



lblDtRno.pack(pady=10)
entDtRno.pack(pady=10)
btnDtSave.pack(pady=10)
btnDtBack.pack(pady=10)



#Designed by https://github.com/dsapan




root.mainloop()



	
	


