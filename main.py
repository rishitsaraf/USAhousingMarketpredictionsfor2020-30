#!/usr/bin/env python
# coding: utf-8


# Importing the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import redis
# from flask import Flask
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image



st.set_page_config(layout="wide")
img = Image.open("./img/home.png")
st.image(img)

st.sidebar.markdown('''
# Contents
- [Introduction](#introduction)
- [Supply](#supply)
    - [Govt influenced factors](#government-influenced-factors)
    - [Seller influenced factors](#factors-influenced-by-personal-reasons-seller)
    - [Others](#factors-influenced-by-other-reasons)
- [Demand](#demand)
    - [Govt. influenced factors](#factors-influenced-by-the-government)
    - [Buyer Influenced factors](#factors-influenced-by-personal-reasons)
- [Predictions for the next decade](#predictions-for-the-next-decade)
- [Biblography](#biblography)
''', unsafe_allow_html=True)

###########################
st.header('Introduction')
col1,col2 = st.columns((1,1))
col2.write('''
With the U.S. housing market recovery gathering steam and expectations that home prices will rise, it is important to know what factors could influence residential home prices across the U.S. over the next 10 years.

Saying that the housing market is influenced by a myriad of factors could be an understatement. The entire process of reverse engineering something as complex and as complicated as a housing market requires in-depth and unbiased analysis which in turn produces credible predictive analytics.

 On the very basic level, we can distribute the factors into two categories: supply; demand. 
''')

img2 = Image.open("./img/split1.png")
col1.image(img2, use_column_width=True)

#############################
st.header('Supply')
col3,col4 = st.columns((1,1))
col3.write('''
America is facing a new housing crisis. A decade after an epic construction binge, fewer homes are being built per household than at almost any time in U.S. history.
There are several sub-factors of supply which can be categorised as: \n
1) Factors influenced by Govt. e.g. - Regulations\n
2)Factors influenced by the seller/builder (personal) e.g. - Personal incentives not to sell,  The cost of building/development.\n
3)Fators duer to other reasons e.g. - Labour Shortage \n
''')

img3 = Image.open("./img/supply.png")
col4.image(img3, use_column_width=True)
st.write('''\n
We can see here which metropolitian area needs to build more houses in order for the housing supply to keep up with the demand 
''')
col5,col6 = st.columns((1,1))
img4 = Image.open("./img/usmap2.png")
img5 = Image.open("./img/supp.jpg")
col5.header("Housing Supply and Prices over the years")
col5.image(img5, use_column_width=True)
col6.header("single-family unit permits")
col6.image(img4, use_column_width=True)
st.write('''\n
The dearth of housing supply in the United States is caused by a range of factors and varies between markets. Many urban and suburban markets suffer from a shortage of available land. Part of the shortage of available land reflects public policy decisions of municipalities about how to use land. 

''')

## Govt influenced factors
st.header("Government influenced factors")
st.write(" # Rules and Regulations")
col20,col21 = st.columns((1,1))
col20.write(''' A key factor driving limited housing supply is local zoning restrictions. For example, rigid single-family zoning, 
a practice linked with racial segregation, has prevented the construction of multi-family units, which would allow for higher 
density and an increased supply of housing. One can observe this limitation through the types of housing that have been permitted. \n \n
These supply constraints in the housing market have an impact on long-term economic growth and inequality. For instance, these constraints 
increase the cost of housing, which in turn limit labor mobility. Workers cannot afford to move to higher productivity regions that have high 
housing prices, leading them to remain in lower productivity places.

''')
imgnew = Image.open("./img/sellergovt.jpg")
col21.image(imgnew, use_column_width=True)

## Factors influenced by buyers personal reasons
st.header("Factors influenced by personal reasons seller")
st.write(" # Increasing developement costs / Personal Incentives")
col100,col101 = st.columns((1,1))
col100.write('''  Real estate developers are in need of land and capital to build new homes across the United States. This coupled with the extremely high and startling price per acre of the residential land, creates a shortage of supply. 

Sellers who want to sell their properties, have an incentive to sell later at a more inflated rate so they wait if they can to sell their properties.

''')
img100 = Image.open("./img/personalseller.jpg")
col101.image(img100, use_column_width=True)
st.write("The graph below shows the inflation till 2020")
img101 = Image.open("./img/risinghp.png")
st.image(img101, use_column_width=True)


