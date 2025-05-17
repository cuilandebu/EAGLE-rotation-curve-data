import pandas as pd
import numpy as np
import vaex
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

df = pd.read_csv("file_name_file.csv")
df
y_interps = []

for i in range(len(df["ID"])):
    data = vaex.open('/path_file/data_galaksi_{}.h5'.format(df["ID"][i]))
    data_dict = data.to_dict()
    data_pd = pd.DataFrame(data_dict)
    
    # For gas-rich galaxies, the radius is not limited because their effective radii vary greatly
    # ranging from a few to hundreds of kpc.
    # Meanwhile, for star-rich galaxies, the radius is limited to a maximum of 20 kpc because
    # the largest effective radius is 17 kpc
    chek = data_pd[data_pd['Jarak']<20]
    x = chek['Jarak']
    y = chek['Kecepatan']
    f_interp = interp1d(x, y) 
    x_interp = df["2reff"][i] 
    y_interp = f_interp(x_interp) 
    y_interps.append(y_interp) 

    # plot 
    plt.figure()
    plt.plot(x, y, c='royalblue')
    plt.plot(x_interp, y_interp, 'ro', markersize=4, label=r'$(V_{2R_{eff}}, 2R_{eff})$')
    plt.vlines(x_interp, 0, y_interp, linestyle='--', linewidth=1, color='k')
    plt.hlines(y_interp, 0, x_interp, linestyle='--', linewidth=1, color='k')
    plt.xlim(0,); plt.ylim(0,)
    plt.legend(loc='lower right')
    plt.ylabel('Kecepatan (km/s)'); plt.xlabel('Jarak (kpc)')
    #plt.title("Kurva Rotasi EAGLE ID {}".format(df["GalaxyID"][i]))
    #plt.savefig('./gas_rich/{}.jpg'.format(df["ID"][i]), bbox_inches='tight', dpi=100)
    
# saving interpolation result
np.savetxt('./gas_rich/0_hasil_interpolasi.txt', np.c_[y_interps],
           fmt="% 1.5f", header='v2reff_gas')