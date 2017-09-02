"""
This is a peer to peer chat program, wrote in python 2.7
use same network for use it .
p2p chat version 1.0
"""

import Tkinter
import socket
from threading import Thread
import tkMessageBox
import time

class gui:
    def __init__(self,root):
        self.root = root
        self.root.geometry("248x633+10+10")
        self.root.configure(background="white")
        self.root.title("p2p chat")
        self.root.resizable(0,0)
        self.b = 0

        Thread(target=self.layout).start()
        Thread(target=self.server).start()

    def layout(self):
        global text_box, send_msg_box,ip_box,connect_but

        your_ip_label = Tkinter.Label(self.root, text=" your  ip", fg="blue", font=("Helvetica", 16))
        your_ip_label.grid(row=0, column=0)
        ip = socket.gethostbyname(socket.gethostname())
        ip_label = Tkinter.Label(self.root, text=ip, fg="blue", font=("Helvetica", 16))
        ip_label.grid(row=0, column=1)
        your_friend_ip = Tkinter.Label(self.root, text="friend ip", fg="blue", font=("Helvetica", 16))
        your_friend_ip.grid(row=1, column=0)
        ip_box = Tkinter.Entry(self.root, bg="gray", fg="blue")
        ip_box.grid(row=1, column=1)

        connect_but = Tkinter.Button(self.root, text="connect",command=self.client,fg="blue",width=21,bg="cyan",font=("Helvetica", 14))
        connect_but.grid(row=2,column=0,columnspan=3)

        text_box = Tkinter.Text(self.root, fg="blue", width=30, bg="gray")
        text_box.grid(row=3, column=0, columnspan=2)
        send_msg_box = Tkinter.Text(self.root, fg="blue", width=30, height=5, bg="gray")
        send_msg_box.grid(row=4, column=0, columnspan=2)

        send_but = Tkinter.Button(self.root, text="Send",command=self.send_msg, fg="blue", height=2,width=21, bg="magenta", font=("Helvetica", 14))
        send_but.grid(row=5, column=0,columnspan=3)

    def server(self):
        global s
        s = socket.socket()
        host = socket.gethostbyname(socket.gethostname())
        port = 1234
        s.bind((host, port))
        s.listen(5)


    def client(self):
        global s1
        host = ip_box.get()
        s1 = socket.socket()
        port = 1234
        try:
            s1.connect((host, port))
            connect_but.configure(text="connected")
            self.a = 1
            self.b = 1
            Thread(target=self.rec_msg).start()
        except:
            tkMessageBox.showinfo("p2p", "plese enter correct ip")


    def send_msg(self):
        global c
        if(self.b==1):
            if (self.a == 1):
                c, addr = s.accept()
            self.a = 0
            data = send_msg_box.get("1.0", "end-1c")
            c.send(data)
            text_box.insert(Tkinter.END,"You: "+data + "\n")
            send_msg_box.delete('1.0', Tkinter.END)

        else:
            tkMessageBox.showinfo("p2p", "plese connect after send message")


    def rec_msg(self):
        while True:
            try:
                data = s1.recv(1024)
            except:
                print "Error"

            if data:
                text_box.insert(Tkinter.END,"Frd: "+data + "\n")


root = Tkinter.Tk()
gui(root)
root.mainloop()
