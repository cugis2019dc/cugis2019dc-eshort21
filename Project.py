# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:45:34 2019

@author: STEM
"""

# project data actually used
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go

wodf = pandas.read_excel("GISdataES.xlsx",sheet_name = "cancercases")

cancercases = go.Bar(x= wodf["CancerType"],y=wodf["Number"],marker = {"color":wodf["Number"], "colorscale":"sunset"})
titles= go.Layout(title = "Cancer Cases", xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Type of Cancer")),yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Number of Cases",)))
fig = go.Figure(data=[cancercases], layout=titles)
plot(fig)
plot([cancercases])
