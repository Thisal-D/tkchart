import tkchart
try:
    import customtkinter as ctk
except :
    try:
        import os
        os.system("pip install customtkinter")
        os.system("pip install customtkinter --upgrade")
    except:
        pass
import random

root = ctk.CTk()
root.geometry("1900x900")


data = ([x for x in range(-1000,1001)])
x_axis_values =  tuple([x for x in range(1,31)])
line_chart = tkchart.LineChart(master=root, fg_color="#101010", bg_color="#101010",
                               x_axis_data='', y_axis_data="",
                               width=900, height=350,
                               axis_size=1, y_axis_precision=0,
                               x_axis_values=x_axis_values, y_axis_values=(-1000, 1001),
                               x_axis_label_count=20, y_axis_label_count=10,
                               x_axis_section_count=10, y_axis_section_count=10,
                               y_space=10, x_space=10, )
line_chart.pack()
line = tkchart.Line(master=line_chart, style="normal", style_type=(10,5), size=2, color="lightblue",
                    point_highlight="enabled", point_highlight_size=6, fill="enabled", fill_color="#707070",
                    point_highlight_color="lightblue")

def loop():
    line_chart.show_data(line=line ,data=[random.choice(data)])
    root.after(500, loop)
loop()




#line_chart.show_data(line=line ,data=[0,200,400,600,800,1000,800,600,400,200])
#line_chart.show_data(line=line ,data=[0,200,0,600,200,1000,400,600,1000,0])


frame = ctk.CTkScrollableFrame(master=root, width=1000, height=900, fg_color=("#FFFFFF","#151515"))
frame.pack(pady=100)

def line_chart_configure(**kwrgs):
    line_chart.configure(**kwrgs)

def line_configure(**kwrgs):
    line.configure(**kwrgs)


row = 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Line Chart Attributes : ", font=("Arial",25,"bold")).grid(row=row, column=1)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Width : ").grid(row=row, column=1)
column = 2
for width in range(900,1600,100):
    ctk.CTkButton(master=frame, text="{}".format(width), width=90, height=30, command=lambda width_=width: line_chart_configure(width=width_)).grid(row=row, column=column, padx=10, pady=2)
    column += 1

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Height : ").grid(row=row, column=1)
column = 2
for height in range(350,900,50):
    ctk.CTkButton(master=frame, text="{}".format(height), width=90, height=30, command=lambda height_=height: line_chart_configure(height=height_)).grid(row=row, column=column, padx=10, pady=2)
    column += 1

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Axis Size : ").grid(row=row, column=1)
column = 2
for axis_size in range(1,9,1):
    ctk.CTkButton(master=frame, text="{}".format(axis_size), width=90, height=30, command=lambda axis_size_=axis_size: line_chart_configure(axis_size=axis_size_)).grid(row=row, column=column, padx=10, pady=2)
    column += 1

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Y Axis Labels : ").grid(row=row, column=1)
column = 2
for y_axis_label_count in range(0,14,2):
    ctk.CTkButton(master=frame, text="{}".format(y_axis_label_count), width=90, height=30, command=lambda y_axis_label_count_=y_axis_label_count: line_chart_configure(y_axis_label_count=y_axis_label_count_)).grid(row=row, column=column, padx=10, pady=2)
    column += 1   
       
row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="X Axis Labels : ").grid(row=row, column=1)
column = 2
for x_axis_label_count in [0, 1, 2, 4, 5, 10, 20]:
    ctk.CTkButton(master=frame, text="{}".format(x_axis_label_count), width=90, height=30, command=lambda x_axis_label_count_=x_axis_label_count: line_chart_configure(x_axis_label_count=x_axis_label_count_)).grid(row=row, column=column, padx=10, pady=2)
    column += 1 
    
row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Y Axis Precision : ").grid(row=row, column=1)
column = 2
for y_axis_precision in range(0,9,1):
    ctk.CTkButton(master=frame, text="{}".format(y_axis_precision), width=90, height=30, command=lambda y_axis_precision_=y_axis_precision: line_chart_configure(y_axis_precision=y_axis_precision_)).grid(row=row, column=column, padx=10, pady=2)
    column += 1  
    
row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Y Axis values : ").grid(row=row, column=1)
column = 2
values = [(-1000, 1000), (0, 1000), (-2000, 1000), (0, 2000), (-5000,2000)]
for i in range(5):
    ctk.CTkButton(master=frame, text="{}".format(values[i]), width=90, height=30, command=lambda y_axis_values_=values[i]: line_chart_configure(y_axis_values=y_axis_values_)).grid(row=row, column=column, padx=10, pady=2)
    column += 1 
    
