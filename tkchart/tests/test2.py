import customtkinter as ctk

#import module 
import tkchart



#create root
root = ctk.CTk()

#create chart
chart_1 = tkchart.LineChart(master=root ,width = 500 ,height = 400 ,sections = True ,sections_fg = "#202020" ,chart_bg = "#000000" ,chart_fg = "#000000" ,horizontal_fg = "#101010" ,vertical_fg = "#101010" ,text_color = "#ffffff" ,values_display = True  ,chart_line_len = 50, max_value = 1000)


#place / grid / pack chart  ## same as tkinter place / grid / pack
#important place -> relwidth & relheight not supported in chart
chart_1.grid(row=1 ,column=1)
#cerate line for chart

line_1 = tkchart.Line(master=chart_1 ,height = 2 ,color='#ffffff')




values = [900,800,500,300,900,200,100,500,400,0,700]
index = 0
def loop():
    global index
    chart_1.display(line=line_1 ,values=[values[index]])
    index += 1
    if index < len(values) :
        pass
    else:
        chart_1.reset_all()
        index = 0
    root.after(500 ,loop)
loop()

root.mainloop()