# tkchart package 
<br>

## create line chart in tkinter & customtkinter windows

<br><br>

## package requirement :

> tkinter

> customtkinter



## You must install these packages before using this
>tkinter - pip install tk

>customtkinter - pip install customtkinter

<br>

#  you can configure >>

>attributes
![Sample image](https://user-images.githubusercontent.com/93121062/205255031-aefc7522-a8ba-44ee-b594-c5d2d7132c93.png?raw=True)


 ## LineChart Object Configurations


> ``` master : master of chart ``` master = frame1 | master = root

> ```width :  width of chart ```width = 500

>```height : height of chart  ``` height = 500

>```sections : show sections of chart  ``` sections = True | sections = False

>```sections_fg : color of sections  ``` sections_fg = "red" | sections_fg = "#ff0000"

>```sections_count : no of sections  ``` sections_count = 10

>```chart_bg : backgroud color of chart ``` chart_bg = "red" | chart_bg = "#ff0000"

>```chart_fg : foreground color of chart ``` chart_fg = "red" | chart_fg = "#ff0000"

>```horizontal_bar_fg : horizontal bar color ``` horizontal_bar_fg = "red" | horizontal_bar_fg = "#ff0000"

>```horizontal_bar_size : horizontal bar size ``` horizontal_bar_size = 10

>```vertical_bar_fg : vertical bar color ``` vertical_bar_fg = "red" | vertical_bar_fg = "#ff0000"

>```vertical_bar_size : verticak bar size ``` verticak_bar_size = 10

>```text_color : colors of texts in chart ``` text_color = "red" | text_color = "#ff0000"

>```font : font configure in chart ``` font = ('arial',15,'bold')

>```values_labels : show values of labels  ``` values_labels = True | values_labels = False

>```values_labels_count : no. of labels  ``` values_labels_count = 10

>```chart_line_len : length of chart line``` chart_line_len = 10 

>```max_value : maximum display value```  max_value = 1800

>configure spaces  \
>```top_space : ```  top_space = 20 \
>```bottom_space : ```  bottom_space = 20\
>```right_space : ```  right_space = 20\
>```right_space : ```  right_space = 20\
>```x_space : ```  x_space = 100\
>```y_space : ```  y_space = 100





<br>

 ## Line Object Configurations

>```height : height of chart  ``` height = 1 

>```color : color of line  ``` color = "#101010" | color= "black"



# create Chart 

```
#import module 

import tkchart

import customtkinter
```

```
#create root

root = customtkinter.TCk()
```

```
#create chart

chart_1 = tkchart.LineChart(master=root 
                            ,width=1280 ,height=720 
                            ,chart_fg='#050505'
                            ,horizontal_bar_size=15
                            ,vertical_bar_size=15 
                            ,sections=True ,sections_fg="#202020" ,sections_count=5 
                            ,max_value=100
                            ,values_labels=True ,values_labels_count=10
                            ,chart_line_len=80
                            ,text_color='#808080' ,font=('arial',10,'bold') 
                            ,left_space=100 ,right_space=100 ,bottom_space=40 ,top_space=40
                            ,x_space=100 ,y_space=100)

```

```
#place / grid / pack chart  ## same as tkinter place / grid / pack
#important place -> relwidth & relheight not supported in chart

chart_1.pack()
```

```
#create line for chart

line_1 = tkchart.Line(master=chart_1 ,height=4 ,color='#909090')
```

```
# after creating line on chart , you can display values caling like this

chart_1.display(line=line_1 ,values=[100,50,90,10,100,90,75,10,70,1,100,90,75,10,700])
```

```
root.mainloop()
```




## after create chart_1 you can change attributes of chart by configure like this
> chart_1.configure(width=1000 ,height=450 ,chart_bg="#101010" ,chart_fg="#101010".....)

## you can reset chart after display values 
> char_1.reset()

## after create line you can change attributes of line by configure like this

> line_1.configure(height=2 ,color=red)

<br>
<br>
<br>


## More Infomations :- <a href = "https://github.com/Thisal-D/tkchart"> https://github.com/Thisal-D/tkchart </a>


<br>
<br>
<br>
## This is a tkchart package. Thanks For Using..!👌