import tkchart
import customtkinter
import random
import threading
import time

root = customtkinter.CTk()
root.geometry("1280x720")

# values for chart x axis
x_axis_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#create line chart
linechart = tkchart.LineChart(master=root,
                              y_axis_max_value=1000,
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
                              
                              section_color="#404040",
                              
                              data_font_style=("arial","20","bold"),
                              axis_font_style=("arial","11","bold"),
                              
                              x_axis_section_count=10,
                              y_axis_section_count=10,
                              x_axis_label_count=5,
                              y_axis_label_count=15,
                              
                              y_axis_precision=3,
                              
                              y_space=20,
                              x_space=20,
                              
                              x_axis_data_position="side",
                              y_axis_data_position="side"
                             )
#place line chart
linechart.place(x=50, y=50)

#create line 
line1 = tkchart.Line(master=linechart, size=2, color="lightblue")
line2 = tkchart.Line(master=linechart, size=2, color="lightgreen" ,style="dashed", style_type=(5,7))

line3 = tkchart.Line(master=linechart, size=2, color="pink" ,style="dotted", style_type=(4,7))
#display data
data = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]



count = 0

def display_data():
    while True:
        global x_axis_values  , count
       
        #displaying data
        linechart.show_data(line=line1, data=random.choices(data,k=1))
        linechart.show_data(line=line2, data=random.choices(data,k=1))
        linechart.show_data(line=line3, data=random.choices(data,k=1))
        if count > len(x_axis_values):
            x_axis_values = [(x+1) for x in x_axis_values]
        linechart.configure(x_axis_values=x_axis_values)
        count += 1
        
        time.sleep(0.5)

threading.Thread(target=display_data).start()

root.mainloop()