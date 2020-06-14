'''
client 1
Note: run better in pycharm Edu. in order to make the code work,
first run the server first then run the first client, second client, etc



    Waiyat hamdani project : WAE chat services
    first-update: 3/25/2019 second-update: 3/26/2019  third-update:3/27/2019
    fouth-update: 3/28/2019
    
    
    Waiyat group:Waiyat , Aseel , and Elizabeth
    
'''
from threading import Thread
import tkinter.messagebox
from tkinter import*
from tkinter import filedialog
from socket import*



serverName = gethostname()
serverPort = 1201

clientSocket = socket()
clientSocket.connect((serverName,serverPort))

#-----------------------------------------------encrypt Vigenere---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def encryptVigenere(key,m):
  message=str(m)
  messagelist=[]
  #print(keylength)
  keylist=[]
  messagePlusKeyList=[]
  encrypt=[]
  alphatoNumber={"a":0,"b":1, "c":2, "d":3,"e":4,"f":5, "g":6,"h":7,"i":8,
                 "j":9,"k":10, "l":11,"m":12,"n":13,"o":14,"p":15,"q":16,
                 "r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,
                 "z":25," ":26,",":27,".":28,"!":29,"@":30,"?":31,"$":32,"%":33,'^':34,'&':35,
                 "*":36,"(":37,")":38,"-":39,"+":40,"=":41,"1":42,"2":43,
                 "3":44,"4":45,"5":46,"6":47,"7":48,"8":49,"9":50,"0":51,"_":52,'/':53,'.':54,
                 ",":55,"{":56,"}":57,"|":58,"A":59,"B":60,"C":61,"D":62,"E":63,'F':64,'G':65,'H':66,
                 "I":67,"J":68,"K":69,"L":70,"M":71,"N":72,"O":73,"P":74,"Q":75,'R':76,'S':77,
                 "T":78,"U":79,"V":80,"W":81,"X":82,"Y":83,"Z":84,">":85,"<":86,"'":87}
  
  numbertoAlpha={0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k", 11:"l",
                 12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",
                 23:"x",24:"y",25:"z",26:" ",27:",",28:".",29:"!",30:"@",31:"?",32:"$",33:"%",
                 34:"^",35:"&",36:"*",37:"(",38:")",39:"-",40:"+",41:"=",42:"1",43:"2",
                 44:"3",45:"4",46:"5",47:"6",48:"7",49:"8",50:"9",51:"0",52:"_",53:"/",54:".",
                 55:",",56:"{",57:"}",58:"|",59:"A",60:"B",61:"C",62:"D",63:"E",64:"F",65:"G",66:'H',
                 67:"I",68:"J",69:"K",70:"L",71:"M",72:"N",73:"O",74:"P",75:"Q",76:"R",77:"S",
                 78:"T",79:"U",80:"V",81:"W",82:"X",83:"Y",84:"Z",85:">",86:"<",87:"'"}

  i=0
  for i in range(len(message)):
    p = key[i % len(key)]
    keylist.append(alphatoNumber.get(p))
  #print(keylist)

  for o in message:
    messagelist.append(alphatoNumber.get(o))
  #print(messagelist)

  z=0
  for x in messagelist:
    l=x+keylist[z]
    z+=1
    limit=int(len(numbertoAlpha))
    if l <= limit: #the logic of vigenere cypher that i know , when it shif more than the list it go back to zero
      messagePlusKeyList.append(l)#my command is basicly tell them if the l is smaller than the dictionary do nothing
    else:
      #else minus l with the length of the dictionary
      excesiveNumber= l - len(numbertoAlpha)
      messagePlusKeyList.append(excesiveNumber)
  #print(messagePlusKeyList)


  for d in messagePlusKeyList:
    q=numbertoAlpha.get(d)
    encrypt.append(q)
  #print(''.join(encrypt))  #-> i want to see what going on
  return ''.join(encrypt)

