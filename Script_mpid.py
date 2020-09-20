import sys
sys.path.append(r"D:\Desktop\VASP practical\Pymatgen")
from lattace import Lattace
from write import Write
nu = [[1,0,0],
     [0,1,0],
     [0,0,1]]
a = (0,2,2)#absorbed要吸附的晶面
# b = "OH" 
# c = [[0, 0, 0], [-0.793, 0.384, 0.422]]

# my_lattace = Lattace('mp-70', nu)#二水石膏
my_lattace = Lattace('mp-698074',nu)#半水石膏
# my_lattace = Lattace('mp-505531',nu)#半水石膏
# my_lattace.phase('LWAVE', '\nLWAVE = Ture')#('判断要写入的参数是否存在judge=', '要补充写入的参数appendage=')#生成晶胞优化的输入文件
# my_lattace.phase_sol(24.5, 'ISTART', '\nISTART = 1')
# my_lattace.phase_sol(32.7, 'ISTART', '\nISTART = 1')
# my_lattace.phase_sol(20.3, 'ISTART', '\nISTART = 1')
# my_lattace.phase_sol(78.5, 'ISTART', '\nISTART = 1')#产生溶剂化优化的输入文件，参数为介电常数
# 
# 
# my_lattace.absorbed(a,"H2O.gjf",num = 12345678910110121314151617181920212223242526272830)
# my_lattace.poscar_absorbed(a,"CH3OH.pdb",num = 0,selective_dynamic=False )#
my_lattace.slab(a)#生成切面输入文件，参数为(self, miller_index_1, min_slab_size_1=8.0,supercell_1 = f,  min_vacuum_size_1=15)
# my_lattace.sol()#生成切面溶剂和输入文件，参数为(self, EB_K_2, miller_index_2, min_slab_size_2=8.0, supercell_2 = f,  min_vacuum_size_2=15):
# my_lattace.xrd()#生成xrd图像
# my_lattace.phase_out_sol([20.3, 24.5, 32.7, 78.5])#包含各个溶剂中形成能的excel文件
# my_lattace.phase_out_sol_outcar([20.3, 24.5, 32.7, 78.5])#包含各个溶剂中形成能的excel文件，从OUTCAR读
# my_lattace.script([20.3, 24.5, 32.7, 78.5])#生成提交命令

# my_lattace.script()#生成提交命令
# my_lattace.phase_out()#真空中形成能
# f = Lattace('mp-23690')#二水石膏
# f.phase_sol(80)
