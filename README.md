RecalL0025N0752.github.io
# Data archive of rotation curve at redshift 0 from EAGLE simulation

I do my final project and using EAGLE simulation to study Baryonic Tully-Fisher Relation. I use database and data particle from volume 25 cMpc simulation RecalL0025N0752 at redshift 0 and extract the rotation curve for 667 galaxies from data particle. Since the size of data particle is large enough, about 50 GB and computing time to retrieve rotation curve is very long, I decided to save the data and plot of rotation curve that I took in my final project. Here some things I considered you need to know related to the data.

1. EAGLE Public Data Release can be accessed through this link http://icc.dur.ac.uk/Eagle/database.php and you should register first to access the data. There are two kind of data, database and data particle, both can be accessed through the same link as before.
2. The database provided properties of simulated galaxies, at any volume and any redshift, which can be retrieved by input a query in the query box.
3. The data particle should be downloaded before you can use it and as I mention before, the size is large enough. Data particle contains of several snapshots file from one volume at one redshift of simulation. To use this data, we need python code to read each snapshots and we need galaxies properties that we get through the database.
4. Here some publication that might help and guide you to use EAGLE public data
   a. EAGLE main publication: Schaye et al (2015)
      https://ui.adsabs.harvard.edu/abs/2015MNRAS.446..521S/abstract
   b. Publication related to database: McAlpine et al (2016)
      https://arxiv.org/abs/1510.01320
   c. Publication related to data particle: The EAGLE team (2017)
      https://arxiv.org/abs/1706.09899
   
Here I will explain step by step to extract rotation curve.
