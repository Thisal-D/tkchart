import tkinter
from .RequiredSize import RequiredWidth
from .RequiredSize import RequiredHeight
from .Line import *

class LineChart():
   def __init__(self, master=None,
                  width=700,
                  height=400,
                  axis_size=2,
                  axis_color="#909090",
                  bg_color="#303030",
                  fg_color="#252525",
                  data_font_style=("arial", 9, "normal"),
                  axis_font_style=("arial", 9, "normal"),
                  section_color="#909090",
                  
                  y_axis_precision=1,
                  y_axis_label_count=5,
                  y_axis_data="Y",
                  y_axis_max_value=5,
                  y_axis_section_count=0,
                  y_axis_font_color="#909090",
                  y_axis_data_font_color="#909090",
                  y_axis_data_position="top",
                  
                  x_axis_data="X",
                  x_axis_label_count=None,
                  x_axis_values:list=[1, 2, 3, 4, 5],
                  x_axis_section_count=0,
                  x_axis_font_color="#909090",
                  x_axis_data_font_color="#cccccc",
                  x_axis_data_position="top",
                  
                  line_width="auto",
                  y_space=0, x_space=0,
                  *args)->None:
      
      if master != None:
         self.master = master
      if len(args) > 0:
         self.master = args[0]
      
      self.__height = height
      self.__width = width
      
      self.__lines = []
      self.__line_width = line_width
      
      self.__bg_color = bg_color
      self.__fg_color = fg_color
      self.__y_axis_font_color = y_axis_font_color
      self.__y_axis_data_font_color = y_axis_data_font_color
      self.__x_axis_font_color = x_axis_font_color
      self.__x_axis_data_font_color = x_axis_data_font_color
      self.__section_color = section_color

      self.__axis_size = axis_size
      self.__axis_color = axis_color   
      
      self.__x_axis_section_count = x_axis_section_count
      self.__y_axis_section_count = y_axis_section_count
      self.__y_axis_label_count = y_axis_label_count
      
      if x_axis_label_count == None:
         self.__x_axis_label_count = len(x_axis_values)
      else:
         self.__x_axis_label_count = x_axis_label_count
         
      self.__x_labels_values_index_change = 0
      
      self.__y_axis_data = y_axis_data
      self.__x_axis_data = x_axis_data
      
      self.__x_axis_data_position = x_axis_data_position
      self.__y_axis_data_position = y_axis_data_position
   
      self.__y_axis_max_value = y_axis_max_value
      self.__x_axis_values = x_axis_values
   
   
      self.__data_font_style = data_font_style
      self.__y_axis_precision = y_axis_precision
      
      self.__axis_values_font = axis_font_style
   
      self.__main_frame = tkinter.Frame(master=master)
      
      self.__y_axis_frame = tkinter.Frame(master=self.__main_frame)
      self.__x_axis_frame = tkinter.Frame(master=self.__main_frame)
      
      self.__x_space = x_space
      self.__y_space = y_space
      
      self.__y_axis_values_frame = tkinter.Frame(master=self.__main_frame)
      self.__x_axis_values_frame = tkinter.Frame(master=self.__main_frame)
      
      self.__y_axis_data_label = tkinter.Label(master=self.__main_frame)
      self.__x_axis_data_label = tkinter.Label(master=self.__main_frame)
      
      self.__output_frame = tkinter.Frame(master=self.__main_frame)
      self.__output_canvas = tkinter.Canvas(master=self.__output_frame, highlightthickness=0)
      
      self.__force_to_stop_data_showing = False
      self.__is_data_showing_working = False
      
      self.__place_x = 0
      self.__real_height = 0
      self.__real_width = 0
      
      self.__place_info_x = 0
      self.__place_info_y = 0
      self.__place_info_rely = 0
      self.__place_info_relx = 0
      self.__place_info_anchor = 0
      
      self.__pack_info_pady = 0
      self.__pack_info_padx = 0
      self.__pack_info_before = 0
      self.__pack_info_after = 0
      self.__pack_info_side = 0
      self.__pack_info_anchor = 0
      
      self.__grid_info_column = 0
      self.__grid_info_columnspan = 0
      self.__grid_info_padx = 0
      self.__grid_info_pady = 0
      self.__grid_info_row = 0
      self.__grid_info_rowspan = 0
      self.__grid_info_sticky = 0
      
      self.__get_required_widget_size()
      self.__fix_x_axis_label_count()
      self.__place_widget()
      self.__get_line_width()
      self.__create_y_axis_labels()
      self.__create_x_axis_labels()
      self.__create_y_sections()
      self.__create_x_sections()
      self.__set_widget_colors()
      self.__set_widget_font()
      self.__set_widget_text()
      self.__set_x_axis_values()
      self.__reset_chart_info()
   
      
   def __add_decimal_points(self, float_val:float, decimals:int)->float:
      if decimals:
         float_val = round(float(float_val),decimals)
         float_val = str(float_val) + ((decimals-len(str(float_val).split(".")[-1]))*"0")
         return float_val
      else:
         return int(float_val)
   
   
   def __set_widget_colors(self)->None:
      self.__y_axis_frame.configure(bg=self.__axis_color)
      self.__x_axis_frame.configure(bg=self.__axis_color)
      self.__y_axis_values_frame.configure(bg=self.__bg_color)
      self.__x_axis_values_frame.configure(bg=self.__bg_color)
      
      self.__main_frame.configure(bg=self.__bg_color)
      self.__output_frame.configure(bg=self.__fg_color)
      self.__output_canvas.configure(bg=self.__fg_color)
      
      self.__y_axis_data_label.configure(bg=self.__bg_color, fg=self.__y_axis_data_font_color)
      for label in self.__x_axis_values_frame.winfo_children() :
         if type(label) == tkinter.Label:
            label.configure(bg=self.__bg_color, fg=self.__x_axis_font_color)
      
      self.__x_axis_data_label.configure(bg=self.__bg_color, fg=self.__x_axis_data_font_color)
      for label in self.__y_axis_values_frame.winfo_children():
         if type(label) == tkinter.Label:
            label.configure(bg=self.__bg_color, fg=self.__y_axis_font_color)
            
      for section_frame in self.__output_frame.winfo_children():
         if type(section_frame) == tkinter.Frame:
            section_frame.configure(bg=self.__section_color)
      
   
   def __set_widget_font(self)->None:
      self.__y_axis_data_label.configure(font=self.__data_font_style)
      self.__x_axis_data_label.configure(font=self.__data_font_style)
      
      for label in self.__x_axis_values_frame.winfo_children() + self.__y_axis_values_frame.winfo_children() :
         if type(label) == tkinter.Label:
            label.configure(font = self.__axis_values_font)
   
   
   def __set_widget_text(self)->None:
      if self.__y_axis_data_position=="top":
         self.__y_axis_data_label.configure(text=self.__y_axis_data)
      else:
         self.__y_axis_data_label.configure(text="\n".join(self.__y_axis_data))
      
      if self.__y_axis_label_count>0:
         for i,label in enumerate(self.__y_axis_values_frame.winfo_children()):
            value = (self.__y_axis_max_value - (self.__y_axis_max_value/self.__y_axis_label_count)*i)
            value = self.__add_decimal_points(value,self.__y_axis_precision)
            label.configure(text=value)
      self.__x_axis_data_label.configure(text=self.__x_axis_data)
   
   def __set_x_axis_values(self)->None:
      index = -1
      for label in (self.__x_axis_values_frame.winfo_children()):
         value = self.__x_axis_values[index]
         index -= self.__x_labels_values_index_change
         label.configure(text=value)
            
   def __place_widget(self)->None:
      self.__main_frame.configure(width=self.__width, height=self.__height)
      
      self.__y_axis_data_label.place_forget()
      self.__x_axis_data_label.place_forget()
      if self.__y_axis_data_position=="top":
         self.__y_axis_data_label.place(x=0, y=0)
      else:
         self.__y_axis_data_label.place(x=0, y=self.__y_space+self.__y_special_height_space+self.__real_height/2,anchor="w")
      if self.__x_axis_data_position=="top":
         self.__x_axis_data_label.place(rely=1, relx=1, x=-self.__x_axis_data_req_width, y=-self.__x_axis_data_req_height)
      else:
         self.__x_axis_data_label.place(rely=1, y=-self.__x_axis_data_req_height,relx=0, anchor="n",
                                  x=(self.__real_width/2)+self.__y_axis_data_req_width_space_side+self.__y_value_req_width_space+self.__axis_size+self.__x_axis_data_req_width_space_top+self.__x_special_width_space)
      
      self.__y_axis_frame.configure(width=self.__axis_size)
      self.__x_axis_frame.configure(height=self.__axis_size)


      self.__y_axis_frame.place(x=self.__y_value_req_width_space+self.__y_axis_data_req_width_space_side,
                         y=int(self.__y_axis_data_req_height_space_top+(self.__y_value_req_height_space/2)+self.__y_special_height_space),
                         height=self.__const_real_height+self.__y_space+self.__axis_size)
      self.__x_axis_frame.place(x=self.__y_value_req_width_space+self.__y_axis_data_req_width_space_side,
                         rely=1,
                         y=-self.__axis_size+-self.__x_value_req_height_space+-self.__x_axis_data_req_height_space_side,
                         width=self.__const_real_width+self.__axis_size+self.__x_space)
      
      self.__output_frame.place(x=self.__y_value_req_width_space+self.__axis_size+self.__y_axis_data_req_width_space_side,
                                width=self.__const_real_width,
                                height=self.__const_real_height,
                                y=int(self.__y_axis_data_req_height_space_top+(self.__y_value_req_height_space/2)+self.__y_special_height_space+self.__y_space))
      
      
      self.__output_canvas.place(y=0, x=0, height=self.__const_real_height, width=self.__const_real_width)
      
      self.__y_axis_values_frame.place(x=self.__y_axis_data_req_width_space_side, width=self.__y_value_req_width_space, height=self.__height)
      self.__x_axis_values_frame.place(x=0, rely=1, y=-self.__x_value_req_height_space+-self.__x_axis_data_req_height_space_side, height=self.__x_value_req_height_space, width=self.__width)

  
   def __get_line_width(self)->None:
      if self.__line_width== "auto":
         self.__line_width = int(self.__real_width / len(self.__x_axis_values))
      else:
         self.__line_width = self.__line_width
     
     
   def __get_max_required_label_width(self, data, font)->int:
      max_required_width = 0
      for d in data:
         required_width = RequiredWidth(text=d, font=font)
         if max_required_width<required_width:
            max_required_width=required_width
      return max_required_width
   
   
   def __get_max_required_label_height(self, data, font)->int:
      max_required_height = 0
      for d in data:
         required_height = RequiredHeight(text=d, font=font)
         if max_required_height<required_height:
            max_required_height=required_height
      return max_required_height
      
   def __get_required_widget_size(self)->None:
      self.__x_axis_data_req_width_space_top = 0
      self.__x_axis_data_req_height_space_side = 0
      self.__x_axis_data_req_height = RequiredHeight(text=self.__x_axis_data, font=self.__data_font_style)
      self.__x_axis_data_req_width = RequiredWidth(text=self.__x_axis_data, font=self.__data_font_style)
      self.__x_special_width_space = 0
      if self.__x_axis_data_position == "top":
         self.__x_special_width_space = 30
         self.__x_axis_data_req_width_space_top = RequiredWidth(text=self.__x_axis_data, font=self.__data_font_style)
      else:
         self.__x_axis_data_req_height_space_side = RequiredHeight(text=self.__x_axis_data, font=self.__data_font_style)
      
      self.__y_axis_data_req_height_space_top = 0
      self.__y_axis_data_req_height = RequiredHeight(text=self.__y_axis_data, font=self.__data_font_style)
      self.__y_axis_data_req_width = RequiredWidth(text=self.__y_axis_data, font=self.__data_font_style)
      self.__y_special_height_space = 0
      self.__y_axis_data_req_width_space_side = 0
      if self.__y_axis_data_position == "top":
         self.__y_special_height_space = 30
         self.__y_axis_data_req_height_space_top = RequiredHeight(text=self.__y_axis_data[0], font=self.__data_font_style)
      else:
         self.__y_axis_data_req_width_space_side = RequiredWidth(text=self.__y_axis_data[0], font=self.__data_font_style)
      
      self.__y_value_req_height_space = RequiredHeight(text=self.__add_decimal_points(self.__y_axis_max_value, self.__y_axis_precision), font=self.__axis_values_font)
      self.__y_value_req_width_space = RequiredWidth(text=self.__add_decimal_points(self.__y_axis_max_value, self.__y_axis_precision), font=self.__axis_values_font) 
      self.__x_value_req_height_space = RequiredHeight(text=self.__x_axis_values[0], font=self.__axis_values_font)
      #self.__x_value_req_width_space = RequiredWidth(text=self.__add_decimal_points(self.__x_axis_data_max, self.__x_values_decimals), font=self.__axis_values_font) 
      self.__x_value_req_width_space = self.__get_max_required_label_width(data=self.__x_axis_values, font=self.__axis_values_font)
      
      self.__real_width = self.__width - (self.__y_value_req_width_space+self.__axis_size+self.__x_axis_data_req_width_space_top+self.__y_axis_data_req_width_space_side+\
                                          (self.__x_value_req_width_space/2)+self.__x_special_width_space+self.__x_space)
      
      self.__const_real_width = self.__real_width 
      self.__real_height = self.__height - (self.__y_axis_data_req_height_space_top+self.__axis_size+self.__x_value_req_height_space+self.__x_axis_data_req_height_space_side+\
                                          (self.__y_value_req_height_space/2)+self.__y_special_height_space+self.__y_space)
      self.__real_height = self.__real_height  
      
      self.__const_real_height = self.__real_height 
      
      
   def __create_y_axis_labels(self)->None:
      if self.__y_axis_label_count>0:
         y = self.__y_axis_data_req_height_space_top+(self.__y_value_req_height_space/2)+self.__y_special_height_space+self.__y_space
         for i in range(self.__y_axis_label_count):
            tkinter.Label(master=self.__y_axis_values_frame, justify="right" ).place(y=y, x=0,
                                                                          anchor="w" ,width=self.__y_value_req_width_space)
            y += self.__real_height/self.__y_axis_label_count 
            
            
   def __destroy_y_axis_labels(self)->None:
      for y_value in self.__y_axis_values_frame.winfo_children():
         y_value.place_forget()
         y_value.destroy()
         
         
   def __create_x_axis_labels(self)->None:
      x = self.__width - self.__x_axis_data_req_width_space_top-(self.__x_value_req_width_space/2)-self.__x_special_width_space - self.__x_space
      for i in range(self.__x_axis_label_count):
         tkinter.Label(master=self.__x_axis_values_frame).place(rely=1, y=-self.__x_value_req_height_space, x=x, anchor="n")
         x -= self.__const_real_width / self.__x_axis_label_count
         
            
   def __destroy_x_axis_labels(self)->None:
      for x_value in self.__x_axis_values_frame.winfo_children():
         x_value.place_forget()
         x_value.destroy()
         
      
   def __fix_x_axis_label_count(self)->None:
      if self.__x_axis_label_count==0:return
      x_axis_real_label_count = len(self.__x_axis_values)
      if self.__x_axis_label_count > x_axis_real_label_count:
         self.__x_axis_label_count = x_axis_real_label_count
      while x_axis_real_label_count%self.__x_axis_label_count != 0:
         self.__x_axis_label_count+=1
      self.__x_labels_values_index_change = int(x_axis_real_label_count/self.__x_axis_label_count)

            
   def __create_y_sections(self)->None:
      y = 0
      for i in range(self.__y_axis_section_count):
         tkinter.Frame(master=self.__output_frame, height=1, width=self.__real_width, bg=self.__section_color).place(y=y, anchor="w")
         y += self.__real_height/self.__y_axis_section_count
         
         
   def __create_x_sections(self)->None:
      x = self.__const_real_width - 1
      for i in range(self.__x_axis_section_count):
         tkinter.Frame(master=self.__output_frame, height=self.__real_height, width=1 ,bg=self.__section_color).place(x=x, anchor="n")
         x -= (self.__const_real_width  / self.__x_axis_section_count)   
         
         
   def __destroy_y_x_sections(self)->None:
      for widget in self.__output_frame.winfo_children():
         if type(widget) == tkinter.Frame:
            widget.place_forget()
            widget.destroy()
   
         
   def configure(self, width=False, height=False, y_axis_max_value=False, x_axis_values=None, axis_size=False,
                  y_axis_precision=False,
                  x_axis_data=False, data_font_style=False, axis_font_style=False,
                  bg_color=False, axis_color=False, fg_color=False,
                  y_axis_font_color=False, x_axis_font_color=False,
                  y_axis_data_font_color=False, x_axis_data_font_color=False,
                  y_axis_data=False, y_axis_label_count=None, x_axis_label_count=None,
                  y_axis_section_count=None, x_axis_section_count=None, section_color=False,
                  line_width=False,
                  x_axis_data_position=None, y_axis_data_position=None,
                  y_space=None, x_space=None)->None:  
         
      chart_reset_req = False
      fg_color_change_req = False
      chart_y_values_change_req = False
      chart_x_values_change_req = False
      chart_sections_change_req = False

         
      if width:
         if width != self.__width:
            self.__width = width
            chart_reset_req = True
      
      if height:
         if height != self.__height:
            self.__height = height
            chart_reset_req = True
            
      if y_space != None:
         if y_space != self.__y_space:
            self.__y_space = y_space
            chart_reset_req = True
      
      if x_space != None:
         if x_space != self.__x_space:
            self.__x_space = x_space
            chart_reset_req = True
      
      if y_axis_max_value:
         if y_axis_max_value != self.__y_axis_max_value:
            self.__y_axis_max_value = y_axis_max_value
            chart_reset_req = True
      
      if axis_size:
         if axis_size != self.__axis_size:
            self.__axis_size = axis_size
            chart_reset_req = True
            
      """if type(x_values_decimals) != bool:
         if x_values_decimals != self.__x_values_decimals:
            self.__x_values_decimals = x_values_decimals
            chart_reset_req = True"""
      
      if type(y_axis_precision) != bool:
         if y_axis_precision != self.__y_axis_precision:
            self.__y_axis_precision = y_axis_precision
            chart_reset_req = True
      
      if x_axis_data!=False:
         if x_axis_data != self.__x_axis_data:
            self.__x_axis_data = x_axis_data
            chart_reset_req = True
            
      if data_font_style:
         if data_font_style != self.__data_font_style:
            self.__data_font_style = data_font_style
            chart_reset_req = True
            
      if axis_font_style:
         if axis_font_style != self.__axis_values_font:
            self.__axis_values_font = axis_font_style
            chart_reset_req = True
      
      if bg_color:
         if bg_color != self.__bg_color:
            self.__bg_color = bg_color
            fg_color_change_req = True
            
      if axis_color:
         if axis_color != self.__axis_color:
            self.__axis_color = axis_color
            fg_color_change_req = True
            
      if fg_color:
         if fg_color != self.__fg_color:
            self.__fg_color = fg_color
            fg_color_change_req = True
            
      if bg_color:
         if bg_color != self.__bg_color:
            self.__bg_color = bg_color
            fg_color_change_req = True
            
      if y_axis_font_color:
         if y_axis_font_color != self.__y_axis_font_color:
            self.__y_axis_font_color = y_axis_font_color
            fg_color_change_req = True
            
      if x_axis_font_color:
         if x_axis_font_color != self.__x_axis_font_color:
            self.__x_axis_font_color = x_axis_font_color
            fg_color_change_req = True
            
      if y_axis_data_font_color:
         if y_axis_data_font_color != self.__y_axis_data_font_color:
            self.__y_axis_data_font_color = y_axis_data_font_color
            fg_color_change_req = True
            
      if x_axis_data_font_color:
         if x_axis_data_font_color != self.__x_axis_data_font_color:
            self.__x_axis_data_font_color = x_axis_data_font_color
            fg_color_change_req = True

      if section_color:
         if section_color != self.__section_color:
            self.__section_color = section_color
            fg_color_change_req = True
            
      if y_axis_label_count!=None:
         if y_axis_label_count != self.__y_axis_label_count:
            self.__y_axis_label_count = y_axis_label_count
            chart_y_values_change_req = True
      
      if x_axis_label_count!=None:
         if x_axis_label_count != self.__x_axis_label_count:
            self.__x_axis_label_count = x_axis_label_count
            chart_x_values_change_req = True
      
      if x_axis_section_count!=None:
         if x_axis_section_count != self.__x_axis_section_count:
            self.__x_axis_section_count = x_axis_section_count
            chart_sections_change_req = True
            
      if y_axis_section_count!=None:
         if y_axis_section_count != self.__y_axis_section_count:
            self.__y_axis_section_count = y_axis_section_count
            chart_sections_change_req = True
      
      if x_axis_data_position!=None:
         if x_axis_data_position != self.__x_axis_data_position:
            self.__x_axis_data_position = x_axis_data_position
            chart_reset_req = True
            
      if y_axis_data_position!=None:
         if y_axis_data_position != self.__y_axis_data_position:
            self.__y_axis_data_position = y_axis_data_position
            chart_reset_req = True
      
      if y_axis_data != False:
         if y_axis_data != self.__y_axis_data:
            self.__y_axis_data = y_axis_data
            chart_reset_req = True
            
      if x_axis_values != None:
         if x_axis_values != self.__x_axis_values:
            if len(x_axis_values) != len(self.__x_axis_values):
               chart_reset_req = True
            elif self.__get_max_required_label_width(x_axis_values,self.__axis_values_font)!=self.__x_value_req_width_space:
               chart_reset_req = True 
            else:
               self.__x_axis_values = x_axis_values
               self.__set_x_axis_values()
            self.__x_axis_values = x_axis_values
         
      if line_width :
         if line_width != self.__line_width:
            self.__line_width = line_width
            self.__get_line_width()
            self.__call_to_re_show_data()
            
      if chart_reset_req :
         self.__destroy_y_axis_labels()
         self.__destroy_x_axis_labels()
         self.__destroy_y_x_sections()
         
         self.__line_width = "auto"
         self.__get_required_widget_size()
         self.__place_widget()
         self.__get_line_width()
         self.__create_y_axis_labels()
         self.__create_x_axis_labels()
         self.__create_y_sections()
         self.__create_x_sections()
         self.__set_widget_colors()
         self.__set_widget_font()
         self.__set_widget_text()
         self.__set_x_axis_values()
         self.__reset_chart_info()
   
         self.__call_to_re_show_data()
         
      if fg_color_change_req :
         self.__set_widget_colors()
      if chart_y_values_change_req:
         self.__destroy_y_axis_labels()
         self.__create_y_axis_labels()
         self.__set_widget_colors()
         self.__set_widget_font()
         self.__set_widget_text()
         self.__set_x_axis_values()
      if chart_x_values_change_req:
         self.__fix_x_axis_label_count()
         self.__destroy_x_axis_labels()
         self.__create_x_axis_labels()
         self.__set_widget_colors()
         self.__set_widget_font()
         self.__set_widget_text()
         self.__set_x_axis_values()
      if chart_sections_change_req:
         self.__destroy_y_x_sections()
         self.__create_y_sections()
         self.__create_x_sections()

   
   def __reset_chart_info(self)->None:
      self.__output_canvas.delete("all")
      self.__real_width = self.__width - (self.__y_value_req_width_space+self.__axis_size+self.__x_axis_data_req_width_space_top+self.__y_axis_data_req_width_space_side+\
                                          (self.__x_value_req_width_space/2)+self.__x_special_width_space+self.__x_space)
      
      self.__const_real_width = self.__real_width 
      self.__real_height = self.__height - (self.__y_axis_data_req_height_space_top+self.__axis_size+self.__x_value_req_height_space+self.__x_axis_data_req_height_space_side+\
                                          (self.__y_value_req_height_space/2)+self.__y_special_height_space+self.__y_space)
      self.__real_height = self.__real_height
      
      self.__const_real_height = self.__real_height 
      
      self.__output_canvas.place(y=0, x=0, height=self.__const_real_height, width=self.__const_real_width)
      self.__place_x = 0
      
   def __reset_lines_info(self):
      for line in  self.__lines:
         line._Line__reset()
   
   def __call_to_re_show_data(self):
      self.__force_to_stop_data_showing = True
      while  self.__is_data_showing_working:
         pass
      self.__force_to_stop_data_showing = False
      self.__re_show_data()
      
      
   def __re_show_data(self)->None:
      lines_values = [len(line._Line__data) for line in  self.__lines]
      if len(lines_values) > 0:
         self.__reset_chart_info()
         
         maximum_data = max(lines_values)
         max_support = int(self.__real_width/self.__line_width)+1
         
         for line in  self.__lines:
            if maximum_data>max_support:
               line._Line__temp_data = line._Line__data[maximum_data-(max_support)::]
            else:
               line._Line__temp_data = line._Line__data
            line._Line__reset()
         
         lines = self.__lines
         self.lines =[]
         
         for line in lines:
            self.show_data(line=line, data=line._Line__temp_data)
   
   
   def show_data(self, line:Line, data:list)->None:
      re_show_data = False
      if line not in self.__lines:
         self.__lines.append(line)
      line._Line__data += data
      
      if line._Line__hide_state != True :
         for d in data:
            self.__is_data_showing_working = True
            
            if not self.__force_to_stop_data_showing:
               x_start = line._Line__x_end
               y_start = line._Line__y_end
      
               line._Line__x_end += self.__line_width
               line._Line__y_end = (self.__real_height - (self.__real_height/100)*(d/self.__y_axis_max_value*100))  + (line._Line__size)
               
               if line._Line__x_end > self.__real_width and self.__real_width < 20000:
                  self.__place_x -= self.__line_width
                  
                  self.__output_canvas.place(x=self.__place_x,
                                    width=self.__real_width+self.__line_width)
                  
                  self.__real_width += self.__line_width;
               
               elif self.__real_width > 15000:
                  re_show_data = True
                  break;
               
               if line._Line__style  == "dashed" :
                  dash_width = line._Line__style_type[0]
                  space_width = line._Line__style_type[1]
                  total_width = dash_width+space_width
                  real_line_width = ((abs(y_start - line._Line__y_end)**2) + (self.__line_width**2)) ** (1/2)
                  dash_count = real_line_width /( dash_width + space_width)
                  #space_count = real_line_width /( dash_width + space_width)
                  total_change_x = (line._Line__x_end - x_start)
                  total_change_y = (line._Line__y_end - y_start)
                  dash_change_percentage = dash_width/total_width
                  space_change_percentage = space_width/total_width
                  """print(str(dash_change_percentage)+"%" ,str(space_change_percentage)+"%")"""
                  change_x = (total_change_x/dash_count)
                  change_y = (total_change_y/dash_count)
                  dash_change_x = change_x*dash_change_percentage
                  dash_change_y = change_y*dash_change_percentage
                  space_change_x = change_x*space_change_percentage
                  space_change_y = change_y*space_change_percentage
                  if y_start >  line._Line__y_end: line_going = "to_up"
                  else : line_going = "to_down"
                  
                  while (line._Line__x_end>x_start):
                     x_end = x_start+dash_change_x
                     y_end = y_start+dash_change_y
                     if x_end>line._Line__x_end:
                           x_end = x_end - (x_end-line._Line__x_end)
                     if y_end<=line._Line__y_end and line_going=="to_up":
                           y_end = y_end - (y_end-line._Line__y_end)
                     if y_end>line._Line__y_end and  line_going=="to_down":
                           y_end = y_end - (y_end-line._Line__y_end)
                     self.__output_canvas.create_line(x_start, y_start, x_end, y_end
                                                      ,fill=line._Line__color ,width=line._Line__size)
                     x_start += dash_change_x + space_change_x
                     y_start += dash_change_y + space_change_y
                        
               elif line._Line__style == "dotted":
                  circle_size = line._Line__style_type[0]
                  space_width = line._Line__style_type[1]
                  total_width = circle_size+space_width
                  real_line_width = ((abs(y_start - line._Line__y_end)**2) + (self.__line_width**2)) ** (1/2)
                  circle_count = real_line_width /( circle_size + space_width)
                  #space_count = real_line_width /( circle_size + space_width)
                  total_change_x = (line._Line__x_end - x_start)
                  total_change_y = (line._Line__y_end - y_start)
                  circle_change_percentage = circle_size/total_width*100
                  space_change_percentage = space_width/total_width*100
                  """print(str(circle_change_percentage)+"%" ,str(space_change_percentage)+"%")"""
                  circle_change_x = (total_change_x/circle_count)/100*circle_change_percentage
                  circle_change_y = (total_change_y/circle_count)/100*circle_change_percentage
                  space_change_x = (total_change_x/circle_count)/100*space_change_percentage
                  space_change_y = (total_change_y/circle_count)/100*space_change_percentage
                  if y_start >  line._Line__y_end: line_going = "to_up"
                  else : line_going = "to_down"
                  while (line._Line__x_end>x_start):
                        x_end = x_start+circle_change_x
                        y_end = y_start+circle_change_y
                        if x_end>line._Line__x_end:
                           x_end = x_end - (x_end-line._Line__x_end)
                        if y_end<=line._Line__y_end and line_going=="to_up":
                           y_end = y_end - (y_end-line._Line__y_end)
                        if y_end>line._Line__y_end and  line_going=="to_down":
                           y_end = y_end - (y_end-line._Line__y_end)
                        self.__output_canvas.create_oval(x_start-circle_size/2,
                                                   y_start-circle_size/2,
                                                   x_start+circle_size-circle_size/2,
                                                   y_start+circle_size-circle_size/2,
                                                   fill=line._Line__color, outline=line._Line__color )
                        x_start += circle_change_x + space_change_x
                        y_start += circle_change_y + space_change_y
               elif line._Line__style=="line":
                  self.__output_canvas.create_line(x_start, y_start, line._Line__x_end, line._Line__y_end
                                                      ,fill=line._Line__color ,width=line._Line__size)
            else:
               break
         
         if re_show_data:
            self.__re_show_data()
         self.__is_data_showing_working = False
      
      
   def place(self, x=None, y=None, rely=None, relx=None, anchor=None)->None:
      self.__main_frame.place(x=x, y=y, rely=rely, relx=relx, anchor=anchor)
      self.__place_info_x = x
      self.__place_info_y = y
      self.__place_info_rely = rely
      self.__place_info_relx = relx
      self.__place_info_anchor = anchor
      
      
   def pack(self, pady=None, padx=None, before=None, after=None,
            side=None, anchor=None)->None:
      self.__main_frame.pack(pady=pady, padx=padx, before=before, 
                after=after, side=side, anchor=anchor)
      self.__pack_info_pady = pady
      self.__pack_info_padx = padx
      self.__pack_info_before = before
      self.__pack_info_after = after
      self.__pack_info_side = side
      self.__pack_info_anchor = anchor
      
      
   def grid(self, column=None, columnspan=None, padx=None,  pady=None, row=None, 
            rowspan=None, sticky=None)->None:
      self.__main_frame.grid(column=column, columnspan=columnspan, 
               padx=padx,  pady=pady, row=row, rowspan=rowspan, sticky=sticky)
      self.__grid_info_column = column
      self.__grid_info_columnspan = columnspan
      self.__grid_info_padx = padx
      self.__grid_info_pady = pady
      self.__grid_info_row = row
      self.__grid_info_rowspan = rowspan
      self.__grid_info_sticky = sticky
      
      
   def place_forget(self)->None:
      self.__main_frame.place_forget()
      
      
   def pack_forget(self)->None:
      self.__main_frame.pack_forget()
      
      
   def grid_forget(self)->None:
      self.__main_frame.grid_forget()
      
      
   def place_back(self)->None:
      self.__main_frame.place(x=self.__place_info_x, y=self.__place_info_y,
                              rely=self.__place_info_rely, relx=self.__place_info_relx,
                              anchor=self.__place_info_anchor)
      
      
   def pack_back(self)->None:
      self.__main_frame.pack(pady=self.__pack_info_pady, padx=self.__pack_info_padx,
                             before=self.__pack_info_before, after=self.__pack_info_after,
                             side=self.__pack_info_side, 
                             anchor=self.__pack_info_anchor)
      
      
   def grid_back(self)->None:
      self.__main_frame.grid(column=self.__grid_info_column, columnspan=self.__grid_info_columnspan, 
                           padx=self.__grid_info_padx,  pady=self.__grid_info_pady,
                           row=self.__grid_info_row, rowspan=self.__grid_info_rowspan, sticky=self.__grid_info_sticky)
      
      
   def hide(self, line:Line, state:bool)->None:
      if line._Line__hide_state != state:
         line._Line__hide_state = state
         self.__re_show_data()
      
      
   def hide_all(self,state:bool)->None:
      if state == True:
         self.__output_canvas.place_forget()
      self.__force_to_stop_data_showing = True
      while self.__is_data_showing_working :
            pass
      for line in self.__lines:
         line._Line__hide_state = state
      self.__force_to_stop_data_showing = False
      self.__re_show_data()
   
   def reset(self):
      self.__reset_chart_info()
      self.__reset_lines_info()
      