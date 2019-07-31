# -*- coding: utf-8 -*-
"""
def cadbury(c):
    cadbury = c+10
    
    print(cadbury)
    
cadbury(5)

def pineapple(a):
    pineapple = a+10
    
    print(pineapple)
    
pineapple(3)

cadbury=(5)
cadburyBox = cadbury +10
print(cadburyBox)

cadburyBox = 15

def cadburyBox(c):
    cadburyBox = c+5
    
    print(cadburyBox)
    
cadburyBox(15)

# different way
def cadbury(c):
    cadburyBox = c+5
    
    print(cadburyBox)
    
cadbury(15)

#chocolate
def cadburyBox(c,w,d):
    print("there is",c, ",",d,",",w, "in the box")
    
cadburyBox("white chocolate","dark chocolate", "milk chocolate")

#name
print("enter your name:")
X = input("emily")
print("hello" + X)

#age
print("enter your age:")
X = input(16)
print("your age is",+X)
"""
#library
import math

dir(math)

math.sin(60)
"""
#math library
def root(v):
    print("The cubic root of" ,v, "is",math.pow(v,(1/3)))
    
root(8)
"""
"""
#something
r = int(input("enter a value"))

def value(r):
    value = math.pow(r,1/3)
    print("the cubic root of",r, "is",value)
    
"""
'''
# boring
def columbia(c):
    columbia = 10 + c
    
    print(columbia)
    
columbia(19)
#trying
def columbia(a):
    print("the root of",a, "is" ,math.pow(a,(1/2)))
    
columbia(100)

#math library
import math
'''
'''
dir(math)
#chocolate part 2
Cadburymilk = 6
Cadburydark = 5
Cadburywhite = 8
cadbury1 = "milk chocolates"
cadbury2 = "dark chocolates"
cadbury3 = "white chocolates"
 
print("there are",Cadburymilk,cadbury1, "," ,Cadburydark,cadbury2, "and" ,Cadburywhite,cadbury3,"in the box")

#another way chocolate part 2
chocolate1 ={"cadburymilk" :5}
chocolate2 ={"cadburydark" :8}
chocolate3 ={"cadburywhite" :3}

print("There are",chocolate1,",",chocolate2,"and",chocolate3,"in the box")

#one variable chocolate
chocolatebox ={"dark":5,"milk":6,"white":8}
print(chocolatebox)
#Name and age
print("please enter your name")
N =input()
print("your name is " +N)

print("please enter your age")
A =input()
print("your age is " +A)

print("please enter you gender")
G =input()
print("your gender is "+G)
'''
#Name and age dict
studentage ={"steve":32,"lia":28,"vin":45,"katie":38}
print(studentage)
studentgender ={"steve":"m","lia":"'f","vin":"m","katie":"f"}

#list
studentlist =[['steve',32,'m'],["lia",28,"f"],["vin",45,"m"],["katie",38,"f"]]
print(studentlist)

#pandas
import pandas
dir(pandas)

#dataframe
studentdf = pandas.DataFrame(studentlist,columns=("name","age","gender"))
print(studentdf)

#refrences from columns from dataframes student
studentdf["name"]
studentdf["age"]
 #chocolate list
chocolatelist =[["milk",5,],["dark",8,],["white",3,]]
print(chocolatelist)

chocolatedf = pandas.DataFrame(chocolatelist,columns=("type","number"))
print(chocolatedf)
 
chocolatedf["type"]
chocolatedf["number"]

#refrence columns from dataframe
studentlist =[["steve",32,"m"],["laila",28,"f"],["vin",45,"m"],["katie",38,"f"]]
studentlist

import pandas
studentdf = pandas.DataFrame(studentlist,columns=("name","age","gender"),index=["1","2","3","4"])
    
print(studentdf)

import plotly
dir(plotly)

from plotly.offline import plot
import plotly.graph_objs as go

studentbar = go.Bar(x=studentdf["name"],y=studentdf["age"])
plot([studentbar])

from plotly.offline import plot
import plotly.graph_objs as go

chocolatebar = go.Bar(x=chocolatedf["type"],y=chocolatedf["number"])
plot([chocolatebar])

titles = go.Layout(title ="number of chocolates by type")

chocolatebar=go.Bar(x=chocolatedf["type"],y=chocolatedf["number"])

fig = go.Figure(data=[chocolatebar], layout=titles)
plot(fig)




















    
                

    


    

    
    
    
    
    
    
    