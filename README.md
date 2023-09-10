# Data archive of rotation curve at redshift 0 from EAGLE simulation

!! This is readme for data. You can read my summary of final project on file name $\textbf{final-project_journal}$ along with this readme located.

The computation in this work has been done using the facilities of MAHAMERU BRIN HPC, National Research and Innovation Agency of Indonesia (BRIN)

I do my final project using EAGLE simulation to study Baryonic Tully-Fisher Relation. I use database and particle data from volume 25 cMpc simulation RecalL0025N0752 at redshift 0 and extract the rotation curve for 667 galaxies relies on particle data. Since the size of particle data is large enough, about 50 GB and computing time to retrieve rotation curve is very long, I decided to save the data and plot of rotation curve that I took in my final project. All data can be accessed through the following link: https://drive.google.com/drive/folders/1WB9Og43qbiOnurZs2B7QB_MaA8MWDJUQ?usp=sharing

The following is a description of the folder in the data link.
1. Basically, folder RecalL0025N0752 contain two kind folder, data (rotation curve and rotation curve decomposition) and plot (rotation curve, rotation curve decomposition, and interpolation).
2. Each folder (except folder interpolation) contains samples of two types of galaxies, pressure and rotational supported. It's distinguished by KappaCoRot (I'll explain below).
3. In the folder rotcur_plot, there is a folder named "cut" which contains a plot of the rotation curve only up to a radius of 15 kpc.
4. Folder decomposition_data contains data for each components (star, gas, and dark matter) and so for decomposition_plot contains plot for each components.
5. Interpolation is performed for galaxies with different baryon mass predominance, to obtain rotation velocity at two effective radii. Hence in the folder interpolation there are plot for two samples of galaxies, dominated by stellar masses and gas masses. Data for effective radii (by querying database) and the result of interpolation also provided.

Then, here some things I considered you need to know related to the data.
1. EAGLE Public Data Release can be accessed through this link http://icc.dur.ac.uk/Eagle/database.php and you should register first to access the data. There are two kind of data, database and data particle, both can be accessed through the same link as before.
2. The database provided properties of simulated galaxies, at any volume and any redshift, which can be retrieved by input a query in the query box.
3. The data particle should be downloaded before you can use it and as I mention before, the size is large enough. Data particle contains of several snapshots file from one volume at one redshift of simulation. To use this data, we need python code to read each snapshots and we need galaxies properties that we get through the database.
4. Here some publication that might help and guide you to use EAGLE public data \
   a. EAGLE main publication: Schaye et al (2015) \
      https://ui.adsabs.harvard.edu/abs/2015MNRAS.446..521S/abstract \
   b. Publication related to database: McAlpine et al (2016) \
      https://arxiv.org/abs/1510.01320 \
   c. Publication related to data particle: The EAGLE team (2017) \
      https://arxiv.org/abs/1706.09899 
   
I have been extract the rotation curve for 667 galaxies but I only use 207 galaxies at my final project. The difference is on morphology of galaxies, characterizing by parameter KappaCoRot. I only select rotational supported galaxies with KappaCoRot $\geq$ 0.4. Below is the query command I entered in the database.

SELECT \
     sh.GalaxyID, \
     sh.Mass as m_tot, \
     sh.MassType_Star as m_star, \
     sh.MassType_Gas as m_gas, \
     MassType_Star + MassType_Gas as m_bary, \
     sh.VmaxRadius as r_vmax, \
     sh.Vmax as v_max, \
     recal.KappaCoRot, \
     sh.GroupNumber as GN, \
     sh.SubGroupNumber as SGN, \
     sh.CentreOfMass_x as cx, \
     sh.CentreOfMass_y as cy, \
     sh.CentreOfMass_z as cz, \
     sh.HalfMassRad_Star as Reff_star \
     sh.HalfMassRad_Gas as Reff_gas \
FROM \
     RecalL0025N0752_Subhalo as sh, \
     RecalL0025N0752_MorphoKinem as recal \
WHERE \
     sh.Snapnum = 28 \
     and MassType_Star + MassType_Gas >= 3.9705e8 \
     and MassType_Star + MassType_Gas <= 3.7660e11 \
     and sh.MassType_Gas > 0 \
     and KappaCoRot >= 0.4 \
     and sh.GalaxyID = recal.GalaxyID \
ORDER BY \
     m_bary asc

It obtain 207 rotational supported galaxies. To get another 460 galaxies, change the KappaCoRot >= 0.4 with KappaCoRot < 0.4 and it will result galaxies with morphology pressure supported (Correa, 2017). The parameter GN, SGN, cx, cy, and cz are used to retrieve the rotation curve using the code given in the paper The EAGLE Team (2017).
