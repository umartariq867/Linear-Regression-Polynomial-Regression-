# -*- coding: utf-8 -*-
"""Decision Trees.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11NtpS9phfYYfZ1E8mDw5n8KIkGhArz_Z
"""

from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

clf.predict([[9, 2]])

clf.predict_proba([[9, 2]])

from sklearn.datasets import load_iris
from sklearn import tree
X, y = load_iris(return_X_y=True)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

tree.plot_tree(clf)

from sklearn import tree
X = [[0, 0], [2, 2]]
y = [0.5, 2.5]
clf = tree.DecisionTreeRegressor()
clf = clf.fit(X, y)

clf.predict([[1, 1]])





# print(__doc__)

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.tree import DecisionTreeRegressor

# # Create a random dataset
# rng = np.random.RandomState(1)
# X = np.sort(200 * rng.rand(100, 1) - 100, axis=0)
# y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
# y[::5, :] += (0.5 - rng.rand(20, 2))

# # Fit regression model
# regr_1 = DecisionTreeRegressor(max_depth=2)
# regr_2 = DecisionTreeRegressor(max_depth=5)
# regr_3 = DecisionTreeRegressor(max_depth=8)
# regr_1.fit(X, y)
# regr_2.fit(X, y)
# regr_3.fit(X, y)

# # Predict
# X_test = np.arange(-100.0, 100.0, 0.01)[:, np.newaxis]
# y_1 = regr_1.predict(X_test)
# y_2 = regr_2.predict(X_test)
# y_3 = regr_3.predict(X_test)

# # Plot the results
# plt.figure()
# s = 25
# plt.scatter(y[:, 0], y[:, 1], c="navy", s=s,
#             edgecolor="black", label="data")
# plt.scatter(y_1[:, 0], y_1[:, 1], c="cornflowerblue", s=s,
#             edgecolor="black", label="max_depth=2")
# plt.scatter(y_2[:, 0], y_2[:, 1], c="red", s=s,
#             edgecolor="black", label="max_depth=5")
# plt.scatter(y_3[:, 0], y_3[:, 1], c="orange", s=s,
#             edgecolor="black", label="max_depth=8")
# plt.xlim([-6, 6])
# plt.ylim([-6, 6])
# plt.xlabel("target 1")
# plt.ylabel("target 2")
# plt.title("Multi-output Decision Tree Regression")
# plt.legend(loc="best")
# plt.show()









