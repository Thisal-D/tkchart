import tkchart
import customtkinter as ctk
import random

root = ctk.CTk()

chart_1 = tkchart.LineChart(master=root 
                            ,width=1280 ,height=720 
                            ,chart_fg='#050505'
                            ,horizontal_bar_size=15
                            ,vertical_bar_size=15 
                            ,sections=True ,sections_fg="#202020" ,sections_count=5 
                            ,max_value=150
                            ,values_labels=True ,values_labels_count=10
                            ,chart_line_len=80
                            ,text_color='#808080' ,font=('arial',10,'bold') 
                            ,left_space=100 ,right_space=100 ,bottom_space=40 ,top_space=40
                            ,x_space=100 ,y_space=100)
chart_1.pack()

line_1 = tkchart.Line(master=chart_1 ,height=4 ,color='#909090')

values = [x for x in range(121)]

def loop():
    chart_1.display(line=line_1 ,values=random.choices(values ,k=1))
    root.after(100,loop)
loop()

root.mainloop()
