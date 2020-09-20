import sys
sys.path.append(r"D:\Desktop\VASP practical\Pymatgen")
from crystalcalculate import Crystalcalculate



my_Crystalcalculate = Crystalcalculate(r'F:\cp2k practical\useful\bassanitepvp300')
my_Crystalcalculate.latticeplane(crystalsystem='trigonal',a=7.653,b=7.653,c=7.653,
                                 alpha=110.712,beta=110.712,gamma=110.712,h1=0,k1=0,l1=1,)



'''
cubic tetragonal orthorhombic hexagonal trigonal monoclinic triclinic
'''