import customtkinter as ctk
import tkinter as tk
from .RequredGeometry import RequredWidth

class LineChart():
   def __init__(self ,*args ,master=None ,width=600 ,height=300 
                ,sections=None ,sections_count=10 ,sections_fg="#303030"
                ,chart_bg = '#101010' ,chart_fg = '#202020' 
                ,horizontal_bar_fg = "#404040" ,horizontal_bar_size=2 ,vertical_bar_fg = "#404040" ,vertical_bar_size=2
                ,text_color = "#ffffff" ,font=None ,values_labels=False ,values_labels_count=10 ,max_value=1000 
                ,chart_line_len = 30 
                ,top_space=10 ,bottom_space=10 ,left_space=10 ,right_space=10 ,x_space=40 ,y_space=40
                ,line_highlight=False ,line_highlight_size=0) :
      
      # user input main width & height
      self.main_width = width
      self.main_height = height
      
      #get master of chart widget
      try:
         self.master = args[0]
      except:
         self.master = master
      
      # values for tkchart
      self.font = font
      self.values_labels = values_labels
      self.values_labels_count = values_labels_count
      self.sections = sections
      self.sections_count = sections_count
      self.sections_fg = sections_fg
      self.chart_bg = chart_bg
      self.chart_fg = chart_fg
      
      self.vertical_bar_fg = vertical_bar_fg
      self.vertical_bar_size = vertical_bar_size
      self.horizontal_bar_fg = horizontal_bar_fg
      self.horizontal_bar_size = horizontal_bar_size
      
      self.text_color = text_color
      self.chart_line_len = chart_line_len
      self.max_value = max_value
      
      
      self.left_space = RequredWidth(text=max_value ,font=font)   + left_space

      self.right_space = right_space
      self.top_space = top_space
      self.bottom_space = bottom_space
      
      self.x_space = x_space
      self.y_space = y_space
      
      self.set_chart_canvas_info()

      self.chart_main_background = ctk.CTkFrame(master=self.master)
      self.chart_values_backgroud = ctk.CTkFrame(master=self.chart_main_background)
      self.values_label_1 = tk.Label(master=self.chart_main_background ,width=self.right_space ,fg=self.text_color ,font=self.font ,bg=self.chart_bg)
      self.values_label_n = tk.Label(master=self.chart_main_background ,width=self.right_space ,fg=self.text_color ,font=self.font ,bg=self.chart_bg)
      self.chart_vertical_bar = ctk.CTkFrame(master=self.chart_main_background)
      self.chart_horizontal_bar = ctk.CTkFrame(master=self.chart_main_background)
      self.chart_canvas_backgroud = ctk.CTkFrame(master=self.chart_main_background)
      self.chart_canvas =  ctk.CTkCanvas(master=self.chart_canvas_backgroud ,highlightthickness=0)

      self.configure_chart_geomatry()
      self.configure_chart_colors()
      
      if self.sections == True :
         self.configure_sections()
      if self.values_labels == True :
         self.configure_values_label()
         
      self.line_highlight = line_highlight
      self.line_highlight_size = line_highlight_size
      
               
   def configure_chart_geomatry(self):
      self.chart_main_background.configure(width=self.main_width,
                                           height=self.main_height)
      self.chart_values_backgroud.place(y=self.top_space+self.y_space+self.horizontal_bar_size)
      self.chart_vertical_bar.place(x=self.left_space,
                                    y=self.top_space)
      self.chart_horizontal_bar.place(x=self.left_space,
                                      y=self.main_height-self.bottom_space-self.horizontal_bar_size)
      self.chart_canvas_backgroud.place(x=self.left_space+self.vertical_bar_size,
                                        y=self.top_space+self.y_space+self.horizontal_bar_size)
      self.chart_canvas.place(x=0,y=0)   
      
      self.chart_values_backgroud.configure(width=self.left_space, height=self.main_height-(self.horizontal_bar_size*2+self.top_space+self.y_space+self.bottom_space ))
      self.chart_vertical_bar.configure(width=self.vertical_bar_size ,height=self.main_height-(self.top_space+self.bottom_space))
      self.chart_horizontal_bar.configure(height=self.horizontal_bar_size ,width=self.main_width-(self.left_space+self.right_space))
      self.chart_canvas_backgroud.configure(width=self.main_width-(self.left_space+self.vertical_bar_size+self.x_space+self.right_space) ,
                                            height=self.main_height-(self.horizontal_bar_size*2+self.top_space+self.y_space+self.bottom_space))
      self.chart_canvas.configure(width=self.main_width-5-(self.left_space+self.vertical_bar_size+self.x_space+self.right_space) ,
                                  height=self.main_height-(self.horizontal_bar_size*2+self.top_space+self.y_space+self.bottom_space))
      
      self.re_display_chart() 
   def configure_chart_colors(self):
      self.chart_main_background.configure(fg_color=self.chart_bg)
      self.chart_values_backgroud.configure(fg_color=self.chart_bg)
      self.chart_vertical_bar.configure(fg_color=self.vertical_bar_fg )
      self.chart_horizontal_bar.configure(fg_color=self.horizontal_bar_fg)
      self.chart_canvas_backgroud.configure(fg_color=self.chart_fg)
      self.chart_canvas.configure(bg=self.chart_fg)
    
   
   def delete_sections(self):
      for widget in self.chart_canvas_backgroud.winfo_children():
         if type(widget) == tk.Frame :
            widget.destroy()
   def configure_sections(self):
      y_ = 0
      for i in range(1 ,self.sections_count+1) :
         tk.Frame(master=self.chart_canvas_backgroud ,height=1 ,bg=self.sections_fg).place(relwidth=1 ,width=-5 ,y=y_)
         y_ = (self.main_height-(self.horizontal_bar_size*2+self.top_space+self.y_space+self.bottom_space)) / self.sections_count * i
   
   def delete_values_label(self):
      self.values_label_1.place_forget()
      for widget in self.chart_values_backgroud.winfo_children():
         if type(widget) == tk.Label:
            widget.destroy()
      self.values_label_n.place_forget()
           
   def configure_values_label(self):
      self.values_label_1.config(anchor='e' ,text=str(round(self.max_value+0.0,1))+" " ,fg=self.text_color ,font=self.font ,bg=self.chart_bg,width=self.left_space )
      self.values_label_1.place(y=self.top_space+self.y_space+self.horizontal_bar_size,anchor='w'  )
      
      for i in range(1 ,self.values_labels_count) :
         text_ = round(self.max_value / self.values_labels_count * (self.values_labels_count - i),1)
         y_ = (self.main_height-(self.horizontal_bar_size*2+self.top_space+self.y_space+self.bottom_space)) / self.values_labels_count * i
         tk.Label(master=self.chart_values_backgroud ,
                  anchor='e' ,text=str(text_)+" " ,fg=self.text_color ,font=self.font ,\
                     bg=self.chart_bg,width=self.left_space).place(y=y_ ,anchor='w')
      
      self.values_label_n.configure(anchor='e' ,text=str(0.0)+" " ,fg=self.text_color ,font=self.font ,bg=self.chart_bg ,width=self.left_space )
      self.values_label_n.place(y=self.main_height-self.bottom_space-self.horizontal_bar_size  ,anchor='w')
 
   def configure(self ,master=None ,width=None ,height=None 
                ,sections=None ,sections_count=None ,sections_fg=None
                ,chart_bg = None ,chart_fg = None
                ,horizontal_bar_fg = None ,horizontal_bar_size=None ,vertical_bar_fg =None ,vertical_bar_size=None
                ,text_color = None ,font=None ,values_labels=None ,values_labels_count=None ,max_value=None 
                ,chart_line_len = None 
                ,top_space=None ,bottom_space=None ,left_space=None ,right_space=None ,x_space=None ,y_space=None
                ,line_highlight=None ,line_highlight_size=None) :
      

      reset_chart_geomatry = False
      reset_chart_colors = False
      reset_left_space = False
      reset_sections = False
      reset_values_labels = False
      
      if master != None :
         self.master = master
         reset_chart_geomatry = True
      
      if width != None:
         self.main_width = width
         reset_chart_geomatry = True
         
      if height != None:
         self.main_height = height
         reset_chart_geomatry = True
         
      if horizontal_bar_size != None:
         self.horizontal_bar_size = horizontal_bar_size
         reset_chart_geomatry = True
         
      if vertical_bar_size != None:
         self.vertical_bar_size = vertical_bar_size
         reset_chart_geomatry = True
      
      if top_space != None:
         self.top_space = top_space
         reset_chart_geomatry = True
         
      if bottom_space != None:
         self.bottom_space = bottom_space
         reset_chart_geomatry = True
      
      if right_space != None :
         self.right_space = right_space
         reset_chart_geomatry = True
      
      if x_space != None:
         self.x_space = x_space
         reset_chart_geomatry = True
         
      if y_space != None:
         self.y_space = y_space
         reset_chart_geomatry = True
      
      if text_color != None :
         self.text_color = text_color
      
      if chart_bg != None :
         self.chart_bg = chart_bg
         reset_chart_colors = True
      
      if chart_fg != None :
         self.chart_fg = chart_fg
         reset_chart_colors = True
      
      if horizontal_bar_fg != None :
         self.horizontal_bar_fg =horizontal_bar_fg
         reset_chart_colors = True
      
      if vertical_bar_fg != None :
         self.vertical_bar_fg = vertical_bar_fg
         reset_chart_colors = True
      
      if chart_fg != None :
         self.chart_fg = chart_fg
         reset_chart_colors = True
         
      if max_value != None :
        
         reset_chart_geomatry = True
         reset_left_space = True
         reset_values_labels = True
    
      if font != None:
         reset_chart_geomatry = True
         reset_left_space = True
         reset_values_labels = True
         
      if left_space != None:
         if font != None :
               self.font = font 
         if max_value != None :
               self.max_value = max_value
         self.left_space = left_space + RequredWidth(text=self.max_value ,font=self.font)
         reset_chart_geomatry = True
      else:
         if reset_left_space :
            self.left_space = self.left_space - RequredWidth(text=self.max_value ,font=self.font)
            if font != None :
               self.font = font 
            if max_value != None :
               self.max_value = max_value
            self.left_space = self.left_space + RequredWidth(text=self.max_value ,font=self.font)
      
      
      if sections_count != None:
         self.sections_count = sections_count
         reset_sections = True
      if sections_fg != None:
         self.sections_fg = sections_fg
         reset_sections = True
      if text_color != None :
         self.text_color = text_color
         reset_values_labels =True
      if values_labels_count != None:
         self.values_labels_count = values_labels_count
         values_labels_count =True
         
      if reset_values_labels == True:
         self.delete_values_label()
      if values_labels == None :
         if self.values_labels == True:
            self.delete_values_label()
            self.configure_values_label()
      elif values_labels == True :
            self.delete_values_label()
            self.values_labels = True
            self.configure_values_label()
      elif values_labels == False:
         self.delete_values_label()
         self.values_labels = False
      
      if reset_sections == True:
         self.delete_sections()
      if sections == None :
         if self.sections == True:
            self.delete_sections()
            self.configure_sections()
      elif sections == True :
            self.delete_sections()
            self.sections = True
            self.configure_sections()
      elif sections == False:
         self.delete_sections()
         self.sections = False
         
      if chart_line_len != None :
         self.chart_line_len = chart_line_len
         reset_chart_geomatry = True
      
      if line_highlight != None :
         if self.line_highlight != line_highlight :
            self.line_highlight = line_highlight
            reset_chart_geomatry = True
      
      if line_highlight_size != None:
         if self.line_highlight_size != line_highlight_size:
            self.line_highlight_size = line_highlight_size
            reset_chart_geomatry = True
      
      if reset_chart_colors == True:
         self.configure_chart_colors()
      if reset_chart_geomatry == True :
         self.configure_chart_geomatry()
         
         
      
   
   
   def place(self ,x=None ,y=None ,rely=None ,relx=None ,anchor=None):
      self.chart_main_background.place(x=x ,y=y ,rely=rely ,relx=relx ,anchor=anchor)
      
   def pack(self ,x=None ,y=None ,pady=None ,padx=None ,before=None ,expand=None ,fill=None ,after=None 
            ,side=None ,ipadx=None ,ipady=None ,anchor=None):
      self.chart_main_background.pack(pady=pady ,padx=padx ,before=before , expand=expand ,fill=fill
                               ,after=after ,side=side ,ipadx=ipadx ,ipady=ipady ,anchor=anchor)
      
   def grid(self ,column=None ,columnspan=None ,ipadx=None ,ipady=None , padx=None , pady=None ,row=None 
            ,rowspan=None ,sticky=None):
      self.chart_main_background.grid(column=column ,columnspan=columnspan ,ipadx=ipadx ,ipady=ipady ,
                               padx=padx , pady=pady ,row=row ,rowspan=rowspan ,sticky=sticky)
      
      
   def reset_chart_canvas_place_info(self):
      self.chart_x = 0 
      self.chart_width = self.main_width-5-(self.left_space+self.vertical_bar_size+self.x_space+self.right_space)
      self.chart_height = self.main_height-(self.horizontal_bar_size*2+self.top_space+self.y_space+self.bottom_space)
      self.chart_canvas.place(x=0 ,y=0)   
      
      self.chart_canvas.configure(width=self.main_width-5-(self.left_space+self.vertical_bar_size+self.x_space+self.right_space),
                                  height=self.main_height-(self.horizontal_bar_size*2+self.top_space+self.y_space+self.bottom_space))
      self.chart_canvas.delete("all")
   
   def set_chart_canvas_info(self):
      self.chart_display_lines = []
      
   def reset(self):
      self.reset_chart_canvas_place_info()
      self.chart_display_lines = []

   def re_display_chart(self):
      self.reset_chart_canvas_place_info()
      
      if len(self.chart_display_lines) > 0 :
         index_ = int(((self.chart_width) / self.chart_line_len) - ((self.chart_width)/ self.chart_line_len)*2)
         max_displayed_values = len(self.chart_display_lines[0].values)
         for line in self.chart_display_lines:
            if max_displayed_values < len(line.values):
               max_displayed_values = len(line.values)
               
         for line in self.chart_display_lines:
            line.values += [None for x in range(max_displayed_values-len(line.values))]
            line.values = line.values[index_:]
            
         for line in self.chart_display_lines:
            while None in line.values :
               line.values.remove(None)
               
         temp_display_lines = self.chart_display_lines
         self.set_chart_canvas_info()
         
         for line in temp_display_lines:
            line.x_end =  self.chart_line_len*-1
            line.y_end = 0
            temp_values = line.values
            line.values = []
            if len(temp_values) != 0 :
               self.display(values=temp_values ,line=line)

   def display(self ,line=None ,values:list=[]):
      if line not in self.chart_display_lines:
         self.chart_display_lines.append(line)
      
      line.values += values
      x_start = line.x_end
      y_start = line.y_end

      for value in values:
         line.x_end += self.chart_line_len
         line.y_end = (self.chart_height - (self.chart_height/100)*(value/self.max_value*100) + (line.line_height/2))
         self.chart_canvas.create_line(x_start,y_start,line.x_end,line.y_end
                                            ,fill=line.line_color ,width=line.line_height)
         
         if self.line_highlight :
            self.chart_canvas.create_aa_circle(x_start,y_start,self.line_highlight_size)
   
         
         if line.x_end > self.chart_width :
            self.chart_x -= self.chart_line_len
            self.chart_width += self.chart_line_len
            if self.chart_width > self.main_width*2 :
               self.re_display_chart()
            else:
               self.chart_canvas.place(x=self.chart_x,
                                        y=0)      
               self.chart_canvas.configure(width=self.chart_width
                                           ,height=self.main_height-(self.horizontal_bar_size*2+self.top_space+self.y_space+self.bottom_space))
      
         x_start = line.x_end
         y_start = line.y_end