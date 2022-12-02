# tkchart

### Create charts in tkinter & customtkinter windows!

<hr>


## Attrubutes of tkchart
![Screenshot (46)](https://user-images.githubusercontent.com/93121062/205255031-aefc7522-a8ba-44ee-b594-c5d2d7132c93.png)


> Examples
![Screenshot 2022-12-02 142902](https://user-images.githubusercontent.com/93121062/205255962-8904f155-5254-4b21-b0d1-9350bc14fd73.png)



>> ![123](https://user-images.githubusercontent.com/93121062/204732876-1d3f7526-93ea-4e5e-905b-b768020fd572.png)

>> ![2022-11-30 12-48-43](https://user-images.githubusercontent.com/93121062/204732953-440646dd-2ef6-4fbb-9da3-640d72faa799.gif)


>> ![2022-11-30 12-23-55](https://user-images.githubusercontent.com/93121062/204729605-44027b37-c9f5-4588-a316-1205e5917ae2.gif)




> Code Example for create and display values on it

```
#import packages
import tkchart
import customtkinter as ctk
import random

#create root 
root = ctk.CTk()

#create line chart
chart_1 = tkchart.LineChart(master=root 
                            ,width=1280 ,height=720 
                            ,chart_fg='#101010'
                            ,horizontal_bar_size=10 ,horizontal_bar_fg="#444444"
                            ,vertical_bar_size=10 ,vertical_bar_fg="#444444"
                            ,sections=True ,sections_fg="#444444" ,sections_count=10 
                            ,max_value=2000000 
                            ,values_labels=True ,values_labels_count=10
                            ,chart_line_len=100
                            ,text_color='#00ff00' ,font=('arial',10,'bold') 
                            ,left_space=10 ,right_space=10 ,bottom_space=40 ,top_space=40
                            ,x_space=00 ,y_space=10)
chart_1.pack()

#create line for line chart
line_1 = tkchart.Line(master=chart_1 ,height=4 ,color='#ffffff')

#display values using loop
values = [x for x in range(2000000+1)]
def loop():
    chart_1.display(line=line_1 ,values=random.choices(values ,k=1))
    root.after(500,loop)
loop()

root.mainloop()
```

> output

>> ![Screenshot_20221202_022900](https://user-images.githubusercontent.com/93121062/205256131-3c806073-225b-4c4a-971d-35b86fc26a29.png)


# pypi for more infomation -> <a href="https://pypi.org/project/tkchart/"> https://pypi.org/project/tkchart </a>

# instal package ->  pip install tkchart
