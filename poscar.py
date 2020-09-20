class Poscar():
    import os
    print (os.getcwd()) 
    f = [[1,0,0],
         [0,1,0],
         [0,0,1]]
    def __init__(self,dire,supercell = f,):
        self.dire=dire
        self.supercell = supercell
        
    os.chdir(r"D:\Desktop\VASP practical\Input")  
    print (os.getcwd())   
    
    def slab(self,name):
        
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
        os.chdir(self.dire) 
        print (os.getcwd())
        poscar = Poscar.from_file("POSCAR")
        relax = poscar.structure

        custom_settings = {"NPAR": 4,'ICHARG':2,} # 用户的INCAR 设置
        relax = MVLSlabSet(relax, user_incar_settings=custom_settings)
        #Vasp输入文件生成器
        

        dire =str(name)
        #设置一个用作存储输入文件的名称

        relax.write_input(dire)  #将生成的VASP输入文件写入存储
        
        
        diree = os.chdir("./" + dire) 
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
            
            
    