## Factors influenced by other reasons
st.header("Factors influenced by other reasons")
st.write(''' # Labor Shortage ''')
col3,col4 = st.columns((1,1))
col3.write(''' The home construction is impeded by the labor shortage. \n

More than 2 million new construction workers are needed over the next three years \n to meet demand, according to industry experts.  
The labor shortage began in 2008 during the Great Recession. \n Older tradespeople kept retiring and fewer young people want to work with their hands. Then, training programs took a hit during the pandemic. 
It is estimated that this gap to only grow in turn leading to a drastic increase in the construction costs, further leading to lesser afordable houses. 
''')
data = {'Labor Shortage(%)':[14, 33, 40]}
chart_data = pd.DataFrame(data,index=["2010", "2020", "2030"])
col4.bar_chart(chart_data)


###############################

st.header('Demand')
col3,col4 = st.columns((1,1))
col4.write('''
The demand for houses is not only surging, but it’s doing so in the midst of a shortage of homes on the market, with supply at its lowest levels in years. The gap between demand and supply is widening at an alarming rate and driving home prices up and out of reach of many buyers searching for their dream home today.

The U.S. is short 5.24 million homes, an increase of 1.4 million from the 2019 gap of 3.84 million, according to new research from Realtor.com.
''')
img3 = Image.open("./img/demand.png")
col3.image(img3, use_column_width=True)

##govt influenced factors
st.header("Factors influenced by the government")
st.write(''' # Mortgage and Interest Rates ''')
st.write('''
    The Federal Funds rate directly influences short-term interest rates, like the interest you’d pay on a credit card or a 1-3 year personal loan. When interest rates rise, people spend less and save more which slows inflation. \n
    Mortgage underwriters approve homebuyers to borrow up to a certain maximum amount, based on the home value (through a ratio called loan-to-value), the borrower’s income (through a metric called the front-end ratio), and the borrower’s other debts (through a metric called the back-end ratio). If mortgage interest rates rise and everything else stays the same — borrowers have the same income and same debt levels — the borrower won’t qualify for as expensive of a mortgage as they previously could.
''')
col10,col11 = st.columns((1,1))
img6 = Image.open("./img/inflation.png")
col11.image(img6, use_column_width=True)
col11.write(''' 
United States inflation rate for the past 1 year. \n

The federal funds rate is the interest rate that banks charge other banks for these overnight loans. Interest rates do have a very noticeable effect. Rising interest rates make buying or selling a home more difficult, and decreasing interest rates make buying and selling easier. Higher mortgage rates mean higher monthly payments, which fewer buyers can afford, which means less demand and lower home prices. 
''')
img4 = Image.open("./img/intgovt.png")
col10.image(img4, use_column_width=True)

##buyer personal influenced factors
st.header("Factors influenced by personal reasons")
st.write(''' # Unemployment and Wages ''')
col3,col4 = st.columns((1,1))
img3 = Image.open("./img/unempvswages.png")
col3.image(img3, use_column_width=True)
img4 = Image.open("./img/emppart.png")
col4.image(img4, use_column_width=True)
col3.write(''' When unemployment is rising, fewer people will be able to afford a house. But, even the fear of unemployment may 
discourage people from entering the property market. \n

An increase in jobs, employees and wages consequently results in an increase in income for all workers in a country. 
With that, an increase in income also increases the demand for affordable housing.
''')

st.write("Demand for housing is dependent upon income. With higher economic growth and rising incomes, people will be able to spend more on houses; this will increase demand and push up prices. In fact, demand for housing is often noted to be income elastic (luxury good); rising incomes leading to a bigger % of income being spent on houses. Similarly, in a recession, falling incomes will mean people can’t afford to buy and those who lose their job may fall behind on their mortgage payments and end up with their home repossessed.")

