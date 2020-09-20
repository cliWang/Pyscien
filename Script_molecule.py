import sys
sys.path.append(r"D:\Desktop\VASP practical\Pymatgen")
from molecule import Molecule
from write import Write
c = [[2,0,0],
     [0,2,0],
     [0,0,1]]




my_Molecule = Molecule("CH3OH.gjf"，15,15,15)#二水石膏
my_Molecule.phase('LWAVE', '\nLWAVE = Ture')#('判断要写入的参数是否存在judge=', '要补充写入的参数appendage=')#生成晶胞优化的输入文件


