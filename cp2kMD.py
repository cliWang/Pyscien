class cp2kMD():
    def __init__(self,dire):

        self.dire = dire



    def POSTAIMD(self,filename,rdf_fir,rdf_sec,):

        from ase.io import read, write
        import os
        import MDAnalysis
        import MDAnalysis.analysis.rdf
        import MDAnalysis.analysis.rms
        import matplotlib.pyplot as plt
        import pandas as pd


        os.chdir(self.dire)
        # write('traj.pdb', read(filename))



        u = MDAnalysis.Universe(filename, permissive=True)
        u.dimensions = [73, 73, 73, 90, 90, 90]
        u.atoms.write("traj.pdb",frames='all')
        u.atoms.write("crystal.xyz")
        g1= u.select_atoms(rdf_fir)
        g2= u.select_atoms(rdf_sec)
        rdf = MDAnalysis.analysis.rdf.InterRDF(g1,g2,nbins=75, range=(0.0, min(u.dimensions[:3])/2.0))
                  
        rdf.run()
        fig = plt.figure(figsize=(5,4))
        ax = fig.add_subplot(111)
        ax.plot(rdf.bins, rdf.rdf, 'k-',  label="rdf")
        ax.legend(loc="best")
        ax.set_xlabel(r"Distance ($\AA$)")
        ax.set_ylabel(r"RDF")
        fig.savefig("RDF_all.png")





        ref = MDAnalysis.Universe(filename, permissive=True) 
        ref.trajectory[0]
        R = MDAnalysis.analysis.rms.RMSD(u, ref,
           select="all",         # superimpose on whole backbone of all atoms # align based on all atoms
           groupselections=[rdf_fir,rdf_sec],
           filename="rmsd_all.dat",center=True)#,   # CORE
        timestep=0.0005  #0.5fs from fs to ps as Reader has no dt information, set to 1.0 ps          
        R.run()
        rmsd = R.rmsd.T   # transpose makes it easier for plotting
        time = rmsd[1]*timestep

        da = {'time':time,'all':rmsd[2],rdf_fir:rmsd[3],rdf_sec:rmsd[4]}
        df=pd.DataFrame(da)#构造原始数据文件
        df.to_excel("RMSD.xlsx")#生成Excel文件，并存到指定文件路径下




        fig = plt.figure(figsize=(5,4))
        ax = fig.add_subplot(111)
        ax.plot(time, rmsd[2], 'k-',  label="all")
        ax.plot(time, rmsd[3], 'r--', label=rdf_fir)
        ax.plot(time, rmsd[4], 'b--', label=rdf_sec)
        ax.legend(loc="best")
        ax.set_xlabel("time (ps)")
        ax.set_ylabel(r"RMSD ($\AA$)")
        fig.savefig("rmsd_md_analysis.png")


    def Energychek(self):
        from ase.io import read, write
        import os
        import MDAnalysis
        import MDAnalysis.analysis.rdf
        import MDAnalysis.analysis.rms
        import matplotlib.pyplot as plt
        import pandas as pd
        import re


        os.chdir(self.dire)

        font1 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'24'
        }



        
        df = pd.read_csv('ab-initio-1.ener',sep='\s+',skipinitialspace=True,engine='python',)


        a1=df['Step']
        a2=df['Nr.']
        a3=df['Time[fs]']
        a4=df['Kin.[a.u.]']
        a5=df['Temp[K]']
        a6=df['Pot.[a.u.]']
        # a7=df['Time[fs]']

        fig = plt.figure(figsize=(20,16),dpi=300)
        plt.subplot(2,2,1)
        plt.scatter(a1, a2, alpha=0.85, label='Kin',linewidth=2)
        # plt. scatter(litt, liss, alpha=0.85, label='Energy',linewidth=2)
        plt.xlabel(r"Time (fs)",fontsize=28,family='Times New Roman')
        plt.ylabel(r"Energy (a.u).",fontsize=28,family='Times New Roman')
        plt.legend(edgecolor='none', prop=font1,)
        plt.tick_params(labelsize=16)

        plt.subplot(2,2,2)
        plt.scatter(a1, a4, alpha=0.85, label='Pot',linewidth=2,c='orange')
        # plt. scatter(litt, liss, alpha=0.85, label='Energy',linewidth=2)
        plt.xlabel(r"Time (fs)",fontsize=28,family='Times New Roman')
        plt.ylabel(r"Energy (a.u).",fontsize=28,family='Times New Roman')
        plt.legend(edgecolor='none', prop=font1,)
        plt.tick_params(labelsize=16)


        plt.subplot(2,2,3) 
        plt.scatter(a1, a5, alpha=0.85, label='Cons Qty',linewidth=2,c='grey')
        # plt. scatter(litt, liss, alpha=0.85, label='Energy',linewidth=2)
        plt.xlabel(r"Time (fs)",fontsize=28,family='Times New Roman')
        plt.ylabel(r"Energy (a.u).",fontsize=28,family='Times New Roman')
        plt.legend(edgecolor='none', prop=font1,)
        plt.tick_params(labelsize=16)

        plt.subplot(2,2,4)
        plt.scatter(a1, a3, alpha=0.85, label='Temp',linewidth=2,c='forestgreen')
        plt.xlabel(r"Time (fs)",fontsize=28,family='Times New Roman')
        plt.ylabel(r"Temp (K)",fontsize=28,family='Times New Roman')
        # plt.ylim((0,10000))
        plt.legend(edgecolor='none', prop=font1,)
        plt.tick_params(labelsize=16)

        # plt.subplot(2,3,5)
        # plt.scatter(a1, a6, alpha=0.85, label='UsedTime',linewidth=2,c='purple')
        # plt.xlabel(r"Time (fs)",fontsize=28,family='Times New Roman')
        # plt.ylabel(r"UsedTime (s)",fontsize=28,family='Times New Roman')
        # plt.legend(edgecolor='none', prop=font1,)
        # plt.tick_params(labelsize=16)
        

        # a8=[]
        # for i, element in enumerate(a6):
        #     nv=a6[:i]
        #     su = sum(nv)
        #     a8.append(su/60)
        
        # plt.subplot(2,3,6)
        # plt.scatter(a1, a8, alpha=0.85, label='Accumtime',linewidth=2,c='cadetblue')
        # # plt.plot(a1, a7, alpha=0.85, label='Energy',linewidth=2)
        # plt.xlabel(r"Time (fs)",fontsize=28,family='Times New Roman')
        # plt.ylabel(r"Accumtime (min)",fontsize=28,family='Times New Roman')
        # plt.legend(edgecolor='none', prop=font1,)
        # plt.tick_params(labelsize=16)



        dm = pd.DataFrame({'Time (fs)':a1,'Kin':a2,'Temp':a3,'Pot':a4,'Cons Qty':a5,'UsedTime':a6})
        dm.to_excel("Energychek.xlsx")


        # 以下是图片的格式设置
        # 设置横纵坐标的名称以及对应字体格式
        font2 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'x-large'
        }

        # plt.xlim((0,12))
        # plt.ylim((0))
        #不显示Y轴的刻度
        # plt.yticks([])

        #设置图例对应格式和字体
        # auto_adjust_subplotpars(fig, renderer,(2,3) , [1,1,1,1,1,1], (2,3,1), ax_bbox_list=None, pad=1.08, h_pad=None, w_pad=None, rect=None)
        plt.subplots_adjust(wspace =0.3,hspace =0.3 )
        #存储为
        plt.savefig('Energychek.png', transparent=True,format='png')#指定分辨率,边界紧，背景透明
        plt.show()
        print ('congratulate！！！')

    def Energy(self):
        from ase.io import read, write
        import os
        import MDAnalysis
        import MDAnalysis.analysis.rdf
        import MDAnalysis.analysis.rms
        import matplotlib.pyplot as plt
        import pandas as pd
        import re


        os.chdir(self.dire)

        font1 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'24'
        }

        f=open('ab-initio-pos-1.pdb','r')
        alllines=f.readlines()
        f.close()
        liss=[]
        litt=[]
        for eachline in alllines:
            if "E = " in eachline:
                a=re.search("E = .*",eachline)
                c=a.group()
                liss.append(float(c[3:]))

                b=re.search("Step\s.*, time",eachline)
                # print(b.group())
                d=b.group()
                # print(d[:-6])
                litt.append(float(d[:-6][5:]))

        dm = pd.DataFrame({'Step':litt,'Energy':liss})
        dm.to_excel("Energy.xlsx")

        plt.scatter(litt, liss, alpha=0.85, label='Energy',linewidth=2)
        # plt.plot(a1, a7, alpha=0.85, label='Energy',linewidth=2)
        plt.xlabel(r"Step ",fontsize=24,family='Times New Roman')
        plt.ylabel(r"Energy (eV)",fontsize=24,family='Times New Roman')
        plt.legend(edgecolor='none', prop=font1)
        plt.tick_params(labelsize=16)

        plt.savefig('Energy.png',bbox_inches='tight', transparent=True,dpi=600,format='png')#指定分辨率,边界紧，背景透明
        plt.show()







    def PREAIMD(self,para='matflow cp2k -r 10 --cutoff 300 --kpoints-scheme NONE -d mdcal --md-steps 100'):

        from pymatgen.core.trajectory import Trajectory
        import shutil
        import os

        os.chdir(self.dire)
        # shutil.copyfile(r"D:\Desktop\VASP practical\subscript\XDATCAR_toolkit.py","./XDATCAR_toolkit.py")
        # wawe = 'python' +' '+str(para)
        wawe =str(para)
        with open("change.cmd",'w') as f:
            f.write(wawe)

        result2 = os.popen('change').read()
        print(result2)


        

    def rewrite(self,):
        from pymatgen.core.trajectory import Trajectory
        import shutil
        import os
        import re


        os.chdir(self.dire)
        os.chdir("./mdcal")
        print (os.getcwd())
        shutil.copyfile(r"D:\Desktop\cp2k Practical\Std_inp\sub.sh","./sub.sh")
        shutil.copyfile(r"D:\Desktop\cp2k Practical\Std_inp\DFT.inc","./DFT.inc")
        shutil.copyfile(r"D:\Desktop\cp2k Practical\Std_inp\MOTIONNVT.inc","./MOTIONNVT.inc")
        

        with open('aimd.inp', 'r+') as f:
            content = f.read()  
            f.seek(0, 0)
            f.write('@set data /public1/soft/cp2k/7.1/exe/Linux-x86-64-intel/data\n@set RESTART 0\n@set PROJECT_NAME ab-initio \n\n\n'+content)
        f.close()
        

        l=["@if ${RESTART} == 1\n","&EXT_RESTART\n","          RESTART_FILE_NAME ./${PROJECT_NAME}-1.restart\n","            RESTART_DEFAULT T\n","    &END EXT_RESTART\n","@endif\n"]
        with open('aimd.inp', 'r+') as j:

            # addcont = j.read()
            j.seek(0, 2)
            j.writelines(l)
        j.close()
    

        f=open('aimd.inp','r')
        alllines=f.readlines()
        f.close()
        f=open('aimd.inp','w+')
        for eachline in alllines:
            if "BASIS_MOLOPT" in eachline:
                a=re.sub("BASIS_MOLOPT","${data}/BASIS_MOLOPT",eachline)
            else:
                a=re.sub("GTH_POTENTIALS","${data}/GTH_POTENTIALS",eachline)
            
            f.writelines(a)
        f.close()



        f=open('aimd.inp','r')
        alllines=f.read()
        f.close()
        f=open('aimd.inp','w+')
        r=re.compile(r"&DFT(.*)&END DFT",re.DOTALL)
        a=r.sub(r"@INCLUDE 'DFT.inc'",alllines) 
        f.write(a)
        f.close()


        f=open('aimd.inp','r')
        alllines=f.read()
        f.close()
        f=open('aimd.inp','w+')
        rv=re.compile(r"&MOTION(.*)&END MOTION",re.DOTALL)
        a=rv.sub(r"@INCLUDE 'MOTIONNVT.inc'",alllines)  
        f.write(a)
        f.close()

        f=open('aimd.inp','r')
        alllines=f.read()
        f.close()
        f=open('aimd.inp','w+')
        rv=re.compile(r"PROJECT ab-initio",re.DOTALL)
        a=rv.sub(r"PROJECT ${PROJECT_NAME}",alllines)  
        f.write(a)
        f.close()

        os.chdir(self.dire)
        print("DONE")
