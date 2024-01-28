import tkchart as tkc

import customtkinter as ctk



root = ctk.CTk()

chart = tkc.LineChart(master=root, y_data_max=1000, x_data_min_max=(0,-10), width=1481, height=754.5, x_sections_count=0, x_labels_count=0, y_labels_count=0, y_sections_count=00 ,x_data="S",y_data="GB")
chart.place(x=10, y=10)


line = tkc.Line(master=chart, color="red",  mode="circle", mode_style=(10,10))
line2 = tkc.Line(master=chart, color="#ffffff", size=4, mode="line")
line3 = tkc.Line(master=chart, color="green", size=4, mode="dash", mode_style=(10,10))

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