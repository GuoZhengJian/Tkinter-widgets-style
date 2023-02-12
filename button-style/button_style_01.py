# -*- coding: utf-8 -*-
"""
bilibili: 键盘侠十指如飞

B站主页: https://space.bilibili.com/9570945

AcFun主页: https://www.acfun.cn/u/72762081
"""

import tkinter as tk


class MyWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-topmost', True)
        self.config({'background': '#ffffff'})
        self.geometry('1886x168+9+16')
        self.update()

        # 实例按钮风格
        self.widget_style_args()
        self.button_style()

    def widget_style_args(self):
        """小部件风格的参数."""
        self.dynamic_args = [5,10,15,10,5]
        # self.dynamic_color = ['#87c0ca', '#5aa4ae', '#108b96', '#5aa4ae', '#87c0ca'] #{bg: '#a2d2e2'}
        # self.dynamic_color = ['#9bb496', '#81a380', '#698e6a', '#81a380', '#9bb496'] #{bg: '#bed2bb'}
        # self.dynamic_color = ['#6f94cd', '#5976ba', '#2e59a7', '#5976ba', '#6f94cd'] #{bg: '#88abda'}
        # self.dynamic_color = ['#5da39d', '#3d8e86', '#206864', '#3d8e86', '#5da39d'] #{bg: '#88bfb8'}
        self.dynamic_color = ['#bcd4e7', '#a3bbdb', '#8aabcc', '#a3bbdb', '#bcd4e7'] #{bg: '#d4e5ef'}

    def button_style(self):
        """按钮风格, 梯度放大."""
        self.myframe = tk.Frame(self)
        self.myframe.config({'background': '#FFFFFF'})
        self.myframe.place(relx=0.15, rely=0.15, height=100)
        
        for i in range(1, 26):
            mybutton = tk.Button(self.myframe, text=i)
            mybutton.config({'borderwidth': 0,
                            'relief': 'ridge',
                            'background': '#d4e5ef',
                            'foreground': '#FFFFFF',
                            'activebackground': '#1abc9c',
                            'font': '-family {@Malgun Gothic} -size 15 -weight bold',
                            })
            mybutton.pack(side='left', anchor='center', expand=False, pady=0, padx=0, ipady=0, ipadx=10)

            # bind事件
            mybutton.bind('<Enter>', self.Enter_bind, add='+')         # 鼠标或按键飘过时的样式;
            mybutton.bind('<Leave>', self.Leave_bind, add='+')         # 鼠标或按键飘过时的样式;

    def Enter_bind(self, event):
        """鼠标进入组件时触发."""
        print('正在执行Button_%s'%event.widget.cget('text'), '\n')
        
        widget_location = self.myframe.winfo_children().index(event.widget)
        widget_location_list = [i for i in range(widget_location-2, widget_location+3)]

        for i in widget_location_list:
            widget_index = widget_location_list.index(i)

            # 动态效果的 ipady 和 background 参数.
            dynamic_ipady = self.dynamic_args[widget_index]
            dynamic_background = self.dynamic_color[widget_index]

            # 剔除小于0 和 大于最大索引位置的动态小部件索引位置
            if i >= 0 and i < len(self.myframe.winfo_children()):

                # 动态颜色
                widget_obj = self.myframe.winfo_children()[i]
                widget_obj.config({'background': dynamic_background})

                # 动态大小
                widget_pack_dict = widget_obj.pack_info()
                del widget_pack_dict['in']
                old_ipady = widget_pack_dict.get('ipady')
                new_ipady = old_ipady + dynamic_ipady
                widget_pack_dict.update({'ipady': new_ipady})
                widget_obj.pack(widget_pack_dict)

    def Leave_bind(self, event):
        """鼠标离开组件时触发."""
        widget_location = self.myframe.winfo_children().index(event.widget)
        widget_location_list = [i for i in range(widget_location-2, widget_location+3)]

        for i in widget_location_list:
            widget_index = widget_location_list.index(i)

            # 动态效果的 ipady 参数.
            dynamic_ipady = self.dynamic_args[widget_index]

            # 剔除小于0 和 大于最大索引位置的动态小部件索引位置
            if i >= 0 and i < len(self.myframe.winfo_children()):

                # 动态颜色
                widget_obj = self.myframe.winfo_children()[i]
                widget_obj.config({'background': '#d4e5ef'})

                # 动态大小
                widget_pack_dict = widget_obj.pack_info()
                del widget_pack_dict['in']
                old_ipady = widget_pack_dict.get('ipady')
                new_ipady = old_ipady - dynamic_ipady
                widget_pack_dict.update({'ipady': new_ipady})
                widget_obj.pack(widget_pack_dict)


    @classmethod
    def start_mainloop(cls):
        root = cls()
        root.mainloop()


if __name__ == '__main__':
    MyWindow.start_mainloop()
