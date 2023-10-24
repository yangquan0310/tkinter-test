from tkinter import *
from views import LoginPage

class MyApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        self.geometry("500x500")
        self.resizable(False, False)


if __name__ == "__main__":
    app = MyApp()
    LoginPage(app) 
    app.mainloop()