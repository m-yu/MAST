Required files for GA+STEM simulation 
-------------------------------------

Au_u3.eam: EAM potential file

PSF.txt: pre-calculated PSF, 976 x 976 pixels  

STEM_ref: file including atomic coordinates of a Au309 Ino-Decahedron structure

STEM_run.py: set up parameters for simualtion

submit.sh: submit script

Output files for GA+STEM simulation
-----------------------------------

Output.txt: from 2 to 5 cols: generation #; fitness function; energy per atom in eV; alpha*chi2


Visulization
------------

image.py: readin a strucutre (xyz format) and precalculated PSF, simulate STEM image using convolution method.  
