
import pymatgen.core.structure

import pymatgen.core.sites

from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from matplotlib import pyplot as plt
from pymatgen.ext.matproj import MPRester
from pymatgen.io.vasp.inputs import Poscar

from pymatgen.io.cif import CifWriter
from pymatgen.cli.pmg_plot import get_chgint_plot
from pymatgen.io.vasp.outputs import Chgcar,Wavecar,VolumetricData,Procar,Elfcar
import os

from pymatgen.util.plotting import pretty_plot

dire = r'D:\Desktop\合作计算数据\数据\FeS101-O2'
os.chdir(dire)
print (os.getcwd())
wavecar = Wavecar(filename ='WAVECAR')
poscar = Poscar.from_file("POSCAR")
chgcar = wavecar.get_parchg(poscar,0,1)
# procar = Procar('PROCAR')
# data = procar.data
struct = poscar.structure
s = chgcar.structure
finder = SpacegroupAnalyzer(s, symprec=0.1)
sites = [sites[0] for sites in finder.get_symmetrized_structure().equivalent_sites]
atom_ind = [s.sites.index(site) for site in sites]  
for i in atom_ind:
    d = chgcar.get_integrated_diff(i, 1, 30)
    plt.plot(d[:, 0], d[:, 1],
                 label="Atom {} - {}".format(i, s[i].species_string))
plt.legend(loc="upper left")
plt.xlabel("Radius (A)")
plt.ylabel("Integrated charge (e)")
plt.tight_layout()
plt.show()
  


# print (chgcar)
# chgcar = Chgcar(poscar, data = {'total': [1,1,-1]})
# chgcar1 = chgcar.from_file('CHGCAR')

# get_chgint_plot({'chgcar_file':'./CHGCAR','radius':'1'})