         
class Line():
   def __init__(self ,*arg ,master=None ,color="#ffffff" ,height=1):
      try :
         chart = arg[0]
      except:
         chart = master

      self.line_color = color
      self.line_height = height
      self.y_end = 0
      self.x_end  = chart.chart_line_len*-1
      self.values = []
   
   def configure(self , color=None ,height=None) :
      if color != None:
         self.line_color = color
      if height != None:
         self.line_height = height
