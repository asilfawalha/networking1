'''
server
Note: run better in pycharm Edu. in order to make the code work,
first run the server first then run the first client, second client, etc



    Waiyat hamdani project : WAE chat services
    first update: 3/25/2019
    second update:3/26/2019
    third update: 3/27/2019
    Waiyat group:Waiyat , Aseel , and Elizabeth
    
'''
from socket import*
from threading import Thread
import tkinter
'''import mychat'''
from tkinter import Button
from tkinter import Label
from tkinter import StringVar
from tkinter import Entry

global clist
clist=[]

def startserver():
    host = ""
    port = 1201         
    soc = socket(AF_INET,SOCK_STREAM)
    print("Socket created")
    soc.bind((host, port))
    soc.listen(5)       # connection up to 5 requests
    print("Socket now listening")

#------- infinite loop- do not reset for every connection requests------------------
    while True:
        connection, address = soc.accept()
        clist.append(connection)
        ip, port = str(address[0]), str(address[1])
        print("Connected with ip:" + ip + " and port:" + port)
        Thread(target=reciveandsend, args=(connection, ip, port)).start()
        
    soc.close()
#-----------------------------------------------------------------------------------

def reciveandsend(connection, ip, port):
    while True:
      sentence = connection.recv(1024).decode()
      print(sentence)
      for c in clist:
          c.send(sentence.encode())
          
def serverstart(event=None):
    root=tkinter.Tk()
    def end():
        root.destroy()
    end()
    startserver()

def pathfinder():
    root=tkinter.Tk()
    root.title("partfinder roots")
    root.geometry("250x100")
    root.configure(background='#4DF9F2')
    frame=tkinter.Frame(root)
    titlelabel=Label(root,text="Pathfinder Server",background='#4DF9F2',font=("Helvetica", 16))
    titlelabel.pack()
    '''labels= Label(root,text="How many clients?(2 to 5): ")
    labels.pack()
    clientss= StringVar()
    entrys= Entry(root,textvariable=clientss)
    entrys.pack()'''
    btnserver = Button(root, text='Start Server',command=serverstart)
    btnserver.pack()
    '''entrys.bind(btnserver)'''

    root.mainloop()


def main():
    pathfinder()

if __name__ == "__main__":
    main()
