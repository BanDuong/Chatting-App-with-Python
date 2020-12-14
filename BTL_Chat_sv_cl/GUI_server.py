from tkinter import *
import socket
import threading

def Exit():
    exit()

def Server():
        conn, add = s.accept()
        print("Connected by ",add)
        data=conn.recv(1024)
        msg=e.get()
        lb2["text"]=data
        conn.sendall(msg.encode("utf-8"))
        conn.close()
#-----------------------------------------------------#

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
PORT=8888
HOST=socket.gethostname()
ADD=(HOST,PORT)
s.bind(ADD)
s.listen(1)

#-------------------------------------------------------#
t=Tk()
t.title("----SERVER---")

fr1=Frame(t,bg="#FFF9A0")
fr1.pack()

lb = Label(fr1, text="Show messages", font=("Consolas", 14),relief="raised",bord=1,bg="#9CFF11",fg="#C00641",width=40)
lb.pack()

lb2 = Label(fr1,text="", font=("Consolas",11),relief="raised",height=7,width=50,bg="powderblue")
lb2.pack()

lb4 = Label(fr1, text="Write messages", font=("Consolas", 14),relief="raised",bord=1,bg="#9CFF11",fg="#C00641",width=40)
lb4.pack()

e=Entry(fr1,width=50,font=("Consolas",11),relief="raised",bg="purple",fg="white")
e.focus()
e.pack()

bt_send=Button(fr1,text="Send",command=Server,height=2,width=10,bg="#FFB717",font=("consolas",11,"bold"),fg="red")
bt_send.pack(side="left")

bt_exit=Button(fr1,text="Exit",command=Exit,height=2,width=10,bg="#FFB717",font=("consolas",11,"bold"),fg="red")
bt_exit.pack(side="right")

t.resizable(width=False,height=False)

th=threading.Thread(target=Server)
th.start()

t.mainloop()
