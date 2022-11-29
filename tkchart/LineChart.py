import customtkinter as ctk
import tkinter as tk


class LineChart():
   def __init__(self ,*args ,master=None ,width=400 ,height=270 
                ,sections=None ,sections_fg="#303030"
                ,chart_bg = '#101010' ,chart_fg = '#202020' 
                ,horizontal_fg = "#404040" ,vertical_fg = "#404040" 
                ,text_color = "#ffffff" ,font=None ,values_display=False ,max_value=1000 
                ,chart_line_len = 30) :
   
      self.width_ = width
      self.height_ = height
      try:
         master_ = args[0]
      except:
         master_ = master
      font_ = font
  
      self.values_display = values_display
      self.sections = sections

    

      #chart main background 
      #vertical bar 
      #horizontal bar
      self.chart_bg_frame = ctk.CTkFrame(master=master_ ,fg_color=chart_bg ,width=self.width_ ,height=self.height_)
      
      self.chart_vertical_bar = ctk.CTkFrame(self.chart_bg_frame  ,fg_color=vertical_fg ,height=self.height_-120 ,width=2)
      self.chart_vertical_bar.place(x=60 ,y=60)
      self.chart_horizontal_bar = ctk.CTkFrame(self.chart_bg_frame ,fg_color=horizontal_fg ,width=self.width_-120 ,height=2)
      self.chart_horizontal_bar.place(y=self.height_-60 ,x=60)
   
      self.chart_display_frame = ctk.CTkFrame(self.chart_bg_frame  ,fg_color=chart_fg)
      self.chart_display_frame.place(x=62 ,y=120 ,width=self.width_-180 ,height=self.height_-180)
      
      self.chart_display_canvas =  ctk.CTkCanvas(self.chart_display_frame  ,bg=chart_fg ,highlightthickness=0 ,width = self.width_-185 , height=self.height_-180)
      self.chart_display_canvas.place(x=0 ,y=0)

      #section bars 9
      self.section_bar1 = tk.Frame(self.chart_display_frame ,bg=sections_fg)
      self.section_bar2 = tk.Frame(self.chart_display_frame ,bg=sections_fg)
      self.section_bar3 = tk.Frame(self.chart_display_frame ,bg=sections_fg)
      self.section_bar4 = tk.Frame(self.chart_display_frame ,bg=sections_fg)
      self.section_bar5 = tk.Frame(self.chart_display_frame ,bg=sections_fg) 
      self.section_bar6 = tk.Frame(self.chart_display_frame ,bg=sections_fg) 
      self.section_bar7 = tk.Frame(self.chart_display_frame ,bg=sections_fg)  
      self.section_bar8 = tk.Frame(self.chart_display_frame ,bg=sections_fg)  
      self.section_bar9 = tk.Frame(self.chart_display_frame ,bg=sections_fg)  
      self.section_bar10 = tk.Frame(self.chart_display_frame ,bg=sections_fg)  
      if sections == True:
         self.section_bar1.place(y=(self.height_-180)/10*0 ,relwidth=1 ,width=-10 ,height=1 )
         self.section_bar2.place( y=(self.height_-180)/10*1 ,width=self.width_-180-10 ,height=1 )
         self.section_bar3.place( y=(self.height_-180)/10*2 ,width=self.width_-180-10 ,height=1 )
         self.section_bar4.place( y=(self.height_-180)/10*3 ,width=self.width_-180-2 ,height=1 )
         self.section_bar5.place( y=(self.height_-180)/10*4 ,width=self.width_-180-2 ,height=1 )
         self.section_bar6.place( y=(self.height_-180)/10*5 ,width=self.width_-180-2 ,height=1 )
         self.section_bar7.place( y=(self.height_-180)/10*6 ,width=self.width_-180-2 ,height=1 )
         self.section_bar8.place( y=(self.height_-180)/10*7 ,width=self.width_-180-2 ,height=1 )
         self.section_bar9.place( y=(self.height_-180)/10*8 ,width=self.width_-180-2 ,height=1 )
         self.section_bar10.place(y=(self.height_-180)/10*9 ,width=self.width_-180-2 ,height=1 )
        
      
      self.section_label_1  = tk.Label(self.chart_bg_frame ,text='0' ,width=7 ,justify="right" ,bg=chart_bg ,fg=text_color ,font=font_)
      self.section_label_2  = tk.Label(self.chart_bg_frame ,text='0' ,width=7 ,justify="right" ,bg=chart_bg ,fg=text_color ,font=font_)
      self.section_label_3  = tk.Label(self.chart_bg_frame ,text='0' ,width=7 ,justify="right" ,bg=chart_bg ,fg=text_color ,font=font_)
      self.section_label_4  = tk.Label(self.chart_bg_frame ,text='0' ,width=7 ,justify="right" ,bg=chart_bg ,fg=text_color ,font=font_)
      self.section_label_5  = tk.Label(self.chart_bg_frame ,text='0' ,width=7 ,justify="right" ,bg=chart_bg ,fg=text_color ,font=font_)
      self.section_label_6  = tk.Label(self.chart_bg_frame ,text='0' ,width=7 ,justify="right" ,bg=chart_bg ,fg=text_color ,font=font_)
      self.section_label_7  = tk.Label(self.chart_bg_frame ,text='0' ,width=7 ,justify="right" ,bg=chart_bg ,fg=text_color ,font=font_)
      self.section_label_8  = tk.Label(self.chart_bg_frame ,text='0' ,width=7 ,justify="right" ,bg=chart_bg ,fg=text_color ,font=font_)
      self.section_label_9  = tk.Label(self.chart_bg_frame ,text='0' ,width=7 ,justify="right" ,bg=chart_bg ,fg=text_color ,font=font_)
      self.section_label_10 = tk.Label(self.chart_bg_frame ,text='0' ,width=7 ,justify="right" ,bg=chart_bg ,fg=text_color ,font=font_)
      self.section_label_11 = tk.Label(self.chart_bg_frame ,text='0' ,width=7 ,justify="right" ,bg=chart_bg ,fg=text_color ,font=font_)
      if self.values_display == True :
         self.section_label_1.place( y=(self.height_-180)/10*0+120 ,anchor='w')
         self.section_label_2.place( y=(self.height_-180)/10*1+120 ,anchor='w')
         self.section_label_3.place( y=(self.height_-180)/10*2+120 ,anchor='w')
         self.section_label_4.place( y=(self.height_-180)/10*3+120 ,anchor='w')
         self.section_label_5.place( y=(self.height_-180)/10*4+120 ,anchor='w')
         self.section_label_6.place( y=(self.height_-180)/10*5+120 ,anchor='w')
         self.section_label_7.place( y=(self.height_-180)/10*6+120 ,anchor='w')
         self.section_label_8.place( y=(self.height_-180)/10*7+120 ,anchor='w')
         self.section_label_9.place( y=(self.height_-180)/10*8+120 ,anchor='w')
         self.section_label_10.place(y=(self.height_-180)/10*9+120 ,anchor='w')
         self.section_label_11.place(y=(self.height_-180)/10*10+120 ,anchor='w')
      
      self.max_value = max_value
      self.set_values(self.max_value)
      
      self.chart_line_len = chart_line_len
      self.chart_place_x = 0
      self.lines = []
      self.chart_width = self.width_ - 185
      self.chart_height = self.height_ - 180
   
     
      
   def place(self ,x=None ,y=None ,rely=None ,relx=None ,anchor=None):
      self.chart_bg_frame.place(x=x ,y=y ,rely=rely ,relx=relx ,anchor=anchor)
      
   def pack(self ,x=None ,y=None ,pady=None ,padx=None ,before=None ,expand=None ,fill=None ,after=None ,side=None ,ipadx=None ,ipady=None ,anchor=None):
      # -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
      self.chart_bg_frame.pack(x=x ,y=y ,pady=pady ,padx=padx ,
                               before=before , expand=expand ,fill=fill ,after=after ,side=side ,
                               ipadx=ipadx ,ipady=ipady ,anchor=anchor)
      
   def grid(self ,column=None ,columnspan=None ,ipadx=None ,ipady=None ,
            padx=None , pady=None ,row=None ,rowspan=None ,sticky=None):
      self.chart_bg_frame.grid(column=column ,columnspan=columnspan ,ipadx=ipadx ,ipady=ipady ,
                               padx=padx , pady=pady ,row=row ,rowspan=rowspan ,sticky=sticky)
      

         
   def configure(self,width=None ,height=None ,sections=None ,sections_fg=None ,chart_bg=None ,chart_fg=None ,
               horizontal_fg=None ,vertical_fg=None ,text_color=None ,font=None ,values_display=None ,
               chart_line_len=None ,max_value=None):
      def place_sections(self ,**kwrg):
         width_=kwrg['width_'] 
         height_= kwrg['height_']
         self.section_bar1.place(y=(height_-180)/10*0+2,width=width_-180-2 ,height=1 )
         self.section_bar2.place( y=(height_-180)/10*1 ,width=width_-180-2 ,height=1 )
         self.section_bar3.place( y=(height_-180)/10*2 ,width=width_-180-2 ,height=1 )
         self.section_bar4.place( y=(height_-180)/10*3 ,width=width_-180-2 ,height=1 )
         self.section_bar5.place( y=(height_-180)/10*4 ,width=width_-180-2 ,height=1 )
         self.section_bar6.place( y=(height_-180)/10*5 ,width=width_-180-2 ,height=1 )
         self.section_bar7.place( y=(height_-180)/10*6 ,width=width_-180-2 ,height=1 )
         self.section_bar8.place( y=(height_-180)/10*7 ,width=width_-180-2 ,height=1 )
         self.section_bar9.place( y=(height_-180)/10*8 ,width=width_-180-2 ,height=1 )
         self.section_bar10.place(y=(height_-180)/10*9 ,width=width_-180-2 ,height=1 )
      def place_forget_sections(self):
         self.section_bar1.place_forget()
         self.section_bar2.place_forget()
         self.section_bar3.place_forget()
         self.section_bar4.place_forget()
         self.section_bar5.place_forget()
         self.section_bar6.place_forget()
         self.section_bar7.place_forget()
         self.section_bar8.place_forget()
         self.section_bar9.place_forget()
         self.section_bar10.place_forget()
      def place_labels(self ,**kwrg):
         height_ = kwrg['height_']
         self.section_label_1.place( y=(height_-180)/10*0+120 ,anchor='w')
         self.section_label_2.place( y=(height_-180)/10*1+120 ,anchor='w')
         self.section_label_3.place( y=(height_-180)/10*2+120 ,anchor='w')
         self.section_label_4.place( y=(height_-180)/10*3+120 ,anchor='w')
         self.section_label_5.place( y=(height_-180)/10*4+120 ,anchor='w')
         self.section_label_6.place( y=(height_-180)/10*5+120 ,anchor='w')
         self.section_label_7.place( y=(height_-180)/10*6+120 ,anchor='w')
         self.section_label_8.place( y=(height_-180)/10*7+120 ,anchor='w')
         self.section_label_9.place( y=(height_-180)/10*8+120 ,anchor='w')
         self.section_label_10.place(y=(height_-180)/10*9+120 ,anchor='w')
         self.section_label_11.place(y=(height_-180)/10*10+120 ,anchor='w')
      def place_forget_labels(self):
         self.section_label_1.place_forget()
         self.section_label_2.place_forget()
         self.section_label_3.place_forget()
         self.section_label_4.place_forget()
         self.section_label_5.place_forget()
         self.section_label_6.place_forget()
         self.section_label_7.place_forget()
         self.section_label_8.place_forget()
         self.section_label_9.place_forget()
         self.section_label_10.place_forget()
         self.section_label_11.place_forget()
            
      def reset_chart(self ,**kwrg):
         width_ = kwrg['width_']
         height_ = kwrg['height_']
         self.chart_bg_frame.configure(width=width_ ,height=height_)
         self.chart_vertical_bar.place(height=height_-120 ,width=2 ,x=60 ,y=60)
         self.chart_horizontal_bar.place(width=width_-120 ,height=2 ,y=height_-60 ,x=60)
         self.chart_display_frame.place(x=62 ,y=120 ,width=width_-180 ,height=height_-180)
         self.chart_display_canvas.configure(width=width_-185 ,height=height_-180)
   
         if self.sections == True:
            place_sections(self ,width_=width_ ,height_=height_)
         if self.values_display == True:
            place_labels(self ,height_=height_)
         
      
      reset = False
      if width != None:
         self.width_ = width
         reset = True
    
      if height != None:
         self.height_ = height
         reset = True
      
      if sections != None:
         self.sections = sections
         if self.sections == True:
            self.sections = True
            place_sections(self ,width_=self.width_ ,height_=self.height_)
         else:
            if self.sections == False or self.sections == None :
               self.sections= False
               place_forget_sections(self)
   
      if chart_bg != None:
         self.chart_bg_frame.configure(fg_color=chart_bg)
         
      if chart_fg != None:
         self.chart_display_frame.configure(fg_color=chart_fg)
         self.chart_display_canvas.configure(bg=chart_fg)
      if sections_fg != None :
         self.section_bar1.configure(bg=sections_fg) 
         self.section_bar2.configure(bg=sections_fg) 
         self.section_bar3.configure(bg=sections_fg) 
         self.section_bar4.configure(bg=sections_fg)  
         self.section_bar5.configure(bg=sections_fg)  
         self.section_bar6.configure(bg=sections_fg)  
         self.section_bar7.configure(bg=sections_fg)  
         self.section_bar8.configure(bg=sections_fg)  
         self.section_bar9.configure(bg=sections_fg) 
         self.section_bar10.configure(bg=sections_fg) 
      if horizontal_fg != None:
         self.chart_horizontal_bar.configure(fg_color=horizontal_fg)
      if vertical_fg != None :
         self.chart_vertical_bar.configure(fg_color=vertical_fg)
      if text_color != None or chart_bg != None or font!=None:
         self.section_label_1.configure(fg=text_color ,bg=chart_bg ,font=font)
         self.section_label_2.configure(fg=text_color ,bg=chart_bg ,font=font)
         self.section_label_3.configure(fg=text_color ,bg=chart_bg ,font=font)
         self.section_label_4.configure(fg=text_color ,bg=chart_bg ,font=font)
         self.section_label_5.configure(fg=text_color ,bg=chart_bg ,font=font)
         self.section_label_6.configure(fg=text_color ,bg=chart_bg ,font=font)
         self.section_label_7.configure(fg=text_color ,bg=chart_bg ,font=font)
         self.section_label_8.configure(fg=text_color ,bg=chart_bg ,font=font)
         self.section_label_9.configure(fg=text_color ,bg=chart_bg ,font=font)
         self.section_label_10.configure(fg=text_color ,bg=chart_bg ,font=font)
         self.section_label_11.configure(fg=text_color ,bg=chart_bg ,font=font)
      
      
      if values_display != None :
         self.values_display = values_display
         if self.values_display == True:
            place_labels(self ,height_=self.height_)
         elif self.values_display==False:
            place_forget_labels(self)

      if chart_line_len != None :
         reset = True
         self.chart_line_len = chart_line_len
      
      if max_value != None:
         reset = True
         self.max_value = max_value
         self.set_values(self.max_value)
      
      self.chart_width = self.width_ - 185
      self.chart_height = self.height_ - 180
      if reset :
         reset_chart(self ,width_=self.width_ ,height_=self.height_)
         
         #redisplay values
         self.reset_chart_display()
            
   def set_values(self ,*arg):
      max_value = arg[0]
      self.section_label_1.configure(text=(max_value/10*10))
      self.section_label_2.configure(text=max_value/10*9)
      self.section_label_3.configure(text=max_value/10*8)
      self.section_label_4.configure(text=max_value/10*7)
      self.section_label_5.configure(text=max_value/10*6)
      self.section_label_6.configure(text=max_value/10*5)
      self.section_label_7.configure(text=max_value/10*4)
      self.section_label_8.configure(text=max_value/10*3)
      self.section_label_9.configure(text=max_value/10*2)
      self.section_label_10.configure(text=max_value/10*1)
      self.section_label_11.configure(text=max_value/10*0)

   def reset_chart_display(self):
      self.chart_display_canvas.place(x=0 ,y=0 ,width = self.width_-185 , height=self.height_-180)
      self.chart_place_x = 0 
      self.chart_width = self.width_ - 185
      self.chart_height = self.height_ - 180
      self.chart_display_canvas.delete("all")
   
      index_ = int(((self.width_-180) / self.chart_line_len) - ((self.width_-180 )/ self.chart_line_len)*2)
    
      if len(self.lines) != 0:
         max_displayed_values = len(self.lines[0].values)
         for line in self.lines:
            if max_displayed_values < len(line.values):
               max_displayed_values = len(line.values)
               
   
         for line in self.lines:
            line.values += [None for x in range(max_displayed_values-len(line.values))]
            line.values = line.values[index_:]

            
         for line in self.lines:
            while None in line.values :
               line.values.remove(None)
               
         lines = self.lines
         self.lines = []
         
         for line in lines:
            line.x_end =  self.chart_line_len*-1
            line.y_end = 0
            temp_values = line.values
            line.values = []
            if len(temp_values) != 0 :
               self.display(values=temp_values ,line=line)
               
   def reset_all(self):
      for line in self.lines:
         line.x_end = self.chart_line_len*-1
         line.y_end = 0
         line.values = [] 
         
      self.chart_place_x = 0
      self.lines = []
      self.chart_width = self.width_ - 185
      self.chart_height = self.height_ - 180

      self.chart_display_canvas.delete("all")
      self.chart_bg_frame.configure(width=self.width_ ,height=self.height_)
      self.chart_vertical_bar.place(height=self.height_-120 ,width=2 ,x=60 ,y=60)
      self.chart_horizontal_bar.place(width=self.width_-120 ,height=2 ,y=self.height_-60 ,x=60)
      self.chart_display_frame.place(x=62 ,y=120 ,width=self.width_-180 ,height=self.height_-180)
      self.chart_display_canvas.configure(width=self.width_-185 ,height=self.height_-180)
      self.chart_display_canvas.place(x=0 ,y=0)

       
   def display(self ,line=None ,values=None):
      if line not in self.lines:
         self.lines.append(line)
      
      line.values += values
      x_start = line.x_end
      y_start = line.y_end
      chart_reset_required = False
      

      for value in values:
         line.x_end += self.chart_line_len
         line.y_end = (self.chart_height - (self.chart_height/100)*(value/self.max_value*100) + (line.line_height/2))
         self.chart_display_canvas.create_line(x_start,y_start,line.x_end,line.y_end
                                            ,fill=line.line_color ,width=line.line_height)
         if line.x_end >= self.chart_width :
            self.chart_width += self.chart_line_len
            self.chart_place_x -= self.chart_line_len
            if self.chart_width > self.chart_width*2 :
               chart_reset_required = True
               break
            else:
               self.chart_display_canvas.place(x=self.chart_place_x ,y=0 ,width=self.chart_width)
         x_start = line.x_end
         y_start = line.y_end
      
      if chart_reset_required:
         self.reset_chart_display()
     