         
class Line():
   def __init__(self ,*arg ,master=None ,color="#ffffff" ,height=1 ,
                line_highlight=False ,line_highlight_size=0,line_highlight_color="#ffffff"):
      try :
         chart = arg[0]
      except:
         chart = master

      self.line_color = color
      self.line_height = height
      self.y_end = 0
      self.x_end  = chart.chart_line_len*-1
      self.values = []
      self.line_highlight = line_highlight
      self.line_highlight_size = line_highlight_size
      self.line_highlight_color = line_highlight_color
   
   def configure(self , color=None ,height=None ,line_highlight=None ,line_highlight_size=None ,line_highlight_color=None) :
      if color != None:
         self.line_color = color
      if height != None:
         self.line_height = height
         
      if line_highlight != None :
         self.line_highlight = line_highlight
        
      if line_highlight_size != None:
         self.line_highlight_size = line_highlight_size
           
      if line_highlight_color != None:
         self.line_highlight_color = line_highlight_color
 
