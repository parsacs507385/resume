from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = np.array([])
for i in range(0, 100):
    if i < 33:
        y = np.append(y, 1)
    elif 33 <= i < 66:
        y = np.append(y, 2)
    else:
        y = np.append(y, 3)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x.reshape(-1, 1), y.reshape(-1, 1))
classes = model.predict(x.reshape(-1, 1))

plt.scatter(x, y, c=classes)
plt.show()