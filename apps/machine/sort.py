# -*- coding: utf-8 -*-
from sklearn import linear_model

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

import numpy as np
import matplotlib.pyplot as plt


def linearAnalyseTab(tab):

    # Convert format to be numpy compliant
    abs_axis = np.array([[i] for i in range(len(tab))])
    ntab = np.array(tab)

    reg = linear_model.LinearRegression()
    reg.fit(abs_axis, ntab)

    # Plot outputs
    x = np.linspace(0, len(tab)-1)

    plt.scatter(abs_axis, ntab, color='black')

    plt.plot(ntab, color='blue', linewidth=1)
    plt.plot(x, reg.coef_*x + reg.intercept_, color='red', linewidth=1)

    plt.axis([0, 8, -50, 150])
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Tab distribution')
    plt.text(0.5, 120, 'coef = {}+{}'.format(reg.coef_, reg.intercept_))

    plt.show()

    return [reg.coef_, reg.intercept_]

def polynomialAnalyseTab(tab):

    # numpy.array compliant from Python.list into numpy.Array
    ntab = np.array(tab)

    # abs_axis simulated
    abs_axis = np.linspace(0, len(tab)-1, len(tab))
    abs_smooth = np.linspace(0, len(tab)-1, len(tab)*100)

    # Data formating
    y = ntab[:, np.newaxis]
    X = abs_axis[:, np.newaxis]
    X_smooth = abs_smooth[:, np.newaxis]

    # plot the list point in a graph to compare with the regression
    plt.scatter(abs_axis, ntab, color='black')

    color = ['blue', 'red', 'green']
    # for each of those degrees, try to interpolate
    for count, degree in enumerate([5,6,7]):
        # Create the polynomial regression
         model = make_pipeline(PolynomialFeatures(degree), Ridge())

         # training  f(X[n]) = y[n]
         model.fit(X,y)

         # apply function found to those points
         y_plot = model.predict(X_smooth)

         # Print my regression
         plt.plot(X_smooth ,y_plot, color[count], linewidth=1,
                  label="degree {}".format(degree))

    plt.legend(loc='lower left')
    plt.show()

    return 0

