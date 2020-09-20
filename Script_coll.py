import sys
sys.path.append(r"D:\Desktop\VASP practical\Pymatgen")
from Collage_picture import Coll_pic

my_collage = Coll_pic(r'D:\Desktop\experimental data\FeS\collage_in_python\Fig1\Materials\ori')
my_collage.m_collage_pic(content='(a,b,c,d,e,f)',a="(2,3,1)",
                          b="(2,3,2)",c="(2,3,3)",d="(2,3,4)",e='(2,3,5)',f='2,3,6')
# my_collage.transparent_back(content='(a,b,c,d,e,f)')
# 
# 
# 
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:02:34 2020

@author: 41958
"""


import sys
sys.path.append(r"D:\Desktop\VASP practical\Pymatgen")
from Collage_picture import Coll_pic




my_collage = Coll_pic(r'F:\VASP practical\Input\-111')

# my_collage.m_collage_pic(content='(a,b,c,d,e,f,g,h,i,j)',rows=5,columns=2)
# my_collage.m_collage_pic(content='(k,l,m,n,o,p,q,r,s,t)',rows=5,columns=2)
my_collage.m_collage_pic(content='u,v,w,x,y,z',rows=5,columns=2)
