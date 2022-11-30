# tkchart

## Create line chart in tkinter & customtkinter windows

> Examples

>> ![12321313](https://user-images.githubusercontent.com/93121062/204732527-19a1dc1f-722d-4b38-9ce8-18dd8d74b917.png)

>> ![123](https://user-images.githubusercontent.com/93121062/204732876-1d3f7526-93ea-4e5e-905b-b768020fd572.png)

>> ![2022-11-30 12-48-43](https://user-images.githubusercontent.com/93121062/204732953-440646dd-2ef6-4fbb-9da3-640d72faa799.gif)


>> ![2022-11-30 12-23-55](https://user-images.githubusercontent.com/93121062/204729605-44027b37-c9f5-4588-a316-1205e5917ae2.gif)




> Code Example for create and display values on it

```
#IMPORT PACKAGES
import tkchart 
import customtkinter 
import random


root = customtkinter.CTk()
root.title("tkchart")
root.geometry("1920x1080")
root.config(bg="#101010")
root.attributes('-alpha',0.97)

#create chart
chart_1 = tkchart.LineChart(master=root ,width=700 ,height=400 ,chart_fg='#121212' 
                            ,chart_bg='#101010' ,sections=False ,values_display=True ,sections_fg="#606060"
                            ,text_color='#ffffff' ,font=('arial',9,'bold') ,vertical_fg="#606060" ,horizontal_fg="#606060" ,chart_line_len=60)
chart_1.place(relx=0.5 ,rely=0.5 ,anchor='center')

#configure max_values
chart_1.configure(max_value=1000)

#create line  1 for chart
line_1 = tkchart.Line(master=chart_1 ,color="gold" ,height=2)
#create line 2 for chart
line_2 = tkchart.Line(master=chart_1 ,color="#00ffff" ,height=2)

#values for disaply , #using ranfom display randomly selected values
values_ = [x for x in range(1001)]
#display values
def loop():
    #display values
    chart_1.display(line=line_1 ,values=[random.choice(values_)])
    chart_1.display(line=line_2 ,values=[random.choice(values_)])
    root.after(1000,loop)
loop()

root.mainloop()
```

> output

>> ![2022-11-30 12-28-43](https://user-images.githubusercontent.com/93121062/204730121-fa363a8a-a5b8-45ba-b9dd-d70c7beef5bb.gif)


# you can customsize lot of things 

```
with sections
```

>>> ![with secions](https://user-images.githubusercontent.com/93121062/204731328-20a46171-d9bf-4852-b85c-a304ee2644ee.png)
>>> ![Screenshot 2022-11-30 124058](https://user-images.githubusercontent.com/93121062/204731334-a402c5e9-fb59-41bd-a198-2436a3f730c7.png)
>>> ![Screenshot 2022-11-30 124217](https://user-images.githubusercontent.com/93121062/204731335-e61aabbb-6d5a-40b0-96e4-dc25dc6049e7.png)


```
without sections
```
>>> ![without secions](https://user-images.githubusercontent.com/93121062/204731386-54e9405a-8312-4a31-9baf-7ee3855ad41e.png)



# Examples
> 
>> ![2022-11-30 12-23-55](https://user-images.githubusercontent.com/93121062/204730316-6df6b3fb-ae19-4b30-854d-5f0834755d50.gif)
>> ![2022-11-30 12-28-43](https://user-images.githubusercontent.com/93121062/204730332-96c9f06e-43c1-4efe-8986-46abf9d43333.gif)
>> ![2022-11-30 12-26-33](https://user-images.githubusercontent.com/93121062/204730334-bb619042-6104-4c76-98b4-ceaf56f1402f.gif)
>>  ![2022-11-30 12-28-00](https://user-images.githubusercontent.com/93121062/204730337-2bf67d82-4b61-4084-8abe-5f76c228697e.gif)


