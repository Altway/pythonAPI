# -*- coding: utf-8 -*-
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

def analyseTab(tab):

    # Convert format to be numpy compliant
    n_abs_axis = np.array([[i] for i in range(len(tab))])
    n_tab = np.array(tab)


    reg = linear_model.LinearRegression()
    reg.fit(n_abs_axis, n_tab)

    # Plot outputs
    # x = np.linspace(0, len(tab)-1)

    # plt.scatter(n_abs_axis, n_tab, color='black')

    # plt.plot(n_tab, color='blue', linewidth=1)
    # plt.plot(x, reg.coef_*x + reg.intercept_, color='red', linewidth=1)

    # plt.axis([0, 8, -50, 150])
    # plt.xlabel('Index')
    # plt.ylabel('Value')
    # plt.title('Tab distribution')
    # plt.text(0.5, 120, 'coef = {}+{}'.format(reg.coef_, reg.intercept_))

    # plt.show()

    return [reg.coef_, reg.intercept_]
