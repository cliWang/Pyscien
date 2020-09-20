import os
import sys
sys.path.append(r"D:\Desktop\VASP practical\Pymatgen")
from continue_plot import Continue
# my_sta = Continue(r'D:\Desktop\合作计算数据\CONTAR\CONTACR\SFeS001OO\poscar') 
my_sta = Continue(r'D:\Desktop\合作计算数据\picture\FeS') 
# my_sta.plotdos_orb(name1='s',name2='p',name3 = 'd')#name1='s',name2='p',name3 = 'd'
# my_sta.plotdos_elem('O')#'Fe','S','O'
# my_sta.site_orbital_dos(0,30,'sp','up')

# my_sta.site_orbital_dos_mirror(0,200,'spd','up')

# my_sta.plot_band()#自建
# my_sta.electronic_structure('O')#电子结构示意图

# my_sta.plotbandDOS()#
# my_sta.plotband()#pumatgen默认
# my_sta.site_spd_dos(0,3)#参数是位点值
# my_sta.site_spd_dos_mirror(0,200,'spd')#参数是位点值

# my_sta.absorbed_plot([0,0,1])
my_sta.absorb_site_spd_dos_mirror([0,0,1],'12.png',b_atomnum1 =17,b_atomnum2 =26,b_atomnum3 =23,m_atomnum=1,a_atomnum1 = 29,a_atomnum2 = 21,a_atomnum3 = 12,am_atomnum1 = 54,am_atomnum2 = 55)
# my_sta.absorb_site_spd_dos_mirror_1([0,0,1],'3.png',b_atomnum1 =12,b_atomnum2 =9,b_atomnum3 =10,m_atomnum=1,a_atomnum1 = 12,a_atomnum2 = 9,a_atomnum3 = 10,am_atomnum1 = 47,am_atomnum2 = 48)
#(miller_index_1,num1,num2,atomnum1 ='12_21',atomnum3 ='1',atomnum20 ='12_21',atomnum21 ='12_21')
#num1=吸附前晶面示意图切面编号，num2=吸附后示意图编号，atomnum1 =吸附前需要的原子编号
#atomnum3=吸附前分子中需要的原子编号atomnum20=吸附后吸附剂需要的原子编号，atomnum21 =吸附后吸附质原子编号