import sys
sys.path.append(r"D:\Desktop\VASP practical\Pymatgen")
from poscar import Poscar


my_lattace = Poscar(r'E:\VASP practical\Input\zwf\jiasuan')#二水石膏

my_lattace.slab('jiasuan')#生成吸附结构输入文件
