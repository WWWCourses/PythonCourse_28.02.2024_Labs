import matplotlib.pyplot as plt
import numpy as np

# 0-9a-f
#(255)FF
#(15) F
# Red:  FF
# Green:00
# Blue: FF

x = np.arange(5)
y = x**2

fig, axes=plt.subplots()
# axes.plot(x, y, color='#FF00FF')
# axes.plot(x, y, color='#F0F', linestyle='--', linewidth=3, marker='s')
axes.plot(x, y, 's--r', linewidth=3)
# axes.plot(x, y, color='purple')

# Show the plot
plt.show()