import streamlit as st
from retanguloUI import RetanguloUI

#RetanguloUI.main()
"""
import pandas as pd

px = [0, 1, 2, 3]
py = [10, 5, 15, 10]
dic = { "x" : px, "y" : py }
chart_data = pd.DataFrame(dic)
st.line_chart(chart_data, x = "x", y = "y") 

xmin = 5
xmax = 15
n = 100
d = (xmax - xmin)/n  # 0.5
px = []
py = []
x = xmin
while x < xmax:
    y = x**2 - 5*x + 6
    px.append(x)
    py.append(y)
    x = x + d
x = xmax
y = x**2 - 5*x + 6
px.append(x)
py.append(y)

dic = { "x" : px, "y" : py }
chart_data = pd.DataFrame(dic)
st.line_chart(chart_data, x = "x", y = "y") 

#delta = 5*5 - 4*1*6 = 1
#x1 = (5 + 1) / 2 = 3
#x2 = (5 - 1) / 2 = 2

"""

import pandas as pd
import numpy as np
import math
r = 10
n = 100
d = 2*r/100
pontos = []
xmin = -r
xmax = r
x = xmin
while x < xmax:
    y = math.sqrt(r**2 - x**2)
    pontos.append([x, y, -y])
    x = x + d
x = xmax
y = math.sqrt(r**2 - x**2)
pontos.append([x, y, -y])

chart_data = pd.DataFrame(pontos, columns=["x", "y1", "y2"])
st.line_chart(chart_data, x = "x", y = ["y1", "y2"] ) 

#print(np.random.randn(20, 3))
#print(pontos)









 




