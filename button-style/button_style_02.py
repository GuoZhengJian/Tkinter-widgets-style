# -*- coding: utf-8 -*-


import tkinter as tk


class MyWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-topmost', True)
        self.config({'background': '#000000'})
        self.geometry('1886x168+9+16')
        self.update()
        
        # 实例按钮风格
        self.button_style()
        
    def button_style(self):
        """按钮风格.
        
        使用label小部件来模拟按钮, 可以实现更丰富的效果.
        """
        self.myframe = tk.Frame(self)
        self.myframe.config({'background': '#000000'})
        self.myframe.place(relx=0.12, rely=0.15, height=100)
        
        for i in range(1, 6):
            mybutton = tk.Label(self.myframe, text="PAGE %s"%i)            
            mybutton.config({'width': 20,
                             'height': 1,
                             'borderwidth': 0,
                             'background': '#2f3542',
                             'foreground': '#FFFFFF',
                             'activebackground': '#e67e22',
                             'font': '-family {@Malgun Gothic} -size 15 -weight bold',
                             'cursor': 'hand2',
                             })
            mybutton.pack(side='left', anchor='center', expand=False, pady=0, padx=20, ipady=10, ipadx=0)

            # bind事件
            mybutton.bind('<Enter>', self.Enter_bind, add='+')         # 鼠标或按键飘过时的样式;
            mybutton.bind('<Leave>', self.Leave_bind, add='+')         # 鼠标或按键飘过时的样式;
            mybutton.bind('<Button-1>', self.Button_1_bind, add='+')   # 鼠标或按键按下和释放时的样式;
            mybutton.bind('<Double-Button-1>', self.Double_Button_1_bind, add='+')   # 鼠标双击时的样式;
            mybutton.bind('<FocusIn>', self.FocusIn_bind, add='+')     # 组件获得和失去焦点时的样式;
            mybutton.bind('<FocusOut>', self.FocusOut_bind, add='+')   # 组件获得和失去焦点时的样式;


    def Enter_bind(self, event):
        """鼠标进入组件时触发."""
        event.widget.config({'background': '#57606f',
                             'foreground': '#FFFFFF',
                             })
  
    def Leave_bind(self, event):
        """鼠标离开组件时触发."""
        event.widget.config({'background': '#2f3542',
                             'foreground': '#FFFFFF',
                             })
        
    def Button_1_bind(self, event):
        """鼠标按下时触发."""
        event.widget.focus_set()
        
    def Double_Button_1_bind(self, event):
        """鼠标双击时的事件."""
        pass

    def FocusIn_bind(self, event):
        """组件获得焦点时触发."""
        event.widget.config({'state': 'active'})
        event.widget.config({'background': '#d35400',
                             'foreground': '#000000',
                             })

    def FocusOut_bind(self, event):
        """组件失去焦点时触发."""
        event.widget.config({'state': 'normal'})
        event.widget.config({'background': '#2f3542',
                             'foreground': '#FFFFFF',
                             })

    
    @classmethod
    def start_mainloop(cls):
        root = cls()
        root.mainloop()
        
        
if __name__ == '__main__':
    MyWindow.start_mainloop()