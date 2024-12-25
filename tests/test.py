import tkchart
import customtkinter


root = customtkinter.CTk()
linechart = tkchart.LineChart(master=root,
                            width=1000, 
                            height=600,
                            bar_size=5
                            )
linechart.pack(pady=200)

root.mainloop()