import tkinter as tk

import requests
from lxml import etree


class HuiLv:
    def __init__(self):
        # 获取数据
        ans = {}
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        url = 'https://www.boc.cn/sourcedb/whpj/'
        response = requests.get(url=url, headers=headers)
        response.encoding = 'utf-8'  # 一般都是先将对象转化编码类型再转为文本
        response = response.text
        xmal = etree.HTML(response)
        l = xmal.xpath(r'//div[@class="BOC_main"]/div[1]/div[2]/table//tr')
        for i in l[1:]:
            ans.update({i.xpath(r'./td[1]/text()')[0]: round(float(i.xpath(r'./td[6]/text()')[0]) / 100, 2)})
        ans = list(ans.items())
        ans = sorted(ans, key=lambda x: x[1], reverse=True)
        ans.insert(0, ('货币名称', '/RMB'))
        ans.insert(0, ('货币名称', '/RMB'))
        self.huilv(ans)
    def huilv(self,ans):
        #数据展示
        self.win = tk.Tk()
        self.win.title('今日汇率(中行折算价）')
        for r in range(0, len(ans) - 1, 2):
            for c in range(0, 4):
                name = tk.Text(self.win, width=10, height=2, bg='CadetBlue3')  # 创建一个text窗口

                name.insert('end', ans[r + c // 2][c % 2])  # 在刚刚创建的窗口里写入默认的文本

                name.grid(row=r, column=c)  # 将该text窗口放在第r行，第c列
        if len(ans) % 2 == 1:
            name = tk.Text(self.win, width=10, height=2, bg='CadetBlue3')  # 创建一个text窗口
            name.insert('end', ans[len(ans) - 1][0])  # 在刚刚创建的窗口里写入默认的文本
            name.grid(row=len(ans) - 1, column=0)
            name = tk.Text(self.win, width=10, height=2, bg='CadetBlue3')  # 创建一个text窗口
            name.insert('end', ans[len(ans) - 1][1])  # 在刚刚创建的窗口里写入默认的文本
            name.grid(row=len(ans) - 1, column=1)
        self.win.mainloop()
