import matplotlib.pyplot as plt
import matplotlib.cm
import pandas as pd
import datetime
import pandas.io.data as web


from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

m = Basemap(projection='mill',
            llcrnrlat = 25,
            llcrnrlon = -130,
            urcrnrlat = 50,
            urcrnrlon = -60,
            resolution = 'l')

m.drawmapboundary(linewidth=1, fill_color='#46bcec')
m.drawcoastlines()
m.drawcountries(linewidth=1.5)
m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')

m.drawstates(linewidth=0.5, linestyle='solid', color='#044efa', antialiased=1, ax=None, zorder=None)







plt.show()