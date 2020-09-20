class Cif():
    import os
    print (os.getcwd()) 
    f = [[1,0,0],
         [0,1,0],
         [0,0,1]]
    def __init__(self,cif_route,supercell ):
        self.cif_route = cif_route
        self.supercell = supercell
        
    os.chdir(r"D:\Desktop\VASP practical\Cif library")  
    print (os.getcwd())   
    
    def slab(self, miller_index_1, min_slab_size_1=8.0,  min_vacuum_size_1=15):
        
        from pymatgen.analysis.adsorption import AdsorbateSiteFinder, plot_slab, reorient_z
        from pymatgen.core.surface import Slab, SlabGenerator, generate_all_slabs, Structure, Lattice, ReconstructionGenerator
        from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
        from pymatgen.core.structure import Structure
        from pymatgen.io.cif import CifParser
        from matplotlib import pyplot as plt
        from pymatgen.io.vasp.inputs import Poscar
        from pymatgen.io.vasp.sets import MVLSlabSet
        import shutil
        import os
        ##mpr = MPRester()#密钥#密钥

        ass = self.cif_route
        print(ass)
        # os.chdir(r"E:\VASP practical\Input")
        # print (os.getcwd()) 

        # Note that you must provide your own API Key, which can
        # be accessed via the Dashboard at materialsproject.org
        #mpr = MPRester()#密钥
        struct = CifParser(ass)
        structure = struct.get_structures()[0]
        print (structure)
        os.chdir(r"E:\VASP practical\Input")  
        print (os.getcwd())

        structure = SpacegroupAnalyzer(structure).get_conventional_standard_structure()
        #空间群分析
        need_miller_index = miller_index_1#通过米勒指数，确定要切的晶面
        
        slab = SlabGenerator(structure, miller_index=need_miller_index, min_slab_size=min_slab_size_1,\
                             min_vacuum_size=min_vacuum_size_1, center_slab=True)
        #晶面生成器参数
            
        for n, slabs in enumerate(slab.get_slabs()):
            slabs_bak = slabs.copy()#可能的晶面
            slabs.make_supercell(self.supercell)
            #晶胞扩充
            
            
            
            A = Poscar(slabs) #将切面转换为Poscar
            relax = A.structure #将Poscar 转换为结构信息
            custom_settings = {"NPAR": 4} # 用户的INCAR 设置
            relax = MVLSlabSet(relax, user_incar_settings=custom_settings)
            #Vasp输入文件生成器
            
            fig = plt.figure()#绘图--确立画布
            ax = fig.add_subplot(111)#绘图--确立位置
            plot_slab(slabs, ax, adsorption_sites=False)#绘图
            dire = str(ass) + "---" + str(need_miller_index) + '----' + str(n)
            #设置一个用作存储输入文件的名称
            relax.write_input(dire)  #将生成的VASP输入文件写入存储
            os.chdir(r"E:\VASP practical\Input")  
            print (os.getcwd())



            plt.savefig('002',format='png')#将该名称用于保存图片
            
            
            
        os.chdir("./" + dire) 
        #定义一个更改当前目录的变量
        dire2 = './vaspstd_sub' 
        #确立脚本名称
        shutil.copy(r"C:\Users\41958\.spyder-py3\vaspstd_sub", dire2 )
        #将脚本写入VASP输入文件所在文件夹
        
        # os.chdir("../")
        #将当前目录改为默认目录
        os.chdir(r"D:\Desktop\VASP practical\workdir")
        print (os.getcwd())
        print ('finished')
            
            
    def sol(self, EB_K_2, miller_index_2, min_slab_size_2=8.0,  min_vacuum_size_2=15):
        from pymatgen.analysis.adsorption import AdsorbateSiteFinder, plot_slab, reorient_z
        from pymatgen.core.surface import Slab, SlabGenerator, generate_all_slabs, Structure, Lattice, ReconstructionGenerator
        from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
        from pymatgen.core.structure import Structure
        from pymatgen.io.cif import CifParser
        from matplotlib import pyplot as plt
        from pymatgen.io.vasp.inputs import Poscar
        from pymatgen.io.vasp.sets import MVLSlabSet
        import shutil
        import os
        ##mpr = MPRester()#密钥#密钥

        ass = self.cif_route
        print(ass)
        # os.chdir(r"E:\VASP practical\Input")
        # print (os.getcwd()) 

        # Note that you must provide your own API Key, which can
        # be accessed via the Dashboard at materialsproject.org
        #mpr = MPRester()#密钥
        struct = CifParser(ass)
        structure = struct.get_structures()[0]
        print (structure)

        os.chdir(r"E:\VASP practical\Input")  
        print (os.getcwd())
        structure = SpacegroupAnalyzer(structure).get_conventional_standard_structure()
        #空间群分析
        need_miller_index = miller_index_2#通过米勒指数，确定要切的晶面
        
        slab = SlabGenerator(struct, miller_index=need_miller_index, min_slab_size=min_slab_size_2,\
                             min_vacuum_size=min_vacuum_size_2, center_slab=True)
        #晶面生成器参数
            
        for n, slabs in enumerate(slab.get_slabs()):
            slabs_bak = slabs.copy()#可能的晶面
            slabs.make_supercell(self.supercell)
            #晶胞扩充
            
            
            
            A = Poscar(slabs) #将切面转换为Poscar
            relax = A.structure #将Poscar 转换为结构信息
            custom_settings = {"NPAR": 4} # 用户的INCAR 设置
            relax = MVLSlabSet(relax, user_incar_settings=custom_settings)
            #Vasp输入文件生成器
            
            fig = plt.figure()#绘图--确立画布
            ax = fig.add_subplot(111)#绘图--确立位置
            plot_slab(slabs, ax, adsorption_sites=False)#绘图
            dire = str(ass) + "---" + "sol" + str(EB_K_2)+ str(need_miller_index) + '----' + str(n)
            #设置一个用作存储输入文件的名称
            plt.savefig(dire)#将该名称用于保存图片
            relax.write_input(dire)  #将生成的VASP输入文件写入存储
            
            
            
            
            
            
            
            os.chdir("./" + dire) 
            #定义一个更改当前目录的变量
            dire2 = './vaspstd_sub' 
            #确立脚本名称
            shutil.copy(r"C:\Users\41958\.spyder-py3\vaspstd_sub", dire2 )
            #将脚本写入VASP输入文件所在文件夹
            
            eb = str(EB_K_2)
            ls = str('TURE')
            with open('INCAR', 'a') as file_object:
                file_object.write('LSOL = ' + ls + '\n' + 'EB_K = ' + eb )
            
            
            
            
            
            
            # os.chdir("../")
            #将当前目录改为默认目录
            os.chdir(r"D:\Desktop\VASP practical\workdir")
            print (os.getcwd())
            print ('finished')
        
    def xrd(self,):
        import os
        from pymatgen import Lattice, Structure
        from pymatgen.analysis.diffraction.xrd import XRDCalculator
        from IPython.display import Image, display
        from pymatgen.io.cif import CifParser
        ass = self.cif_route
        print(ass)
        # os.chdir(r"E:\VASP practical\Input")
        # print (os.getcwd()) 

        # Note that you must provide your own API Key, which can
        # be accessed via the Dashboard at materialsproject.org
        #mpr = MPRester()#密钥
        struct = CifParser(ass)
        structure = struct.get_structures()[0]
        print (structure)
        os.chdir(r"E:\VASP practical\Input")  
        print (os.getcwd())
        c = XRDCalculator()
        c.show_plot(structure)
        
        print (os.getcwd()) 




    def phase(self,judge='',appendage=""):
        import os
        import re
        from pymatgen import Structure
        from pymatgen.io.vasp.sets import MPRelaxSet
        from pymatgen.io.cif import CifParser
        import shutil
        
        ass = self.cif_route
        print(ass)
        # os.chdir(r"E:\VASP practical\Input")
        # print (os.getcwd()) 

        # Note that you must provide your own API Key, which can
        # be accessed via the Dashboard at materialsproject.org
        #mpr = MPRester()#密钥
        struct = CifParser(ass)
        structure = struct.get_structures()[0]
        print (structure)

        
        os.chdir(r"E:\VASP practical\Input")  
        print (os.getcwd())
        structure.make_supercell(self.supercell)

        custom_settings = {"NPAR": 4} # user custom incar settings
        relax = MPRelaxSet(structure, user_incar_settings=custom_settings)
        os.chdir(r"E:\VASP practical\Input")  
        print (os.getcwd())
        relax.write_input(ass + '---' + 'phase')
        os.chdir("./" + ass + '---' + 'phase') 
            #定义一个更改当前目录的变量
        dire2 = './vaspstd_sub' 
            #确立脚本名称
        shutil.copy(r"C:\Users\41958\.spyder-py3\vaspstd_sub", dire2 )
        
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
            
                #将两个参数写入INCAR
        
        
        os.chdir(r"D:\Desktop\VASP practical\workdir")
        print (os.getcwd())
        
        
        
        
    def phase_sol(self,EB_K_2,judge='',appendage=""):
        import os
        from pymatgen import Structure
        from pymatgen.io.vasp.sets import MPRelaxSet
        from pymatgen.io.cif import CifParser
        import shutil
        
        ass = self.cif_route
        print(ass)
        # os.chdir(r"E:\VASP practical\Input")
        # print (os.getcwd()) 

        # Note that you must provide your own API Key, which can
        # be accessed via the Dashboard at materialsproject.org
        #mpr = MPRester()#密钥
        struct = CifParser(ass)
        structure = struct.get_structures()[0]
        print (structure)

        os.chdir(r"E:\VASP practical\Input")  
        print (os.getcwd())
        custom_settings = {"NPAR": 4} # user custom incar settings
        relax = MPRelaxSet(structure, user_incar_settings=custom_settings)
        os.chdir(r"E:\VASP practical\Input")  
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



    def phase_out_sol(self,EB_K_3):
        from pymatgen.io.vasp import Vasprun
        import os
        from pymatgen.io.cif import CifParser
        from pathlib import Path
        import matplotlib.pyplot as plt
        import pandas as pd
        #mpr = MPRester()#密钥
        ass = self.cif_route
        # direc = ass + '---' + 'phase'
        # os.chdir(r"D:\Desktop\VASP practical\Output")
        # os.chdir("./" + direc) 
        # v = Vasprun("vasprun.xml")
        # print(v.final_energy) # final total energy
        # s = v.final_structure
        # s.to(filename="Si-relax.cif") # save relaxed structure into cif file
        # print(s) # relaxed structure

        os.chdir(r"D:\Desktop\VASP practical\Output")
        
        print (os.getcwd())
        x_ax = []
        y_ax = []

        for n in EB_K_3:
            my_file = Path("./" + ass + '---' + "sol" + str(n) + 'phase')
            if my_file.exists():
                os.chdir("./" + ass + '---' + "sol" + str(n) + 'phase')
                print (os.getcwd())
                v = Vasprun("vasprun.xml")
                print(v.final_energy) # final total energy
                x_ax.append(n)
                y_ax.append(v.final_energy)
                s = v.final_structure
                s.to(filename= ass + '---' + "sol" + str(n) + ".cif") # save relaxed structure into cif file
                # print(s) # relaxed structure
                os.chdir(r"D:\Desktop\VASP practical\Output")
                print (os.getcwd())
            else:
                print('not find')


        df=pd.DataFrame({'Dielectric constant':x_ax,'Formation energy':y_ax})#构造原始数据文件
        df.to_excel(r"D:\Desktop\VASP practical\Output\2.xlsx")#生成Excel文件，并存到指定文件路径下
        print('Done!!')
        
    def phase_out(self):
        from pymatgen.io.vasp import Vasprun
        import os
        from pymatgen.io.cif import CifParser
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
        from pymatgen.io.cif import CifParser
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
        
        
    def script(self,EB_K_2):
        import regex as re
        from pymatgen.io.vasp import Vasprun
        import os
        from pymatgen.io.cif import CifParser
        from pathlib import Path
        import matplotlib.pyplot as plt
        import pandas as pd
        #mpr = MPRester()#密钥
        ass = self.cif_route
        
        os.chdir(r"E:\VASP practical\Input")
        
        print (os.getcwd())
        x_ax = []
        

        for n in EB_K_2:
            my_file = Path("./" + ass + '---' + "sol" + str(n) + 'phase')
            if my_file.exists():
                os.chdir("./" + ass + '---' + "sol" + str(n) + 'phase')
                print (os.getcwd())
               
