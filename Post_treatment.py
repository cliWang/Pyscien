class Post_treatment():
    def __init__(self,dire):

        self.dire = dire
    def Wullff(self,formate,surface_energy,pic_name,directions=(3,4,4),x=0.47,y=-16):
        from pymatgen.core.surface import SlabGenerator, generate_all_slabs, Structure, Lattice
        # Import the neccesary tools for making a Wulff shape
        from pymatgen.analysis.wulff import WulffShape
        from pymatgen.ext.matproj import MPRester
        from pymatgen.io.cif import CifParser
        import matplotlib.pyplot as plt
        import matplotlib.image as mpimg
        import pandas as pd
        import os
        if 'cif' in str(formate):

            os.chdir(r"D:\Desktop\VASP practical\Cif library")  
            print (os.getcwd())   
            structure = CifParser(str(pic_name)+'.cif')
            struct = structure.get_structures()[0]
        else:
            mpr = MPRester()

            mp_id = formate
            struct = mpr.get_structure_by_material_id(mp_id)
        surface_energies = surface_energy
        miller_list = surface_energies.keys()
        e_surf_list = surface_energies.values()
        font2 = {'family' : 'Times New Roman','fontsize':'40' , 'weight' : 'bold',}
        wulffshape = WulffShape(struct.lattice, miller_list, e_surf_list)
        print(wulffshape.area_fraction_dict)
        os.chdir(self.dire)
        dict1 = wulffshape.area_fraction_dict
        xx =[]
        yy =[]
        for key,value in dict1.items():
            xx.append(key)
            yy.append(value)
 
        cc=wulffshape.effective_radius
        bb =wulffshape.volume
        dd = wulffshape.shape_factor
        print(wulffshape.effective_radius)
        res=pd.DataFrame({'Slab':xx,'area':yy})#构造原始数据文件
        df = res.sort_values(by='area', ascending=True) 
        with open(str(pic_name)+'.txt','w') as f:

            f.write('effective radius:' +str(cc)+'         '+"volume:"+str(bb)+'         '+"shape factor:"+str(dd))
        print (cc)       
        # os.chdir(r"D:\Desktop\VASP practical\workdir")
        df.to_excel(str(pic_name)+".xlsx")#生成Excel文件，并存到指定文件路径下
        wulffshape.get_plot(bar_on=True,aspect_ratio=(8,8) ,bar_pos=[0, 0.85, 1.1, 0.045],direction=directions)


        plt.title(str(pic_name),font2,x=x,y=y)  
        
        plt.savefig(str(pic_name)+".png",bbox_inches='tight', transparent=True,dpi=600,format='png')


        plt.show
        os.chdir(r"D:\Desktop\VASP practical\workdir")
        print ('finished')

    def RMSDs(self,group):
        import MDAnalysis
        import MDAnalysis.analysis.rms
        from MDAnalysis.tests.datafiles import PSF, DCD, CRD
        from MDAnalysis.analysis import rms
        import matplotlib.pyplot as plt
        import os

        os.chdir(self.dire)

        u = MDAnalysis.Universe('XDATCAR.pdb', permissive=True)
        ref = MDAnalysis.Universe('XDATCAR.pdb', permissive=True)     # reference (with the default ref_frame=0)
        ref.trajectory[0] #
        R = MDAnalysis.analysis.rms.RMSD(u, ref,
           select="all",         # superimpose on whole backbone of all atoms # align based on all atoms
           groupselections=group,
           filename="rmsd_all.dat",center=True)#
        timestep=0.0005  #0.5fs from fs to ps as Reader has no dt information, set to 1.0 ps          
        R.run()
        rmsd = R.rmsd.T   # transpose makes it easier for plotting
        time = rmsd[1]*timestep
        fig = plt.figure(figsize=(5,4))
        ax = fig.add_subplot(111)
        ax.plot(time, rmsd[2], 'k-',  label="all")
        ax.plot(time, rmsd[3], 'r--', label=str(group[0]))
        ax.plot(time, rmsd[4], 'b--', label=str(group[1]))
        font1 = {'family' : 'Times New Roman',
        'weight' : 'bold',
        }
        ax.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
        ax.set_xlabel("time (ps)")
        ax.set_ylabel(r"RMSD ($\AA$)")
        fig.savefig("rmsd_md_analysis.png",bbox_inches='tight', transparent=True,dpi=600,format='png')


    def RDF(self,type1,type2):
        import MDAnalysis
        import MDAnalysis.analysis.rdf
        import matplotlib.pyplot as plt
        # import matplotlib as plt
        

        import os

        os.chdir(self.dire) 
        print (os.getcwd())
        u = MDAnalysis.Universe('XDATCAR.pdb', permissive=True)
        g1= u.select_atoms(type1)
        g2= u.select_atoms(type2)
        rdf = MDAnalysis.analysis.rdf.InterRDF(g1,g2,nbins=75, range=(0.0, min(u.dimensions[:3])/2.0))
                   
        rdf.run()

        fig = plt.figure(figsize=(5,4))
        ax = fig.add_subplot(111)
        ax.plot(rdf.bins, rdf.rdf, 'g-',  label="rdf")
        font1 = {'family' : 'Times New Roman',
        'weight' : 'bold',
        }
        ax.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
        ax.set_xlabel(r"Distance ($\AA$)")
        ax.set_ylabel(r"RDF")
        fig.savefig("RDF_all.png",bbox_inches='tight', transparent=True,dpi=600,format='png')
        plt.show()



    def pdb_change(self,para='-p -t 0.5  --pbc'):

        from pymatgen.core.trajectory import Trajectory
        import shutil
        import os

        os.chdir(self.dire)
        shutil.copyfile(r"D:\Desktop\VASP practical\subscript\XDATCAR_toolkit.py","./XDATCAR_toolkit.py")
        wawe = 'python XDATCAR_toolkit.py' +' '+str(para)
        with open("change.cmd",'w') as f:
            f.write(wawe)

        result2 = os.popen('change').read()
        print(result2)
        #-t 0.5用于指定时间步为0.5 fs，--pbc用于获取基于第一帧演变的连续轨迹-b参数用于指定转换从哪一帧开始，-e参数用于指定转换到哪一帧结束。
        #
        #
        #
        #
        #



    def Diffusion(self,skip=10,spaces='S',temp=[300,310,350,390]):
        from pymatgen.analysis.diffusion_analyzer import DiffusionAnalyzer, fit_arrhenius,get_arrhenius_plot
        import shutil
        import os

        os.chdir(self.dire)
        filePath=self.dire
        file=[]
        for dirpath, dirnames, filenames in os.walk(filePath):
            # print(dirpath)
            for name in dirnames:
                path = os.path.join(filePath, name)
                path1 = os.path.join(path,'vasprun.xml')
                print(path1)
                file.append(str(path1))


        diff= DiffusionAnalyzer.from_files(file,specie=spaces,step_skip = skip)
        diff.get_msd_plot()
        diff.get_summary_dict()
        fit = fit_arrhenius(temps=temp,diffusivities=diff.diffusivity)
        plot = get_arrhenius_plot(temps=temp,diffusivities=diff.diffusivity)


    def Vibration(self,maxx=4500):
        import os
        import numpy as np
        from pymatgen.io.phonopy import get_phonopy_structure 
        import pymatgen as pmg
        from pymatgen.io.vasp.outputs import Vasprun
        from pymatgen.io.vasp import Poscar
        from pymatgen.symmetry.kpath import KPathSeek,KPathBase

        from phonopy import Phonopy
        from phonopy.structure.atoms import Atoms as PhonopyAtoms
        from pymatgen.phonon.plotter import PhononBSPlotter
        from pymatgen.phonon.bandstructure import PhononBandStructureSymmLine
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
        q_start  = np.array([0.0, 0.0, 0.0])
        q_end    = np.array([0.5, 0.0, 0.0])
        band = []
        for i in range(51):
            band.append(q_start + (q_end - q_start) / 50 * i)
        bands.append(band)
        
        # path 2
        q_start  = np.array([0.5, 0.0, 0.0])
        q_end    = np.array([0.5, 0.5, 0.0])
        band = []
        for i in range(51):
            band.append(q_start + (q_end - q_start) / 50 * i)
        bands.append(band)
        

        # # path 3
        # q_start  = np.array([0.5, 0.5, 0.0])
        # q_end    = np.array([-0.0, -0.0, 0.0])
        # band = []
        # for i in range(51):
        #     band.append(q_start + (q_end - q_start) / 50 * i)
        # bands.append(band)


        # # path 4
        # q_start  = np.array([0.0, 0.0, 0.0])
        # q_end    = np.array([0.5, 0.5, 0.5])
        # band = []
        # for i in range(51):
        #     band.append(q_start + (q_end - q_start) / 50 * i)
        # bands.append(band)
    




        print(bands)

        phonon.set_band_structure(bands)



        phonon.plot_band_structure().show()
        phonon.plot_band_structure().savefig("BAND.png")
        mesh = [31, 31, 31]
        phonon.set_mesh(mesh)

        phonon.set_total_DOS()
        phonon.write_total_DOS()
        phonon.plot_total_DOS().show()
        phonon.plot_total_DOS().savefig("DOS.png")
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


        line1 = ax.plot(x_ax, y_ax,c="grey")
        ax.set_xlim([maxx, 0])




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
        # ax.legend(edgecolor='none', prop=font1)

        # plt.legend(edgecolor='none', prop=font1)
        # plt.set_facecolor('none') 
        ax.set_facecolor('none') 

        #存储为
        fig.savefig('FTIR.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
        plt.show()


    def Vibrationauto(self,maxx=4500):
        import os
        import numpy as np
        from pymatgen.io.phonopy import get_phonopy_structure 
        import pymatgen as pmg
        from pymatgen.io.vasp.outputs import Vasprun
        from pymatgen.io.vasp import Poscar
        from pymatgen.symmetry.kpath import KPathSeek,KPathBase
        from phonopy.phonon.band_structure import get_band_qpoints_and_path_connections
        from phonopy import Phonopy
        from phonopy.structure.atoms import Atoms as PhonopyAtoms
        from pymatgen.phonon.plotter import PhononBSPlotter
        from pymatgen.phonon.bandstructure import PhononBandStructureSymmLine
        import csv
        import pandas as pd
        import matplotlib.pyplot as plt
        
        os.chdir(self.dire)
        print (os.getcwd())

        poscar = Poscar.from_file("POSCAR-unitcell")
        structure = poscar.structure
        scell = [[2,0,0],[0,2,0],[0,0,2]]
        vrun = Vasprun("vasprun.xml")
        phonopyAtoms = get_phonopy_structure(structure)
        phonon = Phonopy(phonopyAtoms, scell)

        phonon.set_force_constants(-vrun.force_constants)

        labels = ['L_2', 'GAMMA', 'V_2']
        # labels = ['K', "$\\Gamma$", 'L', 'W', 'X']
        # bands = []
        cd=KPathSeek(structure)
        cds=cd.kpath
        # print(cds)
        for k,v in cds.items():
            if "kpoints" in k:

                dics=v 
            else:
                dicss=v
        print(dics)
        print(dicss)


        # bands=[]
        # for k,v in dics.items():
        #     if k in dicss[0]:
        #         bands.append(v)

        path=[]
        # 
        
        # bandd1=[]
        # for k,v in dics.items():
        #     for i in dicss[0]:
        #             if k in i:
        #                 bandd1.append(v)                  
        # path.append(bandd1)

        bandd1=[]
        for i in dicss[1]:
            for k,v in dics.items():
                if k in i:
                    bandd1.append(v)                  
        path.append(bandd1)
        print(dicss[1])
        qpoints, connections = get_band_qpoints_and_path_connections(path, npoints=51)
        phonon.run_band_structure(qpoints, path_connections=connections, labels=labels)

        print(path)


        # kpoints=cd.get_kpoints

        # print(kpoints)

        # phonon.set_band_structure(bands,labels=labels)



        phonon.plot_band_structure().show()
        phonon.plot_band_structure().savefig("BAND.png",bbox_inches='tight', transparent=True,dpi=300,format='png')
        # phonon.write_band_structure()
        mesh = [31, 31, 31]
        phonon.set_mesh(mesh)

        phonon.set_total_DOS()
        phonon.write_total_DOS()
        phonon.plot_total_DOS().show()
        phonon.plot_total_DOS().savefig("DOS.png")
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


        line1 = ax.plot(x_ax, y_ax,c='grey')
        ax.set_xlim([maxx, 0])




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
        # ax.legend(edgecolor='none', prop=font1)

        # plt.legend(edgecolor='none', prop=font1)
        # plt.set_facecolor('none') 
        ax.set_facecolor('none') 

        #存储为
        fig.savefig('FTIR.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
        plt.show()




    def MVibrationauto(self,maxx=4500):
        import os
        import numpy as np
        from pymatgen.io.phonopy import get_phonopy_structure 
        import pymatgen as pmg
        from pymatgen.io.vasp.outputs import Vasprun
        from pymatgen.io.vasp import Poscar
        from pymatgen.symmetry.kpath import KPathSeek,KPathBase
        from phonopy.phonon.band_structure import get_band_qpoints_and_path_connections
        from phonopy import Phonopy
        from phonopy.structure.atoms import Atoms as PhonopyAtoms
        from pymatgen.phonon.plotter import PhononBSPlotter
        from pymatgen.phonon.bandstructure import PhononBandStructureSymmLine
        import csv
        import pandas as pd
        import matplotlib.pyplot as plt
        
        os.chdir(self.dire)
        print (os.getcwd())

        poscar = Poscar.from_file("POSCAR")
        structure = poscar.structure
        scell = [[2,0,0],[0,2,0],[0,0,2]]
        vrun = Vasprun("vasprun.xml")
        phonopyAtoms = get_phonopy_structure(structure)
        phonon = Phonopy(phonopyAtoms, scell)

        phonon.set_force_constants(-vrun.force_constants)

        # labels = ["$\\Gamma$", "X", "U", "K", "L"]
        labels = ['K', "$\\Gamma$", 'L', 'W', 'X']
        # bands = []
        cd=KPathSeek(structure)
        cds=cd.kpath
        # print(cds)
        for k,v in cds.items():
            if "kpoints" in k:

                dics=v 
            else:
                dicss=v
        print(dics)
        print(dicss)


        # bands=[]
        # for k,v in dics.items():
        #     if k in dicss[0]:
        #         bands.append(v)

        path=[]
        # 
        
        # bandd1=[]
        # for k,v in dics.items():
        #     for i in dicss[0]:
        #             if k in i:
        #                 bandd1.append(v)                  
        # path.append(bandd1)

        bandd1=[]
        for i in dicss[1]:
            for k,v in dics.items():
                if k in i:
                    bandd1.append(v)                  
        path.append(bandd1)
        print(dicss[1])
        qpoints, connections = get_band_qpoints_and_path_connections(path, npoints=51)
        phonon.run_band_structure(qpoints, path_connections=connections, labels=labels)

        print(path)


        # kpoints=cd.get_kpoints

        # print(kpoints)

        # phonon.set_band_structure(bands,labels=labels)



        phonon.plot_band_structure().show()
        phonon.plot_band_structure().savefig("BAND.png",bbox_inches='tight', transparent=True,dpi=300,format='png')
        # phonon.write_band_structure()
        mesh = [31, 31, 31]
        phonon.set_mesh(mesh)

        phonon.set_total_DOS()
        phonon.write_total_DOS()
        phonon.plot_total_DOS().show()
        phonon.plot_total_DOS().savefig("DOS.png")
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


        line1 = ax.plot(x_ax, y_ax,c='grey')
        ax.set_xlim([maxx, 0])




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
        # ax.legend(edgecolor='none', prop=font1)

        # plt.legend(edgecolor='none', prop=font1)
        # plt.set_facecolor('none') 
        ax.set_facecolor('none') 

        #存储为
        fig.savefig('FTIR.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
        plt.show()

    def Phonopy(self,maxx=4500):

        import os
        import numpy as np
        from pymatgen.io.phonopy import get_phonopy_structure 
        import pymatgen as pmg
        from pymatgen.io.vasp.outputs import Vasprun
        from pymatgen.io.vasp import Poscar
        from phonopy import Phonopy
        from phonopy.structure.atoms import Atoms as PhonopyAtoms
        from pymatgen.phonon.plotter import PhononBSPlotter
        from pymatgen.phonon.bandstructure import PhononBandStructureSymmLine
        import csv
        import pandas as pd
        import matplotlib.pyplot as plt
        import subprocess
        from ruamel import yaml


        os.chdir(self.dire)
        print (os.getcwd())

        eb=str("phonopy --fc vasprun.xml")

        with open('command.bat', 'w') as file_object:
            file_object.write(eb )
        subprocess.Popen("command.bat")


        ex=str('phonopy --dim="2 2 2" -c POSCAR-unitcell band.conf' )

        with open('command1.bat', 'w') as file_object:
            file_object.write(ex )
        subprocess.Popen("command1.bat")

        ex=str('phonopy -bandplot band.yaml' )

        with open('command2.bat', 'w') as file_object:
            file_object.write(ex )
        subprocess.Popen("command2.bat")

        ex=str('phonopy -p band.conf' )

        with open('command3.bat', 'w') as file_object:
            file_object.write(ex )
        subprocess.Popen("command3.bat")

        # with open('band.yaml', 'r', encoding='utf-8') as f:
        #     print(yaml.load(f.read(),Loader=yaml.Loader))
        #     ir=yaml.load(f.read(),Loader=yaml.Loader)
        #     type(ir)
        #     vu=PhononBandStructureSymmLine.from_dict(ir)
        #     PhononBSPlotter(vu).show()




    def Energy(self):
        from pymatgen.io.vasp import Vasprun
        import os
        os.chdir(self.dire)
        print (os.getcwd())

        v = Vasprun("vasprun.xml")
        print(v.final_energy) # final total energy
        s = v.final_structure
        s.to(filename="relaxed.cif") # save relaxed structure into cif file
        print(s) # relaxed structure







