import matplotlib.pyplot as plt
import matplotlib.cm
import pandas as pd
import datetime
from pandas_datareader import data, wb


from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

import shapefile 

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

m.readshapefile("tl_2016_01_sldu", "alabama")
m.readshapefile("tl_2016_02_sldu", "alaska")
m.readshapefile("tl_2016_04_sldu", "arizona")
m.readshapefile("tl_2016_05_sldu", "arkansas")
m.readshapefile("tl_2016_06_sldu", "california")
m.readshapefile("tl_2016_08_sldu", "colorado")
m.readshapefile("tl_2016_09_sldu", "connecticut")
m.readshapefile("tl_2016_10_sldu", "delaware")
m.readshapefile("tl_2016_11_sldu", "district of columbia")
m.readshapefile("tl_2016_12_sldu", "florida")
m.readshapefile("tl_2016_13_sldu", "georgia")
m.readshapefile("tl_2016_15_sldu", "hawaii")
m.readshapefile("tl_2016_16_sldu", "idaho")
m.readshapefile("tl_2016_17_sldu", "illinois")
m.readshapefile("tl_2016_18_sldu", "indiana")
m.readshapefile("tl_2016_19_sldu", "iowa")
m.readshapefile("tl_2016_20_sldu", "kansas")
m.readshapefile("tl_2016_21_sldu", "kentucky")
m.readshapefile("tl_2016_22_sldu", "louisiana")
m.readshapefile("tl_2016_23_sldu", "maine")
m.readshapefile("tl_2016_24_sldu", "maryland")
m.readshapefile("tl_2016_25_sldu", "massachusetts")
m.readshapefile("tl_2016_26_sldu", "michigan")
m.readshapefile("tl_2016_27_sldu", "minnesota")
m.readshapefile("tl_2016_28_sldu", "mississippi")
m.readshapefile("tl_2016_29_sldu", "missouri")
m.readshapefile("tl_2016_30_sldu", "montana")
m.readshapefile("tl_2016_31_sldu", "nebraska")
m.readshapefile("tl_2016_32_sldu", "nevada")
m.readshapefile("tl_2016_33_sldu", "new hampshire")
m.readshapefile("tl_2016_34_sldu", "new jersey")
m.readshapefile("tl_2016_35_sldu", "new mexico")
m.readshapefile("tl_2016_36_sldu", "new york")
m.readshapefile("tl_2016_37_sldu", "north carolina")
m.readshapefile("tl_2016_38_sldu", "north dakota")
m.readshapefile("tl_2016_39_sldu", "ohio")
m.readshapefile("tl_2016_40_sldu", "oklahoma")
m.readshapefile("tl_2016_41_sldu", "oregon")
m.readshapefile("tl_2016_42_sldu", "pennsylvania")
m.readshapefile("tl_2016_44_sldu", "rhode island")
m.readshapefile("tl_2016_45_sldu", "south carolina")
m.readshapefile("tl_2016_46_sldu", "south dakota")
m.readshapefile("tl_2016_47_sldu", "tennessee")
m.readshapefile("tl_2016_48_sldu", "texas")
m.readshapefile("tl_2016_49_sldu", "utah")
m.readshapefile("tl_2016_50_sldu", "vermont")
m.readshapefile("tl_2016_51_sldu", "virginia")
m.readshapefile("tl_2016_53_sldu", "washington")
m.readshapefile("tl_2016_54_sldu", "west virginia")
m.readshapefile("tl_2016_55_sldu", "wisconsin")
m.readshapefile("tl_2016_56_sldu", "wyoming")


plt.show() 
