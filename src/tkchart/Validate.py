from typing import Tuple
from .FontStyle import FontStyle
import tkinter

class Validate:

    def _error_font(value: str) -> str:
        return FontStyle._fontStyle(value, "red", "black", "underline")


    def _var_font(value:str) -> str:
        return FontStyle._fontStyle(value, "green", "black", "italic")


    def _isTuple(value: any, var: str) -> None:
        if type(value) != tuple:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be tuple.')}"
            )
            
            
    def _isList(value: any, var: str) -> None:
        if type(value) != list:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be list.')}"
            )
            
            
    def _isInt(value: any, var: str) -> None:
        if type(value) != int:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be int.')}"
            )
    

    def _isBool(value: any, var: str) -> None:
        if type(value) != bool:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be bool.')}"
            )


    def _isFloat(value: any, var: str) -> None:
        if type(value) != float:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be float.')}"
            )


    def _isStr(value: any, var: str) -> None:
        if type(value) != str:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be str.')}"
            )


    def _isNumeric(value: any, var: str) -> None:
        if type(value) == int or type(value) == float:
            ...
        else:
            raise TypeError(
                f"{Validate._var_font(var)} {Validate._error_font('must be int or float.')}"
            )
            

    def _isValidColor(value: any, var: str) -> None:
        Validate._isStr(value, var)
        try:
            tkinter.Label(fg=value)
        except:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be valid color. eg:- '#ff0000'/ 'red'")}'''
            )


    def _isValidFont(value: any, var: str) -> None:
        Validate._isTuple(value, var)
        try:
            tkinter.Label(font=value)
        except:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be valid font. eg:- ('arial',10,'bold')")}'''
            )
            

    def _isValidFunction(value: any, var: str) -> None:
        if not callable(value) and value != None:
            raise TypeError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be function with two parameters or *args.")}'''
            )


    def _isValidXAxisIndices(values: Tuple[int, ...], indices: any, var: str) -> None:
        if indices != None:
            Validate._isTuple(indices, var)
            Validate._isValidIndices(indices, var)
            for index in indices:
                if index >= len(values):
                    raise ValueError(
                        f'''{Validate._var_font(var)} {Validate._error_font("values must be lower than length of x_axis_values.")}'''
                    )


    def _isValidXAxisLabelCount(values: any, var: str) -> None:
        if values != None:
            Validate._isInt(values, var)


    def _isValidStyleType(value: any, var: str) -> None:
        Validate._isTuple(value, var)
        if len(value) == 2:
            if type(value[0]) == int and type(value[1]) == int:
                ...
            else:
                raise TypeError(
                    f'''{Validate._var_font(var)} {Validate._error_font("values must be integers.")}'''
                )
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("length must be two.")}'''
            )
        

    def _isValidDataPostion(value: any, var: str) -> None:
        Validate._isStr(value, var)
        if value == "top" or value == "side":
            ...
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be 'top' or 'side'.")}'''
            )


    def _isValidLineStyle(value: any, var: str) -> None:
        Validate._isStr(value, var)
        if value == "dotted" or value == "dashed" or value == "normal":
            ...
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be 'normal' or 'dotted' or 'dashed'.")}'''
            )


    def _isValidSectionStyle(value: any, var: str) -> None:
        Validate._isStr(value, var)
        if value == "dashed" or value == "normal":
            ...
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be 'normal' or 'dashed'.")}'''
            )


    def _isValidXAxisPointSpacing(value: any, var: str) -> None:
        if type(value) == int:
            ...
        elif type(value) == str and value == "auto":
            ...
        else:
            raise TypeError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be integer or 'auto'.")}'''
            )


    def _isValidPointerState_Lock(value: any, var: str) -> None:
        Validate._isStr(value, var)
        if value == "disabled" or value == "enabled":
            ...
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be 'disabled' or 'enabled'.")}'''
            )
              
              
    def _isValidLineHighlight(value: any, var: str) -> None:
        Validate._isStr(value, var)
        if value == "disabled" or value == "enabled":
            ...
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be 'disabled' or 'enabled'.")}'''
            )
            
            
    def _isValidLineFill(value: any, var: str) -> None:
        Validate._isStr(value, var)
        if value == "disabled" or value == "enabled":
            ...
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be 'disabled' or 'enabled'.")}'''
            )
            
            
    def _isValidYAxisValues(value: any, var: str) -> None:
        Validate._isTuple(value, var)
        if value == (None,None):
            raise ValueError(
                        f'''{Validate._var_font(var)} {Validate._error_font("must be provide.")}'''
                    )
        if len(value) == 2:
            if type(value[0]) == int or type(value[0]) == float and type(
                    value[1]) == int or type(value[1]) == float:
                if value[0] < value[1]:
                    ...
                else:
                    raise ValueError(
                        f'''{Validate._var_font(var)} {Validate._error_font("first value must be less than second value.")}'''
                    )
            else:
                raise TypeError(
                    f'''{Validate._var_font(var)} {Validate._error_font("values must be integer or float.")}'''
                )
        else:
            raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("length must be two.")}'''
            )
            
            
    def _isValidXAxisValues(value: any, var: str) -> None:
        if value == (None, "None", None, "None"):
            raise ValueError(
                        f'''{Validate._var_font(var)} {Validate._error_font("must be provide.")}'''
                    )
        Validate._isTuple(value, "x_axis_values")


    def _isValidYAxisMaxValue(value: any, var: str) -> None:
        Validate._isNumeric(value, var)
        if value == 0:
            raise TypeError(
                f'''{Validate._var_font(var)} {Validate._error_font("must be less than 0 or bigger than 0")}'''
            )
    
    
    def _isValidLine(value: any, var: str) -> None:
        from .Line import Line
        if type(value) != Line:
            raise TypeError(
                f'''{Validate._var_font(var)} {Validate._error_font("type must be tkchart.Line")}'''   
            )
            
            
    def _isValidLineChart(value: any, var: str) -> None:
        from .LineChart import LineChart
        if type(value) != LineChart:
            raise TypeError(
                f'''{Validate._var_font(var)} {Validate._error_font("type must be tkchart.LineChart")}'''   
            )
            
            
    def _isValidData(value: any, var: str) -> None:
        Validate._isList(value, var)
        if all(isinstance(value, (int, float)) for value in value):
            ...
        else:
            raise TypeError(
                f'''{Validate._var_font(var)} {Validate._error_font("all values in the list should be either int or float.")}'''
            )

    
    def _isValidIndices(value: any, var: str) -> None:
        if all(isinstance(value, (int)) for value in value):
            ...
        else:
            raise TypeError(
                f'''{Validate._var_font(var)} {Validate._error_font("all values should be int.")}'''
            )
            
            
    def _invalidCget(var: str) -> None:
        raise ValueError(
                f'''{Validate._var_font(var)} {Validate._error_font("Invalid attribute.")}'''
            )