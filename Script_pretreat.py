# -*- coding: utf-8 -*-
"""
Created on Fri May 15 08:35:58 2020

@author: 41958
"""

'''
  File "D:\Software\AN\lib\site-packages\phonopy\api_phonopy.py", line 1012, in run_band_structure
    raise RuntimeError(msg)'''






import sys
sys.path.append(r"D:\Desktop\VASP practical\Pymatgen")
from pretreat import Pretreatment

apec=[{"Ca2+": 1},{"Ca2+": 1},{"S2-": 1},{"S2-": 1},
      {"O2-": 1},{"O2-": 1},{"O2-": 1},{"O2-": 1},{"O2-": 1},{"O2-": 1},{"O2-": 1},{"O2-": 1},{"O2-": 1},
      {"H2-": 1},{"H2-": 1}] 
cvv = [[1,0,0],
    [0,2,0],
    [0,0,2]]
my_Pretreatment=Pretreatment(r'E:\VASP practical\Input\ISOTOPE\prim')
# my_Pretreatment.disorder(apecies=apec,spacegroup="C2")

# my_Pretreatment.Static()
# my_Pretreatment.Scf()
# my_Pretreatment.isotope(before="POMASS =    1.000", change="POMASS =    2.000")
'''以下为声子谱部分'''
# my_Pretreatment.Phonopy(mpid='mp-698074',supcell='"2 2 1"')#半水mpid='mp-698074'
'''分步运行，不能同时运行'''
my_Pretreatment.Phonopyinput(mpid='mp-698074',intt=900)#二水mpid='mp-23690'