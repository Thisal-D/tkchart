import tkchart
import customtkinter as ctk
import random

root = ctk.CTk()

chart_1 = tkchart.LineChart(master=root 
                            ,width=1920 ,height=980 
                            ,chart_fg='#101010'
                            ,horizontal_bar_size=10 ,horizontal_bar_fg="#444444"
                            ,vertical_bar_size=10 ,vertical_bar_fg="#444444"
                            ,sections=True ,sections_fg="#444444" ,sections_count=50 
                            ,max_value=2000000 
                            ,values_labels=True ,values_labels_count=50
                            ,chart_line_len=100
                            ,text_color='#00ff00' ,font=('arial',10,'bold') 
                            ,left_space=10 ,right_space=10 ,bottom_space=40 ,top_space=40
                            ,x_space=00 ,y_space=10)
chart_1.pack()

line_1 = tkchart.Line(master=chart_1 ,height=4 ,color='#ffffff')

values = [x for x in range(2000000+1)]

def loop():
    chart_1.display(line=line_1 ,values=random.choices(values ,k=1))
    root.after(500,loop)
loop()

root.mainloop()
