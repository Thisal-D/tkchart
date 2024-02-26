import tkchart
import customtkinter
import random

root = customtkinter.CTk()

root.geometry("1048x599+442+239")


def func(*args):
    label.configure(text=args[0])
    label2.configure(text=args[1])
    label3.configure(text=args[2])
    label4.configure(text=args[3])

    
linechart = tkchart.LineChart(master=root,
                            width=1500, 
                            height=700,
                            axis_size=5,
                             
                            y_axis_section_count=10,
                            x_axis_section_count=0,
                            y_axis_label_count=10,
                            
                            y_axis_data="GB",
                            x_axis_data="S",
                            x_axis_values=[x for x in range(1,11,1)],
                            x_axis_label_count=10,
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
                            axis_font_style= ("Arial", 10,"bold"),
                            
                            pointing_callback_function = func,
                            pointer_color="#00ffff",
                            pointer_state="enabled",
                            pointing_values_precision=4
                            )

linechart.place(x=100, y=10)


line = tkchart.Line(master=linechart,
                color="#ff0000",
                size=1,
                style="line",
                style_type=(4,10),
                )

line2 = tkchart.Line(master=linechart,
                color="#00ff00",
                size=1,
                style="line",
                style_type=(4,10))

line3 = tkchart.Line(master=linechart,
                color="#0000ff",
                size=1,
                style="line",
                style_type=(4,10))

line4 = tkchart.Line(master=linechart,
                color="#ffff00",
                size=1,
                style="line",
                style_type=(4,10))

frame = customtkinter.CTkFrame(master=root, width=30, height=30, fg_color="#ff0000")
frame.place(x=1650, y=300)
label = customtkinter.CTkLabel(master=root, font=("arial",13, "bold"), text="")
label.place(x=1700, y=300)

frame2 = customtkinter.CTkFrame(master=root, width=30, height=30, fg_color="#00ff00")
frame2.place(x=1650, y=350)
label2 = customtkinter.CTkLabel(master=root, font=("arial",13, "bold"), text="")
label2.place(x=1700, y=350)

frame3 = customtkinter.CTkFrame(master=root, width=30, height=30, fg_color="#0000ff")
frame3.place(x=1650, y=400)
label3 = customtkinter.CTkLabel(master=root, font=("arial",13, "bold"), text="")
label3.place(x=1700, y=400)

frame4 = customtkinter.CTkFrame(master=root, width=30, height=30, fg_color="#ffff00")
frame4.place(x=1650, y=450)
label4 = customtkinter.CTkLabel(master=root, font=("arial",13, "bold"), text="")
label4.place(x=1700, y=450)


data = [0,100,200,300,400,500,600,700,800,900,1000]
def loop2():
    if start:
        linechart.show_data(data=[random.choice(data)], line=line)
        linechart.show_data(data=[random.choice(data)], line=line2)
        linechart.show_data(data=[random.choice(data)], line=line3)
        linechart.show_data(data=[random.choice(data)], line=line4)
    root.after(1000,loop2)

start = True
def stop_start():
    global start
    if start:
        start= False
    else:
        start= True
#calling to loop
btn = customtkinter.CTkButton(master=root, text="Stop/Start", command=stop_start)
btn.place(x=1700,y=600)

loop2()
root.mainloop()