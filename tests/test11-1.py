import customtkinter as ctk
import tkchart
import random

root=ctk.CTk()
root.geometry("1048x599+442+239")

root.configure(fg_color="#100e17")


chart = tkchart.LineChart(master=root,
                          bg_color="#100e17", chart_color="#100e17",
                          width=900, height=400,
                          x_data_min_max=(0,10), y_data_max=100,
                          x_sections_count=10, y_sections_count=10,
                          )
chart.pack(pady=100)

line = tkchart.Line(master=chart, size=3, mode='dash', mode_style=(10,10), color="lightblue",)
line2 = tkchart.Line(master=chart, size=3, mode='circle', mode_style=(10,10), color="lightgreen",)


data =  [x for  x in range(0,101)]
def loop():
    chart.show_data(line=line, data=[random.choice(data)])
    chart.show_data(line=line2, data=[random.choice(data)])
    root.after(500,loop)
loop()

root.mainloop()