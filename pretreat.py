class Pretreatment():
    import os
    def __init__(self,dire= r'E:\VASP practical\Input\Disorder_structure' ):
        self.dire = dire
    
        

    def disorder(self,apecies,spacegroup="C2"):
        from pymatgen import Structure, Lattice
        from pymatgen.io.vasp.sets import MPRelaxSet
        import numpy as np
        import os

        cod=[]
        for i in apecies:
            cod.append(np.random.rand(3).tolist())

        # print(cod)


        custom_settings = {"NELMIN": 5}
        specie = apecies
     
        cuau = Structure.from_spacegroup(sg=spacegroup, lattice=Lattice.cubic(10), species=apecies, coords=cod)
        relax = MPRelaxSet(cuau, user_incar_settings=custom_settings)
        os.chdir(self.dire)
        print (os.getcwd())
        gge=[]
        for n in specie:
            for key,value in n.items():

                gge.append(key)
        jji=[]
        for j in gge:
            jji.append(str(j)[:-2])

        str1 = "-".join(jji)
        print (str1)


        relax.write_input(str(str1)) 





    def Static (self):
        from pymatgen.io.vasp.sets import MPStaticSet
        import shutil
        import os
        filePath=self.dire
        for dirpath, dirnames, filenames in os.walk(filePath):
            # print(dirpath)
            for name in dirnames:
                if 'static' not in str(name):
                    path = os.path.join(filePath, name)
                    custom_settings = {"NELM": 60,'NPAR':4} # user custom incar settings
                    static = MPStaticSet.from_prev_calc(path, standardize=True,
                                                        user_incar_settings=custom_settings)
                    
                    diree = os.chdir(self.dire)

                    static.write_input("static_"+str(name))


                    pat = os.path.join(self.dire, "static_"+str(name))
                    os.chdir(pat)
                    #定义一个更改当前目录的变量
                    dire2 = './vaspstd_sub' 
                    #确立脚本名称
                    shutil.copy(r"C:\Users\41958\.spyder-py3\vaspstd_sub", dire2 )



    def Scf (self):
        from pymatgen.io.vasp.sets import MPNonSCFSet
        import shutil
        import os
        filePath=self.dire
        for dirpath, dirnames, filenames in os.walk(filePath):
            # print(dirpath)
            for name in dirnames:
                if 'dos' not in str(name):
                    path = os.path.join(filePath, name)

                    custom_settings = {"LAECHG": "False", "LVHAR": "False",'NPAR':4} # user custom incar settings
                    dos = MPNonSCFSet.from_prev_calc(path, mode="line",reciprocal_density=200,
                                                     user_incar_settings=custom_settings)
                    os.chdir(self.dire)
                    dos.write_input("dos_"+str(name))

                    pat = os.path.join(self.dire, "dos_"+str(name))
                    diree = os.chdir(pat) 
                    #定义一个更改当前目录的变量
                    dire2 = './vaspstd_sub' 
                    #确立脚本名称
                    shutil.copy(r"C:\Users\41958\.spyder-py3\vaspstd_sub", dire2 )
                    shutil.copy(os.path.join(path,'WAVECAR'), os.path.join(pat,'WAVECAR') )



    def isotope (self,before="POMASS =    1.000", change="POMASS =    3.000"):
        from pymatgen.io.vasp.outputs import Poscar
        from pymatgen.io.vasp.inputs import PotcarSingle
        from pymatgen.io.vasp.outputs import Potcar
        from pymatgen.io.vasp.sets import MPNMRSet
        import shutil
        import os
        os.chdir(self.dire)
        print (os.getcwd())
        poscar= Poscar.from_file("POSCAR")
        # structure = poscar.structure
        print (poscar)
        potcar= Potcar.from_file("POTCAR")
        potc=str(potcar)

        cc= potc.replace(before,change)

        vv=PotcarSingle(cc,)
        vv.write_file("POTCAR_1")

        print (vv)




    def Phonopy (self,mpid,supcell):
        from pymatgen.io.vasp.outputs import Poscar
        from pymatgen.io.vasp.inputs import Kpoints, Poscar
        from pymatgen.io.vasp.outputs import Potcar
        from pymatgen.io.vasp.sets import MPNMRSet
        from pymatgen.io.phonopy import get_displaced_structures
        from pymatgen.symmetry.bandstructure import HighSymmKpath
        import shutil
        import os
        import subprocess
        from pymatgen import Structure
        from pymatgen.io.vasp.sets import MPRelaxSet
        from pymatgen.ext.matproj import MPRester
        import shutil
        from shutil import copyfile
        import sys

        os.chdir(self.dire)
        print (os.getcwd()) 

        # isExists=os.path.exists(mpid+"isotope")
        # if not isExists:
        #     os.mkdir( mpid+"isotope" )
        #     print ("Directory created")

        # else:
        #     print (' directory already exists')



        # pat = os.path.join(self.dire, mpid+"isotope")
        # diree = os.chdir(pat)
        # print (os.getcwd()) 
        # print ("Directory entered ") 
        

        mpr = MPRester() 
        mp_id = mpid
        structure = mpr.get_structure_by_material_id(mp_id)
        relax = MPRelaxSet(structure)
        relax.write_input(mp_id+"isotope")       
        print ("Input created") 

        pat = os.path.join(self.dire, mpid+"isotope")
        os.chdir(pat)
        print (os.getcwd()) 
        print ("Directory entered ") 
        
                    
        eb=str("phonopy -d --dim="+supcell)

        with open('command.bat', 'w') as file_object:
            file_object.write(eb )
        subprocess.Popen("command.bat")
        for filenames in os.walk(pat):
            print (filenames)



    def Phonopyinput (self,mpid,intt):
        from pymatgen.io.vasp.outputs import Poscar
        from pymatgen.io.vasp.inputs import Kpoints, Poscar
        from pymatgen.io.vasp.outputs import Potcar
        from pymatgen.io.vasp.sets import MPNMRSet
        from pymatgen.io.phonopy import get_displaced_structures
        from pymatgen.symmetry.bandstructure import HighSymmKpath
        import shutil
        import os
        import subprocess
        from pymatgen import Structure
        from pymatgen.io.vasp.sets import MPRelaxSet
        from pymatgen.ext.matproj import MPRester
        import shutil
        from shutil import copyfile
        import sys
        from pymatgen.symmetry.kpath import KPathSeek,KPathBase


        os.chdir(self.dire)
        print (os.getcwd()) 

        ptt = os.path.join(self.dire, mpid+"isotope")
        os.chdir(ptt)
        poscar= Poscar.from_file("POSCAR")
        structure = poscar.structure
        for filenames in os.walk(ptt):
            print (filenames)




        dire3 = './INCAR' 
        #确立脚本名称
        shutil.copy(r"D:\Desktop\VASP practical\Input\INCAR_std\INCAR_phono", dire3 )        
        print ("INCAR copied") 
        
        dire2 = './vaspstd_sub' 
        #确立脚本名称
        shutil.copy(r"D:\Desktop\VASP practical\Input\INCAR_std\vaspstd_sub", dire2 )        
        print ("vaspstd_sub copied") 

        # os.chdir(self.dire)
        # os.chdir(ptt)
        # print (os.getcwd())

        # print ("Right")
        copyfile("POSCAR","POSCAR-unitcell")

        copyfile("SPOSCAR","POSCAR")
        print ("POSCAR copied") 


        # cd=KPathSeek(structure)
        # # jh=cd.get_kpoints
        # kk=Kpoints.automatic_linemode(divisions=10, ibz=cd)
        # # kk=Kpoints.automatic_density(structure, kppa=intt)
        # kk.write_file("KPOINTS")
        print ("KPOINTS writed")

        os.chdir(self.dire)
        sys.exit()


        # poscar= Poscar.from_file("POSCAR")
        # structure = poscar.structure

        # structure.make_supercell(ff)
        # phostru=get_displaced_structures(pmg_structure=structure)
        # # print(phostru)
        # prcf=Poscar(phostru[1])
        # print(prcf)
        # prcf.write_file('POSCAR')




        # # hh=HighSymmKpath(structure)
        # kk=Kpoints.automatic_density(structure, kppa=intt)
        # kk.write_file("KPOINTS")


        # print (kk)

