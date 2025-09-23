# Anderson-Localization
This project consists in studying the Anderson transition in strongly magnetized QCD.

Most of the files contain 400 eigenvalues measured with dyniso. Some files (in particular the
low-temperature ones) only have 300, but this will be updated in the future. The relevant columns
for us are the folowing:

1: Real part of the eigenvalue (always 0)
2: Imaginary part of the eigenvalue
3: Norm of the eigenvectors (always 1)
4: IPR multiplied by a volume = Ns^3 * Nt factor
5: IPR3 multiplied by a volume factor

PS: The old files, namely, those that contain only 300 eigenvalues don't have IPR3 in their 5th
column.

The ensembles that are complete, i.e., that have all magnetic fields measured on all the available
configurations contain an empty file named COMPLETE. 

# LCP code

There are two ways of using the LCP code:

1 - To calculate the lattice spacing "a" in fm for a given beta:

    python3 lcp_2stout.py -a <beta>

   where <beta> is the inverse gauge coupling

2 - To calculate beta from the lattice spacing:

   python3 lcp_2stout.py -b <a>

   where <a> is the lattice spacing in fm.
