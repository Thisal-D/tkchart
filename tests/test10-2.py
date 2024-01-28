import customtkinter as ctk
import tkchart
import random

root=ctk.CTk()
root.geometry("1048x599+442+239")

root.configure(fg_color="#ffffff")


chart = tkchart.LineChart(master=root,
                          bar_color="#202020", x_values_color="#202020", y_values_color="#202020",
                          bg_color="#ffffff", chart_color="#ffffff",
                          width=900, height=400,
                          x_data_min_max=(0,10), y_data_max=100)
chart.pack(pady=100)

line = tkchart.Line(master=chart, size=2, mode='dash', mode_style=(5,10), color="blue",)


data =  [x for  x in range(0,101)]
def loop():
    chart.show_data(line=line, data=[random.choice(data)])
    root.after(500,loop)
loop()

root.mainloop()