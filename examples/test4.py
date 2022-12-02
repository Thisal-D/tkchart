import tkchart
import customtkinter as ctk
import random

root = ctk.CTk()

chart_1 = tkchart.LineChart(master=root 
                            ,width=600 ,height=400 
                            ,chart_fg='#101010'
                            ,horizontal_bar_size=10 ,horizontal_bar_fg="#444444"
                            ,vertical_bar_size=10 ,vertical_bar_fg="#444444"
                            ,sections=True ,sections_fg="#444444" ,sections_count=5 
                            ,max_value=2000000
                            ,values_labels=True ,values_labels_count=10
                            ,chart_line_len=80
                            ,text_color='#444444' ,font=('arial',10,'bold') 
                            ,left_space=10 ,right_space=10 ,bottom_space=40 ,top_space=40
                            ,x_space=00 ,y_space=10)
chart_1.pack()

line_1 = tkchart.Line(master=chart_1 ,height=3 ,color='#ffffff')

values = [x for x in range(2000000+1)]

def loop():
    chart_1.display(line=line_1 ,values=random.choices(values ,k=1))
    root.after(100,loop)
loop()

root.mainloop()
