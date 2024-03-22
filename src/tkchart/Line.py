from typing import Union, Tuple
from .Validate import Validate
from .FontStyle import FontStyle


class Line():
   def __init__(self,
               master: any = None,
               color: str = "#768df1",
               size: int = 1,
               style: str = "normal", 
               style_type: Tuple[int, int] = (4,4),
               point_highlight: str = "disabled",
               point_highlight_size: int = 4,
               point_highlight_color: str = "#768df1",
               fill: str = "disabled",
               fill_color: str = "#5d6db6",
               *args: any
               ) -> None:
      """
      Initialize a Line object.

         Args:
            master (LineChart): The master object.
            color (str): The color of the line.
            size (int): The size/thickness of the line.
            style (str): The style of the line (e.g., 'normal', 'dashed', 'dotted').
            style_type (Tuple[int, int]): The style type for dashed or dotted lines.
            point_highlight (str): Whether point highlighting is enabled or disabled.
            point_highlight_size (int): The size of points used for highlighting.
            point_highlight_color (str): The color of points used for highlighting.
            fill (str): Whether fill for the line is enabled or disabled.
            fill_color (str): The color of the fill for the line.
      """
      
      if master == None:
         if len(args) != 0:
            master = args[0]
         else:
            raise ValueError(f'''{FontStyle._fontStyle("master","green", "black", "italic")} {FontStyle._fontStyle("parameter value is not provided", "red", "black", "underline")}''')
      
      Validate._isValidLineChart(master, "master")
      Validate._isValidColor(color, "color")
      Validate._isInt(size, "size")
      Validate._isValidLineStyle(style, "style")
      Validate._isValidStyleType(style_type, "style_type")
      Validate._isValidLineHighlight(point_highlight, "point_highlight")
      Validate._isInt(point_highlight_size, "point_highlight_size")
      Validate._isValidColor(point_highlight_color, "point_highlight_color")
      Validate._isValidLineFill(fill, "fill")
      Validate._isValidColor(fill_color, "fill_color")
      
      self.__master = master
      self.__color = color
      self.__size = size
      self.__y_end = 0
      self.__x_end  = self.__master._LineChart__x_axis_point_spacing* -1
      self.__data = []
      self.__temp_data = []
      self.__ret_data = []
      self.__hide_state = False
      self.__style = style
      self.__style_type = style_type
      self.__point_highlight = point_highlight
      self.__point_highlight_size = point_highlight_size
      self.__point_highlight_color = point_highlight_color
      self.__fill = fill
      self.__fill_color = fill_color


   def configure(self, 
                  color: str = None, 
                  size: int = None,
                  style: str = None,
                  style_type: Tuple[int, int] = None,
                  point_highlight: str = None,
                  point_highlight_size: int = None,
                  point_highlight_color: str = None,
                  fill: str = None,
                  fill_color:str = None,
                 ) -> None:
      """
      Configure attributes of the Line object.

         Args:
            color (str): The color of the line.
            size (int): The size/thickness of the line.
            style (str): The style of the line (e.g., 'normal', 'dashed', 'dotted').
            style_type (Tuple[int, int]): The style type for dashed or dotted lines.
            point_highlight (str): Whether point highlighting is enabled or disabled.
            point_highlight_size (int): The size of points used for highlighting.
            point_highlight_color (str): The color of points used for highlighting.
            fill (str): Whether fill for the line is enabled or disabled.
            fill_color (str): The color of the fill for the line.
      """
      changes_req = False
      
      if color != None:
         Validate._isValidColor(color, "color")
         self.__color = color
         changes_req = True
         
      if size != None:
         Validate._isInt(size, "size")
         self.__size = size
         changes_req = True
         
      if style != None:
         Validate._isValidLineStyle(style, "style")
         self.__style = style
         changes_req = True
         
      if style_type != None:
         Validate._isValidStyleType(style_type, "style_type")
         self.__style_type = style_type
         changes_req = True
         
      if point_highlight != None:
         Validate._isValidLineHighlight(point_highlight, "point_highlight")
         self.__point_highlight = point_highlight
         changes_req = True
         
      if point_highlight_size != None:
         Validate._isInt(point_highlight_size, "point_highlight_size")
         self.__point_highlight_size = point_highlight_size
         changes_req = True

      if point_highlight_color != None:
         Validate._isValidColor(point_highlight_color, "point_highlight_color")
         self.__point_highlight_color = point_highlight_color
         changes_req = True
      
      if fill != None:
         Validate._isValidLineFill(fill, "fill")
         self.__fill = fill
         changes_req = True
      
      if fill_color != None:
         Validate._isValidColor(fill_color, "fill_color")
         self.__fill_color = fill_color
         changes_req = True
      
      if changes_req:
         self.__master._LineChart__apply_line_configuration()
           
   
   def __reset(self) -> None:
      """
      Reset the Line object.
      """
      self.__y_end = 0
      self.__x_end  = self.__master._LineChart__x_axis_point_spacing* -1
      self.__data = []


   def reset(self) -> None:
      """
      Reset the line.
      """
      self.__reset()
      self.__master._LineChart__call_reshow_data()

      
   def cget(self, attribute_name: str) -> any:
      """
      Get the value of a Line attribute.

         Args:
            attribute_name (str): Name of the attribute.

         Returns:
            any: Value of the attribute.
      """
      
      if attribute_name == "master": return self.__master
      if attribute_name == "color": return self.__color
      if attribute_name == "size": return self.__size
      if attribute_name == "style": return self.__style
      if attribute_name == "style_type": return self.__style_type
      if attribute_name == "point_highlight": return self.__point_highlight
      if attribute_name == "point_highlight_size": return self.__point_highlight_size
      if attribute_name == "point_highlight_color": return self.__point_highlight_color
      if attribute_name == "fill": return self.__fill
      if attribute_name == "fill_color": return self.__fill_color
      
      if attribute_name == "__all__":
         {
         "master" : self.__master,
         "color" : self.__color,
         "size" : self.__size,
         "style" : self.__style,
         "style_type" : self.__style_type,
         "point_highlight" : self.__point_highlight,
         "point_highlight_size" : self.__point_highlight_size,
         "point_highlight_color" : self.__point_highlight_color,
         "fill" : self.__fill,
         "fill_color" : self.__fill_color
         }
      Validate._invalidCget(attribute_name)