#kk = 'energy  without entropy=     -278.28980146  energy(sigma->0) =     -278.28980146'    
# pattern = re.compile(r'\e+n+t+r+o+p+y+')
                
# d=pattern.findall(kk)
                
                x_ax.append(n)
                
                os.chdir(r"E:\VASP practical\Input")
                print (os.getcwd())
                
            else:
                print('not find')

        with open('script', 'w') as f:
            f.write('cd ~/;cd wcl;cd VASP;' +'cd ' + ass + '---' + 'phase;' +'sbatch vaspstd_sub;' + 'cd ../;' + 'cd ' + ass + '---' + "sol" + str(EB_K_2[0]) + 'phase;' +'sbatch vaspstd_sub;'+ 'cd ../;' + 'cd ' + ass + '---' + "sol" + str(EB_K_2[1]) + 'phase;'+'sbatch vaspstd_sub;' + 'cd ../;' + 'cd ' + ass + '---' + "sol" + str(EB_K_2[2]) + 'phase;' +'sbatch vaspstd_sub;'+ 'cd ../;' + 'cd ' + ass + '---' + "sol" + str(EB_K_2[3]) + 'phase;' +'sbatch vaspstd_sub;' + 'squeue')
            # f.close()
            # data = f.readlines()
            # print(f)
        
        os.startfile(r"E:\VASP practical\Input\script")
        




    def absorbed (self,millerindex_1, absorbate_1, absorba,  judge='',appendage=""):

        from pymatgen import Structure, Lattice, MPRester, Molecule
        import pymatgen.core.structure

        import pymatgen.core.sites
        from pymatgen.analysis.adsorption import AdsorbateSiteFinder, reorient_z, plot_slab
        from pymatgen.core.surface import generate_all_slabs
        from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
        from matplotlib import pyplot as plt
        from pymatgen.io.cif import CifParser
        from pymatgen.io.vasp.inputs import Poscar
        from pymatgen.io.vasp.sets import MVLSlabSet
        from pymatgen.io.cif import CifWriter
        import os
        import shutil

        ass = self.cif_route
        print(ass)
        # os.chdir(r"E:\VASP practical\Input")
        # print (os.getcwd()) 

        # Note that you must provide your own API Key, which can
        # be accessed via the Dashboard at materialsproject.org
        #mpr = MPRester()#密钥
        struct = CifParser(ass)
        structure = struct.get_structures()[0]
        print (structure)

        os.chdir(r"E:\VASP practical\Input")  
        print (os.getcwd())
        # fcc_ni = Structure.from_spacegroup("Fm-3m", Lattice.cubic(3.5), ["Ni", "Ni"],
        # [[0, 0, 0], [0.5, 0.5, 0.5]])
        slabs = generate_all_slabs(structure, max_index=1, min_slab_size=8.0,
        min_vacuum_size=10.0)

        millerindex = millerindex_1
        struct_111 = [slab for slab in slabs if slab.miller_index==millerindex_1][0]

        asf_ni_111 = AdsorbateSiteFinder(struct_111)
        ads_sites = asf_ni_111.find_adsorption_sites()



        # print(ads_sites)
        assert len(ads_sites) == 4

        fig = plt.figure()
        ax = fig.add_subplot(111)
        plot_slab(struct_111, ax, adsorption_sites=True)


        fig = plt.figure()
        ax = fig.add_subplot(111)
         
        adsorbate = Molecule(absorbate_1, absorba)
        ads_structs = asf_ni_111.generate_adsorption_structures(adsorbate,
        repeat=[1, 1, 1])
        A = Poscar(reorient_z(ads_structs[0])) #将切面转换为Poscar
        open('POSCAR', 'w').write(str(A))
        p = Poscar.from_file('POSCAR')
        # w = CifWriter(A.struct)
        # w.write_file('mystructure.cif')
        path = r'E:\VASP practical\Input\POSCAR'  # 文件路径
        if os.path.exists(path):  # 如果文件存在
            # 删除文件，可使用以下两种方法。
            os.remove(path)  
        #os.unlink(path)
        else:
            print('no such file:%s'%my_file)  # 则返回文件不存在
        # w = CifWriter(A.struct)
        # w.write_file('mystructure.cif')

        relax = p.structure #将Poscar 转换为结构信息
        custom_settings = {"NPAR": 4} # 用户的INCAR 设置
        relaxs = MVLSlabSet(relax, user_incar_settings=custom_settings)
        # Vasp输入文件生成器
        dire = str(ass) + "---"+ str(absorbate_1)+ str(millerindex_1) 
        # print (relax)
        relaxs.write_input(dire)
        os.chdir("./" + dire) 
        print (os.getcwd()) 
            #定义一个更改当前目录的变量
        dire2 = './vaspstd_sub' 
            #确立脚本名称
        shutil.copy(r"C:\Users\41958\.spyder-py3\vaspstd_sub", dire2 )

        eb = appendage#添加其他INCAR参数
        
        with open('INCAR', 'r') as f1:
            lines = f1.readlines()
        
        with open('INCAR', 'w') as f2:
             for line in lines:
                 if judge in line:
                     continue
                 f2.write(line)
            
        with open('INCAR', 'a') as f3:
            f3.write(eb)





        plot_slab(ads_structs[0], ax, adsorption_sites=False, decay=0.09)
        # open('POSCAR001', 'w').write(str(Poscar(reorient_z(ads_structs[0]))))

        os.chdir(r"D:\Desktop\VASP practical\workdir")
        print (os.getcwd())
        print ('finished')









        
        
# my_lattace = Lattace('mp-698074')#半水石膏
# # my_lattace.phase_out()#生成晶胞优化的输入文件
# go = my_lattace.phase_sol(66,judge='LWAVE',  appendage= '\nLWAVE = Ture')
# print('yoo')