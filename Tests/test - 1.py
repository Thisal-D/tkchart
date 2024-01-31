import tkchart
import customtkinter


root = customtkinter.CTk()
root.geometry("1048x599+442+239")

linechart = tkchart.LineChart(master=root,
                            width=800, 
                            height=400,
                            axis_size=5,
                             
                            y_axis_section_count=10,
                            x_axis_section_count=10,
                            y_axis_label_count=10,
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            x_axis_values=[x for x in range(2,60,2)],
                            y_axis_max_value=1000,
                            y_axis_precision=4,
                          
                            section_color="#404040",
                            y_axis_font_color="#707070",
                            x_axis_font_color="#707070",
                            x_axis_data_font_color="lightblue",
                            y_axis_data_font_color="lightblue",
                            bg_color="#202020",
                            fg_color="#202020",
                            axis_color="#707070",
                            
                            data_font_style= ("Arial", 15,"bold"),
                            axis_font_style= ("Arial", 10,"bold")
                            )


linechart.pack(pady=100)

line = tkchart.Line(master=linechart,
                color="lightblue",
                size=2,
                style="dashed",
                style_type=(4,10))

line2 = tkchart.Line(master=linechart,
                color="red",
                size=2,
                style="line",
                )

line3 = tkchart.Line(master=linechart,
                color="blue",
                size=4,
                style="dotted",
                style_type=(4,10))

import random
data = [0,100,200,300,400,500,600,700,800,900,1000]
def loop():
 
    linechart.show_data(data=[random.choice(data)], line=line3)
    linechart.show_data(data=[random.choice(data)], line=line2)
    linechart.show_data(data=[random.choice(data)], line=line)
    root.after(1000,loop)
#calling to loop
loop()
root.mainloop()