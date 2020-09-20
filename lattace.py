class Lattace():
    import os
    print (os.getcwd()) 
    f = [[1,0,0],
         [0,1,0],
         [0,0,1]]
    def __init__(self,mp_id,supercell = f,):
        self.mp_id = mp_id
        self.supercell = supercell
        
    os.chdir(r"F:\VASP practical\Input")  
    print (os.getcwd())   
    
    def slab(self, miller_index_1, min_slab_size_1=8.0,  min_vacuum_size_1=15):
        
        from pymatgen.analysis.adsorption import AdsorbateSiteFinder, plot_slab, reorient_z
        from pymatgen.core.surface import Slab, SlabGenerator, generate_all_slabs, Structure, Lattice, ReconstructionGenerator
        from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
        from pymatgen.core.structure import Structure
        from pymatgen.ext.matproj import MPRester
        from matplotlib import pyplot as plt
        from pymatgen.io.vasp.inputs import Poscar
        from pymatgen.io.vasp.sets import MVLSlabSet
        import shutil
        import os
        mpr = MPRester()#密钥

        mp_id = self.mp_id#通过mp_id来索引结构
        struct = mpr.get_structure_by_material_id(mp_id)
        #获取结构信息
        struct = SpacegroupAnalyzer(struct).get_conventional_standard_structure()
        #空间群分析
        need_miller_index = miller_index_1#通过米勒指数，确定要切的晶面
        
        slab = SlabGenerator(struct, miller_index=need_miller_index, min_slab_size=min_slab_size_1,\
                             min_vacuum_size=min_vacuum_size_1, center_slab=True)
        #晶面生成器参数
        gh = str(miller_index_1).replace(" ", "")
        for n, slabs in enumerate(slab.get_slabs()):
            slabs_bak = slabs.copy()#可能的晶面
            slabs.make_supercell(self.supercell)
            #晶胞扩充
            cc = slabs.surface_area
            os.chdir(r"F:\VASP practical\Input")  
            print (os.getcwd())             
            print(n)
            
            A = Poscar(slabs) #将切面转换为Poscar
            relax = A.structure #将Poscar 转换为结构信息
            custom_settings = {"NPAR": 4} # 用户的INCAR 设置
            relax = MVLSlabSet(relax, user_incar_settings=custom_settings)
            #Vasp输入文件生成器
            
            fig = plt.figure()#绘图--确立画布
            ax = fig.add_subplot(111)#绘图--确立位置
            plot_slab(slabs, ax, adsorption_sites=False)#绘图
            dire = str(mp_id) + "---" + str(gh) + '----' + str(n)

            #设置一个用作存储输入文件的名称
            plt.show()
            # plt.savefig(dire)#将该名称用于保存图片
            relax.write_input(str(gh) + '--' + str(n))  #将生成的VASP输入文件写入存储
            dire_1 = str(gh) + '--' + str(n)
            
            diree = os.chdir("./" + dire_1)
            fig.savefig('slab.png',bbox_inches='tight', transparent=True,dpi=600,format='png') 
            #定义一个更改当前目录的变量
            dire2 = './vaspstd_sub' 
            #确立脚本名称
            shutil.copy(r"C:\Users\41958\.spyder-py3\vaspstd_sub", dire2 )
            #将脚本写入VASP输入文件所在文件夹
            with open('surface_area','w') as f:
                f.write(str(cc))
            print (cc)
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
        from pymatgen.ext.matproj import MPRester
        from matplotlib import pyplot as plt
        from pymatgen.io.vasp.inputs import Poscar
        from pymatgen.io.vasp.sets import MVLSlabSet
        import shutil
        import os
        mpr = MPRester()#密钥

        mp_id = self.mp_id#通过mp_id来索引结构
        struct = mpr.get_structure_by_material_id(mp_id)
        #获取结构信息
        struct = SpacegroupAnalyzer(struct).get_conventional_standard_structure()
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
            dire = str(mp_id) + "---" + "sol" + str(EB_K_2)+ str(need_miller_index) + '----' + str(n)
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
        os.chdir(r"D:\Desktop\VASP practical\workdir")
        from pymatgen import Lattice, Structure
        from pymatgen.analysis.diffraction.xrd import XRDCalculator
        from IPython.display import Image, display
        from pymatgen.ext.matproj import MPRester
        mpr = MPRester()
        mp_id = self.mp_id
        structure = mpr.get_structure_by_material_id(mp_id)
        c = XRDCalculator()
        print (c)
        c.show_plot(structure)
        print (os.getcwd()) 




    def phase(self,judge='',appendage=""):
        import os
        import re
        os.chdir(r"F:\VASP practical\Input")
        print (os.getcwd())
        from pymatgen import Structure
        from pymatgen.io.vasp.sets import MPRelaxSet
        from pymatgen.ext.matproj import MPRester
        import shutil
        
        mpr = MPRester()
        mp_id = self.mp_id
        structure = mpr.get_structure_by_material_id(mp_id)
        structure.make_supercell(self.supercell)

        custom_settings = {"NPAR": 4} # user custom incar settings
        relax = MPRelaxSet(structure, user_incar_settings=custom_settings)
        relax.write_input(mp_id + '---' + 'phase')
        os.chdir("./" + mp_id + '---' + 'phase') 
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
        os.chdir(r"F:\VASP practical\Input")
        print (os.getcwd())
        from pymatgen import Structure
        from pymatgen.io.vasp.sets import MPRelaxSet
        from pymatgen.ext.matproj import MPRester
        import shutil
        
        mpr = MPRester()
        mp_id = self.mp_id
        structure = mpr.get_structure_by_material_id(mp_id)
        custom_settings = {"NPAR": 4} # user custom incar settings
        relax = MPRelaxSet(structure, user_incar_settings=custom_settings)
        relax.write_input(mp_id + '---' + "sol" + str(EB_K_2) + 'phase')
        os.chdir("./" + mp_id + '---' + "sol" + str(EB_K_2) + 'phase') 
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
        from pymatgen.ext.matproj import MPRester
        from pathlib import Path
        import matplotlib.pyplot as plt
        import pandas as pd
        mpr = MPRester()
        mp_id = self.mp_id
        # direc = mp_id + '---' + 'phase'
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
            my_file = Path("./" + mp_id + '---' + "sol" + str(n) + 'phase')
            if my_file.exists():
                os.chdir("./" + mp_id + '---' + "sol" + str(n) + 'phase')
                print (os.getcwd())
                v = Vasprun("vasprun.xml")
                print(v.final_energy) # final total energy
                x_ax.append(n)
                y_ax.append(v.final_energy)
                s = v.final_structure
                s.to(filename= mp_id + '---' + "sol" + str(n) + ".cif") # save relaxed structure into cif file
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
        from pymatgen.ext.matproj import MPRester
        from pathlib import Path
        import matplotlib.pyplot as plt
        import pandas as pd
        mpr = MPRester()
        mp_id = self.mp_id
        direc = mp_id + '---' + 'phase'
        os.chdir(r"D:\Desktop\VASP practical\Output")
        os.chdir("./" + direc) 
        v = Vasprun("vasprun.xml")
        h = v.final_energy
        print(h) # final total energy
        s = v.final_structure
        s.to(filename=mp_id + ".cif") # save relaxed structure into cif file
        print('Done!!') # relaxed structure
        return h
    
    
    
    def phase_out_sol_outcar(self,EB_K_3):
        import regex as re
        from pymatgen.io.vasp import Vasprun
        import os
        from pymatgen.ext.matproj import MPRester
        from pathlib import Path
        import matplotlib.pyplot as plt
        import pandas as pd
        mpr = MPRester()
        mp_id = self.mp_id
        
        os.chdir(r"D:\Desktop\VASP practical\Output")
        
        print (os.getcwd())
        x_ax = []
        y_ax = []
        os.chdir(mp_id + '---' + 'phase')
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
            my_file = Path("./" + mp_id + '---' + "sol" + str(n) + 'phase')
            if my_file.exists():
                os.chdir("./" + mp_id + '---' + "sol" + str(n) + 'phase')
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
        from pymatgen.ext.matproj import MPRester
        from pathlib import Path
        import matplotlib.pyplot as plt
        import pandas as pd
        mpr = MPRester()
        mp_id = self.mp_id
        
        os.chdir(r"F:\VASP practical\Input")
        
        print (os.getcwd())
        x_ax = []
        

        for n in EB_K_2:
            my_file = Path("./" + mp_id + '---' + "sol" + str(n) + 'phase')
            if my_file.exists():
                os.chdir("./" + mp_id + '---' + "sol" + str(n) + 'phase')
                print (os.getcwd())
               
