import tkchart
import customtkinter
import random
import threading
import time

root = customtkinter.CTk()
root.geometry("1280x720")

# values for chart x axis
x_axis_values = ('2020 Year', '2021 Year', '2022 Year', '2023 Year', '2024 Year')
#create line chart
linechart = tkchart.LineChart(master=root,
                              y_axis_values=(0 ,1000),
                              x_axis_values=x_axis_values,
                              
                              width=1000, height=500,
                              axis_size=5,
                          
                              
                              bg_color="#202020",
                              fg_color="#202020",

                              axis_color="#707070",
                    
                              x_axis_data_font_color="lightblue",
                              y_axis_data_font_color="lightblue",
                              
                              x_axis_font_color="#707070",
                              y_axis_font_color="#707070",
                              
                              x_axis_section_color="#404040",
                              y_axis_section_color="#404040",
                              
                              data_font_style=("arial","20","bold"),
                              axis_font_style=("arial","11","bold"),
                              
                              x_axis_section_count=10,
                              y_axis_section_count=10,
                              
                              y_axis_label_count=15,
                             )
#place line chart
linechart.place(x=50, y=50)

#create line 
line = tkchart.Line(master=linechart, size=2, color="lightblue")

#display data
data = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]



def display_data():
    while True:
        #displaying data
        linechart.show_data(line=line, data=random.choices(data,k=1))
        time.sleep(0.5)

threading.Thread(target=display_data).start()

root.mainloop()