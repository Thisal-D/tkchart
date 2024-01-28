import tkchart
import customtkinter


root = customtkinter.CTk()
root.geometry("1048x599+442+239")

linechart = tkchart.LineChart(master=root,
                            width=800, 
                            height=400,
                            bar_size=5,
                            
                            
                            y_sections_count=5,
                            x_sections_count=5,
                            y_labels_count=5,
                            x_labels_count=5,
                            
                            y_data="GB",
                            x_data="S",
                            x_data_min_max=(20,60),
                            y_data_max=1000,
                            x_values_decimals=4,
                            y_values_decimals=5,
                            
                            sections_color="#404040",
                            y_values_color="#707070",
                            x_values_color="#707070",
                            x_data_color="lightblue",
                            y_data_color="lightblue",
                            bg_color="#202020",
                            chart_color="#202020",
                            bar_color="#707070",
                            
                            x_y_data_font = ("Arial", 15,"bold"),
                            x_y_values_font = ("Arial", 10,"bold")
                            )


linechart.pack(pady=100)


line = tkchart.Line(master=linechart,
                color="lightblue",
                size=2,
                mode="dash",
                mode_style=(4,10))


import random
data = [0,100,200,300,400,500,600,700,800,900,1000]
def loop():
    linechart.show_data(data=[random.choice(data)], line=line)
    root.after(250,loop)
#calling to loop
loop()
root.mainloop()