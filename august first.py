# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:06:16 2019

@author: STEM
"""
#import pandas
import pandas
dir(pandas)

#import math
import math
dir(math)

#i did it
math.sin(math.pi/2) 

math.sin(math.pi/6)

# project data
import pandas

dir(pandas)

import plotly

# project data actually used
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go

wodf = pandas.read_excel("GISdataES.xlsx",sheet_name = "womenOccupation")

womenoccupation = go.Bar(x= wodf["occupation"],y=wodf["women"],marker = {"color":wodf["women"], "colorscale":"picnic"})
titles= go.Layout(title = "Percentage of Women in Occuapations", xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="occupation")),yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="percentage",)))
fig = go.Figure(data=[womenoccupation], layout=titles)
plot(fig)
plot([womenoccupation])





