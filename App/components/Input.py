from tkinter import *
from tkinter.messagebox import *
class InputFrame(Frame): # 继承Frame类 
    def __init__(self, master=None): 
        Frame.__init__(self, master) 
        self.root = master #定义内部变量root 
        self.itemName = StringVar() 
        self.importPrice = StringVar() 
        self.sellPrice = StringVar() 
        self.deductPrice = StringVar() 
        self.createPage() 
    
    def createPage(self): 
        Label(self).grid(row=0, stick=W, pady=10) 
        Label(self, text = '姓名: ').grid(row=1, stick=W, pady=10) 
        Entry(self, textvariable=self.itemName).grid(row=1, column=1, stick=E) 
        Label(self, text = '性别: ').grid(row=2, stick=W, pady=10) 
        Entry(self, textvariable=self.importPrice).grid(row=2, column=1, stick=E) 
        Label(self, text = '年龄: ').grid(row=3, stick=W, pady=10) 
        Entry(self, textvariable=self.sellPrice).grid(row=3, column=1, stick=E) 
        Label(self, text = '年级: ').grid(row=4, stick=W, pady=10) 
        Entry(self, textvariable=self.deductPrice).grid(row=4, column=1, stick=E) 
        Button(self, text='录入').grid(row=6, column=1, stick=E, pady=10) 

if __name__ == "__main__":
    app = Tk()
    app.geometry("500x500")
    InputFrame(app).pack()
    app.mainloop()