row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="X Axis Values : ").grid(row=row, column=1)
column = 2
for x_axis_values in range(1, 90, 10):
    ctk.CTkButton(master=frame, text="range({},{})".format(x_axis_values,x_axis_values+20), width=90, height=30, command=lambda x_axis_values_=[x for x in range(x_axis_values,x_axis_values+20)]: line_chart_configure(x_axis_values=tuple(x_axis_values_))).grid(row=row, column=column, padx=10, pady=2)
    column += 1 

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Y Axis Sections : ").grid(row=row, column=1)
column = 2
for y_axis_section_count in range(0, 14, 2):
    ctk.CTkButton(master=frame, text="{}".format(y_axis_section_count), width=90, height=30, command=lambda y_axis_section_count_=y_axis_section_count: line_chart_configure(y_axis_section_count=y_axis_section_count_)).grid(row=row, column=column, padx=10, pady=2)
    column += 1   

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="X Axis Sections : ").grid(row=row, column=1)
column = 2
for x_axis_section_count in range(0, 14, 2):
    ctk.CTkButton(master=frame, text="{}".format(x_axis_section_count), width=90, height=30, command=lambda x_axis_section_count_=x_axis_section_count: line_chart_configure(x_axis_section_count=x_axis_section_count_)).grid(row=row, column=column, padx=10, pady=2)
    column += 1   
    
row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="x xis point spacing : ").grid(row=row, column=1)
ctk.CTkButton(master=frame, text="{}".format("Auto"), width=90, height=30, command=lambda : line_chart_configure(x_axis_point_spacing="auto")).grid(row=row, column=2, padx=10, pady=2)
column = 3
for x_axis_point_spacing in range(10, 40, 5):
    ctk.CTkButton(master=frame, text="{}".format(x_axis_point_spacing), width=90, height=30, command=lambda x_axis_point_spacing_=x_axis_point_spacing: line_chart_configure(x_axis_point_spacing=x_axis_point_spacing_)).grid(row=row, column=column, padx=10, pady=2)
    column += 1

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Y Space : ").grid(row=row, column=1)
column = 2
for y_space in range(0, 90, 10):
    ctk.CTkButton(master=frame, text="{}".format(y_space), width=90, height=30, command=lambda y_space_=y_space: line_chart_configure(y_space=y_space_)).grid(row=row, column=column, padx=10, pady=2)
    column += 1

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="X Space : ").grid(row=row, column=1)
column = 2
for x_space in range(0, 90, 10):
    ctk.CTkButton(master=frame, text="{}".format(x_space), width=90, height=30, command=lambda x_space_=x_space: line_chart_configure(x_space=x_space_)).grid(row=row, column=column, padx=10, pady=2)
    column += 1  
    
row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Y Axis Data : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("Y"), width=90, height=30, command=lambda:line_chart_configure(y_axis_data="Y")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("Y-AXIS"), width=90, height=30, command=lambda:line_chart_configure(y_axis_data="Y-AXIS")).grid(row=row, column=column, padx=10, pady=2)

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="X Axis Data : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("X"), width=90, height=30, command=lambda:line_chart_configure(x_axis_data="X")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("X-AXIS"), width=90, height=30, command=lambda:line_chart_configure(x_axis_data="X-AXIS")).grid(row=row, column=column, padx=10, pady=2)

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="X Axis Data Position : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("top"), width=90, height=30, command=lambda:line_chart_configure(x_axis_data_position="top")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("side"), width=90, height=30, command=lambda:line_chart_configure(x_axis_data_position="side")).grid(row=row, column=column, padx=10, pady=2)

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Y Axis Data Position : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("top"), width=90, height=30, command=lambda:line_chart_configure(y_axis_data_position="top")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("side"), width=90, height=30, command=lambda:line_chart_configure(y_axis_data_position="side")).grid(row=row, column=column, padx=10, pady=2)

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Data Font Style : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("('arial',10,'normal')"), width=90, height=30, command=lambda:line_chart_configure(data_font_style=("arial",10,"normal"))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("('arial',10,'bold')"), width=90, height=30, command=lambda:line_chart_configure(data_font_style=("arial",10,"bold"))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("('arial',15,'normal')"), width=90, height=30, command=lambda:line_chart_configure(data_font_style=("arial",15,"normal"))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("('arial',15,'bold')"), width=90, height=30, command=lambda:line_chart_configure(data_font_style=("arial",15,"bold"))).grid(row=row, column=column, padx=10, pady=2)

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Axis Font Style : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("('arial',10,'normal')"), width=90, height=30, command=lambda:line_chart_configure(axis_font_style=("arial",10,"normal"))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("('arial',10,'bold')"), width=90, height=30, command=lambda:line_chart_configure(axis_font_style=("arial",10,"bold"))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("('arial',12,'normal')"), width=90, height=30, command=lambda:line_chart_configure(axis_font_style=("arial",12,"normal"))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("('arial',12,'bold')"), width=90, height=30, command=lambda:line_chart_configure(axis_font_style=("arial",12,"bold"))).grid(row=row, column=column, padx=10, pady=2)

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="X Section Color : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("#000000"), width=90, height=30, command=lambda:line_chart_configure(x_axis_section_color="#000000")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#303030"), width=90, height=30, command=lambda:line_chart_configure(x_axis_section_color="#303030")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#454545"), width=90, height=30, command=lambda:line_chart_configure(x_axis_section_color="#454545")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#606060"), width=90, height=30, command=lambda:line_chart_configure(x_axis_section_color="#606060")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#757575"), width=90, height=30, command=lambda:line_chart_configure(x_axis_section_color="#757575")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#909090"), width=90, height=30, command=lambda:line_chart_configure(x_axis_section_color="#909090")).grid(row=row, column=column, padx=10, pady=2)
column += 1


