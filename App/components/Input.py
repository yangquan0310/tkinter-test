from tkinter import *
from tkinter.messagebox import *
from borax.calendars.lunardate import LunarDate
class InputFrame(Frame): # 继承Frame类 
    def __init__(self, master=None): 
        Frame.__init__(self, master) 
        self.root = master #定义内部变量root 
        self.itemName = StringVar() 
        self.importPrice = StringVar() 
        self.sellPrice = StringVar() 
        self.deductPrice = StringVar() 
        self.year=1996
        self.month=3
        self.day=10
        self.createPage() 
    
    def createPage(self): 
        Label(self, text = '出生日期').grid(row=1,column=3) 
        Label(self, text = '年: ').grid(row=2, column=0, stick=W,pady=10)
        self.year_entry=Entry(self, textvariable=self.importPrice)
        self.year_entry.grid(row=2, column=1, stick=W)
        Label(self, text = '月: ').grid(row=2, column=2, stick=W,pady=10)
        self.month_entry=Entry(self, textvariable=self.sellPrice)
        self.month_entry.grid(row=2, column=3, stick=W, pady=10)
        Label(self, text = '日: ').grid(row=2, column=4, stick=W,pady=10)
        self.day_entry=Entry(self, textvariable=self.deductPrice)
        self.day_entry.grid(row=2, column=5, stick=W, pady=10)
        Button(self, text='计算', command=self.compute).grid(row=3, column=3, pady=10)

    def compute(self):
        def has_non_digit_characters(input_string):
            for char in input_string:
                if not char.isdigit():
                    return True  # 如果找到非数字字符，返回True
            return False  # 如果没有找到非数字字符，返回False
        self.year=self.year_entry.get()
        self.month=self.month_entry.get()
        self.day=self.day_entry.get()
        if len(self.year) == 0 or len(self.month) == 0 or len(self.day) == 0:
            showinfo(title='错误', message='请输入出生日期')
        else:
            if (has_non_digit_characters(self.year) and has_non_digit_characters(self.month) and has_non_digit_characters(self.day)):
                showinfo(title='错误', message='请输入正确的出生日期')
            else:
                self.year=int(self.year_entry.get())
                self.month=int(self.month_entry.get())
                self.day=int(self.day_entry.get())
                self.lunar_date = LunarDate.from_solar_date(self.year, self.month, self.day)
                self.ganzhi_brith=self.lunar_date.strftime('%o年%p月%q日')
                self.ganzhi_brith_year=self.ganzhi_brith[0:2]
                self.ganzhi_brith_month=self.ganzhi_brith[3:5]
                self.ganzhi_brith_day=self.ganzhi_brith[6:8]
                self.now=LunarDate.today()
                self.ganzhi_now=self.now.strftime('%o年%p月%q日')
                self.ganzhi_now_year=self.ganzhi_now[0:2]
                self.ganzhi_now_month=self.ganzhi_now[3:5]
                self.ganzhi_now_day=self.ganzhi_now[6:8]
                text=Text(self, width=50, height=10)
                text.grid(row=4, column=1,columnspan=6, stick=W, pady=15)
                text.insert(INSERT, "出生于%s"%(self.ganzhi_brith))
                text.insert(INSERT, "\n")
                text.insert(INSERT, "今天是%s"%(self.ganzhi_now))
                text.insert(INSERT, "\n")
                text.insert(INSERT, "你的日柱天干“%s”和年干“%s”呈“%s”关系"%(self.__tianganshishen__(self.ganzhi_brith_day[0:1],self.ganzhi_now_year[0:1])))
                text.insert(INSERT, "\n")
                text.insert(INSERT, "你的日柱天干“%s”和月干“%s”呈“%s”关系"%(self.__tianganshishen__(self.ganzhi_brith_day[0:1],self.ganzhi_now_month[0:1])))
                text.insert(INSERT, "\n")
                text.insert(INSERT, "你的日柱天干“%s”和日干“%s”呈“%s”关系"%(self.__tianganshishen__(self.ganzhi_brith_day[0:1],self.ganzhi_now_day[0:1])))
    def __tianganshishen__(self,tiangan1,tiangan2):
        # 天干和十神关系
        tian_gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        ten_god_relations = {
            "甲": ["比肩", "劫财", "食神", "伤官", "偏财", "正财", "七杀", "正官", "偏印", "正印"],
            "乙": ["劫财", "比肩", "正印", "偏印", "正官", "七杀", "正财", "偏财", "伤官", "食神"],
            "丙": ["食神", "伤官", "比肩", "劫财", "偏印", "正印", "正官", "七杀", "偏财", "正财"],
            "丁": ["伤官", "食神", "劫财", "比肩", "正印", "偏印", "正财", "偏财", "七杀", "正官"],
            "戊": ["偏财", "正财", "食神", "伤官", "比肩", "劫财", "偏印", "正印", "正官", "七杀"],
            "己": ["正财", "偏财", "伤官", "食神", "劫财", "比肩", "正印", "偏印", "正官", "七杀"],
            "庚": ["七杀", "正官", "偏财", "正财", "食神", "伤官", "劫财", "比肩", "偏印", "正印"],
            "辛": ["正官", "七杀", "正财", "偏财", "伤官", "食神", "劫财", "比肩", "正印", "偏印"],
            "壬": ["偏印", "正印", "七杀", "正官", "偏财", "正财", "食神", "伤官", "比肩", "劫财"],
            "癸": ["正印", "偏印", "正官", "七杀", "正财", "偏财", "伤官", "食神", "劫财", "比肩"]
        }
        relation = ten_god_relations[tiangan1][tian_gan.index(tiangan2)]
        return tiangan1,tiangan2,relation


if __name__ == "__main__":
    app = Tk()
    app.geometry("500x500")
    InputFrame(app).pack()
    app.mainloop()