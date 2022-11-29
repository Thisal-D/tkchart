# tkchart package 
<br>

## create line chart in tkinter & customtkinter windows

<br><br>

## package requirement :

> tkinter

> customtkinter

<br><br>





<br>






#  you can configure >>

 ## LineChart Object Configurations


> ``` master : master of chart ``` master = frame1 | master = root

> ```width :  width of chart ```width = 500

>```height : height of chart  ``` height = 500

>```sections : show sections of chart  ``` sections = True | sections = False

>```sections_fg : color of sections  ``` sections_fg = "red" | sections_fg = "#ff0000"

>```chart_bg : backgroud color of chart ``` chart_bg = "red" | chart_bg = "#ff0000"

>```chart_fg : foreground color of chart ``` chart_fg = "red" | chart_fg = "#ff0000"

>```horizontal_fg : horizontal bar color ``` horizontal_fg = "red" | horizontal_fg = "#ff0000"

>```vertical_fg : vertical bar color ``` vertical_fg = "red" | vertical_fg = "#ff0000"

>```text_color : colors of texts in chart ``` text_color = "red" | text_color = "#ff0000"

>```font : font configure in chart ``` font = ('arial',15,'bold')

>```values_display : show values of sections  ``` values_display = True | values_display = False

>```chart_line_len : length of char line``` chart_line_len = 10 

>```max_value : maximum display value```  max_value = 1800




<br>

 ## Line Object Configurations

>```height : height of chart  ``` height = 1 

>```color : color of line  ``` color = "#101010" | color= "black"



# create Chart 

```
#import module 

import tkchart
```


```
#create chart

chart_1 = tkchart.LineChart(master=root ,width = 500 ,height = 500 ,sections = True ,sections_fg = "#202020" ,chart_bg = "#000000" ,chart_fg = "#000000" ,horizontal_fg = "#101010" ,vertical_fg = "#101010" ,text_color = "#ffffff" ,values_display = True  ,chart_line_len = 50, max_value = 1800)
```

```
#place / grid / pack chart  ## same as tkinter place / grid / pack
#important place -> relwidth & relheight not supported in chart

chart_1.pack()
```

```
#create line for chart

line_1 = tkchart.Line(master=chart_1 ,height = 2 ,color='#ffffff')
```

```
# after creating line on chart , you can display values caling like this

chart_1.display(line=line_1 ,values=[12321]) # values should be list
```




## after create chart_1 you can change attributes of chart by configure like this
> chart_1.configure(width=1000 ,height=450 ,chart_bg="#101010" ,chart_fg="#101010".....)

## you can reset chart after display values 
> char_1.reset_all()

## after create line you can change attributes of line by configure like this

> line_1.configure(height=2 ,color=red)

<br>
<br>
<br>


## More Infomations :- <a href = "https://github.com/Thisal-D/tkchart"> https://github.com/Thisal-D/tkchart </a>


<br>
<br>
<br>
## This is a tkchart package. Thanks For Using..!👍👍👍👌