row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Y Section Color : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("#000000"), width=90, height=30, command=lambda:line_chart_configure(y_axis_section_color="#000000")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#303030"), width=90, height=30, command=lambda:line_chart_configure(y_axis_section_color="#303030")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#454545"), width=90, height=30, command=lambda:line_chart_configure(y_axis_section_color="#454545")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#606060"), width=90, height=30, command=lambda:line_chart_configure(y_axis_section_color="#606060")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#757575"), width=90, height=30, command=lambda:line_chart_configure(y_axis_section_color="#757575")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#909090"), width=90, height=30, command=lambda:line_chart_configure(y_axis_section_color="#909090")).grid(row=row, column=column, padx=10, pady=2)
column += 1


row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="X Axis Section Style : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("normal"), width=90, height=30, command=lambda:line_chart_configure(x_axis_section_style="normal")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("dashed"), width=90, height=30, command=lambda:line_chart_configure(x_axis_section_style="dashed")).grid(row=row, column=column, padx=10, pady=2)
column += 1

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="X Axis Style Type : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("(10, 5)"), width=90, height=30, command=lambda:line_chart_configure(x_axis_section_style_type=(10, 5))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("(20, 5)"), width=90, height=30, command=lambda:line_chart_configure(x_axis_section_style_type=(20, 5))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("(20, 10)"), width=90, height=30, command=lambda:line_chart_configure(x_axis_section_style_type=(10, 20))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("(20, 10)"), width=90, height=30, command=lambda:line_chart_configure(x_axis_section_style_type=(20, 10))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("(5, 5)"), width=90, height=30, command=lambda:line_chart_configure(x_axis_section_style_type=(5, 5))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("(20, 20)"), width=90, height=30, command=lambda:line_chart_configure(x_axis_section_style_type=(20, 20))).grid(row=row, column=column, padx=10, pady=2)
column += 1

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Y Axis Section Style : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("normal"), width=90, height=30, command=lambda:line_chart_configure(y_axis_section_style="normal")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("dashed"), width=90, height=30, command=lambda:line_chart_configure(y_axis_section_style="dashed")).grid(row=row, column=column, padx=10, pady=2)
column += 1

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Y Axis Style Type : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("(10, 5)"), width=90, height=30, command=lambda:line_chart_configure(y_axis_section_style_type=(10, 5))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("(20, 5)"), width=90, height=30, command=lambda:line_chart_configure(y_axis_section_style_type=(20, 5))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("(20, 10)"), width=90, height=30, command=lambda:line_chart_configure(y_axis_section_style_type=(10, 20))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("(20, 10)"), width=90, height=30, command=lambda:line_chart_configure(y_axis_section_style_type=(20, 10))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("(5, 5)"), width=90, height=30, command=lambda:line_chart_configure(y_axis_section_style_type=(5, 5))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("(20, 20)"), width=90, height=30, command=lambda:line_chart_configure(y_axis_section_style_type=(20, 20))).grid(row=row, column=column, padx=10, pady=2)
column += 1


