import math
import numpy as np
from pandas import DataFrame, Series

import plotly.graph_objs as go


# ---- for price
def log(l, slot=False):
    for x in l:
        x += 1
        if slot: 
            result = math.ceil(math.log(x, 2))
        else: 
            result = math.log(x, 2)
        yield result

def price_scale(l, n=500):
    for x in l:
        if x > n: yield n
        else: yield x
            
def avg(l):
    return sum(l)/len(l)

def median(l):
    l = np.array(l)
    return np.median(l)   


# ---- for brand
def brand_None(x):
    try: # x is str
        len(x)
        return x
    except: # x is NaN
        return "None"

def brand_dict2Series(d):
    brand, price = list(zip(*d.items()))
    result = Series(list(price), index=list(brand))
    result = result.sort_values(ascending=False)
    return result

def brand_box_plot(d, show=None):
    """brand vs price box plot
    input:
        d = dictionary {brand_name: [price1, price2, .....]}
        show = only show N instances in the plot (show all if None)
    output:
        fig = brand vs price box plot
    """
    data = []
    counter = 0
    for k, v in d.items():
        data.append( go.Box(y=v, name=k) )
        counter += 1
        if counter == 10: break
            
    layout= go.Layout(
        title= 'Brand vs Price box plot',
        hovermode= 'closest',
        xaxis= dict(
            title= 'Brand Name',
            ticklen= 5,
            zeroline= False,
            gridwidth= 2,
        ),
        yaxis=dict(
            title= 'Price',
            ticklen= 5,
            gridwidth= 2,
        ),
        showlegend= False
    )
    fig= go.Figure(data=data, layout=layout)
    return fig

def brand_median_price_plot(S, top_n=None):
    """brand name versus median price scatter plot
    input:
        S = Series([brand_median_price], index=brand_name)
        top_n = only list most top_n expensive brand (list all brand if None)
    output:
        fig = brand name versus median price scatter plot
    """
    trace = go.Scatter(
        x = S.index[:top_n],
        y = S.values[:top_n],
        mode = 'markers'
    )

    layout= go.Layout(
        title= 'Top {} Expensive Brand'.format(top_n),
        hovermode= 'closest',
        xaxis= dict(
            title= 'Brand Name',
            ticklen= 5,
            zeroline= False,
            gridwidth= 2,
        ),
        yaxis=dict(
            title= 'Median Price',
            ticklen= 5,
            gridwidth= 2,
        ),
        showlegend= False
    )
    fig= go.Figure(data=[trace], layout=layout)
    return fig