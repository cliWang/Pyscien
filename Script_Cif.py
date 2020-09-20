import sys
sys.path.append(r"D:\Desktop\VASP practical\Pymatgen")
from cif import Cif
from write import Write
c = [[2,0,0],
     [0,2,0],
     [0,0,1]]

a = (1,1,1)#切面，
b = "OH" #吸附质
c = [[0, 0, 0], [-0.793, 0.384, 0.422]]#吸附质坐标



my_lattace = Cif("Bassanite.cif")#二水石膏
#my_lattace = Lattace('FeS.cif')#半水石膏
# my_lattace.phase('LWAVE', '\nLWAVE = Ture')#('判断要写入的参数是否存在judge=', '要补充写入的参数appendage=')#生成晶胞优化的输入文件
# my_lattace.phase_sol(24.5, 'ISTART', '\nISTART = 1')
# my_lattace.phase_sol(32.7, 'ISTART', '\nISTART = 1')
# my_lattace.phase_sol(20.3, 'ISTART', '\nISTART = 1')
# my_lattace.phase_sol(78.5, 'ISTART', '\nISTART = 1')#产生溶剂化优化的输入文件，参数为介电常数
# 
# 
# my_lattace.absorbed(a,b,c,'bulesde')#
my_lattace.slab([1,1,1])#生成切面输入文件，参数为(self, miller_index_1, min_slab_size_1=8.0,supercell_1 = f,  min_vacuum_size_1=15)
# my_lattace.sol()#生成切面溶剂和输入文件，参数为(self, EB_K_2, miller_index_2, min_slab_size_2=8.0, supercell_2 = f,  min_vacuum_size_2=15):
# my_lattace.xrd()#生成xrd图像
# my_lattace.phase_out_sol([20.3, 24.5, 32.7, 78.5])#包含各个溶剂中形成能的excel文件
# my_lattace.phase_out_sol_outcar([20.3, 24.5, 32.7, 78.5])#包含各个溶剂中形成能的excel文件，从OUTCAR读
# my_lattace.script([20.3, 24.5, 32.7, 78.5])#生成提交命令

# my_lattace.script()#生成提交命令
# my_lattace.phase_out()#真空中形成能
# f = Lattace('mp-23690')#二水石膏
# f.phase_sol(80)
