import tkinter
from typing import Union, Tuple, List
from .Utils import Utils
from .Validate import Validate
from .FontStyle import FontStyle
from .Line import Line

class LineChart():
   def __init__(self,
                  master: any = None,
                  width: int = 700,
                  height: int = 400,
                  axis_size: int = 2,
                  
                  axis_color: str = "#909090",
                  bg_color: str = "#303030",
                  fg_color: str = "#252525",
                  data_font_style: Tuple[str, int, str] = ("arial", 9, "normal"),
                  axis_font_style: Tuple[str, int, str] = ("arial", 9, "normal"),
                  
                  y_axis_precision: int = 1,
                  y_axis_data: any = "Y",
                  y_axis_label_count: int = 5,
                  y_axis_values: Tuple[Union[int, float], Union[int, float]] = (None, None),
                  y_axis_font_color: str = "#909090",
                  y_axis_data_font_color: str = "#909090",
                  y_axis_data_position: str = "top",
                  y_axis_section_count: int = 0,
                  y_axis_section_style: str = "normal",
                  y_axis_section_style_type: Tuple[int, int] = (100, 50),
                  y_axis_section_color: str = None,
                  
                  x_axis_data: str = "X",
                  x_axis_label_count: int = None,
                  x_axis_values: Tuple[any, ...] = (1, 2, 3, 4, 5),
                  x_axis_display_values_indices: Tuple[int, ...] = None,
                  x_axis_font_color: str = "#909090",
                  x_axis_data_font_color: str = "#cccccc",
                  x_axis_data_position: str = "top",
                  x_axis_section_count: int=0,
                  x_axis_section_style: str = "normal",
                  x_axis_section_style_type: Tuple[int, int] = (100, 50),
                  x_axis_section_color: str = None,
                  
                  line_width: Union[int, str] = "auto",
                  y_space: int = 0, 
                  x_space: int = 0,
                  
                  pointer_state: str = "disabled",
                  pointing_callback_function: callable = None,
                  pointer_color: str = "#606060",
                  pointing_values_precision: int = 1,
                  pointer_lock: str = "disabled",
                  pointer_size: int = 4,
                  *args: any,
                  
                  ########DEPRECATED#########
                  y_axis_max_value:int = None,
                  section_color:str = None,
                  ###########################
                  ) -> None:
      
      Validate._isInt(height, "height")
      Validate._isInt(width, "width")
      Validate._isInt(axis_size, "axis_size")
      Validate._isInt(y_space, "y_space")
      Validate._isInt(x_space, "x_space")
      Validate._isInt(y_axis_precision, "y_axis_precision")
      Validate._isInt(y_axis_label_count, "y_axis_label_count")
      Validate._isInt(y_axis_section_count, "y_axis_section_count")
      Validate._isInt(x_axis_section_count, "x_axis_section_count")
      Validate._isInt(pointing_values_precision, "pointing_values_precision")
      Validate._isInt(pointer_size, "pointer_size")
      Validate._isTuple(x_axis_values, "x_axis_values")
      ####################################################ENABLE  2024.3.30####################################################
      #Validate._isValidYAxisValues(y_axis_values, "y_axis_values")
      #Validate._isValidColor(y_axis_section_color, "y_axis_section_color")
      #Validate._isValidColor(x_axis_section_color, "x_axis_section_color")
      ####################################################ENABLE  2024.3.30####################################################
      Validate._isValidColor(axis_color, "axis_color")
      Validate._isValidColor(bg_color, "bg_color")
      Validate._isValidColor(fg_color, "fg_color")
      Validate._isValidColor(y_axis_font_color, "y_axis_font_color")
      Validate._isValidColor(x_axis_font_color, "x_axis_font_color")
      Validate._isValidColor(y_axis_data_font_color, "y_axis_data_font_color")
      Validate._isValidColor(x_axis_data_font_color, "x_axis_data_font_color")
      Validate._isValidColor(pointer_color, "pointer_color")
      Validate._isValidFont(data_font_style, "data_font_style")
      Validate._isValidFont(axis_font_style, "axis_font_style")
      Validate._isValidDataPostion(y_axis_data_position, "y_axis_data_position")
      Validate._isValidDataPostion(x_axis_data_position, "x_axis_data_position")
      Validate._isValidStyleType(y_axis_section_style_type, "y_axis_section_style_type")
      Validate._isValidStyleType(x_axis_section_style_type, "x_axis_section_style_type")
      Validate._isValidSectionStyle(y_axis_section_style, "y_axis_section_style")
      Validate._isValidSectionStyle(x_axis_section_style, "x_axis_section_style")
      Validate._isValidLineWidth(line_width, "line_width")
      Validate._isValidPointerState_Lock(pointer_state, "pointer_state")
      Validate._isValidPointerState_Lock(pointer_lock, "pointer_lock")
      Validate._isValidFunction(pointing_callback_function, "pointing_callback_function")
      Validate._isValidXAxisIndices(x_axis_values, x_axis_display_values_indices, "x_axis_display_values_indices")
      Validate._isValidXAxisLabelCount(x_axis_label_count, "x_axis_label_count")
      
      ####################################################REMOVE  2024.3.30####################################################
      y_axis_values_set_using = "y_axis_values"
      if y_axis_max_value  != None:
         if y_axis_values == (None, None):
            y_axis_values_set_using = "y_axis_max_value"
            Validate._isValidYAxisMaxValue(y_axis_max_value, "y_axis_max_value")
            print(FontStyle._fontStyle("\ny_axis_max_value : ", "red", "black", "normal"), end = "") 
            print(FontStyle._fontStyle("Parameter is deprecated & not support to configure, it will be removed soon.", "red", "black", "underline"))
            print(FontStyle._fontStyle("Use", "red", "black", "underline") 
                  + FontStyle._fontStyle(" y_axis_values ", "green", "black", "italic") 
                  + FontStyle._fontStyle("instead.", "red", "black", "underline"))
         else:
            Validate._isValidYAxisValues(y_axis_values, "y_axis_values")
      elif y_axis_values == (None, None):
            y_axis_values = (-10,10)
      else:
         Validate._isValidYAxisValues(y_axis_values, "y_axis_values")
      
      section_color_set_using = "y_x_axis_section_color"
      if section_color != None:
         if x_axis_section_color == None and y_axis_section_color == None:
            section_color_set_using = "section_color"
            Validate._isValidColor(section_color, "section_color")
            print(FontStyle._fontStyle("\nsection_color : ", "red", "black", "normal"), end = "") 
            print(FontStyle._fontStyle("Parameter is deprecated & not support to configure, it will be removed soon.", "red", "black", "underline"))
            print(FontStyle._fontStyle("Use", "red", "black", "underline") + FontStyle._fontStyle(" y_axis_section_color ", "green", "black", "italic") 
                  + FontStyle._fontStyle("&", "red", "black", "underline")
                  + FontStyle._fontStyle(" x_axis_section_color ", "green", "black", "italic") 
                  + FontStyle._fontStyle("instead.", "red", "black", "underline"))
         else:
            if x_axis_section_color != None:
               Validate._isValidColor(x_axis_section_color, "x_axis_section_color")
            else:
               x_axis_section_color = "#909090"
   
            if y_axis_section_color != None:
               Validate._isValidColor(y_axis_section_color, "y_axis_section_color") 
            else:
               y_axis_section_color = "#909090"
      else:
         if x_axis_section_color == None:
            x_axis_section_color = "#909090"
         else :
            Validate._isValidColor(x_axis_section_color, "x_axis_section_color")
            
         if y_axis_section_color == None:
            y_axis_section_color = "#909090"
         else:
            Validate._isValidColor(y_axis_section_color, "y_axis_section_color")
      ####################################################REMOVE  2024.3.30####################################################

      if master != None:
         self.master = master
      elif len(args) != 0:
         self.master = args[0]
      else:
         self.master = master
   
      self.__height = height
      self.__width = width
      self.__axis_size = axis_size
      self.__axis_color = axis_color   
      self.__line_width = line_width
      self.__line_width_handle_by = "auto"
      self.__data_font_style = data_font_style
      self.__axis_font_style = axis_font_style
      self.__lines = []
      
      self.__bg_color = bg_color
      self.__fg_color = fg_color
      self.__y_axis_font_color = y_axis_font_color
      self.__y_axis_data_font_color = y_axis_data_font_color
      ####################################################ENABLE  2024.3.30####################################################
      #self.__y_axis_section_color = y_axis_section_color
      ####################################################ENABLE  2024.3.30####################################################
      self.__y_axis_section_style = y_axis_section_style
      self.__y_axis_section_style_type = y_axis_section_style_type
      self.__y_axis_section_count = y_axis_section_count
      self.__y_axis_label_count = y_axis_label_count
      self.__y_axis_data = y_axis_data
      self.__y_axis_data_position = y_axis_data_position
      self.__y_axis_values = y_axis_values
      
      ####################################################ENABLE  2024.3.30####################################################
      #self.__y_axis_min_value = y_axis_values[0]
      #self.__y_axis_max_value = y_axis_values[1]
      ####################################################ENABLE  2024.3.30####################################################
      
      ####################################################REMOVE  2024.3.30####################################################
      if y_axis_values_set_using == "y_axis_values" :
         self.__y_axis_min_value = y_axis_values[0]
         self.__y_axis_max_value = y_axis_values[1]
      else:
         if y_axis_max_value>0:
            self.__y_axis_min_value = 0
            self.__y_axis_max_value = y_axis_max_value
         elif y_axis_max_value <0:
            self.__y_axis_max_value = 0
            self.__y_axis_min_value = y_axis_max_value
            
      if section_color_set_using == "section_color":
         self.__y_axis_section_color = section_color
         self.__x_axis_section_color = section_color
      else:
         self.__y_axis_section_color = y_axis_section_color
         self.__x_axis_section_color = x_axis_section_color
      ####################################################REMOVE  2024.3.30####################################################
         
      self.__y_axis_precision = y_axis_precision
      self.__y_space = y_space
      
      self.__x_axis_font_color = x_axis_font_color
      self.__x_axis_data_font_color = x_axis_data_font_color
      ####################################################ENABLE  2024.3.30####################################################
      #self.__x_axis_section_color = x_axis_section_color
      ####################################################ENABLE  2024.3.30####################################################
      self.__x_axis_section_style = x_axis_section_style
      self.__x_axis_section_style_type = x_axis_section_style_type
      self.__x_axis_section_count = x_axis_section_count
      self.__x_axis_label_count = x_axis_label_count
      self.__x_axis_display_values_indices = x_axis_display_values_indices
      self.__x_labels_values_index_change = 1
      self.__x_axis_data = x_axis_data
      self.__x_axis_data_position = x_axis_data_position
      self.__x_axis_values = x_axis_values
      self.__x_axis_values_handle_by = "auto"
      self.__x_space = x_space
        	
      self.__force_to_stop_data_showing = False
      self.__is_data_showing_working = False
      
      self.__pointer_state = pointer_state
      self.__pointing_callback_function = pointing_callback_function
      self.__pointing_values_precision = pointing_values_precision
      self.__pointer_lock = pointer_lock
      self.__pointer_size = pointer_size
      self.__pointer_color = pointer_color

      self.__place_x = 0
      self.__real_height = 0
      self.__real_width = 0
      self.__const_real_height = 0
      self.__const_real_width = 0
      
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
      
      
      if self.__line_width == "auto":
         self.__line_width_handle_by = "auto"
      else:
         self.__line_width_handle_by = "manual"
      
      if  self.__x_axis_display_values_indices != None :
         self.__x_axis_display_values_indices = Utils._sort_tuple(self.__x_axis_display_values_indices)
         self.__x_axis_values_handle_by = "label_indices"
      elif self.__x_axis_label_count != None:
         self.__x_axis_values_handle_by = "label_count"
      else:
         self.__x_axis_values_handle_by = "auto"
      

      self.__create_widgets()
      
      self.__configure_required_widget_size()
      self.__configure_x_axis_labels_info()
      self.__configure_line_width()
      
      self.__create_x_axis_labels()
      self.__set_x_axis_values()
      
      self.__create_y_axis_labels()
      self.__set_y_axis_values()
         
      self.__create_y_axis_sections()
      self.__create_x_axis_sections()
      
      self.__set_x_y_axis_data_texts()
      
      self.__set_pointer_state()
      self.__set_pointer_size()
   
      self.__set_widgets_fonts()
      self.__set_widgets_colors()
      
      self.__place_widgets()
      self.__reset_chart_info()
      
   def __create_widgets(self) -> None:
      self.__main_frame = tkinter.Frame(master=self.master)
      self.__y_axis_frame = tkinter.Frame(master=self.__main_frame)
      self.__x_axis_frame = tkinter.Frame(master=self.__main_frame)
      self.__x_axis_values_frame = tkinter.Frame(master=self.__main_frame)
      self.__y_axis_values_frame = tkinter.Frame(master=self.__main_frame)
      self.__y_axis_data_label = tkinter.Label(master=self.__main_frame)
      self.__x_axis_data_label = tkinter.Label(master=self.__main_frame)
      self.__output_frame = tkinter.Frame(master=self.__main_frame)
      self.__output_canvas = tkinter.Canvas(master=self.__output_frame, highlightthickness=0)
      self.__pointer = tkinter.Frame(master=self.__output_canvas)
   
   def __set_pointer_state(self) -> None:
      if self.__pointer_state == "enabled":
         self.__output_canvas.bind("<Leave>",self.__hide_pointer)
         self.__output_canvas.bind("<Motion>",self.__return_pointed_values)
      elif self.__pointer_state == "disabled":
         self.__output_canvas.unbind("<Leave>")
         self.__output_canvas.unbind("<Motion>")
   
   
   def __set_widgets_colors(self) -> None:
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
         
      self.__pointer.configure(bg=self.__pointer_color)
      
   
   def __set_widgets_fonts(self) -> None:
      self.__y_axis_data_label.configure(font=self.__data_font_style)
      self.__x_axis_data_label.configure(font=self.__data_font_style)
      
      for label in self.__y_axis_values_frame.winfo_children() :
         if type(label) == tkinter.Label:
            label.configure(font=self.__axis_font_style)
      
      for label in self.__x_axis_values_frame.winfo_children()  :
         if type(label) == tkinter.Label:
            label.configure(font=self.__axis_font_style)


   def __set_pointer_size(self) -> None:
      self.__pointer.configure(width=self.__pointer_size)
      self.__pointer.config(height=self.__const_real_height)
      
      
   def __place_widgets(self) -> None:
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
                         y=float(self.__y_axis_data_req_height_space_top+(self.__y_value_req_height_space/2)+self.__y_special_height_space),
                         height=self.__const_real_height+self.__y_space+self.__axis_size)
      self.__x_axis_frame.place(x=self.__y_value_req_width_space+self.__y_axis_data_req_width_space_side,
                         rely=1,
                         y=-self.__axis_size+-self.__x_value_req_height_space+-self.__x_axis_data_req_height_space_side,
                         width=self.__const_real_width+self.__axis_size+self.__x_space)
      
      self.__output_frame.place(x=self.__y_value_req_width_space+self.__axis_size+self.__y_axis_data_req_width_space_side,
                                width=self.__const_real_width,
                                height=self.__const_real_height,
                                y=float(self.__y_axis_data_req_height_space_top+(self.__y_value_req_height_space/2)+self.__y_special_height_space+self.__y_space))
      
      
      self.__output_canvas.place(y=0, x=0, height=self.__const_real_height, width=self.__const_real_width)
      
      self.__y_axis_values_frame.place(x=self.__y_axis_data_req_width_space_side, width=self.__y_value_req_width_space, height=self.__height)
      self.__x_axis_values_frame.place(x=0, rely=1, y=-self.__x_value_req_height_space+-self.__x_axis_data_req_height_space_side, height=self.__x_value_req_height_space, width=self.__width)


   def __configure_line_width(self) -> None:
      if self.__line_width_handle_by== "auto":
         self.__line_width = (self.__real_width / len(self.__x_axis_values))
      elif self.__line_width_handle_by== "manual":
         self.__line_width = self.__line_width
     
      
   def __configure_required_widget_size(self) -> None:
      self.__x_axis_data_req_width_space_top = 0
      self.__x_axis_data_req_height_space_side = 0
      self.__x_axis_data_req_height = Utils._RequiredHeight(text=self.__x_axis_data, font=self.__data_font_style)
      self.__x_axis_data_req_width = Utils._RequiredWidth(text=self.__x_axis_data, font=self.__data_font_style)
      self.__x_special_width_space = 0
      if self.__x_axis_data_position == "top":
         self.__x_special_width_space = 30
         self.__x_axis_data_req_width_space_top = Utils._RequiredWidth(text=self.__x_axis_data, font=self.__data_font_style)
      else:
         self.__x_axis_data_req_height_space_side = Utils._RequiredHeight(text=self.__x_axis_data, font=self.__data_font_style)
      
      self.__y_axis_data_req_height_space_top = 0
      self.__y_axis_data_req_height = Utils._RequiredHeight(text=self.__y_axis_data, font=self.__data_font_style)
      self.__y_axis_data_req_width = Utils._RequiredWidth(text=self.__y_axis_data, font=self.__data_font_style)
      self.__y_special_height_space = 0
      self.__y_axis_data_req_width_space_side = 0
      if self.__y_axis_data_position == "top":
         self.__y_special_height_space = 30
         self.__y_axis_data_req_height_space_top = Utils._RequiredHeight(text=self.__y_axis_data[0], font=self.__data_font_style)
      else:
         self.__y_axis_data_req_width_space_side = Utils._RequiredWidth(text=self.__y_axis_data[0], font=self.__data_font_style)
      
      if self.__y_axis_label_count == 0:
         self.__y_value_req_height_space = 1
         self.__y_value_req_width_space = 1
      else:
         if len(Utils._format_float_with_precision(self.__y_axis_max_value, self.__y_axis_precision)) > len(Utils._format_float_with_precision(self.__y_axis_min_value, self.__y_axis_precision)) :
            y_value_temp = self.__y_axis_max_value
         else:
            y_value_temp = self.__y_axis_min_value
         self.__y_value_req_height_space = Utils._RequiredHeight(text=Utils._format_float_with_precision(y_value_temp, self.__y_axis_precision), font=self.__axis_font_style)
         self.__y_value_req_width_space = Utils._RequiredWidth(text=Utils._format_float_with_precision(y_value_temp, self.__y_axis_precision), font=self.__axis_font_style)
         
      self.__x_value_req_height_space = Utils._RequiredHeight(text=self.__x_axis_values[0], font=self.__axis_font_style)
      #self.__x_value_req_width_space = RequiredWidth(text=format_float_with_precision(self.__x_axis_data_max, self.__x_values_decimals), font=self.__axis_font_style) 
      self.__x_value_req_width_space = Utils._get_max_required_label_width(data=self.__x_axis_values, font=self.__axis_font_style)
      
      self.__real_width = self.__width - (self.__y_value_req_width_space+self.__axis_size+self.__x_axis_data_req_width_space_top+self.__y_axis_data_req_width_space_side+\
                                          (self.__x_value_req_width_space/2)+self.__x_special_width_space+self.__x_space)
      
      self.__const_real_width = self.__real_width 
      self.__real_height = self.__height - (self.__y_axis_data_req_height_space_top+self.__axis_size+self.__x_value_req_height_space+self.__x_axis_data_req_height_space_side+\
                                          (self.__y_value_req_height_space/2)+self.__y_special_height_space+self.__y_space)
      self.__real_height = self.__real_height  
      
      self.__const_real_height = int(self.__real_height)
      
      self.__y_axis_values_gap = abs(self.__y_axis_max_value - self.__y_axis_min_value)
      

   def __set_x_y_axis_data_texts(self) -> None:
      if self.__y_axis_data_position=="top":
         self.__y_axis_data_label.configure(text=self.__y_axis_data)
      else:
         self.__y_axis_data_label.configure(text="\n".join(self.__y_axis_data))
      self.__x_axis_data_label.configure(text=self.__x_axis_data)
   
   
   def __set_y_axis_values(self) -> None:
      if self.__y_axis_label_count>0:
         for i,label in enumerate(self.__y_axis_values_frame.winfo_children()):
            value = (self.__y_axis_max_value - ((self.__y_axis_values_gap)/self.__y_axis_label_count)*i)
            if self.__y_axis_min_value == 0 and i==self.__y_axis_label_count:
               value = 0
            value = Utils._format_float_with_precision(value,self.__y_axis_precision)
            label.configure(text=value)
            
   def __create_y_axis_labels(self) -> None:
      if self.__y_axis_label_count>0:
         y = self.__y_axis_data_req_height_space_top+(self.__y_value_req_height_space/2)+self.__y_special_height_space+self.__y_space
         for i in range(self.__y_axis_label_count+1):
            tkinter.Label(master=self.__y_axis_values_frame, justify="right" ).place(y=y, x=0,
                                                                          anchor="w" ,width=self.__y_value_req_width_space)
            y += self.__real_height/self.__y_axis_label_count 
            
            
   def __destroy_y_axis_labels(self) -> None:
      for y_value in self.__y_axis_values_frame.winfo_children():
         y_value.place_forget()
         y_value.destroy()
         
   
   def __set_x_axis_values_using_label_count(self) -> None:
      index = -1
      for label in (self.__x_axis_values_frame.winfo_children()):
         value = self.__x_axis_values[index]
         index -= self.__x_labels_values_index_change
         label.configure(text=value)
         
         
   def __set_x_axis_values_using_indices(self) -> None:
      index = -1
      for label in (self.__x_axis_values_frame.winfo_children()):
         value =  self.__x_axis_values[self.__x_axis_display_values_indices[index]]
         index -= 1
         label.configure(text=value)
         

   def __create_x_axis_labels_using_label_count(self) -> None:
      x = self.__width - self.__x_axis_data_req_width_space_top-(self.__x_value_req_width_space/2)-self.__x_special_width_space - self.__x_space
      for i in range(self.__x_axis_label_count):
         tkinter.Label(master=self.__x_axis_values_frame).place(rely=1, y=-self.__x_value_req_height_space, x=x, anchor="n")
         x -= self.__const_real_width / self.__x_axis_label_count
         
         
   def __create_x_axis_labels_using_indices(self) -> None:
      x = self.__width - self.__x_axis_data_req_width_space_top-(self.__x_value_req_width_space/2)-self.__x_special_width_space - self.__x_space
      for i in range(self.__x_axis_label_count):
         if  (self.__x_axis_label_count-(i+1)) in  self.__x_axis_display_values_indices:
            tkinter.Label(master=self.__x_axis_values_frame).place(rely=1, y=-self.__x_value_req_height_space, x=x, anchor="n")
         x -= self.__const_real_width / self.__x_axis_label_count
         
   
   def __create_x_axis_labels(self) -> None:
      if self.__x_axis_values_handle_by == "label_indices":
         self.__create_x_axis_labels_using_indices()
      else:
         self.__create_x_axis_labels_using_label_count()
      
         
   def __set_x_axis_values(self) -> None:
      if self.__x_axis_values_handle_by == "label_indices":
         self.__set_x_axis_values_using_indices()
      else:
         self.__set_x_axis_values_using_label_count()
   
   
   def __destroy_x_axis_labels(self) -> None:
      for x_value in self.__x_axis_values_frame.winfo_children():
         x_value.place_forget()
         x_value.destroy()
         
      
   def __configure_x_axis_labels_info(self) -> None:
      if self.__x_axis_values_handle_by == "label_indices" : 
         self.__x_axis_label_count = len(self.__x_axis_values)
        
      elif self.__x_axis_values_handle_by=="auto":
         self.__x_axis_label_count=len(self.__x_axis_values)
         self.__x_labels_values_index_change = 1
         
      elif self.__x_axis_values_handle_by=="label_count":
         if self.__x_axis_label_count == 0:
            return
         x_axis_real_label_count = len(self.__x_axis_values)
         if self.__x_axis_label_count > x_axis_real_label_count:
            self.__x_axis_label_count = x_axis_real_label_count
         while x_axis_real_label_count%self.__x_axis_label_count != 0:
            self.__x_axis_label_count+=1
         self.__x_labels_values_index_change = int(x_axis_real_label_count/self.__x_axis_label_count)
            
            
   def __create_y_axis_sections(self) -> None:
      y = 0
      if self.__y_axis_section_style == "normal":
         for i in range(self.__y_axis_section_count):
            tkinter.Frame(master=self.__output_frame, height=1, width=self.__const_real_width, bg=self.__y_axis_section_color).place(y=y, anchor="w")
            y += self.__real_height/self.__y_axis_section_count
      else:
         width_ = self.__y_axis_section_style_type[0] 
         space_ = self.__y_axis_section_style_type[1]
         for i in range(self.__y_axis_section_count):
            x_ = self.__const_real_width-width_
            while x_ > -(width_+space_) :
               tkinter.Frame(master=self.__output_frame, height=1, width=width_, bg=self.__y_axis_section_color).place(y=y, anchor="w", x=x_)
               x_ -= width_ + space_
            y += self.__real_height/self.__y_axis_section_count
     
         
   def __create_x_axis_sections(self) -> None:
      x = self.__const_real_width - 1
      if  self.__x_axis_section_style == "normal":
         for i in range(self.__x_axis_section_count):
            tkinter.Frame(master=self.__output_frame, height=self.__const_real_height, width=1 ,bg=self.__x_axis_section_color).place(x=x, anchor="n")
            x -= (self.__const_real_width  / self.__x_axis_section_count) 
      else:
         height_ = self.__x_axis_section_style_type[0] 
         space_ = self.__x_axis_section_style_type[1]
         for i in range(self.__x_axis_section_count):
            y_ = 0
            while y_ < self.__const_real_height :
               tkinter.Frame(master=self.__output_frame, height=height_, width=1 ,bg=self.__x_axis_section_color).place(x=x, anchor="n", y=y_)
               y_ += height_ + space_
            x -= (self.__const_real_width  / self.__x_axis_section_count) 
      

   def __destroy_x_y_sections(self) -> None:
      for widget in self.__output_frame.winfo_children():
         if type(widget) == tkinter.Frame :
            widget.place_forget()
            widget.destroy()
               
         
   def configure(self,
                  width: int = None,
                  height: int = None,
                  axis_size: int = None,
                  line_width: Union[int, str] = None, 
                  
                  bg_color: str = None,
                  axis_color: str = None,
                  fg_color: str = None,
                  data_font_style: Tuple[str, int, str] = None,
                  axis_font_style: Tuple[str, int, str] = None,
            
                  y_axis_values: Union[int, float]=None,
                  y_axis_precision: int = None,
                  y_axis_font_color: str = None,
                  y_axis_data_font_color: str = None,
                  y_axis_section_count: int = None,
                  y_axis_section_color: str = None,
                  y_axis_section_style: str = None,
                  y_axis_section_style_type: Tuple[int, int] = None,
                  y_axis_label_count: int=None,
                  y_axis_data: any = None,
                  y_axis_data_position: str = None,
                  y_space: int = None,
                  
                  x_axis_values: Tuple[any, ...] = None,
                  x_axis_data: any = None,
                  x_axis_font_color: str = None,
                  x_axis_data_font_color: str = None,
                  x_axis_label_count: int = None,
                  x_axis_section_count: int = None,
                  x_axis_section_style: str = None,
                  x_axis_section_style_type: Tuple[int, int] = None,
                  x_axis_section_color: str = None,
                  x_axis_display_values_indices: Tuple[int, ...] = None,
                  x_axis_data_position: str = None,
                  x_space: int = None ,
                  
                  pointer_state: str = None,
                  pointing_values_precision: int = None,
                  pointer_color: str = None, 
                  pointer_lock: str = None,
                  pointing_callback_function: callable = None, 
                  pointer_size: int = None
                  ) -> None:  
         
      chart_reset_req = False
      widget_color_change_req = False
      widget_size_change_req = False
      widget_font_change_req = False
      chart_y_values_change_req = False
      chart_x_values_change_req = False
      chart_sections_change_req = False
      chart_sections_color_change_req = False
      chart_x_labels_change_req = False
      chart_y_labels_change_req = False
      pointer_state_change_req = False
      pointer_size_change_req = False
      reshow_data_req = False
         
      if width != None:
         Validate._isInt(width, "width")
         if width != self.__width:
            self.__width = width
            chart_reset_req = True
      
      if height != None:
         Validate._isInt(height, "height")
         if height != self.__height:
            self.__height = height
            chart_reset_req = True
            
      if y_space != None:
         Validate._isInt(y_space, "y_space")
         if y_space != self.__y_space:
            self.__y_space = y_space
            chart_reset_req = True
      
      if x_space != None:
         Validate._isInt(x_space, "x_space")
         if x_space != self.__x_space:
            self.__x_space = x_space
            chart_reset_req = True
      
      if y_axis_values != None:
         Validate._isValidYAxisValues(y_axis_values, "y_axis_values")
         if y_axis_values != self.__y_axis_values:
            self.__y_axis_values = y_axis_values
            self.__y_axis_min_value = y_axis_values[0]
            self.__y_axis_max_value = y_axis_values[1]
            chart_reset_req = True
      
      if axis_size != None:
         Validate._isInt(axis_size, "axis_size")
         if axis_size != self.__axis_size:
            self.__axis_size = axis_size
            chart_reset_req = True
      
      if y_axis_precision != None:
         Validate._isInt(y_axis_precision, "y_axis_precision")
         if y_axis_precision != self.__y_axis_precision:
            self.__y_axis_precision = y_axis_precision
            chart_reset_req = True
      
      if x_axis_data != None:
         if x_axis_data != self.__x_axis_data:
            self.__x_axis_data = x_axis_data
            chart_reset_req = True
            
      if data_font_style != None:
         Validate._isValidFont(data_font_style, "data_font_style")
         if data_font_style != self.__data_font_style:
            self.__data_font_style = data_font_style
            chart_reset_req = True
            
      if axis_font_style != None:
         Validate._isValidFont(axis_font_style, "axis_font_style")
         if axis_font_style != self.__axis_font_style:
            self.__axis_font_style = axis_font_style
            chart_reset_req = True
      
      if bg_color != None:
         Validate._isValidColor(bg_color, "bg_color")
         if bg_color != self.__bg_color:
            self.__bg_color = bg_color
            widget_color_change_req = True
            
      if axis_color != None:
         Validate._isValidColor(axis_color, "axis_color")
         if axis_color != self.__axis_color:
            self.__axis_color = axis_color
            widget_color_change_req = True
            
      if fg_color != None:
         Validate._isValidColor(fg_color, "fg_color")
         if fg_color != self.__fg_color:
            self.__fg_color = fg_color
            widget_color_change_req = True
            
      if y_axis_font_color != None:
         Validate._isValidColor(y_axis_font_color, "y_axis_font_color")
         if y_axis_font_color != self.__y_axis_font_color:
            self.__y_axis_font_color = y_axis_font_color
            widget_color_change_req = True
            
      if x_axis_font_color != None:
         Validate._isValidColor(x_axis_font_color, "x_axis_font_color")
         if x_axis_font_color != self.__x_axis_font_color:
            self.__x_axis_font_color = x_axis_font_color
            widget_color_change_req = True
            
      if y_axis_data_font_color != None:
         Validate._isValidColor(y_axis_data_font_color, "y_axis_data_font_color")
         if y_axis_data_font_color != self.__y_axis_data_font_color:
            self.__y_axis_data_font_color = y_axis_data_font_color
            widget_color_change_req = True
            
      if x_axis_data_font_color != None:
         Validate._isValidColor(x_axis_data_font_color, "x_axis_data_font_color")
         if x_axis_data_font_color != self.__x_axis_data_font_color:
            self.__x_axis_data_font_color = x_axis_data_font_color
            widget_color_change_req = True

      if x_axis_section_color != None:
         Validate._isValidColor(x_axis_section_color, "x_axis_section_color")
         if x_axis_section_color != self.__x_axis_section_color:
            self.__x_axis_section_color = x_axis_section_color
            chart_sections_color_change_req = True
      
      if y_axis_section_color != None:
         Validate._isValidColor(y_axis_section_color, "y_axis_section_color")
         if y_axis_section_color != self.__y_axis_section_color:
            self.__y_axis_section_color = y_axis_section_color
            chart_sections_color_change_req = True
      
      if y_axis_section_style != None:
         Validate._isValidSectionStyle(y_axis_section_style, "y_axis_section_style")
         if y_axis_section_style != self.__y_axis_section_style:
            self.__y_axis_section_style = y_axis_section_style
            chart_sections_change_req = True
      
      if x_axis_section_style != None:
         Validate._isValidSectionStyle(x_axis_section_style, "x_axis_section_style")
         if x_axis_section_style != self.__x_axis_section_style:
            self.__x_axis_section_style = x_axis_section_style
            chart_sections_change_req = True
            
      if y_axis_section_style_type != None:
         Validate._isValidStyleType(y_axis_section_style_type, "y_axis_section_style_type")
         if y_axis_section_style_type != self.__y_axis_section_style_type:
            self.__y_axis_section_style_type = y_axis_section_style_type
            chart_sections_change_req = True
      
      if x_axis_section_style_type != None:
         Validate._isValidStyleType(x_axis_section_style_type, "x_axis_section_style_type")
         if x_axis_section_style_type != self.__x_axis_section_style_type:
            self.__x_axis_section_style_type = x_axis_section_style_type
            chart_sections_change_req = True
      
      if y_axis_label_count!=None:
         Validate._isInt(y_axis_label_count, "y_axis_label_count")
         if y_axis_label_count != self.__y_axis_label_count:
            if y_axis_label_count == 0 or self.__y_axis_label_count == 0:
               chart_reset_req = True
            self.__y_axis_label_count = y_axis_label_count
            chart_y_labels_change_req = True
            widget_color_change_req = True
      
      if x_axis_section_count!=None:
         Validate._isInt(x_axis_section_count, "x_axis_section_count")
         if x_axis_section_count != self.__x_axis_section_count:
            self.__x_axis_section_count = x_axis_section_count
            chart_sections_change_req = True
         
      if y_axis_section_count!=None:
         Validate._isInt(y_axis_section_count, "y_axis_section_count")
         if y_axis_section_count != self.__y_axis_section_count:
            self.__y_axis_section_count = y_axis_section_count
            chart_sections_change_req = True
      
      if x_axis_data_position!=None:
         Validate._isValidDataPostion(x_axis_data_position, "x_axis_data_position")
         if x_axis_data_position != self.__x_axis_data_position:
            self.__x_axis_data_position = x_axis_data_position
            chart_reset_req = True
            
      if y_axis_data_position!=None:
         Validate._isValidDataPostion(y_axis_data_position, "y_axis_data_position")
         if y_axis_data_position != self.__y_axis_data_position:
            self.__y_axis_data_position = y_axis_data_position
            chart_reset_req = True
      
      if y_axis_data != None:
         if y_axis_data != self.__y_axis_data:
            self.__y_axis_data = y_axis_data
            chart_reset_req = True
            
      if x_axis_values != None:
         if x_axis_values != self.__x_axis_values:
            Validate._isTuple(x_axis_values, "x_axis_values")
            if self.__x_axis_values_handle_by == "label_indices":
               if x_axis_display_values_indices != None :
                  Validate._isValidXAxisIndices(x_axis_values, x_axis_display_values_indices, "x_axis_display_values_indices")
               else:
                  Validate._isValidXAxisIndices(x_axis_values, self.__x_axis_display_values_indices, "x_axis_display_values_indices")
            if len(x_axis_values) != len(self.__x_axis_values):
               chart_reset_req = True
            elif Utils._get_max_required_label_width(x_axis_values,self.__axis_font_style)!=self.__x_value_req_width_space:
               chart_reset_req = True
            else:
               chart_x_values_change_req = True
            self.__x_axis_values = x_axis_values
            
      if x_axis_display_values_indices!=None:
         if x_axis_values == None:
            Validate._isValidXAxisIndices(self.__x_axis_values, x_axis_display_values_indices, "x_axis_display_values_indices")
         self.__x_axis_values_handle_by = "label_indices"
         x_axis_display_values_indices = Utils._sort_tuple(x_axis_display_values_indices)
         if x_axis_display_values_indices != self.__x_axis_display_values_indices:
            self.__x_axis_display_values_indices = x_axis_display_values_indices
            chart_x_labels_change_req = True
            widget_color_change_req = True
            widget_font_change_req = True
      
      elif x_axis_label_count!=None:
         Validate._isValidXAxisLabelCount(x_axis_label_count, "x_axis_label_count")
         self.__x_axis_values_handle_by = "label_count"
         if x_axis_label_count != self.__x_axis_label_count:
            self.__x_axis_label_count = x_axis_label_count
            chart_x_labels_change_req = True
            widget_color_change_req = True
            widget_font_change_req = True
         
      if pointer_color!=None:
         Validate._isValidColor(pointer_color, "pointer_color")
         self.__pointer_color = pointer_color
         widget_color_change_req = True
      
      if pointing_callback_function != None:
         Validate._isValidFunction(pointing_callback_function, "pointing_callback_function")
         self.__pointing_callback_function = pointing_callback_function
         
      if pointing_values_precision != None:
         Validate._isInt(pointing_values_precision, "pointing_values_precision")
         self.__pointing_values_precision = pointing_values_precision
      
      if pointer_lock!=None:
         Validate._isValidPointerState_Lock(pointer_lock, "pointer_lock")
         self.__pointer_lock = pointer_lock
         
      if pointer_state!=None:
         Validate._isValidPointerState_Lock(pointer_state, "pointer_state")
         self.__pointer_state = pointer_state
         pointer_state_change_req = True
      
      if pointer_size != None:
         Validate._isInt(pointer_size, "pointer_size")
         self.__pointer_size = pointer_size
         pointer_size_change_req = True
         
      if line_width != None:
         Validate._isValidLineWidth(line_width, "line_width")
         if line_width != self.__line_width:
            if line_width == "auto":
               self.__line_width_handle_by = "auto"
            else:
               self.__line_width_handle_by = "manual"
            self.__line_width = line_width
            reshow_data_req = True
      
      if chart_reset_req :
         self.__destroy_x_axis_labels()
         self.__destroy_y_axis_labels()
   
         self.__destroy_x_y_sections()
         
         self.__configure_required_widget_size()
         self.__configure_line_width()
         
         self.__configure_x_axis_labels_info()
         self.__create_x_axis_labels()
         self.__set_x_axis_values()
         
         self.__create_y_axis_labels()
         self.__set_y_axis_values()
            
         self.__create_y_axis_sections()
         self.__create_x_axis_sections()
         
         self.__set_x_y_axis_data_texts()
         
         self.__set_pointer_state()
         self.__set_pointer_size()
      
         self.__set_widgets_fonts()
         self.__set_widgets_colors()
         
         self.__place_widgets()
         self.__reset_chart_info()
      
         self.__call_reshow_data()
      
      if chart_x_labels_change_req:
         self.__configure_x_axis_labels_info()
         self.__destroy_x_axis_labels()
         self.__create_x_axis_labels()
         self.__set_x_axis_values()
      
      elif chart_y_labels_change_req:
         self.__destroy_y_axis_labels()
         self.__create_y_axis_labels()
         self.__set_y_axis_values()
         
      if chart_x_values_change_req:
         self.__set_x_axis_values()
         
      if chart_sections_change_req or chart_sections_color_change_req:
         self.__destroy_x_y_sections()
         self.__create_y_axis_sections()
         self.__create_x_axis_sections()
            
      if widget_color_change_req :
         self.__set_widgets_colors()
      
      if widget_size_change_req == True:
         self.__set_pointer_size()
         
      if reshow_data_req:
         self.__configure_line_width()
         self.__call_reshow_data()
      
      if pointer_size_change_req:
         self.__set_pointer_size()
         
      if pointer_state_change_req:
         self.__set_pointer_state()
         
      if widget_font_change_req:
         self.__set_widgets_fonts()
   
   
   def __reset_chart_info(self) -> None:
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
      
      
   def __reset_lines_info(self) -> None:
      for line in  self.__lines:
         line._Line__reset()
   
   
   def __call_reshow_data(self) -> None:
      self.__force_to_stop_data_showing = True
      while  self.__is_data_showing_working:
         pass
      self.__force_to_stop_data_showing = False
      self.__reshow_data()
      
      
   def __reshow_data(self) -> None:
      lines_values = [len(line._Line__data) for line in  self.__lines]
      if len(lines_values) > 0:
         self.__reset_chart_info()
         
         maximum_data = max(lines_values)
         max_support = int(self.__const_real_width/self.__line_width)+1
         
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
   
   
   def show_data(self, line: Line, data: List[Union[int, float]]) -> None:
      Validate._isValidLine(line, "line")
      Validate._isValidData(data, "data")
      
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
         
               if d >=0 :
                  d = d - self.__y_axis_min_value
                  line._Line__y_end = self.__const_real_height - ((d )/self.__y_axis_values_gap * self.__const_real_height)
               else:
                  d = abs(d) +self.__y_axis_max_value
                  line._Line__y_end = ((d)/self.__y_axis_values_gap * self.__const_real_height)
               line._Line__y_end += ((line._Line__size)/2)

               if round(line._Line__x_end) > round(self.__real_width) and self.__real_width < 15000:
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
                  total_change_x = (line._Line__x_end - x_start)
                  total_change_y = (line._Line__y_end - y_start)
                  dash_change_percentage = dash_width/total_width
                  space_change_percentage = space_width/total_width
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
                  total_change_x = (line._Line__x_end - x_start)
                  total_change_y = (line._Line__y_end - y_start)
                  circle_change_percentage = circle_size/total_width*100
                  space_change_percentage = space_width/total_width*100
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
                        
               elif line._Line__style=="normal":
                  self.__output_canvas.create_line(x_start, y_start, line._Line__x_end, line._Line__y_end
                                                      ,fill=line._Line__color ,width=line._Line__size)
               
               if line._Line__style=="dashed" or line._Line__style=="normal":
                  if line._Line__point_highlight == "enabled" and line._Line__point_highlight_size > 0 : 
                     highlight_size =  line._Line__point_highlight_size /2 
                     self.__output_canvas.create_oval(line._Line__x_end - highlight_size,
                                                      line._Line__y_end - highlight_size,
                                                      line._Line__x_end + highlight_size,
                                                      line._Line__y_end + highlight_size,
                                                      fill=line._Line__point_highlight_color,
                                                      outline=line._Line__point_highlight_color,
                                                      )
            else:
               break
   
         if re_show_data:
            self.__reshow_data()
         self.__is_data_showing_working = False
   
   
   def __hide_pointer(self, event: tkinter.Event) -> None:
      self.__pointer.place_forget()
     
     
   def __return_pointed_values(self, event: tkinter.Event):
      def round_x(x):
         x_ = (x//self.__line_width)*self.__line_width
         if x%self.__line_width >= self.__line_width/2:
            x_ += self.__line_width
         return x_
      max_sup= int(self.__const_real_width/self.__line_width)
      max_view = max_sup + 1
      values = []
      try:
         max_data = max([len(line._Line__data) for line in self.__lines])
         if self.__pointer_lock=="enabled":
            event_x = round_x(event.x)
         else:
            event_x = event.x
         if self.__const_real_width >= self.__real_width:
            event_x_converted = event_x
         else:
            event_x_converted = event_x-(self.__line_width*(max_data-max_view))
         width_x = self.__const_real_width - (self.__const_real_width - (self.__line_width*max_sup))
         index_float = ((event_x_converted/width_x)*max_sup)
         index_round_float = round(index_float)
         if event_x == self.__real_width :
            self.__pointer.place(x=((event_x-self.__pointer_size/2)-2) ,y=0)
         else:
            self.__pointer.place(x=((event_x-self.__pointer_size/2)+1) ,y=0)
         index_int = int((index_float))
         x_index = index_int
         if index_float !=0  and index_float == index_int:
            x_index -= 1
         for line in self.__lines:
            line._Line__ret_data = line._Line__data + (max_data-len(line._Line__data))  * [None]
            line._Line__ret_data = line._Line__ret_data[-int(max_view)::] 
            line._Line__ret_data = line._Line__ret_data + (int(max_view) - len(line._Line__ret_data)) * [None]
         for line in self.__lines:
            try:
               if self.__pointer_lock=="enabled":
                  value = line._Line__ret_data[int(index_round_float)]
               else:
                  if index_float == index_int:
                     value = line._Line__ret_data[index_int]
                  else:
                     value = line._Line__ret_data[index_int]
                     value = value  + (((line._Line__ret_data[index_int+1] - value) * (index_float - index_int)))
               values.append(Utils._format_float_with_precision(float(value),self.__pointing_values_precision ))
            except Exception as error:
               values.append("null")
         if self.__pointing_callback_function != None:
            try:
               self.__pointing_callback_function(self.__x_axis_values[x_index],values)
            except Exception as e:
               self.__pointing_callback_function("null",values)
      except:
         pass

   def place(self,
             x: int = None,
             y: int = None,
             rely: Union[int, float] = None,
             relx: Union[int, float] = None,
             anchor: str = None
             ) -> None: 
      self.__main_frame.place(x=x, y=y, rely=rely, relx=relx, anchor=anchor)
      self.__place_info_x = x
      self.__place_info_y = y
      self.__place_info_rely = rely
      self.__place_info_relx = relx
      self.__place_info_anchor = anchor
      
      
   def pack(self,
            pady: int = None,
            padx: int = None,
            before: any = None,
            after: any = None,
            side: str = None,
            anchor: str = None
            ) -> None:
      self.__main_frame.pack(pady=pady, padx=padx, before=before, 
                after=after, side=side, anchor=anchor)
      self.__pack_info_pady = pady
      self.__pack_info_padx = padx
      self.__pack_info_before = before
      self.__pack_info_after = after
      self.__pack_info_side = side
      self.__pack_info_anchor = anchor
      
      
   def grid(self,
            column: int = None, 
            columnspan: int = None, 
            padx: int = None,  
            pady: int = None, 
            row: int = None, 
            rowspan: int = None, 
            sticky: str = None
            ) -> None:
      self.__main_frame.grid(column=column, columnspan=columnspan, 
               padx=padx,  pady=pady, row=row, rowspan=rowspan, sticky=sticky)
      self.__grid_info_column = column
      self.__grid_info_columnspan = columnspan
      self.__grid_info_padx = padx
      self.__grid_info_pady = pady
      self.__grid_info_row = row
      self.__grid_info_rowspan = rowspan
      self.__grid_info_sticky = sticky
      
      
   def place_forget(self) -> None:
      self.__main_frame.place_forget()
      
      
   def pack_forget(self) -> None:
      self.__main_frame.pack_forget()
      
      
   def grid_forget(self) -> None:
      self.__main_frame.grid_forget()
      
      
   def place_back(self) -> None:
      self.__main_frame.place(x=self.__place_info_x, y=self.__place_info_y,
                              rely=self.__place_info_rely, relx=self.__place_info_relx,
                              anchor=self.__place_info_anchor)
      
      
   def pack_back(self) -> None:
      self.__main_frame.pack(pady=self.__pack_info_pady, padx=self.__pack_info_padx,
                             before=self.__pack_info_before, after=self.__pack_info_after,
                             side=self.__pack_info_side, 
                             anchor=self.__pack_info_anchor)
      
      
   def grid_back(self) -> None:
      self.__main_frame.grid(column=self.__grid_info_column, columnspan=self.__grid_info_columnspan, 
                           padx=self.__grid_info_padx,  pady=self.__grid_info_pady,
                           row=self.__grid_info_row, rowspan=self.__grid_info_rowspan, sticky=self.__grid_info_sticky)
      
   
   def hide(self, line: Line, state: bool) -> None:
      Validate._isValidLine(state, "line")
      Validate._isBool(state, "state")
      if line._Line__hide_state != state:
         line._Line__hide_state = state
         self.__reshow_data()
      
      
   def hide_all(self, state: bool) -> None:
      Validate._isBool(state, "state")
      if state == True:
         self.__output_canvas.place_forget()
      self.__force_to_stop_data_showing = True
      while self.__is_data_showing_working :
            pass
      for line in self.__lines:
         line._Line__hide_state = state
      self.__force_to_stop_data_showing = False
      self.__reshow_data()
   
   
   def reset(self) -> None:
      self.__reset_chart_info()
      self.__reset_lines_info()