row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Axis Color : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("#000000"), width=90, height=30, command=lambda:line_chart_configure(axis_color="#000000")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#151515"), width=90, height=30, command=lambda:line_chart_configure(axis_color="#151515")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#252525"), width=90, height=30, command=lambda:line_chart_configure(axis_color="#252525")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#505050"), width=90, height=30, command=lambda:line_chart_configure(axis_color="#505050")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#909090"), width=90, height=30, command=lambda:line_chart_configure(axis_color="#909090")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#FFFFFF"), width=90, height=30, command=lambda:line_chart_configure(axis_color="#FFFFFF")).grid(row=row, column=column, padx=10, pady=2)
column += 1

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="BG Color : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("#000000"), width=90, height=30, command=lambda:line_chart_configure(bg_color="#000000")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#151515"), width=90, height=30, command=lambda:line_chart_configure(bg_color="#151515")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#252525"), width=90, height=30, command=lambda:line_chart_configure(bg_color="#252525")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#505050"), width=90, height=30, command=lambda:line_chart_configure(bg_color="#505050")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#707070"), width=90, height=30, command=lambda:line_chart_configure(bg_color="#707070")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#FFFFFF"), width=90, height=30, command=lambda:line_chart_configure(bg_color="#FFFFFF")).grid(row=row, column=column, padx=10, pady=2)
column += 1

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="FG Color : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("#000000"), width=90, height=30, command=lambda:line_chart_configure(fg_color="#000000")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#151515"), width=90, height=30, command=lambda:line_chart_configure(fg_color="#151515")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#252525"), width=90, height=30, command=lambda:line_chart_configure(fg_color="#252525")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#505050"), width=90, height=30, command=lambda:line_chart_configure(fg_color="#505050")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#707070"), width=90, height=30, command=lambda:line_chart_configure(fg_color="#707070")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#FFFFFF"), width=90, height=30, command=lambda:line_chart_configure(fg_color="#FFFFFF")).grid(row=row, column=column, padx=10, pady=2)
column += 1

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Y Axis Font Color : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("#000000"), width=90, height=30, command=lambda:line_chart_configure(y_axis_font_color="#000000")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#151515"), width=90, height=30, command=lambda:line_chart_configure(y_axis_font_color="#151515")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#252525"), width=90, height=30, command=lambda:line_chart_configure(y_axis_font_color="#252525")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#505050"), width=90, height=30, command=lambda:line_chart_configure(y_axis_font_color="#505050")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#707070"), width=90, height=30, command=lambda:line_chart_configure(y_axis_font_color="#707070")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#FFFFFF"), width=90, height=30, command=lambda:line_chart_configure(y_axis_font_color="#FFFFFF")).grid(row=row, column=column, padx=10, pady=2)
column += 1

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="X Axis Font Color : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("#000000"), width=90, height=30, command=lambda:line_chart_configure(x_axis_font_color="#000000")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#151515"), width=90, height=30, command=lambda:line_chart_configure(x_axis_font_color="#151515")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#252525"), width=90, height=30, command=lambda:line_chart_configure(x_axis_label_count_axis_font_color="#252525")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#505050"), width=90, height=30, command=lambda:line_chart_configure(x_axis_font_color="#505050")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#707070"), width=90, height=30, command=lambda:line_chart_configure(x_axis_font_color="#707070")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#FFFFFF"), width=90, height=30, command=lambda:line_chart_configure(x_axis_font_color="#FFFFFF")).grid(row=row, column=column, padx=10, pady=2)
column += 1

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Y Axis Data Font Color : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("#000000"), width=90, height=30, command=lambda:line_chart_configure(y_axis_data_font_color="#000000")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#151515"), width=90, height=30, command=lambda:line_chart_configure(y_axis_data_font_color="#151515")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#252525"), width=90, height=30, command=lambda:line_chart_configure(y_axis_data_font_color="#252525")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#505050"), width=90, height=30, command=lambda:line_chart_configure(y_axis_data_font_color="#505050")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#707070"), width=90, height=30, command=lambda:line_chart_configure(y_axis_data_font_color="#707070")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#FFFFFF"), width=90, height=30, command=lambda:line_chart_configure(y_axis_data_font_color="#FFFFFF")).grid(row=row, column=column, padx=10, pady=2)
column += 1

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="X Axis Data Font Color : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("#000000"), width=90, height=30, command=lambda:line_chart_configure(x_axis_data_font_color="#000000")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#151515"), width=90, height=30, command=lambda:line_chart_configure(x_axis_data_font_color="#151515")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#252525"), width=90, height=30, command=lambda:line_chart_configure(x_axis_data_font_color="#252525")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#505050"), width=90, height=30, command=lambda:line_chart_configure(x_axis_data_font_color="#505050")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#707070"), width=90, height=30, command=lambda:line_chart_configure(x_axis_data_font_color="#707070")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#FFFFFF"), width=90, height=30, command=lambda:line_chart_configure(x_axis_data_font_color="#FFFFFF")).grid(row=row, column=column, padx=10, pady=2)
column += 1

