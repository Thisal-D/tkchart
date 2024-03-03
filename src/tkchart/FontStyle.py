#include <iostream>
class FontStyle:
    def _get_font_style_code( fg_color , bg_color , style):
        colors_count = 16 ; 
        colors_data = [
                            ["black"   ,"30" ,"40" ] ,
                            ["gray"    ,"90" ,"100"] ,
                            ["red"     ,"31" ,"41" ] ,
                            ["green"   ,"32" ,"42" ] ,
                            ["yellow"  ,"33" ,"43" ] ,
                            ["blue"    ,"34" ,"44" ] ,
                            ["Magenta" ,"35" ,"45" ] ,
                            ["cyan"    ,"36" ,"46" ] ,
                            ["white"   ,"37" ,"47" ] ,
                            ["bright red"     ,"91" ,"101"] ,
                            ["bright green"   ,"92" ,"102"] ,
                            ["bright yellow"  ,"93" ,"103"] ,
                            ["bright blue"    ,"94" ,"104"] ,
                            ["bright magenta" ,"95" ,"105"] ,
                            ["bright cyan"    ,"96" ,"106"] ,
                            ["bright white"   ,"97" ,"107"] ,
                        ] 

    
        for index in range(0, colors_count):
            if (fg_color==colors_data[index][0]):
                fgcolor_code = colors_data[index][1] ;
            
            if (bg_color==colors_data[index][0]):
                bgcolor_code = colors_data[index][2] ;
                
        styles_count = 3 ; 
        styles_code = [
                        ["normal"    ,"0"],
                        ["italic"    ,"3"],
                        ["underline" ,"4"]
                    ] ;
    
        for index in range(0,styles_count):
            if (style==styles_code[index][0]):
                style_code = styles_code[index][1] 
        
        font_code_ = "\x1b[" + style_code + ";" + fgcolor_code   + ";" + bgcolor_code + "m" ;

        return font_code_ ;

    def _fontStyle(text ,fg_color ,bg_color="black" ,style="normal"):
        output_text = FontStyle._get_font_style_code(fg_color ,bg_color ,style) + text + "\x1b[0m" ; 
        return output_text ;