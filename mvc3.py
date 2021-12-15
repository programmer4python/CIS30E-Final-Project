# https://makeapppie.com/2014/05/23/from-apple-to-raspberry-pi-a-mvc-template-for-tkinter/
from tkinter import *
import os
import ipaddress


class MyController():
    def __init__(self,parent):
        self.parent = parent
        self.model = MyModel(self)
        self.view = MyView(self)
        self.view.setEntry_text('')
        self.view.setLabel_text('Input IP address for port scan')
        self.view.setEntry_text2('')
        self.view.setLabel_text2('Input source IP address for DoS attack')
        self.view.setEntry_text3('')
        self.view.setLabel_text3('Input target IP address for DoS attack')
        self.view.setEntry_text4('')
        self.view.setLabel_text4('Input port number for DoS attack')

    def addButtonPressed(self):
        self.view.setLabel_text(self.view.entry_text.get())
        self.model.addToList(self.view.entry_text.get())
    def listChangedDelegate(self):
        a=self.model.getList()
        textfile = open("ip.txt","w")
        for element in a:
            textfile.write(element)
        textfile.close()
    def submitDoSButton(self):
         textfile2 = open("dos_ip.txt","w")
         textfile2.write(self.view.entry_text2.get())
         textfile2.write(",")
         textfile2.write(self.view.entry_text3.get())
         textfile2.write(",")
         textfile2.write(self.view.entry_text4.get())
    def run1(self):
        os.system('python3 scan_ports3a.py')
    def run2(self):
        os.system('sudo python3 sisp3.py')
    def run3(self):
        os.system('python3 final_async3.py')
    def run4(self):
        os.system('python3 pro_graph3.py')
    def quitButtonPressed(self):
        self.parent.destroy()

class MyView(Frame):
    def loadView(self):
        quitButton = Button(self.frame,text  = 'Quit', bg="wheat3",fg="black",command=self.vc.quitButtonPressed)
        quitButton.grid(column=2,row=10)
        addButton = Button(self.frame,text = "Submit",bg="black",fg="white",command=self.vc.addButtonPressed)
        addButton.grid(ipady=25,column=0,row=7)
        entry1 = Entry(self.frame,textvariable=self.entry_text,highlightbackground="RoyalBlue4").grid(row=1,column=0,padx=25,sticky=EW)
        label1 = Label(self.frame,textvariable=self.label_text).grid(row=2,column=0, padx=25,sticky=EW)
        btn1 = Button(self.frame, text="Click to run Port Scan", bg="blue4", fg="white", command=self.vc.run1)
        btn1.grid(column=0, row=8)

        btn2 = Button(self.frame, text="Submit",bg="black",fg="white",command=self.vc.submitDoSButton)
        btn2.grid(padx=25,ipady=25, column=1,row=7)

        entry2 = Entry(self.frame,textvariable=self.entry_text2,highlightbackground="RoyalBlue4").grid(row=1,column=1,padx=25,sticky=EW)
        label2 = Label(self.frame,textvariable=self.label_text2).grid(row=2,column=1,sticky=EW)
        btn3 = Button(self.frame, text="Click to run low-level DoS", bg="royalblue2", fg="white", command=self.vc.run2)
        btn3.grid(padx=25,column=1, row=8)

        entry3 = Entry(self.frame,textvariable=self.entry_text3,highlightbackground="RoyalBlue4").grid(row=3,column=1,sticky=EW)
        label3 = Label(self.frame,textvariable=self.label_text3).grid(padx=25,row=4,column=1,sticky=EW)
        entry4 = Entry(self.frame,textvariable=self.entry_text4,highlightbackground="RoyalBlue4").grid(row=5,column=1,sticky=EW)
        label4 = Label(self.frame,textvariable=self.label_text4).grid(padx=25,row=6,column=1,sticky=EW)

        btn4 = Button(self.frame, text="Click for raw data ", bg="cyan4", fg="white", command=self.vc.run3)
        btn4.grid(pady=10,column=2, row=7)

        btn5 = Button(self.frame, text="Click for live plot ", bg="dodgerblue", fg="white", command=self.vc.run4)
        btn5.grid(pady=20,column=2, row=8)

    def __init__(self,vc):
        self.frame=Frame()
        self.frame.grid(row = 0, column = 0)
        self.vc = vc
        self.entry_text = StringVar()
        self.entry_text.set('ip address')
        self.label_text = StringVar()
        self.label_text.set('ip address to port scan')

        self.entry_text2 = StringVar()
        self.entry_text2.set('source ip address')
        self.label_text2 = StringVar()
        self.label_text2.set('Source ip address')

        self.entry_text3 = StringVar()
        self.entry_text3.set('target ip address')
        self.label_text3 = StringVar()
        self.label_text3.set('Target ip address')

        self.entry_text4 = StringVar()
        self.entry_text4.set('port number for attack')
        self.label_text4 = StringVar()
        self.label_text4.set('Port number for attack')
        self.loadView()

    def getEntry_text(self):
        return self.entry_text.get()
    def setEntry_text(self, text):
        self.entry_text.set(text)
    def getLabel_text(self):
        return self.label_text.get()
    def setLabel_text(self,text):
        self.label_text.set(text)

    def getEntry_text2(self):
        return self.entry_text2.get()
    def setEntry_text2(self,text):
        self.entry_text2.set(text)
    def getLabel_text2(self):
        return self.label_text2.get()
    def setLabel_text2(self,text):
        self.label_text2.set(text)

    def getEntry_text3(self):
        return self.entry_text3.get()
    def setEntry_text3(self,text):
        self.entry_text3.set(text)
    def getLabel_text3(self):
        return self.label_text3.get()
    def setLabel_text3(self,text):
        self.label_text3.set(text)

    def getEntry_text4(self):
        return self.entry_text4.get()
    def setEntry_text4(self,text):
        self.entry_text4.set(text)
    def getLabel_text4(self):
        return self.label_text4.get()
    def setLabel_text4(self,text):
        self.label_text4.set(text)

    def getLabel_text5(self):
        return self.label_text5.get()
    def setLabel_text5(self,text):
        self.label_text5.set(text)

    def getLabel_text6(self):
        return self.label_text6.get()
    def setLabel_text6(self,text):
        self.label_text6.set(text)

class MyModel():
    def __init__(self,vc):
        self.vc = vc
        self.myList = []
        self.count = 0
    def listChanged(self):
        self.vc.listChangedDelegate()
    def getList(self):
        return self.myList

    def addToList(self,item):
        myList = self.myList
        myList.append(item)
        self.myList=myList
        self.listChanged()
        if len(myList) == 2:
            myList.pop()
        ipaddress.ip_address(myList[0])

def main():
    root = Tk()
    frame = Frame(root,bg='#0555ff')
    root.title('Port Scan, Low-level DoS, Resources used')
    root.geometry('800x360')
    app = MyController(root)
    root.mainloop()

if __name__ == '__main__':
    main()

