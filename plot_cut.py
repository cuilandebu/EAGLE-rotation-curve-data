import vaex
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('file_name.csv')
# Plot untuk komponen total + dekomposisi
for i in range(len(df["GalaxyID"])):
    data_all = vaex.open('/rotcur_data/full/data_{}.h5'.format(df["GalaxyID"][i]))
    data_gas = vaex.open('/dekomposisi_data/full/{}_gas.h5'.format(df["GalaxyID"][i]))
    data_star = vaex.open('/dekomposisi_data/full/{}_star.h5'.format(df["GalaxyID"][i]))
    data_dm = vaex.open('/dekomposisi_data/full/{}_dm.h5'.format(df["GalaxyID"][i]))
    data_dict_all = data_all.to_dict()
    data_dict_gas = data_gas.to_dict()
    data_dict_star = data_star.to_dict()
    data_dict_dm = data_dm.to_dict()
    data_pd_all = pd.DataFrame(data_dict_all)
    data_pd_gas = pd.DataFrame(data_dict_gas)
    data_pd_star = pd.DataFrame(data_dict_star)
    data_pd_dm = pd.DataFrame(data_dict_dm)
    cut_all = data_pd_all[data_pd_all['Jarak']<15]
    cut_gas = data_pd_gas[data_pd_gas['Jarak']<15]
    cut_star = data_pd_star[data_pd_star['Jarak']<15]
    cut_dm = data_pd_dm[data_pd_dm['Jarak']<15]
    x_all = cut_all['Jarak']
    y_all = cut_all['Kecepatan']
    x_gas = cut_gas['Jarak']
    y_gas = cut_gas['Kecepatan']
    x_star = cut_star['Jarak']
    y_star = cut_star['Kecepatan']
    x_dm = cut_dm['Jarak']
    y_dm = cut_dm['Kecepatan']
    plt.figure()
    plt.plot(x_all, y_all, c='k', label='Total')
    plt.plot(x_dm, y_dm, c='darkorange', label='Dark matter')
    plt.plot(x_star, y_star, c='r', label='Bintang')
    plt.plot(x_gas, y_gas, c='midnightblue', label='Gas')
    plt.legend(loc='best')
    plt.ylabel('Kecepatan (km/s)'); plt.xlabel('Jarak (kpc)')
    plt.title("Kurva Rotasi EAGLE ID {}".format(df["GalaxyID"][i]))
    plt.savefig('./plot-jarak-cut/full_sample/{}.jpg'.format(df["GalaxyID"][i]), bbox_inches='tight', dpi=200)
