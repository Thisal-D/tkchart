import customtkinter as ctk
import tkchart
import random

root=ctk.CTk()
root.geometry("1048x599+442+239")

root.configure(fg_color="#100e17")


chart = tkchart.LineChart(master=root,
                          bg_color="#100e17", fg_color="#100e17",
                          width=900, height=400,
                          x_axis_values=[x for x in range(1,11)], y_axis_max_value=100)
chart.pack(pady=100)

line = tkchart.Line(master=chart, size=2, style='line', color="lightblue")


data =  [x for  x in range(0,101)]
def loop():
    chart.show_data(line=line, data=[random.choice(data)])
    root.after(500,loop)
loop()

root.mainloop()