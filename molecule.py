class Molecule():
    import os
    print (os.getcwd()) 
    f = [[1,0,0],
         [0,1,0],
         [0,0,1]]
    def __init__(self, cif_route, a, b, c, supercell = f):
        self.cif_route = cif_route
        self.supercell = supercell
        self.a = a 
        self.b = b
        self.c = c
    os.chdir(r"D:\Desktop\VASP practical\Cif library")  
    print (os.getcwd())   
    
    
            
            

        
    def xrd(self,):
        import os
        from pymatgen import Lattice, Structure
        from pymatgen.analysis.diffraction.xrd import XRDCalculator
        from IPython.display import Image, display
        from pymatgen import Structure, Lattice, MPRester, Molecule
        ass = self.cif_route
        print(ass)
        # os.chdir(r"D:\Desktop\VASP practical\Input")
        # print (os.getcwd()) 

        # Note that you must provide your own API Key, which can
        # be accessed via the Dashboard at materialsproject.org
        #mpr = MPRester()#密钥
        molecule = Molecule.from_file(ass)
        structure = molecule.get_boxed_structure(self.a, self.b, self.c)
        print (structure)
        os.chdir(r"D:\Desktop\VASP practical\Input")  
        print (os.getcwd())
        c = XRDCalculator()
        c.show_plot(structure)
        
        print (os.getcwd()) 




    def phase(self):
        import os
        import re
        from pymatgen import Structure
        from pymatgen.io.vasp.sets import MPRelaxSet
        from pymatgen import Structure, Lattice, MPRester, Molecule
        import shutil
        
        ass = self.cif_route
        print(ass)

        for dirpath, dirnames, filenames in os.walk(self.cif_route):
            # print(dirpath)
            for name in filenames:
                path = os.path.join(self.cif_route, name)
                
                molecule = Molecule.from_file(path)
                molecule.apply_operation()
                structure = molecule.get_boxed_structure(self.a,self.b,self.c)
          
            
                os.chdir(r"E:\VASP practical\Input")  
                print (os.getcwd())
                structure.make_supercell(self.supercell)

                custom_settings = {"NELMIN": 5} # user custom incar settings
                relax = MPRelaxSet(structure, user_incar_settings=custom_settings)
                os.chdir(r"E:\VASP practical\Input")  
                print (os.getcwd())
                relax.write_input(str(name))
                os.chdir("./" + str(name)) 
                    #定义一个更改当前目录的变量
                dire2 = './vaspstd_sub' 
                    #确立脚本名称
                shutil.copy(r"C:\Users\41958\.spyder-py3\vaspstd_sub", dire2 )
                
                
                os.chdir(r"D:\Desktop\VASP practical\workdir")
                print (os.getcwd())
                
        
        
        
    def phase_sol(self,EB_K_2,judge='',appendage=""):
        import os
        from pymatgen import Structure
        from pymatgen.io.vasp.sets import MPRelaxSet
        from pymatgen import Structure, Lattice, MPRester, Molecule
        import shutil
        
        ass = self.cif_route
        print(ass)
        # os.chdir(r"D:\Desktop\VASP practical\Input")
        # print (os.getcwd()) 

        # Note that you must provide your own API Key, which can
        # be accessed via the Dashboard at materialsproject.org
        #mpr = MPRester()#密钥
        molecule = Molecule.from_file(ass)
        structure = molecule.get_boxed_structure(self.a,self.b,self.c)
        print (structure)

        os.chdir(r"D:\Desktop\VASP practical\Input")  
        print (os.getcwd())
        custom_settings = {"NELMIN": 5} # user custom incar settings
        relax = MPRelaxSet(structure, user_incar_settings=custom_settings)
        os.chdir(r"D:\Desktop\VASP practical\Input")  
        print (os.getcwd())
        relax.write_input(ass + '---' + "sol" + str(EB_K_2) + 'phase')
        os.chdir("./" + ass + '---' + "sol" + str(EB_K_2) + 'phase') 
            #定义一个更改当前目录的变量
        dire2 = './vaspstd_sub' 
            #确立脚本名称
        shutil.copy(r"C:\Users\41958\.spyder-py3\vaspstd_sub", dire2 )
        
        eb = str(EB_K_2)#将介电常数参数作为字符串
        ls = str('TURE')#加入开启溶剂参数
        with open('INCAR', 'a') as file_object:
            file_object.write('LSOL = ' + ls + '\n' + 'EB_K = ' + eb )
                #将两个参数写入INCAR
        eb = appendage#储存WAVECAR
        
        with open('INCAR', 'r') as f1:
            lines = f1.readlines()
        
        with open('INCAR', 'w') as f2:
             for line in lines:
                 if judge in line:
                     continue
                 f2.write(line)
            
        with open('INCAR', 'a') as f3:
            f3.write(eb)
        
        
        os.chdir(r"D:\Desktop\VASP practical\workdir")
        print (os.getcwd())




        
    def phase_out(self):
        from pymatgen.io.vasp import Vasprun
        import os
        from pymatgen import Structure, Lattice, MPRester, Molecule
        from pathlib import Path
        import matplotlib.pyplot as plt
        import pandas as pd
        #mpr = MPRester()#密钥
        ass = self.cif_route
        direc = ass + '---' + 'phase'
        os.chdir(r"D:\Desktop\VASP practical\Output")
        os.chdir("./" + direc) 
        v = Vasprun("vasprun.xml")
        h = v.final_energy
        print(h) # final total energy
        s = v.final_structure
        s.to(filename=ass + ".cif") # save relaxed structure into cif file
        print('Done!!') # relaxed structure
        return h
    
    
    
    def phase_out_sol_outcar(self,EB_K_3):
        import regex as re
        from pymatgen.io.vasp import Vasprun
        import os
        from pymatgen import Structure, Lattice, MPRester, Molecule
        from pathlib import Path
        import matplotlib.pyplot as plt
        import pandas as pd
        #mpr = MPRester()#密钥
        ass = self.cif_route
        
        os.chdir(r"D:\Desktop\VASP practical\Output")
        
        print (os.getcwd())
        x_ax = []
        y_ax = []
        os.chdir(ass + '---' + 'phase')
        with open("OUTCAR", "r") as v:
            data1 = v.readlines()
        string=str(data1)
        pattern1 = re.compile(r"(?<=energy  without entropy=)\ *\-*\d+\.?\d*")
        c1=pattern1.findall(string)
        print (c1)
        e = c1[-1]
        x_ax.append(1)
        y_ax.append(e)
        os.chdir(r"D:\Desktop\VASP practical\Output")
        print (os.getcwd())
        print (x_ax,y_ax)


        for n in EB_K_3:
            my_file = Path("./" + ass + '---' + "sol" + str(n) + 'phase')
            if my_file.exists():
                os.chdir("./" + ass + '---' + "sol" + str(n) + 'phase')
                print (os.getcwd())
         
                with open("OUTCAR", "r") as f:
                    data = f.readlines()
                string=str(data)
#kk = 'energy  without entropy=     -278.28980146  energy(sigma->0) =     -278.28980146'    
# pattern = re.compile(r'\e+n+t+r+o+p+y+')
                pattern = re.compile(r"(?<=energy  without entropy=)\ *\-*\d+\.?\d*")
                c=pattern.findall(string)
# d=pattern.findall(kk)
                e = c[-1]
                x_ax.append(n)
                y_ax.append(e)
                os.chdir(r"D:\Desktop\VASP practical\Output")
                print (os.getcwd())
                print (n,e)
            else:
                print('not find')


        df=pd.DataFrame({'Dielectric constant':x_ax,'Formation energy':y_ax})#构造原始数据文件
        df.to_excel(r"D:\Desktop\VASP practical\Output\2.xlsx")#生成Excel文件，并存到指定文件路径下
        print('Done!!')
# print (d)
        
        
    