#-------------------------------------------------------decrypt Vigenere--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def decryptVigenere(key,m):
  message=str(m)

  #print(keylength)
  keylist=[]
  messagePlusKeyList=[]
  messagelist=[]
  decrypt=[]
  alphatoNumber={"a":0,"b":1, "c":2, "d":3,"e":4,"f":5, "g":6,"h":7,"i":8,
                 "j":9,"k":10, "l":11,"m":12,"n":13,"o":14,"p":15,"q":16,
                 "r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,
                 "z":25," ":26,",":27,".":28,"!":29,"@":30,"?":31,"$":32,"%":33,'^':34,'&':35,
                 "*":36,"(":37,")":38,"-":39,"+":40,"=":41,"1":42,"2":43,
                 "3":44,"4":45,"5":46,"6":47,"7":48,"8":49,"9":50,"0":51,"_":52,'/':53,'.':54,
                 ",":55,"{":56,"}":57,"|":58,"A":59,"B":60,"C":61,"D":62,"E":63,'F':64,'G':65,'H':66,
                 "I":67,"J":68,"K":69,"L":70,"M":71,"N":72,"O":73,"P":74,"Q":75,'R':76,'S':77,
                 "T":78,"U":79,"V":80,"W":81,"X":82,"Y":83,"Z":84,">":85,"<":86,"'":87}
  
  numbertoAlpha={0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k", 11:"l",
                 12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",
                 23:"x",24:"y",25:"z",26:" ",27:",",28:".",29:"!",30:"@",31:"?",32:"$",33:"%",
                 34:"^",35:"&",36:"*",37:"(",38:")",39:"-",40:"+",41:"=",42:"1",43:"2",
                 44:"3",45:"4",46:"5",47:"6",48:"7",49:"8",50:"9",51:"0",52:"_",53:"/",54:".",
                 55:",",56:"{",57:"}",58:"|",59:"A",60:"B",61:"C",62:"D",63:"E",64:"F",65:"G",66:'H',
                 67:"I",68:"J",69:"K",70:"L",71:"M",72:"N",73:"O",74:"P",75:"Q",76:"R",77:"S",
                 78:"T",79:"U",80:"V",81:"W",82:"X",83:"Y",84:"Z",85:">",86:"<",87:"'"}


  i=0
  for i in range(len(message)):
    p = key[i % len(key)] #it take the sentence into alphabet and the alphabet will module to the key in resulted comparing each position to the message alpabet if the message alpahbet longer it will return to the zero array in key .
    keylist.append(alphatoNumber.get(p))
  #print(keylist)

  for o in message:
    messagelist.append(alphatoNumber.get(o))
  #print(messagelist)

  z=0
  for x in messagelist:

    l=x-keylist[z]
    z+=1
    limit=int(len(numbertoAlpha)) #set the limit from the length of dictionary
    #print(limit)
    if l < 0: #if less than zero plus the length of dictionary
      #print(l)
      negativeNumber = l + len(numbertoAlpha)
      messagePlusKeyList.append(negativeNumber)
    else:
      messagePlusKeyList.append(l)

  #print(messagePlusKeyList)


  for d in messagePlusKeyList:
    q=numbertoAlpha.get(d)
    decrypt.append(q)
  return ''.join(decrypt)
#------------------------------------------------------------when button send press-------------------------------------------------------------------------------------
def send(event=None):
  waiyatmasterkey="waiyat"
  usernames=usr.get()
  sentence = msg.get()
  sentencedata=usernames+">"+sentence
  encryptedmessage=encryptVigenere(waiyatmasterkey,sentencedata)
  
  msg.set("")
  clientSocket.send(bytes(encryptedmessage,"utf8"))
  
  
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------receiving message--------------------------------------------------------------------------------------
def recieve(event=None):
  while True:
    receving = clientSocket.recv(1024).decode("utf8")
    messagereceive= str(receving)
    print(messagereceive)
    waiyatmasterkey="waiyat"
    decryptmessage=decryptVigenere(waiyatmasterkey,messagereceive)
    chat_list.insert(END,decryptmessage)
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------opefile-------------------------------------------------------------------------------------------------
def openfile():  
  filename = filedialog.askopenfilename()
  file= os.path.basename(filename)
  chat_list.insert(END,"sending-->" + file)
  readingfileandsend(file)

def readingfileandsend(filename):
  f=open(filename,"rb")
  datafile=f.read(1024)
  while datafile==True:
    clientSocket.send("f"+datafile)
  
def about():
  tkinter.messagebox.showinfo('About Pathfïnder chat', 'programer:Waiyat,Aseel and Ellizabeth >>>resposible on creating chat and multi-thread server.\n credit: some help come from  my professor Dr. Hao Wu')

def howto():
  tkinter.messagebox.showinfo("how to use Pathfïnder","-In order to used the chat. we need to active the server.py. \n -After done running the server then we can activate mychat, mychat1 and mychat2")

root= Tk()
menubar = Menu(root)
root.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='option',menu =subMenu)
subMenu.add_command(label='open-file',command = openfile)
subMenu.add_command(label='about-us',command=about)
subMenu.add_command(label='how-to-used-chat',command =howto)
subMenu.add_command(label='exit-chat',command= root.destroy)




root.title("Pathfïnder")
root.geometry("460x500")#keep this 460x500 to have the best gui experiance
root.configure(background='#4DF9F2')
titlelabel=Label(root,text="Pathfïnder",background='#4DF9F2',font=("Helvetica", 16))
titlelabel.pack()
usernamelabel=Label(root,text="Username:" ,height=2)
usernamelabel.pack()
usr = StringVar()
entryuser=Entry(root,textvariable=usr)
entryuser.bind(send)
entryuser.place(relx=0.6, rely = 0.07)

#------------------------------------------------------------Chat Scroll box dialog------------------------------------------------------------------
framechatdialog = Text(root)
msg = StringVar()
chat_list =Listbox(framechatdialog, height=21, width=80, yscrollcommand=Scrollbar(framechatdialog).set)
Scrollbar(framechatdialog).pack(side=RIGHT, fill=Y)
chat_list.pack(side=LEFT, fill=BOTH)
framechatdialog.pack()
#----------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------message textfield-----------------------------------------------------------------
entry = Entry(root, textvariable=msg)
entry.bind("<Return>",send)
entry.pack(fill=BOTH, pady=5)
#-----------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------button send message---------------------------------------------------------------
btnsend = Button(root, text='send',command=send)
btnsend.pack()



#------------------------------------------------------------------------------------------------------------------------------------------------
  
receive_thread = Thread(target=recieve)
receive_thread.start()


root.mainloop()

