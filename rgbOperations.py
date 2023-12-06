import numpy as np


def BlendBetweenColorsWithWeight(
        color1: tuple[float,float,float],
        color2: tuple[float,float,float],
        weight: float ,
):
    """Interpolates between color1 and color2 using the the weight float, and returns the resulting color.
    weight is between 0 and 1. 1 resturns color2, 0 color1."""


    weight1 = 1-weight
    weight2 = weight

    c1Array = np.array([color1[0],color1[1],color1[2]])
    c2Array = np.array([color2[0],color2[1],color2[2]])
    
    
    newColor = (c1Array * weight1) + (c2Array * weight2)


    maxValue = max([max(color1),max(color2)]) # get the brightest value of the two colors
    valueFactor = maxValue / max(newColor) # get what color to multiply with to get that color
    newColor = newColor * valueFactor

    return (int(newColor[0]),int(newColor[1]),int(newColor[2]))



print([str(i) for i in range(10)])
    