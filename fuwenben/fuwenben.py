from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QColorDialog, QApplication, QTextEdit, QFontDialog, QDialog, QWidget, \
    QPushButton, QComboBox, QMainWindow, QLabel, QLineEdit
from PyQt5.QtPrintSupport import QPageSetupDialog,QPrintDialog,QPrinter
from PyQt5.QtGui import QIcon, QTextCursor
import sys
#hfheuhfu
import tkinter as tk
flag=0
file_name=''

from idna import unicode
def Qstring2Str(qStr):
    """转换Qstring类型为str类型"""
    return unicode(qStr.toUtf8(), 'utf-8', 'ignore')
class Ui_test(QWidget):
    def __init__(self):
        super().__init__()
        self.creat_info()
        self.printer=QPrinter()#打印模板（用于输出文件打印类型）
        # 搜索相关项
        self.text_content = None
        self.search_key = None
        self.search_sum = 0
        self.search_cur = 0

    def creat_info(self):
        self.setGeometry(400,400,800,500)
        self.setWindowTitle('富文本编辑器')
        self.count=0#记录位置
        self.creat_res()#添加按钮，标签，文本输入框
        self.show()#窗口显示

    def creat_res(self):
        self.t1=QTextEdit(self)
        self.t1.setGeometry(13,100,775,380)
        self.B_search=QPushButton('搜索',self)
        self.B_search.setGeometry(180,60,50,30)
        self.E_search=QLineEdit(self)
        self.E_search.setGeometry(15,60,150,30)
        self.L_search=QLabel(self)
        self.L_search.setGeometry(250,60,50,30)
        self.L_search.setText("0/0")
        self.C_text=QLineEdit(self)
        self.C_text.setGeometry(300,60,150,30)
        self.B_change=QPushButton('替换',self)
        self.B_change.setGeometry(470,60,50,30)
        self.B_changeAll = QPushButton('全部替换', self)
        self.B_changeAll.setGeometry(540, 60, 100, 30)
        self.B_openfile = QPushButton('打开文件', self)
        self.B_openfile.setGeometry(15,15,70,30)
        self.B_openmorefile=QPushButton('打开多文件',self)
        self.B_openmorefile.setGeometry(95,15,100,30)
        self.B_change_font=QPushButton('修改字体',self)
        self.B_change_font.setGeometry(205,15,70,30)
        self.B_change_color=QPushButton('修改颜色',self)
        self.B_change_color.setGeometry(285,15,70,30)
        self.save_file=QPushButton('保存文件',self)
        self.save_file.setGeometry(365,15,70,30)
        self.set_page=QPushButton('页面设置',self)
        self.set_page.setGeometry(445,15,70,30)
        self.print_file=QPushButton('文件打印',self)
        self.print_file.setGeometry(525,15,70,30)
        self.clear_file=QPushButton('清除文本',self)
        self.clear_file.setGeometry(605,15,70,30)
        self.xieti = QPushButton('斜体', self)
        self.xieti.setGeometry(685, 15, 45, 30)
        self.sava_other_file = QPushButton('另存为', self)
        self.sava_other_file.setGeometry(740, 15, 50, 30)
        self.config()

    def config(self):
        #可以像这样添加触发事件，也可使用继承Qweight +重写响应的event函数pressEvent（self,event)
        self.B_openfile.clicked.connect(self.open_file)
        self.B_openmorefile.clicked.connect(self.open_files)
        self.B_change_color.clicked.connect(self.change_color)
        self.B_change_font.clicked.connect(self.change_font)
        self.clear_file.clicked.connect(self.clear_all)
        self.save_file.clicked.connect(self.save_files)
        self.set_page.clicked.connect(self.page_config)
        self.print_file.clicked.connect(self.print_files)
        self.xieti.clicked.connect(self.font_xieti)
        self.sava_other_file.clicked.connect(self.sava_other_files)
        # 文本框内容变化重设被搜索内容
        self.t1.textChanged.connect(self.reset_text_content)
        self.B_search.clicked.connect(self.search)
        self.B_change.clicked.connect(self.change)
        self.B_changeAll.clicked.connect(self.changeAll)

    def open_file(self):
        global flag,file_name
        files=QFileDialog.getOpenFileName(self,'打开本地文件')
        flag=1
        file_name=files[0]
        if files[0]:
            with open(files[0],mode='r',encoding='utf-8',errors='ignore') as f:
                self.t1.setText(f.read())

    def open_files(self):#此处获取得是多个文件，返回得是文件列表
        global flag
        flag=0#就不再是原来的那个文件了，所以保存就应该跳出新文件保存窗口
        files=QFileDialog.getOpenFileNames(self,'打开本地文件')
        if files[0]:
            for file in files[0]:
                with open(file,mode='r',encoding='gb18030',errors='ignore') as f:
                    self.t1.append(f.read())

    def change_font(self):
        # fo为选择的字体,b为是否更改字体因为存在ok和cancel
        fo,b=QFontDialog.getFont()
        if b:
            self.t1.setCurrentFont(fo)

    def change_color(self):
        co=QColorDialog.getColor()
        if co.isValid():#co是否有效
           self.t1.setTextColor(co)

    def save_files(self):
        global flag,file_name
        if flag==1:
            with open(file_name,mode='w',encoding='gb18030',errors='ignore') as f:
                f.write(self.t1.toPlainText())
                return
        file=QFileDialog.getSaveFileName(self,'保存文件')
        if file[0]:
            with open(file[0],mode='r',encoding='gb18030',errors='ignore') as f:
                f.write(self.t1.toPlainText())

    def page_config(self):#页面设置，需要printer打印对象
        page_set=QPageSetupDialog(self.printer,self)
        page_set.exec_()

    def print_files(self):#打印文件，也需要打印对象
        page_print=QPrintDialog(self)
        if QDialog.Accepted==page_print.exec_():
            self.t1.print(self.printer)

    def clear_all(self):
        self.t1.clear()

    def font_xieti(self):
        self.t1.setFontItalic(True)

    def sava_other_files(self):
        file = QFileDialog.getSaveFileName(self, '另存为')
        if file[0]:
            with open(file[0], mode='r', encoding='gb18030', errors='ignore') as f:
                f.write(self.t1.toPlainText())

    def select(self, start, length):
        """选中文字,高亮显示"""
        #cur游标对象
        cur = QTextCursor(self.t1.textCursor())  # 文本浏览框
        cur.setPosition(start)
        cur.setPosition(start + length, QTextCursor.KeepAnchor)
        self.t1.setTextCursor(cur)#获取指定区间的文本

    def reset_text_content(self):
        """改变待搜索内容"""
        self.text_content = None
        self.search_sum = 0
        self.search_cur = 0


    def search(self):
        """搜索"""
        search_word = self.E_search.text()
        if search_word != self.search_key:
            self.search_key = search_word
            self.search_sum = 0
            self.search_cur = 0
        if not self.text_content:#如果text_content为空说明已经更新了文本框内容
            self.text_content = self.t1.toPlainText()#文本浏览框
        if not self.search_sum:#初始化查找总个数
            self.search_sum = self.text_content.count(search_word)
            if self.search_sum != 0:
                start = self.text_content.index(search_word)
                self.count=start
                self.select(start, len(search_word))
                self.search_cur += 1
        else:
            if self.search_cur < self.search_sum:
                start = self.text_content.find(search_word, self.t1.textCursor().position())
                self.count=start
                if start != -1:
                    self.select(start, len(search_word))
                    self.search_cur += 1
            else:
                #如果要检索的超过了检索的个数就重新启动search(对应search_sum和search_cur)
                self.search_sum = 0
                self.search_cur = 0
                self.count=0
                self.search()
        self.t1.setFocus()
        self.L_search.setText("{}/{}".format(self.search_cur, self.search_sum))


    #实际设置替换，也可以使用text_content string的repalce函数替换所有后再将t1文本框数据设置为text_content。但是这样的坏处是不能使用Ctrl+z撤销操作
    def change(self):
        search_word = self.E_search.text()
        change_word=self.C_text.text()
        if not self.text_content:#如果text_content为空说明已经更新了文本框内容
            self.text_content = self.t1.toPlainText()#文本浏览框
        start = self.text_content.find(search_word,self.count)#使用search当前查找到的位置作为起点
        self.select(start, len(search_word))
        self.t1.insertPlainText(change_word)
        # self.text_content=self.text_content.replace(search_word,change_word,1)
        # self.t1.setText(self.text_content)
        self.t1.setFocus()#用于高亮显示

