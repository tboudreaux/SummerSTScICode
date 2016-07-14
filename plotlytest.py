import matplotlib.pyplot as plt
import plotly.plotly as py
import numpy as np
#py.sign_in('tboudreaux', 'Nhv#r&HBlVlb6K9UR#0ihHxX0OK7!2')
x = np.linspace(0, 100, 1000)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plot_url = py.plot_mpl(fig)

print plot_url
