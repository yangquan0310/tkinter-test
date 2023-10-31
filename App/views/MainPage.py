from tkinter import *
from components import InputFrame, AboutFrame
class MainPage(object): 
    def __init__(self, master=None): 
        self.root = master #定义内部变量root 
        self.root.geometry('%dx%d' % (600, 400)) #设置窗口大小 
        self.createPage() 
    
    def createPage(self): 
        self.inputPage = InputFrame(self.root) # 创建不同Frame 
        self.aboutPage = AboutFrame(self.root) 
        self.inputPage.pack() #默认显示数据录入界面 
        menubar = Menu(self.root) 
        menubar.add_command(label='推测', command = self.inputData) 
        menubar.add_command(label='关于', command = self.aboutDisp) 
        self.root['menu'] = menubar # 设置菜单栏 
        
    def inputData(self): 
        self.inputPage.pack() 
        self.aboutPage.pack_forget() 
    
    def aboutDisp(self): 
        self.inputPage.pack_forget()  
        self.aboutPage.pack() 

if __name__ == "__main__":
    app = Tk()
    MainPage(app) 
    app.mainloop()