#实际就是调用多次一次替换
    def changeAll(self):
        search_word = self.E_search.text()
        change_word = self.C_text.text()
        if not self.text_content:  # 如果text_content为空说明已经更新了文本框内容
            self.text_content = self.t1.toPlainText()  # 文本浏览框
            if self.text_content=="":#如果还为空则说明文本框中没有数据了
                return

        #当text_content非空时才能使用find,虽然可能不会为空但是如果不这样使用会报错
        while True:
            if self.text_content=="":
                return
            #index函数如果没有查找到会报错，所以需要添加条件（eg:使用个数条件），相对而言find更好
            # start = self.text_content.index(search_word)#因为是对本身的t1修改，所以他会自动调用其中的reset_text_content函数，
            start=self.text_content.find(search_word)
            # 从而使得text_content又变为空值
            if start==-1:
                return#如果没有找到则说明要查找的也没有了，可以直接结束。
            self.select(start, len(search_word))
            self.t1.insertPlainText(change_word)#是对t1改变了所以需要再获取t1数据
            self.search_sum-=1
            self.text_content=self.t1.toPlainText()


        # self.text_content = self.text_content.replace(search_word, change_word)
        # self.t1.setText(self.text_content)
        # self.t1.setFocus()
if __name__=="__main__":
    ap=QApplication(sys.argv)
    u=Ui_test()
    # u.search()
    sys.exit(ap.exec_())



