         
class Line():
   def __init__(self ,*args ,master=None ,color="#909090" ,size=1):
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
   

   def configure(self , color=None ,size=None) :
      if color != None:
         self.__color = color
      if size != None:
         self.__size = size
   
   def __reset(self):
      self.__y_end = 0
      self.__x_end  = self.__chart._LineChart__line_width* -1
      self.__data = []
