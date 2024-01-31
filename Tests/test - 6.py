import customtkinter as ctk
import tkchart
import random

root=ctk.CTk()
root.geometry("1048x599+442+239")

root.configure(fg_color="#ffffff")


chart = tkchart.LineChart(master=root,
                          axis_color="#202020", x_axis_font_color="#202020", y_axis_font_color="#202020",
                          bg_color="#ffffff", fg_color="#ffffff",
                          width=900, height=400,
                          x_axis_values=[x for x in range(1,10)], y_axis_max_value=100,
                          x_axis_section_count=10, y_axis_section_count=10,
                          )
chart.pack(pady=100)

line = tkchart.Line(master=chart, size=3, style='dashed', style_type=(10,10), color="lightblue",)
line2 = tkchart.Line(master=chart, size=3, style='dotted', style_type=(10,10), color="lightgreen",)


data =  [x for  x in range(0,101)]
def loop():
    chart.show_data(line=line, data=[random.choice(data)])
    chart.show_data(line=line2, data=[random.choice(data)])
    root.after(500,loop)
loop()

root.mainloop()