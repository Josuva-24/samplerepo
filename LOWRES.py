
# Shorter version of Locally Weighted Regression implementation

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression

# Generate dataset
X, y = make_regression(n_samples=100, n_features=1, noise=15, random_state=42)
X = X.flatten()

# LWR function
def lwr(X, y, tau, xq):
    m = len(X)
    W = np.exp(-((X - xq) ** 2) / (2 * tau ** 2))
    X_b = np.c_[np.ones(m), X]
    theta = np.linalg.pinv(X_b.T @ (W[:, None] * X_b)) @ (X_b.T @ (W * y))
    return np.dot([1, xq], theta)

# Predict for all sorted X
X_sorted = np.sort(X)
y_pred = np.array([lwr(X, y, tau=0.5, xq=xi) for xi in X_sorted])

# Plot
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X_sorted, y_pred, color='red', label='LWR Fit (tau=0.5)')
plt.title('Shortened Locally Weighted Regression')
plt.legend()
plt.grid(True)
plt.show()
