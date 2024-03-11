from typing import Union, Tuple
from .Validate import Validate
from .FontStyle import FontStyle

class Line():
   def __init__(self,
               master: any = None,
               color: str = "#909090",
               size: int = 1,
               style: str = "normal", 
               style_type: Tuple[int, int] = (10,5),
               point_highlight: str = "disabled",
               point_highlight_size: int = 0,
               point_highlight_color: str = "#909090",
               *args: any
               ) -> None:
      
      Validate._isValidColor(color, "color")
      Validate._isInt(size, "size")
      Validate._isValidLineStyle(style, "style")
      Validate._isValidStyleType(style_type, "style_type")
      Validate._isValidLineHighlight(point_highlight, "point_highlight")
      Validate._isInt(point_highlight_size, "point_highlight_size")
      Validate._isValidColor(point_highlight_color, "point_highlight_color")
      if master == None:
         if len(args) != 0:
            master = args[0]
         else:
            raise ValueError(f'''{FontStyle._fontStyle("master","green", "black", "italic")} {FontStyle._fontStyle("parameter value is not provided", "red", "black", "underline")}''')
      Validate._isValidLineChart(master, "master")
      
      self.__master = master
      self.__color = color
      self.__size = size
      self.__y_end = 0
      self.__x_end  = self.__master._LineChart__line_width* -1
      self.__data = []
      self.__temp_data = []
      self.__ret_data = []
      self.__hide_state = False
      self.__style = style
      self.__style_type = style_type
      self.__point_highlight = point_highlight
      self.__point_highlight_size = point_highlight_size
      self.__point_highlight_color = point_highlight_color


   def configure(self, 
                  color: str = None, 
                  size: int = None,
                  style: str = None,
                  style_type: Tuple[int, int] = None,
                  point_highlight: str = None,
                  point_highlight_size: int = None,
                  point_highlight_color: str = None,
                 ) -> None:
      
      if color != None:
         Validate._isValidColor(color, "color")
         self.__color = color
         
      if size != None:
         Validate._isInt(size, "size")
         self.__size = size
         
      if style != None:
         Validate._isValidLineStyle(style, "style")
         self.__style = style
         
      if style_type != None:
         Validate._isValidStyleType(style_type, "style_type")
         self.__style_type = style_type
         
      if point_highlight != None:
         Validate._isValidLineHighlight(point_highlight, "point_highlight")
         self.__point_highlight = point_highlight
         
      if point_highlight_size != None:
         Validate._isInt(point_highlight_size, "point_highlight_size")
         self.__point_highlight_size = point_highlight_size
         
      if point_highlight_color != None:
         Validate._isValidColor(point_highlight_color, "point_highlight_color")
         self.__point_highlight_color = point_highlight_color
         
   
   def __reset(self) -> None:
      self.__y_end = 0
      self.__x_end  = self.__master._LineChart__line_width* -1
      self.__data = []