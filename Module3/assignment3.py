import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
df = pd.read_csv('Datasets/wheat.data', header=0, index_col = 0)


fig = plt.figure()

#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Be sure to use the
# optional display parameter c='red', and also label your
# axes
# 
ax = fig.add_subplot(211, projection='3d')
ax.scatter3D(xs=df.area, ys=df.perimeter, zs=df.asymmetry, c='red')
ax.set_xlabel('area')
ax.set_ylabel('perimeter')
ax.set_zlabel('asymmetry')

#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Be sure to use the
# optional display parameter c='green', and also label your
# axes
# 
ax = fig.add_subplot(212, projection='3d')
ax.scatter3D(xs=df.width, ys=df.groove, zs=df.length, c='green')
ax.set_xlabel('width')
ax.set_ylabel('groove')
ax.set_zlabel('length')


plt.show()
