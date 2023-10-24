from tkinter import *
from tkinter.messagebox import *
class AboutFrame(Frame): # 继承Frame类 
    def __init__(self, master=None): 
        Frame.__init__(self, master) 
        self.root = master #定义内部变量root 
        self.createPage() 
        
    def createPage(self): 
        Label(self, text='关于界面').pack() 

if __name__ == "__main__":
    app = Tk()
    app.geometry("500x500")
    AboutFrame(app).pack()
    app.mainloop()