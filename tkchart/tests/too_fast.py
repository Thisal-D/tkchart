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

# after creating line on chart , you can display values caling like this
chart_1.display(line=line_1 ,values=[12321]) # values should be list


values = [1000,800,500,300,900,200,100,500,400,0,700]
index = 0
def loop():
    global index
    chart_1.display(line=line_1 ,values=[values[index]])
    index += 1
    if not(index < len(values)) :
        index = 0
    root.after(100 ,loop)
loop()



#create chart
chart_2 = tkchart.LineChart(master=root ,width = 500 ,height = 400 ,sections = True ,sections_fg = "#202020" ,chart_bg = "#000000" ,chart_fg = "#000000" ,horizontal_fg = "#101010" ,vertical_fg = "#101010" ,text_color = "#ffffff" ,values_display = True  ,chart_line_len = 50, max_value = 1000)


#place / grid / pack chart  ## same as tkinter place / grid / pack
#important place -> relwidth & relheight not supported in chart
chart_2.grid(row=1 ,column=2)
#cerate line for chart

line_2 = tkchart.Line(master=chart_1 ,height = 2 ,color='#ffffff')

# after creating line on chart , you can display values caling like this
chart_2.display(line=line_1 ,values=[12321]) # values should be list


values2 = [1000,800,500,300,900,200,100,500,400,0,700]
index2 = 0
def loop2():
    global index2
    chart_2.display(line=line_2 ,values=[values[index2]])
    index2 += 1
    if not(index2 < len(values2)) :
        index2 = 0
    root.after(50 ,loop2)
loop2()



#create chart
chart_3 = tkchart.LineChart(master=root ,width = 500 ,height = 400 ,sections = True ,sections_fg = "#202020" ,chart_bg = "#000000" ,chart_fg = "#000000" ,horizontal_fg = "#101010" ,vertical_fg = "#101010" ,text_color = "#ffffff" ,values_display = True  ,chart_line_len = 50, max_value = 1000)


#place / grid / pack chart  ## same as tkinter place / grid / pack
#important place -> relwidth & relheight not supported in chart
chart_3.grid(row=1 ,column=3)
#cerate line for chart

line_3 = tkchart.Line(master=chart_1 ,height = 2 ,color='#ffffff')

# after creating line on chart , you can display values caling like this
chart_3.display(line=line_1 ,values=[12321]) # values should be list


values3= [1000,800,500,300,900,200,100,500,400,0,700]
index3 = 0
def loop3():
    global index3
    chart_3.display(line=line_3 ,values=[values[index3]])
    index3 += 1
    if not(index3 < len(values3)) :
        index3 = 0
    root.after(10 ,loop3)
loop3()




root.mainloop()