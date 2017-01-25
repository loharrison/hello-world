# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 18:42:51 2017

@author: liuba
"""

import numpy as np
import pandas
from pandas import DataFrame, Series
import statsmodels.formula.api as sm
from sklearn.linear_model import LinearRegression
import scipy, scipy.stats
import matplotlib.pylab as plt

data_str = '''Region Alcohol Tobacco
North 6.47 4.03
Yorkshire 6.13 3.76
Northeast 6.19 3.77
EastMidlands 4.89 3.34
WestMidlands 5.63 3.47
EastAnglia 4.52 2.92
Southeast 5.89 3.20
Southwest 4.79 2.71
Wales 5.27 3.53
Scotland 6.08 4.51
NorthernIreland 4.02 4.56'''

d = data_str.split('\n')

d=[i.split(' ') for i in d]


for i in range(len( d ) ):
    for j in range(len( d[0] ) ):
            try:
                d[i][j] = float( d[i][j] )
            except:
                pass
df = DataFrame( d[1:], columns=d[0] )

plt.scatter( df.Tobacco, df.Alcohol,
         marker='o',
         edgecolor='b',
         facecolor='none',
         alpha=0.5 )
plt.xlabel('Tobacco')
plt.ylabel('Alcohol')
plt.savefig('alcohol_v_tobacco.png', fmt='png', dpi=100)

df['Eins'] = np.ones(( len(df), ))
Y = df.Alcohol[:-1]
X = df[['Tobacco','Eins']][:-1]
result = sm.OLS( Y, X ).fit()
result.summary()