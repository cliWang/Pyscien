class Write():
    import os
    def __init__(self,dire,dire_ori = r'D:\Desktop\VASP practical\Input\INCAR_std' ):
        self.dire = dire
        self.dire_ori = dire_ori
    def file(self,origin,aim):
        import os
        import shutil
        filePath = self.dire
        os.chdir(self.dire)
        print (os.getcwd())
        
        # for dirpath, dirnames in os.walk(filePath):
            # # print(dirnames)
            # import pandas 
            # import numpy as np
            # import os
            # for d in dirnames:
        for dirpath, dirnames, filenames in os.walk(filePath):
            # print(dirpath)
            for name in dirnames:
                path = os.path.join(filePath, name)
                os.chdir(path)
                print (os.getcwd())
                subfile='D:\Desktop\VASP practical\Input\INCAR_std'
                aimm=os.path.join(subfile, origin)
                shutil.copyfile(aimm, aim)
                # with open(aim,'w') as f:
                #     os.chdir(self.dire_ori)
                #     print (os.getcwd())
                #     f.write(open(origin).read())
                #     # print (origin)
                    # print (open(origin).read())
        os.chdir(self.dire)
        old_name= r'D:\Desktop\VASP practical\Input\INCAR_std\sub.sh'
        new_name= os.path.join(filePath, 'sub.sh')
        shutil.copyfile(old_name, new_name)
        os.chdir(r"D:\Desktop\VASP practical\workdir")
        print (os.getcwd())



    def energy(self):
        import regex as re
        from pymatgen.io.vasp import Vasprun
        import os
        from pymatgen.ext.matproj import MPRester
        from pathlib import Path
        import matplotlib.pyplot as plt
        import pandas as pd
        mpr = MPRester()
        
        
        filePath = self.dire
        x_ax = []
        y_ax = []
       
        for dirpath, dirnames, filenames in os.walk(filePath):

            for name in dirnames:
                path = os.path.join(filePath, name)

                print (path)
                
                os.chdir(path)
                print (os.getcwd())
        
                with open("OUTCAR", "r") as f:
                    data = f.readlines()
                string=str(data)
                pattern = re.compile(r"(?<=energy  without entropy=)\ *\-*\d+\.?\d*")
                c=pattern.findall(string)

                e = c[-1]
                x_ax.append(name)
                y_ax.append(e)


        da = {'Slab':x_ax,'Formation energy':y_ax}
        res=pd.DataFrame(da)#构造原始数据文件
        df = res.sort_values(by='Formation energy', ascending=True)
        a=df['Slab']
        b=df['Formation energy']        
        os.chdir(self.dire)
        print (os.getcwd())
        df.to_excel("2.xlsx")#生成Excel文件，并存到指定文件路径下
        
        fig, ax = plt.subplots()

        ax.scatter(a, b)
        plt.xticks(rotation=81)
        fig.suptitle('Formation energy')
        fig.savefig('Formation energy.png',bbox_inches='tight', transparent=True,dpi=600,format='png')
        plt.show()
        print('Done!!')


    def mol_energy(self):
        import regex as re
        from pymatgen.io.vasp import Vasprun
        import os
        from pymatgen.ext.matproj import MPRester
        from pathlib import Path
        import matplotlib.pyplot as plt
        import pandas as pd
        mpr = MPRester()
        
        
        filePath = self.dire
        
        
        # for dirpath, dirnames in os.walk(filePath):
            # # print(dirnames)
            # import pandas 
            # import numpy as np
            # import os
            # for d in dirnames:
        x_ax = []
        y_ax = []
       
        for dirpath, dirnames, filenames in os.walk(filePath):
            # print(dirpath)
            for name in dirnames:
                path = os.path.join(filePath, name)
                # os.chdir(path)
                # print (os.getcwd())

                
                os.chdir(path)
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
                x_ax.append(name)
                y_ax.append(e)
                # os.chdir(r"D:\Desktop\VASP practical\Output")
                # print (os.getcwd())

        da = {'molecular':x_ax,'Formation energy':y_ax}
        res=pd.DataFrame(da)#构造原始数据文件
        df = res.sort_values(by='Formation energy', ascending=True)
        a=df['molecular']
        b=df['Formation energy']        
        os.chdir(self.dire)
        print (os.getcwd())
        df.to_excel("5.xlsx")#生成Excel文件，并存到指定文件路径下
        
        fig, ax = plt.subplots()

        ax.scatter(a, b)
        plt.xticks(rotation=81)
        fig.suptitle('Formation energy')
        fig.savefig('Formation energy.png',bbox_inches='tight', transparent=True,dpi=600,format='png')
        plt.show()
        print('Done!!')







    def surface_energy(self, unit_energy, unit_number):
        import regex as re
        from pymatgen.io.vasp import Vasprun
        import os
        from pymatgen.ext.matproj import MPRester
        from pathlib import Path
        import matplotlib.pyplot as plt
        import pandas as pd    
        filePath = self.dire   
        os.chdir(self.dire)

        print (os.getcwd())        
        res = pd.read_excel("2.xlsx")
        df = res.sort_values(by='Formation energy', ascending=True)
        a=df['Slab']
        b=df['Formation energy']
        u = []
        # d = []
        # for aa in a:
        #     cc = str(aa)
        #     bb = cc[-15:]
        #     d.append(bb)
        # print (d)
        for dirpath, dirnames, filenames in os.walk(filePath):
            # print(dirpath)
            for name in dirnames:
                path = os.path.join(filePath, name)
                # os.chdir(path)
                # print (os.getcwd())

                
                os.chdir(path)
                # print (os.getcwd())        
                with open('surface_area') as file_obj:
                    content = file_obj.read()
                u.append(content)
                # print(content)
        uu = [ 2*float(x) for x in u ]
        dd = b-unit_number*unit_energy
        ff = (dd/uu)*16.02
        c = ff
        print (c)
        da = {'Slab':a,'Formation energy':b,'surface energy':c,'surface area':u}
        df=pd.DataFrame(da)#构造原始数据文件
        os.chdir(self.dire)
        # print (os.getcwd())
        # 
        df.to_excel("3.xlsx")#生成Excel文件，并存到指定文件路径下

        fig, ax = plt.subplots()
        ax.scatter(a, c)
        # plt.xticks(rotation=81)
        ax.set_xlabel('surface')
        ax.set_ylabel('surface energy  (J/$m^2$)')
        fig.suptitle('surface energy')
        fig.savefig('surface energy.png',bbox_inches='tight', transparent=True,dpi=600,format='png')
        plt.show()
        print('Done!!')

    def molecular(self,name):
        
        import os
        import numpy as np
        from pymatgen.io.phonopy import get_phonopy_structure 
        import pymatgen as pmg
        from pymatgen.io.vasp.outputs import Vasprun
        from pymatgen.io.vasp import Poscar
        from phonopy import Phonopy
        from phonopy.structure.atoms import Atoms as PhonopyAtoms
        import csv
        import pandas as pd
        import matplotlib.pyplot as plt
        os.chdir(self.dire)
        print (os.getcwd())

        poscar = Poscar.from_file("POSCAR")
        structure = poscar.structure
        scell = [[1,0,0],[0,1,0],[0,0,1]]
        vrun = Vasprun("vasprun.xml")
        phonopyAtoms = get_phonopy_structure(structure)
        phonon = Phonopy(phonopyAtoms, scell)

        phonon.set_force_constants(-vrun.force_constants)

        labels = ["$\\Gamma$", "X", "U", "K", "$\\Gamma$", "L", "W"]
        bands = []

        # path 1
        q_start  = np.array([0.5, 0.5, 0.0])
        q_end    = np.array([0.0, 0.0, 0.0])
        band = []
        for i in range(51):
            band.append(q_start + (q_end - q_start) / 50 * i)
        bands.append(band)

        # path 2
        q_start  = np.array([0.0, 0.0, 0.0])
        q_end    = np.array([0.5, 0.0, 0.0])
        band = []
        for i in range(51):
            band.append(q_start + (q_end - q_start) / 50 * i)
        bands.append(band)

        phonon.set_band_structure(bands,labels=labels)

        # phonon.plot_band_structure().show()

        mesh = [31, 31, 31]
        phonon.set_mesh(mesh)

        phonon.set_total_DOS()
        phonon.write_total_DOS()
        # phonon.plot_total_DOS().show()
        # c = np.fromfile('total_dos.dat', dtype=float)

        datContent = [i.strip().split() for i in open("./total_dos.dat").readlines()]
        del datContent[0]
        x_ax = []
        y_ax = []
        for i in datContent:
            x_ax.append(1/((3*(10**8)/(float(i[0])*(10**12)))*100))
            y_ax.append(float(i[1]))





        da = {'Density of states':x_ax,'Frequency':y_ax}
        df=pd.DataFrame(da)#构造原始数据文件
        df.to_excel("Wave number.xlsx")#生成Excel文件，并存到指定文件路径下





        fig, ax = plt.subplots()


        line1 = ax.plot(x_ax, y_ax,label = name)
        ax.set_xlim([4500, 200])




        # 以下是XRD图片的格式设置
        #设置横纵坐标的名称以及对应字体格式
        font2 = {'family' : 'Times New Roman',
        'weight' : 'bold',
        }
        plt.xlabel('Wavenumber ($\mathregular{cm^-}$$\mathregular{^1}$)' ,font2)
        plt.ylabel('Density of states' ,font2)

        #不显示Y轴的刻度
        plt.yticks([])

        #设置图例对应格式和字体
        font1 = {'family' : 'Times New Roman',
        'weight' : 'bold',
        }
        ax.legend(edgecolor='none', prop=font1)

        plt.legend(edgecolor='none', prop=font1)
        # plt.set_facecolor('none') 
        ax.set_facecolor('none') 

        #存储为
        fig.savefig('D:\Desktop\python image\cal_FTIR.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
        plt.show()


    def  copy(self,na='POSCAR'):

        import os
        import shutil
        filePath = self.dire
        os.chdir(self.dire)
        print (os.getcwd())
        
        # for dirpath, dirnames in os.walk(filePath):
            # # print(dirnames)
            # import pandas 
            # import numpy as np
            # import os
            # for d in dirnames:
        # for dirpath, dirnames, filenames in os.walk(filePath):
        #     # print(dirpath)
        #     for name in dirnames:
        #         path = os.path.join(filePath, name)
        #         os.chdir(path)
        #         print (os.getcwd())
        #         with open(aim,'w') as f:
        #             f.write(open(origin).read())
        #             # print (origin)
        #             # print (open(origin).read())
            

        for dirpath, dirnames, filenames in os.walk(filePath):
            # print(dirnames)
            if "new" in str(dirnames):
                print('the folder have been copied')

            else:
                    #     # print(dirpath)
                for name in dirnames:                    
                  # if subfolders!= r'001.txt':                       #当文件名不为“001.txt”时
                                    #当文件名以.txt后缀结尾时
                  #        new_name=subfolders.replace('subfolders','new_subfolders')  
                    new_name = 'new' + '_' + name
                    shutil.copytree(os.path.join(filePath, name),os.path.join(filePath, new_name))
                    # shutil.copyfile(subfolders, new_subfolders)    #复制并重命名文件
                    print(name,"copied as",new_name)    

        for dirpath, dirnames, filenames in os.walk(filePath):
            # print(dirpath)
            for name in dirnames:
                if 'new' in name:
                    path = os.path.join(filePath, name)
                    os.chdir(path)
                    print (os.getcwd())

                    with open('POSCAR','w') as f:
                        f.write(open(na).read())

                        # print (origin)
                        # print (open(origin).read())
                    for dirpath, dirnames, filenames in os.walk(path):
                        print (filenames)
                        for name in filenames:
                            if 'INCAR' in name or 'POSCAR' in name or 'POTCAR' in name or 'KPOINTS' in name or 'vaspstd_sub' in name:
                                print (name)
                            else:
                                path_in = os.path.join(path, name)
                                os.remove(path_in)
        print('\033[5;32;41m Joyce happy \033[0m')
        # print ('\033[0;36m Joyce happy，')


        os.chdir(r"D:\Desktop\VASP practical\workdir")
        # print (os.getcwd())
        
        import matplotlib.pyplot as plt
        import numpy as np
        from matplotlib.patches import Ellipse

        NUM = 250

        ells = [Ellipse(xy=np.random.rand(2) * 10,
                        width=np.random.rand(), height=np.random.rand(),
                        angle=np.random.rand() * 360)
                for i in range(NUM)]

        fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
        for e in ells:
            ax.add_artist(e)
            e.set_clip_box(ax.bbox)
            e.set_alpha(np.random.rand())
            e.set_facecolor(np.random.rand(3))

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        plt.show()
        print('\033[5;32;41m Joyce happy \033[0m')




    def adsorbate_energy(self, unit_energy, unit_number,mol_energy,mol_number):
        import regex as re
        from pymatgen.io.vasp import Vasprun,Oszicar
        import os
        from pymatgen.ext.matproj import MPRester
        from pathlib import Path
        import matplotlib.pyplot as plt
        import pandas as pd

        filePath = self.dire   
        os.chdir(self.dire)

        print (os.getcwd())        
        res = pd.read_excel("2.xlsx")
        df = res.sort_values(by='Formation energy', ascending=True)
        a_slab=df['Slab']#晶面
        a_energy=df['Formation energy']#对应的形成能
        u = []#表面积
        res = pd.read_excel("3.xlsx")
        df = res.sort_values(by='surface_energy', ascending=True)
        b_slab=df['Slab']#晶面
        b_energy=df['Formation energy']#对应的形成能
        b_surf_energy=df['surface energy']#x吸附前表面能
        b_area =df['surface area']#表面积
        double_area = [ 2*float(x) for x in b_area ]#上下两个表面的表面积
        residul_energy = a_energy-unit_number*unit_energy-mol_energy*mol_number#表面带来的能量差
        
        a_surf_energy = (residul_energy/double_area)*16.02#从电子伏特换算到焦耳,吸附后表面能
        adsor_energy=(a_slab-mol_energy*mol_number-b_energy)/mol_number

        da = {'Slab':a_slab,'Surface area':u,'Formation energy before':b_energy,'Formation energy after':a_energy,'Surface energy before':b_surf_energy,'Surface energy after':a_surf_energy,'Adsorption energy':adsor_energy}
        df=pd.DataFrame(da)#构造原始数据文件
        os.chdir(self.dire)
        # print (os.getcwd())
        df.to_excel("4.xlsx")#生成Excel文件，并存到指定文件路径下

        fig1 = plt.subplots()
        ax = fig1.add_subplot(1,1,1)
        line1 = ax.scatter(a_slab, b_surf_energy)
        line2 = ax.scatter(a_slab,a_surf_energy)

        plt.xticks(rotation=81)
        ax.set_xlabel('Slab')
        ax.set_ylabel('surface energy  (J/$m^2$)')
        fig.suptitle('surface energy')
        fig.savefig('surface energy.png',bbox_inches='tight', transparent=True,dpi=600,format='png')
        plt.show()
        fig2 = plt.subplots()
        ax = fig2.add_subplot(1,1,1)
        line1 = ax.scatter(a_slab, adsor_energy)
        plt.xticks(rotation=81)
        ax.set_xlabel('Slab')
        ax.set_ylabel('Adsorption energy  (J/$m^2$)')
        fig.suptitle('Adsorption energy')
        fig.savefig('Adsorption energy.png',bbox_inches='tight', transparent=True,dpi=600,format='png')
        plt.show()
        print('Done!!')








    def muti_adsorbate_energy(self, unit_energy, unit_number,mol_number):
        import regex as re
        from pymatgen.io.vasp import Vasprun,Oszicar
        import os
        from pymatgen.ext.matproj import MPRester
        from pathlib import Path
        import matplotlib.pyplot as plt
        import pandas as pd

        filePath = self.dire   
        os.chdir(self.dire)




        print (os.getcwd())        
        res = pd.read_excel("5.xlsx")
        df = res.sort_values(by='Formation energy', ascending=True)
        a_slab=df['molecular']#晶面
        a_energy=df['Formation energy']#对应的形成能
        u = []#表面积
        res = pd.read_excel("2.xlsx")
        df = res.sort_values(by='surface_energy', ascending=True)
        b_slab=df['Slab']#晶面
        b_energy=df['Formation energy']#对应的形成能


        adsor_energy=(b_energy-a_slab*mol_number-unit_number*unit_energy)/mol_number

        da = {'Slab':a_slab,'Adsorption energy':adsor_energy}
        df=pd.DataFrame(da)#构造原始数据文件
        os.chdir(self.dire)
        # print (os.getcwd())
        df.to_excel("4.xlsx")#生成Excel文件，并存到指定文件路径下

        fig1 = plt.subplots()
        ax = fig1.add_subplot(1,1,1)
        line1 = ax.scatter(a_slab, b_surf_energy)
        line2 = ax.scatter(a_slab,a_surf_energy)

        plt.xticks(rotation=81)
        ax.set_xlabel('Slab')
        ax.set_ylabel('surface energy  (J/$m^2$)')
        fig.suptitle('surface energy')
        fig.savefig('surface energy.png',bbox_inches='tight', transparent=True,dpi=600,format='png')
        plt.show()
        fig2 = plt.subplots()
        ax = fig2.add_subplot(1,1,1)
        line1 = ax.scatter(a_slab, adsor_energy)
        plt.xticks(rotation=81)
        ax.set_xlabel('Slab')
        ax.set_ylabel('Adsorption energy  (J/$m^2$)')
        fig.suptitle('Adsorption energy')
        fig.savefig('Adsorption energy.png',bbox_inches='tight', transparent=True,dpi=600,format='png')
        plt.show()
        print('Done!!')