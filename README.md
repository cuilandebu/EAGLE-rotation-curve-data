# Data archive of rotation curve at redshift 0 from EAGLE simulation

‼️ This repository contains data related to my undergraduate final project. You can find a summary of my final project in the file named $\textbf{final-project-journal}$, located alongside this README ‼️

Feel free to explore, reuse, or extend this dataset for your own research. I made it public in the hope that it can be helpful for others working with EAGLE galaxy simulations and rotation curve analysis.

All computations in this work were carried out using the MAHAMERU High-Performance Computing (HPC) facility provided by the National Research and Innovation Agency of Indonesia (BRIN).

# 🛰️ Project Overview
In my final project, I studied the Baryonic Tully-Fisher Relation using the EAGLE simulation. Specifically, I used data from the RecalL0025N0752 simulation (25 cMpc volume) at redshift 0. From the particle data, I extracted the rotation curves for 667 galaxies. Due to the large size of the particle data (~50 GB) and the long computation time required to extract the curves, I decided to store and share the final data and plots used in my project. \
🔗 All data and plots can be accessed via this link:
https://drive.google.com/drive/folders/1WB9Og43qbiOnurZs2B7QB_MaA8MWDJUQ?usp=sharing

# 📁 Folder Structure
Inside the RecalL0025N0752 directory, you'll find two main types of folders:
1. xyz_data/: Contains rotation curve data and rotation curve decomposition.
2. xyz_plot/: Contains plots of rotation curves, decompositions, and interpolation results.

These include two types of galaxy samples: rotation-supported and pressure-supported, distinguished by the KappaCoRot parameter (explained below).

Details:
1. rotcur_plot/cut/ includes plots of rotation curves limited to a radius of 15 kpc.
2. decomposition_data folder contains the data for each component (stars, gas, and dark matter), and decomposition_plot folder contains the plots for each component.
3. Interpolation is performed for galaxies with different baryonic mass dominance, to obtain the rotation velocity at two effective radii. Hence, in the interpolation folder, there are plots for two samples of galaxies: those dominated by stellar mass and those dominated by gas mass. Data for the effective radii (queried from the database) and the interpolation results are also provided.

# 📘 Notes on EAGLE Data
Here some things I considered you need to know related to the EAGLE simulation's data.
1. The EAGLE Public Data Release is available at http://icc.dur.ac.uk/Eagle/database.php and registrasion is required.
2. There are two kinds of data: the database and the particle data, both accessible through the same link.
3. The database provides the properties of simulated galaxies at any volume and redshift. These can be retrieved by submitting a query in the query box.
4. The particle data must be downloaded before use and, as mentioned earlier, is quite large. Particle data consists of several snapshot files from one volume at one redshift in the simulation. To use this data, Python code is required to read each snapshot, and galaxy properties (from the database) are also needed.
5. Helpful references for working with EAGLE data: \
   a. EAGLE main publication: Schaye et al (2015) \
      https://ui.adsabs.harvard.edu/abs/2015MNRAS.446..521S/abstract \
   b. Database explanation: McAlpine et al (2016) \
      https://arxiv.org/abs/1510.01320 \
   c. Particle data documentation: The EAGLE team (2017) \
      https://arxiv.org/abs/1706.09899 
   
I have extracted the rotation curves for 667 galaxies, but I only used 207 galaxies in my final project. The difference is based on galaxy morphology, characterized by the KappaCoRot parameter. I selected only rotation-supported galaxies with KappaCoRot $\geq$ 0.4. Below is the query I used in the database:

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

This returns 207 rotation-supported galaxies. To get the other 460 galaxies, change the condition from KappaCoRot >= 0.4 with KappaCoRot < 0.4 which will give pressure-supported galaxies (Correa, 2017). \
The parameter GN, SGN, cx, cy, and cz are used to retrieve the rotation curve using the code provided in the paper The EAGLE Team (2017).

If you have a question or willing to discuss, you can find me on robiahoktiavi@gmail.com