row += 1
ctk.CTkFrame(master=frame ,height=10, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)

row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Line Attributes : ", font=("Arial",25,"bold")).grid(row=row, column=1)

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Size : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format(1), width=90, height=30, command=lambda:line_configure(size=1)).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format(2), width=90, height=30, command=lambda:line_configure(size=2)).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format(4), width=90, height=30, command=lambda:line_configure(size=4)).grid(row=row, column=column, padx=10, pady=2)

row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Style : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("line"), width=90, height=30, command=lambda:line_configure(style="normal")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("dashed"), width=90, height=30, command=lambda:line_configure(style="dashed")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("dotted"), width=90, height=30, command=lambda:line_configure(style="dotted")).grid(row=row, column=column, padx=10, pady=2)


row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Style Type : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("(5,10)"), width=90, height=30, command=lambda:line_configure(style_type=(5,10))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("(20,10)"), width=90, height=30, command=lambda:line_configure(style_type=(20,10))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("(10,5)"), width=90, height=30, command=lambda:line_configure(style_type=(10,5))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("(10,30)"), width=90, height=30, command=lambda:line_configure(style_type=(10,30))).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("(1,1)"), width=90, height=30, command=lambda:line_configure(style_type=(1,1))).grid(row=row, column=column, padx=10, pady=2)



row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Color : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("#FF0000"), width=90, height=30, command=lambda:line_configure(color="#FF0000")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("00FF00"), width=90, height=30, command=lambda:line_configure(color="#00FF00")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#0000FF"), width=90, height=30, command=lambda:line_configure(color="#0000FF")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#FF00FF"), width=90, height=30, command=lambda:line_configure(color="#FF00FF")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#00FFFF"), width=90, height=30, command=lambda:line_configure(color="#00FFFF")).grid(row=row, column=column, padx=10, pady=2)



row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Point Hightlight : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("enabled"), width=90, height=30, command=lambda:line_configure(point_highlight="enabled")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("disabled"), width=90, height=30, command=lambda:line_configure(point_highlight="disabled")).grid(row=row, column=column, padx=10, pady=2)
column += 1



row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Point Hightlight Size : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("5"), width=90, height=30, command=lambda:line_configure(point_highlight_size=5)).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("10"), width=90, height=30, command=lambda:line_configure(point_highlight_size=10)).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("15"), width=90, height=30, command=lambda:line_configure(point_highlight_size=15)).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("20"), width=90, height=30, command=lambda:line_configure(point_highlight_size=20)).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("25"), width=90, height=30, command=lambda:line_configure(point_highlight_size=25)).grid(row=row, column=column, padx=10, pady=2)



row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Point Hightlight Color : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("#FF0000"), width=90, height=30, command=lambda:line_configure(point_highlight_color="#FF0000")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("00FF00"), width=90, height=30, command=lambda:line_configure(point_highlight_color="#00FF00")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#0000FF"), width=90, height=30, command=lambda:line_configure(point_highlight_color="#0000FF")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#FF00FF"), width=90, height=30, command=lambda:line_configure(point_highlight_color="#FF00FF")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#00FFFF"), width=90, height=30, command=lambda:line_configure(point_highlight_color="#00FFFF")).grid(row=row, column=column, padx=10, pady=2)




row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Fill : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("enabled"), width=90, height=30, command=lambda:line_configure(fill="enabled")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("disabled"), width=90, height=30, command=lambda:line_configure(fill="disabled")).grid(row=row, column=column, padx=10, pady=2)
column += 1



row += 1
ctk.CTkFrame(master=frame ,height=2, width=1000, fg_color=("#EEEEEE", "#202020")).grid(row=row, columnspan=9)
row += 1
ctk.CTkLabel(text_color=("black", "white"), master=frame, text="Point Hightlight Color : ").grid(row=row, column=1)
column = 2
ctk.CTkButton(master=frame, text="{}".format("#FF0000"), width=90, height=30, command=lambda:line_configure(fill_color="#FF0000")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("00FF00"), width=90, height=30, command=lambda:line_configure(fill_color="#00FF00")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#0000FF"), width=90, height=30, command=lambda:line_configure(fill_color="#0000FF")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#FF00FF"), width=90, height=30, command=lambda:line_configure(fill_color="#FF00FF")).grid(row=row, column=column, padx=10, pady=2)
column += 1
ctk.CTkButton(master=frame, text="{}".format("#00FFFF"), width=90, height=30, command=lambda:line_configure(fill_color="#00FFFF")).grid(row=row, column=column, padx=10, pady=2)


root.mainloop()