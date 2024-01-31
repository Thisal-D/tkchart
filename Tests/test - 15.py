import customtkinter 
import tkchart



root = customtkinter.CTk()

linechart = tkchart.LineChart(master=root,
                            width=800, 
                            height=400,
                            axis_size=5,
                            
                            y_axis_section_count=5,
                            x_axis_section_count=5,
                            y_axis_label_count=5,
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            x_axis_values=[1,2,3,4,5,6,7,8,9,10],
                            y_axis_max_value=1000,
                            y_axis_precision=5,
                            
                            section_color="#404040",
                            x_axis_font_color="#707070",
                            y_axis_font_color="#707070",
                            x_axis_data_font_color="lightblue",
                            y_axis_data_font_color="lightblue",
                            bg_color="#202020",
                            fg_color="#202020",
                            axis_color="#707070",
                            
                            data_font_style=("Arial", 15,"bold"),
                            axis_font_style=("Arial", 10,"bold"),
                            
                            x_space=20,
                            y_space=20,
                            
                            x_axis_data_position="side",
                            y_axis_data_position="size"
                        )

linechart.pack()


line = tkchart.Line(master=linechart,
                color="lightblue",
                size=2,
                style="dashed",
                style_type=(4,10))

import random
data = [0,100,200,300,400,500,600,700,800,900,1000]
def loop():
    linechart.show_data(data=[random.choice(data)], line=line)
    root.after(250,loop)
loop()

root.mainloop()