##predictions for the next decade
st.header("Predictions for the next decade")
st.write('''
The various possible factors that could affect the supply and the demand for housing has been explained in the above sections. 
These factors influence the price of houses. Projection of the numbers for these factors in the 2020-30 decade along with their 
implications have been explained below: \n

''')
col1001, col1002 = st.columns((1,1))
col1001.write('''
After 2020, economic growth is projected to slow. From 2021 to 2030, output is projected to grow at an average annual rate of 1.7% as 
compared to 2.2% in an inflation adjusted 2020 GDP.
In the CBO’s (Congressional Budget Office) projections, the federal budget deficit is $1.0 trillion in 2020 and averages $1.3 trillion 
between 2021 and 2030. Projected deficits rise from 4.6 percent of gross domestic product (GDP) in 2020 to 5.4 percent in 2030. 
\nThis indicates that the output is projected to be higher than the economy’s maximum sustainable output this year to a greater 
degree than it has been in recent years, leading to higher inflation and interest rates after a period in which both were low, on an average.
''')
img1000 = Image.open("./img/deficit%gdp2.png")
col1002.image(img1000, use_column_width=True)

st.write('''
\nIt is predicted, that the the labor force is expected to grow more slowly than it has in the past. 
About one-fourth of the population will be age 65 or older in 2030, contributing to slow projected growth in the labour force and a 
continued decline in the labour force participation rate. Thereby causing a steep shortage for construction labour. It is estimated 
that there will be a 40% shortage by 2030 as compared to the current 33%, causing a hit to the supply. However, a continued strength 
in the demand for labor keeps the unemployment rate low and drives employment and wages higher. This goes for almost all major sectors 
not just labour. Allowing the consumers to have a higher mortgage and buy more expensive homes.\n

House prices in the US have risen by 48.55% in the last ten years (from $173k to $257k) and if they continue to grow at this rate 
for another decade, the average US home will be worth $382k by 2030. 

\nHow could the government could make housing more affordable?
\nDecisions over land use—what types of housing can be built in which locations are largely made by state and local governments. 
One of the most common zoning laws that drives up housing costs is restricting the development of apartments. 
\nThe federal policies also influence the cost of construction through several channels. Construction materials such as lumber and steel 
are subject to U.S. tariffs and trade policy. Immigration policy affects the availability of workers; 
about one-quarter of construction workers are foreign born.
 ''')
#########################################
st.header("Biblography")
html_string = '''<html>
    <head>
        <title> Biblography </title>
    </head>
    <body>
        <table style="border-width: 1;">
            <th style="background-color:lightgray;"> Refernces</th>
            <tr>
                <td>
                    <a href="http://home.llc">home.llc</a>
                </td>
            </tr>
            <tr>
                <td>
                    <a href="www.brookings.edu">brookings.edu</a>
                </td>
            </tr>
            <tr>
                <td>
                    <a href="www.cbo.gov">cbo.gov</a>
                </td>
            </tr>
            <tr>
                <td>
                    <a href="www.opendoor.com">opendoor.com</a>
                </td>
            </tr>
            <tr>
                <td>
                    <a href="http://nar.realtor">nar.realtor</a>
                </td>
            </tr>
            <tr>
                <td>
                    <a href="http://fred.stlouisfed.org">fred.stlouisfed.org</a>
                </td>
            </tr>     
            <tr>
                <td>
                    <a href="https://tradingeconomics.com/">tradingeconomics.com</a>
                </td>
            </tr> 
            <tr>
                <td>
                    <a href="http://bls.gov">bls.gov</a>
                </td>
            </tr>  
            <tr>
                <td>
                    <a href="https://insight.factset.com">insight.factset.com</a>
                </td>
            </tr>
            <tr>
                <td>
                    <a href="https://www.whitehouse.gov">whitehouse.gov</a>
                </td>
            </tr>
            <tr>
                <td>
                    <a href="https://data.worldbank.org">data.worldbank.org</a>
                </td>
            </tr>
            <tr>
                <td>
                    <a href="https://data.worldbank.org">data.worldbank.org</a>
                </td>
            </tr>
            <tr>
                <td>
                    <a href="https://www.cnbc.com">cnbc.com</a>
                </td>
            </tr>         
        </table>
    </body>
</html>'''
st.markdown(html_string, unsafe_allow_html=True)
