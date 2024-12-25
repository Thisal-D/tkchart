from .Validate import *

class Line():
   def __init__(self,
                master = None,
                color: str = "#909090",
                size: int = 1,
                style: str = "normal", 
                style_type: tuple[int, int] = (10,5),
                *args: any
                ) -> None:
      
      Validate._isValidColor(color, "color")
      Validate._isInt(size, "size")
      Validate._isValidLineStyle(style, "style")
      Validate._isValidStyleType(style_type, "style_type")
      
      try :
         self.__master = args[0]
      except:
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


   def configure(self, 
                 color: str = None, 
                 size: int = None,
                 style: str = None,
                 style_type: tuple[int, int] = None
                 ) -> None:
      
      if color != None:
         Validate._isValidColor(color, "color")
      if size != None:
         Validate._isInt(size, "size")
      if style != None:
         Validate._isValidLineStyle(style, "style")
      if style_type != None:
         Validate._isValidStyleType(style_type, "style_type")
      
      if color != None: 
         self.__color = color
      if size != None:
         self.__size = size
         
      if style != None:
         self.__style = style
      if style_type != None:
         self.__style_type = style_type
   
   
   def __reset(self) -> None:
      self.__y_end = 0
      self.__x_end  = self.__master._LineChart__line_width* -1
      self.__data = []


