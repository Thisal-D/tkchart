import tkchart as tkc

import customtkinter as ctk



root = ctk.CTk()

chart = tkc.LineChart(master=root, y_axis_max_value=1000, x_axis_values=[x for x in range(1,11)],
                      width=1481, height=754.5, x_axis_section_count=0,
                      y_axis_label_count=10, y_axis_section_count=10 ,x_axis_data="S",y_axis_data="GB")
chart.place(x=10, y=10)


line = tkc.Line(master=chart, color="red",  style="dotted", style_type=(10,10))
line2 = tkc.Line(master=chart, color="#ffffff", size=4, style="line")
line3 = tkc.Line(master=chart, color="green", size=4, style="dashed", style_type=(10,10))

import random
data = [x for x in range(0,1001,1)]
def loop():
    random.choice(data)
    chart.show_data(line=line2, data =[random.choice(data)])
    chart.show_data(line=line, data = [random.choice(data)])
    chart.show_data(line=line3, data = [random.choice(data)])
    root.after(500,loop)

loop()
root.mainloop()