import customtkinter as ctk

#import module 
import tkchart



#create root
root = ctk.CTk()
root.config(bg="#404040")
#create chart
chart_1 = tkchart.LineChart(master=root ,width = 1900 ,height = 900 ,sections = True ,sections_fg = "#909090"
                            ,chart_bg = "#101010" ,chart_fg = "#101010" 
                            ,horizontal_fg = "#404040" ,vertical_fg = "#404040" ,text_color = "#909090" 
                            ,values_display = True  ,chart_line_len = 100, max_value = 1000)


#place / grid / pack chart  ## same as tkinter place / grid / pack
#important place -> relwidth & relheight not supported in chart
chart_1.pack()
#cerate line for chart

line_1 = tkchart.Line(master=chart_1 ,height = 4 ,color='#909090')
line_2 = tkchart.Line(master=chart_1 ,height = 4 ,color='#ffffff')

# after creating line on chart , you can display values caling like this

values = [1000,800,500,300,900,200,100,500,400,0,700]
index = 0
def loop():
    global index
    chart_1.display(line=line_1 ,values=[values[index]])
    chart_1.display(line=line_2 ,values=[values[index]-200])
    index += 1
    if not(index < len(values)) :
        index = 0
    root.after(500 ,loop)
loop()



root.mainloop()