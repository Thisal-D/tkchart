class Line():
   def __init__(self ,*args ,master=None ,color="#909090" ,size=1, style="line", style_type=(10,5)):
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
      self.__hide_state = False
      
      
      self.__style = style
      self.__style_type = style_type
 

   def configure(self , color=None ,size=None, style=None, style_type=None) :
      if color != None:
         self.__color = color
      if size != None:
         self.__size = size
         
      if style != None:
         self.__style = style
      if style_type != None:
         self.__style_type = style_type
   
   
   def __reset(self):
      self.__y_end = 0
      self.__x_end  = self.__master._LineChart__line_width* -1
      self.__data = []