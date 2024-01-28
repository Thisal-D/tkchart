         
class Line():
   def __init__(self ,*args ,master=None ,color="#909090" ,size=1, mode="line", mode_style=(10,5)):
      try :
         self.__chart = args[0]
      except:
         self.__chart = master

      self.__color = color
      self.__size = size
      self.__y_end = 0
      self.__x_end  = self.__chart._LineChart__line_width* -1
      self.__data = []
      self.__temp_data = []
      self.__hide_state = False
      
      
      self.__mode = mode
      self.__mode_style = mode_style
 

   def configure(self , color=None ,size=None, mode=None, mode_style=None) :
      if color != None:
         self.__color = color
      if size != None:
         self.__size = size
         
      if mode != None:
         self.__mode = mode
      if mode_style != None:
         self.__mode_style = mode_style
   
   
   def __reset(self):
      self.__y_end = 0
      self.__x_end  = self.__chart._LineChart__line_width* -1
      self.__data = []
