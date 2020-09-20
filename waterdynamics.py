class Waterdynamics():
    def __init__(self,dire):

        self.dire = dire



    def RDF(self,rdf_fir,rdf_sec):

        from ase.io import read, write
        import os
        import MDAnalysis
        import MDAnalysis.analysis.rdf
        import MDAnalysis.analysis.rms
        import matplotlib.pyplot as plt
        import pandas as pd


        os.chdir(self.dire)
        # write('traj.pdb', read(filename))



        u = MDAnalysis.Universe('change.xyz',dt=0.001)
        u.dimensions = ([73, 73, 73, 90, 90, 90])
        g1= u.select_atoms(rdf_fir)
        g2= u.select_atoms(rdf_sec)
        rdfOH = MDAnalysis.analysis.rdf.InterRDF(g1,g2,nbins=500, range=(0.0, min(u.dimensions[:3])/2.0),exclusion_block=(1, 1))
                  
        rdfOH.run()

        # rdfHH = MDAnalysis.analysis.rdf.InterRDF(u.select_atoms('name H'),u.select_atoms('name H'),nbins=75, range=(0.0, min(u.dimensions[:3])/2.0))
                  
        # rdfHH.run()

        # rdfOO = MDAnalysis.analysis.rdf.InterRDF(u.select_atoms('name O'),u.select_atoms('name O'),nbins=75, range=(0.0, min(u.dimensions[:3])/2.0))
                  
        # rdfOO.run()
        labels="RDF "+rdf_fir[-1:]+rdf_sec[-1:]
        plt.figure()
        plt.plot(rdfOH.bins, rdfOH.rdf, linestyle='--', label=labels)

        # plt.plot(rdfHH.bins, rdfHH.rdf,   label="RDF HH")
        # plt.plot(rdfOO.bins, rdfOO.rdf,  label="RDF OO")
        df = pd.DataFrame({'Distance':rdfOH.bins,labels:rdfOH.rdf})
        df.to_excel(labels+".xlsx")#生成Excel文件，并存到指定文件路径下
        
        plt.legend(loc="best")
        plt.xlabel(r"Distance ($\AA$)")
        plt.ylabel(r"g(r)")
        plt.xlim((0,15))
        plt.savefig('RDF.png',bbox_inches='tight', transparent=True,dpi=600,format='png')#指定分辨率,边界紧，背景透明
        print("Down")



    def MSD(self,selects,tbegin,tfinal,filename):
        import MDAnalysis
        from MDAnalysis.analysis.waterdynamics import MeanSquareDisplacement as MSD
        import os
        import matplotlib.pyplot as plt
        from MDAnalysis.tests.datafiles import PDB
        import pandas as pd
        from scipy.optimize import curve_fit
        import numpy as np


        os.chdir(self.dire)

        u = MDAnalysis.Universe('change.xyz',dt=0.001)
        

        select= selects
        t0=tbegin
        tf=tfinal
        td=int((tf-t0)/2)
        MSD_analysis = MSD(u,select, t0, tf,td)
        MSD_analysis.run()
        #now we print data ready to graph. The graph
        #represents MSD vs t
        # print(MSD_analysis)
        time = t0/2
        for msd in MSD_analysis.timeseries:
              # print("{time} {msd}".format(time=time, msd=msd))
              time += 1
        tdd=[]
        timec=range(int(t0/2),td+int(t0/2))
        for i in timec:
            tdd.append(i/0.5/1000-timec[0]/0.5/1000)
        print()

        def func(tdd,C,D):
            return C+6*D*tdd
        popt, pcov = curve_fit(func, timec, MSD_analysis.timeseries)
        C=popt[0] # popt里面是拟合系数，读者可以自己help其用法
        D=popt[1]
        yvals=func(timec,C,D)
        plt.xlabel('Time (ps)')
        plt.ylabel(r"MSD ($\AA$)")
        plt.title('MSD')
        plt.scatter(tdd,MSD_analysis.timeseries,marker=r'$\clubsuit$',c="gray",label='Calculated MSD',alpha=0.4)
        # s = np.random.rand(*tdd.shape) * 800 + 500
        plot2=plt.plot(tdd, yvals, '-o', ms=0.2, alpha=0.7, mfc='orange',label='curve fit values',)
        plt.axis([0,4,0,1])
        plt.legend(loc=4)
        plt.show()

        df = pd.DataFrame({'time':tdd,'MSD':MSD_analysis.timeseries,"fit":yvals})
        df.to_excel(selects[-1:]+"MSD.xlsx")#生成Excel文件，并存到指定文件路径下
        print("Diffusion Coefficient is  "+str(D))
        with open("DiffusionCoefficient",'w') as f:
            f.write("Diffusion Coefficient is  "+str(D))
        plt.savefig('MSD.png',bbox_inches='tight', transparent=True,dpi=600,format='png')#指定分辨率,边界紧，背景透明

        
    def RMSDs(self,group):
        import MDAnalysis
        import MDAnalysis.analysis.rms
        from MDAnalysis.tests.datafiles import PSF, DCD, CRD
        from MDAnalysis.analysis import rms
        import matplotlib.pyplot as plt
        import os
        import pandas as pd

        os.chdir(self.dire)

        u = MDAnalysis.Universe('change.xyz', permissive=True)
        ref = MDAnalysis.Universe('change.xyz', permissive=True)     # reference (with the default ref_frame=0)
        ref.trajectory[0] #
        R = MDAnalysis.analysis.rms.RMSD(u, ref,
           select="all",         # superimpose on whole backbone of all atoms # align based on all atoms
           groupselections=group,
           filename="rmsd_all.dat",center=True)#
        timestep=0.001  #0.5fs from fs to ps as Reader has no dt information, set to 1.0 ps          
        R.run()
        rmsd = R.rmsd.T   # transpose makes it easier for plotting
        time = rmsd[1]*timestep
        plt.figure(figsize=(5,4))
        # ax = fig.add_subplot(111)
        plt.plot(time, rmsd[2], 'k-',  label="all",linewidth=2)
        plt.plot(time, rmsd[3], 'r--', label=str(group[0]))
        plt.plot(time, rmsd[4], 'b--', label=str(group[1]))
        plt.plot(time, rmsd[5], 'g--', label=str(group[2]))
        # plt.plot(time, rmsd[6], 'y--', label=str(group[3]))
        print(rmsd[0])
        df = pd.DataFrame({'time':time,"all":rmsd[2],str(group[0]):rmsd[3],str(group[1]):rmsd[4],str(group[2]):rmsd[5]})
        df.to_excel("RMSD.xlsx")#生成Excel文件，并存到指定文件路径下
        font1 = {'family' : 'Times New Roman',
        'weight' : 'bold',
        }
        plt.ylim(0,1.1)
        # plt.pltes(0,1)
        plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
        plt.xlabel("Time (ps)",fontsize=16,family='Times New Roman')
        plt.ylabel(r"RMSD ($\AA$)",fontsize=16,family='Times New Roman')
        plt.savefig("RMSD.png",bbox_inches='tight', transparent=True,dpi=600,format='png')
        print('Down')


    def HBL(self,select1,select2,tbegin,tfinal):
        import MDAnalysis
        import MDAnalysis.analysis.rms
        from MDAnalysis.tests.datafiles import PSF, DCD, CRD
        from MDAnalysis.analysis import rms
        import matplotlib.pyplot as plt
        import os
        import pandas as pd
        from MDAnalysis.analysis.waterdynamics import HydrogenBondLifetimes as HBL

        os.chdir(self.dire)
        u =MDAnalysis.Universe('change.xyz', permissive=True)
        selection1 = select1
        selection2 = select2
        t0=tbegin
        tf=tfinal
        td=int((tf-t0)/2)
        HBL_analysis = HBL(u, selection1, selection2, t0, tf, dtmax=td)
        HBL_analysis.run()
        time = 0
        #now we print the data ready to plot. The first two columns are the HBLc vs t
        #plot and the second two columns are the HBLi vs t graph
        for HBLc, HBLi in HBL_analysis.timeseries:
            print("{time} {HBLc} {time} {HBLi}".format(time=time, HBLc=HBLc, HBLi=HBLi))
            time += 1

        #we can also plot our data
        plt.figure(1,figsize=(18, 6))

        #HBL continuos
        plt.subplot(121)
        plt.xlabel('time')
        plt.ylabel('HBLc')
        plt.title('HBL Continuos')
        plt.plot(range(0,time),[column[0] for column in HBL_analysis.timeseries])

        #HBL intermitent
        plt.subplot(122)
        plt.xlabel('time')
        plt.ylabel('HBLi')
        plt.title('HBL Intermitent')
        plt.plot(range(0,time),[column[1] for column in HBL_analysis.timeseries])

        plt.show()

    def WOR(self,selects,tbegin,tfinal):
        import MDAnalysis
        import MDAnalysis.analysis.rms
        from MDAnalysis.tests.datafiles import PSF, DCD, CRD
        from MDAnalysis.analysis import rms
        import matplotlib.pyplot as plt
        import os
        import pandas as pd
        import MDAnalysis
        from MDAnalysis.analysis.waterdynamics import WaterOrientationalRelaxation as WOR


        os.chdir(self.dire)
        u =MDAnalysis.Universe('change.xyz', permissive=True)
        print(u.residues)
        print(u.atoms.residues)
        select = selects
        t0=tbegin
        tf=tfinal
        td=int((tf-t0)/2)
        WOR_analysis = WOR(u, select, t0, tf,td)
        WOR_analysis.run()
        time = t0/2
        #now we print the data ready to plot. The first two columns are WOR_OH vs t plot,
        #the second two columns are WOR_HH vs t graph and the third two columns are WOR_dip vs t graph
        for WOR_OH, WOR_HH, WOR_dip in WOR_analysis.timeseries:
              print("{time} {WOR_OH} {time} {WOR_HH} {time} {WOR_dip}".format(time=time, WOR_OH=WOR_OH, WOR_HH=WOR_HH,WOR_dip=WOR_dip))
              time += 1
        tdd=[]
        timec=range(int(t0/2),td+int(t0/2))
        for i in timec:
            tdd.append(i/0.5/1000-timec[0]/0.5/1000)
        print()



        fig = plt.figure()
        plt.plot(tdd,[column[0] for column in WOR_analysis.timeseries],label='WOR OH',linestyle='--')
        plt.plot(tdd,[column[1] for column in WOR_analysis.timeseries],label='WOR HH',linestyle='--')
        plt.plot(tdd,[column[2] for column in WOR_analysis.timeseries],label='WOR dip',linestyle='-',linewidth=3,alpha=0.5)

        df = pd.DataFrame({'time':tdd,'WOR OH':[column[0] for column in WOR_analysis.timeseries],'WOR HH':[column[1] for column in WOR_analysis.timeseries],'WOR dip':[column[2] for column in WOR_analysis.timeseries]})
        df.to_excel("WOR.xlsx")#生成Excel文件，并存到指定文件路径下
        font2 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'x-large'
        }
        plt.xlabel('Time (ps)' ,fontsize=16,family='Times New Roman')
        plt.ylabel('WOR' ,fontsize=16,family='Times New Roman')

        plt.ylim((-0.1, 1.1))
        #不显示Y轴的刻度
        # plt.yticks([])

        #设置图例对应格式和字体
        font1 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'large'
        }
        plt.legend(edgecolor='none', prop=font1,)
        # plt.title(str(title))
        #存储为
        fig.savefig('WOR.png',bbox_inches='tight', transparent=True,dpi=600,format='png')#指定分辨率,边界紧，背景透明
        plt.show()





    def AD(self,selects):
        import MDAnalysis
        import MDAnalysis.analysis.rms
        from MDAnalysis.tests.datafiles import PSF, DCD, CRD
        from MDAnalysis.analysis import rms
        import matplotlib.pyplot as plt
        import os
        import pandas as pd
        import MDAnalysis
        from MDAnalysis.analysis.waterdynamics import AngularDistribution as AD
        os.chdir(self.dire)
        u =MDAnalysis.Universe('change.xyz', permissive=True)
        selection = selects
        bins = 2000
        AD_analysis = AD(u,selection,bins)
        AD_analysis.run()
        #now we print data ready to graph. The first two columns are P(cos(theta)) vs cos(theta) for OH vector ,
        #the seconds two columns are P(cos(theta)) vs cos(theta) for HH vector and thirds two columns
        #are P(cos(theta)) vs cos(theta) for dipole vector
        # for bin in range(bins):
              # print("{AD_analysisOH} {AD_analysisHH} {AD_analysisDip}".format(AD_analysis.graph0=AD_analysis.graph[0][bin], AD_analysis.graph1=AD_analysis.graph[1][bin],AD_analysis.graph2=AD_analysis.graph[2][bin]))

        #and if we want to graph our results
        
        # plt.figure(1,figsize=(18, 6))
        fig = plt.figure(figsize=(5,4))
        plt.plot([float(column.split()[0]) for column in AD_analysis.graph[0][:-1]],[float(column.split()[1]) for column in AD_analysis.graph[0][:-1]],linestyle='--',label='PDF cos theta for OH')
        plt.plot([float(column.split()[0]) for column in AD_analysis.graph[1][:-1]],[float(column.split()[1]) for column in AD_analysis.graph[1][:-1]],linestyle='--',label='PDF cos theta for HH')
        plt.plot([float(column.split()[0]) for column in AD_analysis.graph[2][:-1]],[float(column.split()[1]) for column in AD_analysis.graph[2][:-1]],linestyle='-',linewidth=3,alpha=0.5,label='PDF cos theta for dip')

        df = pd.DataFrame({'cos theta for OH':[float(column.split()[0]) for column in AD_analysis.graph[0][:-1]],'P(cos theta) for OH':[float(column.split()[1]) for column in AD_analysis.graph[0][:-1]]
            ,'cos theta for HH':[float(column.split()[0]) for column in AD_analysis.graph[1][:-1]],'P(cos theta) for HH':[float(column.split()[1]) for column in AD_analysis.graph[1][:-1]]
            ,'cos theta for dip':[float(column.split()[0]) for column in AD_analysis.graph[2][:-1]],'P(cos theta) for dip':[float(column.split()[1]) for column in AD_analysis.graph[2][:-1]]})
        df.to_excel("AD.xlsx")#生成Excel文件，并存到指定文件路径下
        font2 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'x-large'
        }
        plt.xlabel('cos theta' ,fontsize=16,family='Times New Roman')
        plt.ylabel('P(cos theta)' ,fontsize=16,family='Times New Roman')

        plt.xlim((-0.99, 0.99))
        plt.ylim((-1, 10))
        #不显示Y轴的刻度
        # plt.yticks([])

        #设置图例对应格式和字体
        font1 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'large'
        }
        plt.legend(edgecolor='none', prop=font1,)
        # plt.title(str(title))
        #存储为
        fig.savefig('AD.png',bbox_inches='tight', transparent=True,dpi=600,format='png')#指定分辨率,边界紧，背景透明
        plt.show()
        # #AD OH
        # plt.subplot(131)
        # plt.xlabel('cos theta')
        # plt.ylabel('P(cos theta)')
        # plt.title('PDF cos theta for OH')
        # plt.plot([float(column.split()[0]) for column in AD_analysis.graph[0][:-1]],[float(column.split()[1]) for column in AD_analysis.graph[0][:-1]])

        # #AD HH
        # plt.subplot(132)
        # plt.xlabel('cos theta')
        # plt.ylabel('P(cos theta)')
        # plt.title('PDF cos theta for HH')
        # plt.plot([float(column.split()[0]) for column in AD_analysis.graph[1][:-1]],[float(column.split()[1]) for column in AD_analysis.graph[1][:-1]])

        # #AD dip
        # plt.subplot(133)
        # plt.xlabel('cos theta')
        # plt.ylabel('P(cos theta)')
        # plt.title('PDF cos theta for dipole')
        # plt.plot([float(column.split()[0]) for column in AD_analysis.graph[2][:-1]],[float(column.split()[1]) for column in AD_analysis.graph[2][:-1]])

        # plt.show()

        




    def SP(self,select1,tbegin,tfinal):
        import MDAnalysis
        import MDAnalysis.analysis.rms
        from MDAnalysis.tests.datafiles import PSF, DCD, CRD
        from MDAnalysis.analysis import rms
        import matplotlib.pyplot as plt
        import os
        import pandas as pd
        import MDAnalysis
        from MDAnalysis.analysis.waterdynamics import SurvivalProbability as SP
        os.chdir(self.dire)
        u =MDAnalysis.Universe('change.xyz', permissive=True)
        
        sp1 = SP(u, select1, verbose=True)
        # sp2 = SP(u, select2, verbose=True)
        t0=tbegin
        tf=tfinal
        td=int((tf-t0)/2)
        sp1.run(start=t0, stop=tf,tau_max=td)
        tau_timeseries1 = sp1.tau_timeseries
        sp_timeseries1 = sp1.sp_timeseries
        # sp2.run(start=t0, stop=tf,tau_max=td)
        # tau_timeseries2 = sp2.tau_timeseries
        # sp_timeseries2 = sp2.sp_timeseries
        # print in console
        # for tau, sp1 in zip(tau_timeseries, sp_timeseries):
        #       print("{time} {sp}".format(time=tau, sp=sp))
        #now we print data ready to graph. The first two columns are P(cos(theta)) vs cos(theta) for OH vector ,
        #the seconds two columns are P(cos(theta)) vs cos(theta) for HH vector and thirds two columns
        #are P(cos(theta)) vs cos(theta) for dipole vector
        # for bin in range(bins):
              # print("{AD_analysisOH} {AD_analysisHH} {AD_analysisDip}".format(AD_analysis.graph0=AD_analysis.graph[0][bin], AD_analysis.graph1=AD_analysis.graph[1][bin],AD_analysis.graph2=AD_analysis.graph[2][bin]))

        #and if we want to graph our results
        
        tdd=[]
        timec=tau_timeseries1
        for i in timec:
            tdd.append(i/0.5/1000)
        print()
        labels=select1[5:6]
        df = pd.DataFrame({'time':tdd,'SP H':sp_timeseries1})
        df.to_excel(labels+"SP.xlsx")#生成Excel文件，并存到指定文件路径下       
        fig = plt.figure(figsize=(5,4))
        plt.plot(tdd, sp_timeseries1,linestyle='--',linewidth=3,alpha=0.8,label='SP H')
        plt.fill_between(tdd, sp_timeseries1, alpha=.15,ec="none",lw=.1,zorder=2)
        # plt.plot(tdd, sp_timeseries2,linestyle='-',linewidth=3,alpha=0.8,label='SP O')

        font2 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'x-large'
        }
        plt.xlabel('Time (ps)' ,fontsize=16,family='Times New Roman')
        plt.ylabel('SP' ,fontsize=16,family='Times New Roman')

        # plt.ylim((0.95, 1))
        #不显示Y轴的刻度
        # plt.yticks([])

        #设置图例对应格式和字体
        font1 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'large'
        }
        plt.legend(edgecolor='none', prop=font1,)
        # plt.title(str(title))
        #存储为
        fig.savefig('SP.png',bbox_inches='tight', transparent=True,dpi=600,format='png')#指定分辨率,边界紧，背景透明
        plt.show()