#kk = 'energy  without entropy=     -278.28980146  energy(sigma->0) =     -278.28980146'    
# pattern = re.compile(r'\e+n+t+r+o+p+y+')
                
# d=pattern.findall(kk)
                
                x_ax.append(n)
                
                os.chdir(r"F:\VASP practical\Input")
                print (os.getcwd())
                
            else:
                print('not find')

        with open('script', 'w') as f:
            f.write('cd ~/;cd wcl;cd VASP;' +'cd ' + mp_id + '---' + 'phase;' +'sbatch vaspstd_sub;' + 'cd ../;' + 'cd ' + mp_id + '---' + "sol" + str(EB_K_2[0]) + 'phase;' +'sbatch vaspstd_sub;'+ 'cd ../;' + 'cd ' + mp_id + '---' + "sol" + str(EB_K_2[1]) + 'phase;'+'sbatch vaspstd_sub;' + 'cd ../;' + 'cd ' + mp_id + '---' + "sol" + str(EB_K_2[2]) + 'phase;' +'sbatch vaspstd_sub;'+ 'cd ../;' + 'cd ' + mp_id + '---' + "sol" + str(EB_K_2[3]) + 'phase;' +'sbatch vaspstd_sub;' + 'squeue')
            # f.close()
            # data = f.readlines()
            # print(f)
        
        os.startfile(r"F:\VASP practical\Input\script")
        




    def absorbed (self,need_miller_index, mole, num, selective_dynamic,min_slab_size_1=8.0 ,min_vacuum_size_1=15,judge='fuchdi',appendage=""):

        from pymatgen import Structure, Lattice, MPRester, Molecule
        import pymatgen.core.structure

        import pymatgen.core.sites
        from pymatgen.analysis.adsorption import AdsorbateSiteFinder, reorient_z, plot_slab
        from pymatgen.core.surface import generate_all_slabs
        from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
        from matplotlib import pyplot as plt
        from pymatgen.ext.matproj import MPRester
        from pymatgen.io.vasp.inputs import Poscar
        from pymatgen.io.vasp.sets import MVLSlabSet
        from pymatgen.io.cif import CifWriter
        import os
        import shutil
        from pymatgen.core.surface import Slab, SlabGenerator, generate_all_slabs, Structure, Lattice, ReconstructionGenerator
        mp_id = self.mp_id
        os.chdir(r"F:\VASP practical\Input")
        print (os.getcwd()) 

        # Note that you must provide your own API Key, which can
        # be accessed via the Dashboard at materialsproject.org
        mpr = MPRester()
        struct = mpr.get_structure_by_material_id(mp_id)
        struct = SpacegroupAnalyzer(struct).get_conventional_standard_structure()
        # fcc_ni = Structure.from_spacegroup("Fm-3m", Lattice.cubic(3.5), ["Ni", "Ni"],
        # [[0, 0, 0], [0.5, 0.5, 0.5]])
        slab = SlabGenerator(struct, miller_index=need_miller_index, min_slab_size=min_slab_size_1,min_vacuum_size=min_vacuum_size_1, center_slab=True)

        for n, slabs in enumerate(slab.get_slabs()):
            if str(n)  in str(num):
                slabs_bak = slabs.copy()#可能的晶面
                slabs.make_supercell(self.supercell)
                print(n)
                #晶胞扩充

                asf_ni_111 = AdsorbateSiteFinder(slabs,selective_dynamics=selective_dynamic)
                ads_sites = asf_ni_111.find_adsorption_sites()



                print(ads_sites)
                assert len(ads_sites) == 4

                fig0 = plt.figure()
                ax = fig0.add_subplot(111)
                plot_slab(slabs, ax, adsorption_sites=False)
                plot_slab(slabs, ax, adsorption_sites=True)

                fig1 = plt.figure()
                ax = fig1.add_subplot(111)
                os.chdir(r"D:\Desktop\VASP practical\Cif library")  
                print (os.getcwd())
                adsorbate = Molecule.from_file(mole)
                os.chdir(r"F:\VASP practical\Input")
                print (os.getcwd())
                print (adsorbate.sites)
                ads_structs = asf_ni_111.add_adsorbate(adsorbate,[ 3.57082469,  0.67922288, 20.0970827 ])
                # ads_structs = asf_ni_111.generate_adsorption_structures(adsorbate,
                # repeat=[1, 1, 1])
                # A = Poscar(ads_structs[0])
                A = str(Poscar(reorient_z(ads_structs))) #将切面转换为Poscar
                open('POSCAR', 'w').write(str(A))
                p = Poscar.from_file('POSCAR')
                # w = CifWriter(A.struct)
                # w.write_file('mystructure.cif')
                path = r'F:\VASP practical\Input\POSCAR'  # 文件路径
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
                dire = str(mp_id) + "---"+ str(mole)+ str(need_miller_index).replace(" ", "") + str(n) 
                # print (relax)
                relaxs.write_input(dire)
                os.chdir("./" + dire) 
                print (os.getcwd()) 
                fig0.savefig('slab.png',bbox_inches='tight', transparent=True,dpi=600,format='png')
                plot_slab(ads_structs, ax, adsorption_sites=False, decay=0.09)
                fig1.savefig('slab_adsobate.png',bbox_inches='tight', transparent=True,dpi=600,format='png')
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





                
                # open('POSCAR001', 'w').write(str(Poscar(reorient_z(ads_structs[0]))))

                os.chdir(r"D:\Desktop\VASP practical\workdir")
                print (os.getcwd())
                print ('finished')


    def fix_absorbed (self,need_miller_index, mole, num,selective_dynamic, min_slab_size_1=8.0,  min_vacuum_size_1=15,judge='fuchdi',appendage=""):
        from pymatgen import Structure, Lattice, MPRester, Molecule
        import pymatgen.core.structure

        import pymatgen.core.sites
        from pymatgen.analysis.adsorption import AdsorbateSiteFinder, reorient_z, plot_slab
        from pymatgen.core.surface import generate_all_slabs
        from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
        from matplotlib import pyplot as plt
        from pymatgen.ext.matproj import MPRester
        from pymatgen.io.vasp.inputs import Poscar
        from pymatgen.io.vasp.sets import MVLSlabSet
        from pymatgen.io.cif import CifWriter
        import os
        import shutil
        from openbabel import openbabel
        from pymatgen.core.surface import Slab, SlabGenerator, generate_all_slabs, Structure, Lattice, ReconstructionGenerator
        mp_id = self.mp_id
        os.chdir(r"F:\VASP practical\Input")
        print (os.getcwd()) 

        # Note that you must provide your own API Key, which can
        # be accessed via the Dashboard at materialsproject.org
        mpr = MPRester()
        struct = mpr.get_structure_by_material_id(mp_id)
        struct = SpacegroupAnalyzer(struct).get_conventional_standard_structure()
        # fcc_ni = Structure.from_spacegroup("Fm-3m", Lattice.cubic(3.5), ["Ni", "Ni"],
        # [[0, 0, 0], [0.5, 0.5, 0.5]])
        slab = SlabGenerator(struct, miller_index=need_miller_index, min_slab_size=min_slab_size_1,min_vacuum_size=min_vacuum_size_1, center_slab=True)

        for n, slabs in enumerate(slab.get_slabs()):
            if str(n)  in str(num):
                slabs_bak = slabs.copy()#可能的晶面
                slabs.make_supercell(self.supercell)
                print(n)
                #晶胞扩充

                asf_ni_111 = AdsorbateSiteFinder(slabs,selective_dynamics=selective_dynamic)
                ads_sites = asf_ni_111.find_adsorption_sites()



                # print(ads_sites)
                assert len(ads_sites) == 4

                fig0 = plt.figure()
                ax = fig0.add_subplot(111)
                plot_slab(slabs, ax, adsorption_sites=False)


                fig1 = plt.figure()
                ax = fig1.add_subplot(111)
                os.chdir(r"D:\Desktop\VASP practical\Cif library")  
                print (os.getcwd())
                obConversion = openbabel.OBConversion()
                obConversion.SetInAndOutFormats("pdb","gjf")
                mol = openbabel.OBMol()
                print (mol)
                c=obConversion.ReadFile(mol, "CH3OH.pdb")
                obConversion.WriteFile(mol, "CH3OH.pdb"+'1.gjf')
                adsorbate = Molecule.from_file("CH3OH.pdb"+'.gjf')
                os.chdir(r"F:\VASP practical\Input")
                print (os.getcwd())
         
                print (adsorbate.sites)
                ads_structs = asf_ni_111.add_adsorbate(adsorbate,(20,20,20),translate=False,)
                # ads_structs = asf_ni_111.generate_adsorption_structures(adsorbate,
                # repeat=[1, 1, 1])
                # A = Poscar(ads_structs[0])
                A = Poscar(reorient_z(ads_structs)) #将切面转换为Poscar
                open('POSCAR', 'w').write(str(A))
                p = Poscar.from_file('POSCAR')
                # w = CifWriter(A.struct)
                # w.write_file('mystructure.cif')
                path = r'F:\VASP practical\Input\POSCAR'  # 文件路径
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
                dire = str(mp_id) + str(selective_dynamic)+ str(mole)+ str(need_miller_index).replace(" ", "")+str(n)  
                # print (relax)
                relaxs.write_input(dire)
                os.chdir("./" + dire) 
                print (os.getcwd()) 
                fig0.savefig('slab.png',bbox_inches='tight', transparent=True,dpi=600,format='png')
                plot_slab(ads_structs, ax, adsorption_sites=False, decay=0.09)
                fig1.savefig('slab_adsobate.png',bbox_inches='tight', transparent=True,dpi=600,format='png')
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





                
                # open('POSCAR001', 'w').write(str(Poscar(reorient_z(ads_structs[0]))))

                os.chdir(r"D:\Desktop\VASP practical\workdir")
                print (os.getcwd())
                print ('finished')




        
# my_lattace = Lattace('mp-698074')#半水石膏
# # my_lattace.phase_out()#生成晶胞优化的输入文件
# go = my_lattace.phase_sol(66,judge='LWAVE',  appendage= '\nLWAVE = Ture')
# print('yoo')