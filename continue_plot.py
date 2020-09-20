class Continue():
    def __init__(self,dire):

        self.dire = dire

    def plotdos_orb(self, name1 = '', name2 = '',name3=''):
        import os
        from pymatgen import Element
        from pymatgen.io.vasp import Vasprun  # 读取vasp作业(vasprun.xml)
        from pymatgen.io.vasp import Vasprun, BSVasprun
        from pymatgen.electronic_structure.plotter import DosPlotter
        from pymatgen.electronic_structure.core import Spin, OrbitalType
        import matplotlib.pyplot as plt
        import numpy as np
        for dirpath, dirnames, filenames in os.walk(self.dire):
            # print(dirpath)
            for name in dirnames:
                path = os.path.join(self.dire, name)
                os.chdir(path)
                print (os.getcwd())
        

        
        # read vasprun.xml，get band and dos information
                dosrun=Vasprun("./vasprun.xml")
                spd_dos = dosrun.complete_dos.get_spd_dos()
                fig, ax = plt.subplots()
                line1, = ax.plot(dosrun.tdos.densities[Spin.up], dosrun.tdos.energies , label='Total DOS',linewidth=8,alpha=0.5,)



                if name1 != '':
                    line2, = ax.plot(spd_dos[OrbitalType.s].densities[Spin.up], dosrun.tdos.energies , label= name1)
                if name2 != '':
                    line3, = ax.plot(spd_dos[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies , label= name2)
                if name3 != '':
                    line4, = ax.plot(spd_dos[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies , label=name3)

                linef = plt.axhline(y=dosrun.efermi,xmin=0, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                linef.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                # ax.set_xlabel('Density of states of Silicon')
                ax.set_ylabel('Energy  /  eV')
                font2 = {'family' : 'Times New Roman','fontsize':'20' , 'weight' : 'bold',} 
                #plt.xlabel('Density of states' ,font2)
                # ax.annotate("Energy  /  eV", xy=(-0.05, 0.3), rotation=90,xycoords=ax.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                # plt.ylabel('E-${E_f}$  /  eV' ,font2)
                # plt.scatter(dosrun.tdos.densities[Spin.up], dosrun.tdos.energies - dosrun.efermi, c="g", alpha=0.5, marker=r'$\clubsuit$',
                #     label="Luck")
                # plt.xlabel("Density of states of Silicon")
                # plt.ylabel("E-${E_f}$  /  eV")
                # plt.legend(loc='upper left')
                # plt.show()
                font1 = {'family' : 'Times New Roman',
                'weight' : 'bold',
                }
                ax.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)

                plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                # plt.set_facecolor('none') 
                ax.set_facecolor('none') 

                #存储为
                fig.savefig('./DOS_orb.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                plt.show()

     
        
        


    def plotdos_elem(self,ele_1='',ele_2='',ele_3='',ele_4=''):

        import os
        from pymatgen import Element
        from pymatgen.io.vasp import Vasprun  # 读取vasp作业(vasprun.xml)
        from pymatgen.io.vasp import Vasprun, BSVasprun
        from pymatgen.electronic_structure.plotter import DosPlotter
        from pymatgen.electronic_structure.core import Spin, OrbitalType
        import matplotlib.pyplot as plt
        import numpy as np
        for dirpath, dirnames, filenames in os.walk(self.dire):
            # print(dirpath)
            for name in dirnames:
                path = os.path.join(self.dire, name)
                os.chdir(path)
                print (os.getcwd())
        


        # read vasprun.xml，get band and dos information
                dosrun=Vasprun("./vasprun.xml")
                spd_dos = dosrun.complete_dos.get_spd_dos()
                cdos = dosrun.complete_dos
                element_dos = cdos.get_element_dos()
                fig, ax = plt.subplots()
                line1, = ax.plot(dosrun.tdos.densities[Spin.up], dosrun.tdos.energies, label='Total DOS',linewidth=8,alpha=0.5,)
          # 2pt line, 2pt break, 10pt line, 2pt break
                # x1 = spd_dos[OrbitalType.d].densities[Spin.up]
                # n = len(dosrun.tdos.energies - dosrun.efermi)
                # f = min(dosrun.tdos.energies - dosrun.efermi)
                # t = max(dosrun.tdos.energies - dosrun.efermi)
                # i = (t-f)/(n)
                # print (f)
                # y = np.arange(f, t, i)
                if ele_1 != '':
                    line1 = ax.plot(element_dos[Element(ele_1)].densities[Spin.up], dosrun.tdos.energies, label=(ele_1))
                if ele_2 != '':
                    line2 = ax.plot(element_dos[Element(ele_2)].densities[Spin.up], dosrun.tdos.energies, label=(ele_2))
                if ele_3 != '':
                    line3 = ax.plot(element_dos[Element(ele_3)].densities[Spin.up], dosrun.tdos.energies, label=(ele_3))
                if ele_4 != '':
                    line3 = ax.plot(element_dos[Element(ele_4)].densities[Spin.up], dosrun.tdos.energies, label=(ele_4))        


                linef = plt.axhline(y=dosrun.efermi,xmin=0, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                linef.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                # ax.set_xlabel('Density of states of Silicon')
                ax.set_ylabel('Energy  /  eV')
                font2 = {'family' : 'Times New Roman','fontsize':'20' , 'weight' : 'bold',} 
                #plt.xlabel('Density of states' ,font2)
                # ax.annotate("Energy  /  eV", xy=(-0.05, 0.3), rotation=90,xycoords=ax.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                # plt.ylabel('E-${E_f}$  /  eV' ,font2)
                # plt.scatter(dosrun.tdos.densities[Spin.up], dosrun.tdos.energies - dosrun.efermi, c="g", alpha=0.5, marker=r'$\clubsuit$',
                #     label="Luck")
                # plt.xlabel("Density of states of Silicon")
                # plt.ylabel("E-${E_f}$  /  eV")
                # plt.legend(loc='upper left')
                # plt.show()
                font1 = {'family' : 'Times New Roman',
                'weight' : 'bold',
                }
                ax.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)

                plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                # plt.set_facecolor('none') 
                ax.set_facecolor('none') 

                #存储为
                fig.savefig('./DOS_ele.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                plt.show()



    def plotbandDOS(self,):
        import os
        from pymatgen import Element
        from pymatgen.io.vasp import Vasprun  # 读取vasp作业(vasprun.xml)
        from pymatgen.io.vasp import Vasprun, BSVasprun
        from pymatgen.electronic_structure.plotter import DosPlotter
        from pymatgen.electronic_structure.core import Spin, OrbitalType
        import matplotlib.pyplot as plt
        import numpy as np
        import matplotlib.pyplot as plt
        from pymatgen.io.vasp.outputs import Vasprun
        from pymatgen.electronic_structure.plotter import BSDOSPlotter,\
        BSPlotter,BSPlotterProjected,DosPlotter
        for dirpath, dirnames, filenames in os.walk(self.dire):
            # print(dirpath)
            for name in dirnames:
                path = os.path.join(self.dire, name)
                os.chdir(path)
                print (os.getcwd())
        

        # fig= plt.subplots()
                # read vasprun.xml，get band and dos information
                bs_vasprun = Vasprun("./vasprun.xml",parse_projected_eigen=True)
                bs_data = bs_vasprun.get_band_structure(line_mode=True)

                dos_vasprun=Vasprun("./vasprun.xml")
                dos_data=dos_vasprun.complete_dos
                pbandpdos_fig = BSDOSPlotter(bs_projection='elements', dos_projection='elements',\
                                     vb_energy_range=5, fixed_cb_energy=5)
                pbandpdos_fig.get_plot(bs=bs_data, dos=dos_data)
                plt.savefig('pbandpdos_fig.png', img_format='png')
                # set figure parameters, draw figure
                # banddos_fig = BSDOSPlotter(bs_projection=None, dos_projection=None, vb_energy_range=5, fixed_cb_energy=5)
                # banddos_fig.get_plot(bs=bs_data, dos=dos_data)
                plt.savefig('./BANDDOS.png',bbox_inches='tight', transparent=True,dpi=300,format='png')

                # fig.savefig('./BANDDOS.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                # plt.show()
        


    def plotband(self,):
        import os
        from pymatgen import Element
        from pymatgen.io.vasp import Vasprun  # 读取vasp作业(vasprun.xml)
        from pymatgen.io.vasp import Vasprun, BSVasprun
        from pymatgen.electronic_structure.plotter import DosPlotter
        from pymatgen.electronic_structure.core import Spin, OrbitalType
        import matplotlib.pyplot as plt
        import numpy as np
        import matplotlib.pyplot as plt
        from pymatgen.io.vasp.outputs import Vasprun
        from pymatgen.electronic_structure.plotter import BSDOSPlotter,\
        BSPlotter,BSPlotterProjected,DosPlotter
        for dirpath, dirnames, filenames in os.walk(self.dire):
            # print(dirpath)
            for name in dirnames:
                path = os.path.join(self.dire, name)
                os.chdir(path)
                print (os.getcwd())
        

                bs_vasprun = Vasprun("./vasprun.xml",parse_projected_eigen=True)
                bs_data = bs_vasprun.get_band_structure(line_mode=True)

                dos_vasprun=Vasprun("./vasprun.xml")
                dos_data=dos_vasprun.complete_dos
                # pbandpdos_fig = BSDOSPlotter(bs_projection='elements', dos_projection='elements',\
                #                      vb_energy_range=5, fixed_cb_energy=5)
                # pbandpdos_fig.get_plot(bs=bs_data, dos=dos_data)

                band_fig = BSPlotter(bs=bs_data)
                band_fig.get_plot()
                plt.savefig('band_fig.png', img_format='png')
                plt.savefig('pbandpdos_fig.png', img_format='png')
                # set figure parameters, draw figure
                # banddos_fig = BSDOSPlotter(bs_projection=None, dos_projection=None, vb_energy_range=5, fixed_cb_energy=5)
                # banddos_fig.get_plot(bs=bs_data, dos=dos_data)
                plt.savefig('./BAND.png',bbox_inches='tight', transparent=True,dpi=300,format='png')
    

    def plot_band(self,):
        import os
        from pymatgen import Element
        from pymatgen.io.vasp import Vasprun  # 读取vasp作业(vasprun.xml)
        from pymatgen.io.vasp import Vasprun, BSVasprun
        from pymatgen.electronic_structure.plotter import DosPlotter
        from pymatgen.electronic_structure.core import Spin, OrbitalType
        import matplotlib.pyplot as plt
        import numpy as np
        import matplotlib.pyplot as plt
        from pymatgen.io.vasp.outputs import Vasprun
        from pymatgen.electronic_structure.plotter import BSDOSPlotter,\
        BSPlotter,BSPlotterProjected,DosPlotter
        for dirpath, dirnames, filenames in os.walk(self.dire):
            # print(dirpath)
            for name in dirnames:
                path = os.path.join(self.dire, name)
                os.chdir(path)
                print (os.getcwd())
        
                dosrun=Vasprun("./vasprun.xml")
                run = BSVasprun("./vasprun.xml", parse_projected_eigen = True)  # 读取vasprun.xml
                bands = run.get_band_structure(line_mode=True, efermi=dosrun.efermi)

                emin = 1e100
                emax = -1e100
                for spin in bands.bands.keys():
                    for band in range(bands.nb_bands):
                        emin = min(emin, min(bands.bands[spin][band]))
                        emax = max(emax, max(bands.bands[spin][band]))
                emin = emin - bands.efermi - 1
                emax = emax - bands.efermi + 1

                kptslist = [k for k in range(len(bands.kpoints))]
                bandTraces = list()
                fig, ax = plt.subplots()
                
                for band in range(bands.nb_bands):
                    bandTraces.append(ax.plot(kptslist,[e - bands.efermi for e in bands.bands[Spin.up][band]],) )


                font2 = {'family' : 'Times New Roman','fontsize':'20' , 'weight' : 'bold',} 
                labels = [r"$L$", r"$\Gamma$", r"$X$", r"$U,K$", r"$\Gamma$"]
                step = len(bands.kpoints) / (len(labels) - 1)
                # vertical lines
                vlines = list()
                for i, label in enumerate(labels):
                    vlines.append(ax.plot([i * step, i * step],[emin, emax]))
                    plt.text(i * step,-12,label,font2,verticalalignment="bottom",horizontalalignment="center")
                # plt.Annotation([1], xy=(i * step, emin),xytext=(i * step-0.1, emin-0.1), )
                # Labels of highsymetry k-points are added as Annotation object
                annotations = list()
                
                # for i, label in enumerate(labels):
                #     annotations.append(ax.annotate(label, xy=(i * step, emin+2),xytext=(i * step, emin-0.01), ))
                # x_labels=ax.set_xticklabels(labels)
                ax.set_ylabel('E-${E_f}$  /  eV',font2)
                ax.set_xlabel('k-points',font2,30)
                plt.ylim([-10,6])
                plt.xlim([0,len(bands.kpoints)])
                ax.set_title(r'Bands diagram', font2)
                ax.xaxis.set_major_locator(plt.NullLocator())
                ax.xaxis.set_major_formatter(plt.NullFormatter())
                plt.tight_layout()
                fig.savefig('./BAND.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                plt.show()
        


    def electronic_structure(self, ele_name):
        import os
        from pymatgen import Element
        os.chdir(self.dire)
        symbol = ele_name
        el = Element(symbol)
        elec_structure = el.full_electronic_structure
        from matplotlib.pyplot import figure, show, rc, grid
        rc('grid', color='#316931', linewidth=0, linestyle='-')
        rc('xtick', labelsize=15)
        rc('ytick', labelsize=15)
        import numpy as np
        # make a square figure
        fig = figure(figsize=(10, 10))
        ax = plt.axes([0.1, 0.1, 0.8, 0.8], polar=True,facecolor='#d5de9c')

        rticks = []
        rlabels = []
        for i, shell in enumerate(elec_structure):
            #Draw the shell
            r = 0.5 * (i + 1)
            rad = [r] * 1000
            theta = [2 * np.pi * j / 1000 for j in range(1000)]
            ax.plot(theta, rad, 'k-', lw=1)
            #Draw the electrons
            rad = [r] * shell[2]
            theta = [2 * np.pi * j / shell[2] for j in range(shell[2])]
            ax.plot(theta, rad, 'o', markersize=15)
            rticks.append(r)
            rlabels.append("{}{}".format(shell[0], shell[1]))

        ax.set_rmax(r + 0.5)

        ax.set_thetagrids([0, 90, 180, 270], [""]*4, color='k')
        ax.set_rgrids(rticks, rlabels)
        ax.set_title("Electronic structure of {}".format(symbol), fontsize=20)
        grid(True)
        fig.savefig('./electronic_structure.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
        show()





    def site_orbital_dos(self, site_number_inital = 0,site_number_final = 30,orbi_1 = 'ps',spin = 'up'):
        import os
        from pymatgen import Element
        from pymatgen.io.vasp import Vasprun  # 读取vasp作业(vasprun.xml)
        from pymatgen.io.vasp import Vasprun, BSVasprun
        from pymatgen.electronic_structure.plotter import DosPlotter
        from pymatgen.electronic_structure.core import Spin, OrbitalType,Orbital
        import matplotlib.pyplot as plt
        import numpy as np
        import shutil
        for dirpath, dirnames, filenames in os.walk(self.dire):
            # print(dirpath)
            for name in dirnames:
                path = os.path.join(self.dire, name)
                os.chdir(path)
                print (os.getcwd())
        

                font2 = {'family' : 'Times New Roman','fontsize':'20' , 'weight' : 'bold',} 
                font1 = {'family' : 'Times New Roman',
                'weight' : 'bold',
                }              
                # read vasprun.xml，get band and dos information
                dosrun=Vasprun("./vasprun.xml")
                complete_dos = dosrun.complete_dos
                structure=complete_dos.structure
                if 'up' in spin:

                    for isite,site in enumerate(structure[site_number_inital:site_number_final]):
                        if 's' in orbi_1:
                            fig, ax = plt.subplots()
                            a = complete_dos.get_site_orbital_dos(site, Orbital.s )

                            line0= ax.plot(a.densities[Spin.up], a.energies, label='S', linewidth=5,alpha=0.5,)
                            #plt.xlabel('Density of states' ,font2)
                            plt.ylabel('E-${E_f}$  /  eV' ,font2)
                            ax.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                            plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1) 
                            ax.set_facecolor('none') 
                            #存储为
                            fig.savefig(str(isite+1)+str(site)+'s_up.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                            plt.show()            
                        if 'p' in orbi_1:
                            fig, ax = plt.subplots()
                            a = complete_dos.get_site_orbital_dos(site, Orbital.px )
                            b = complete_dos.get_site_orbital_dos(site, Orbital.py )
                            c = complete_dos.get_site_orbital_dos(site, Orbital.pz )
                            line0= ax.plot(a.densities[Spin.up], a.energies, label='${p_x}$', linewidth=5,alpha=0.5,)
                            line1= ax.plot(b.densities[Spin.up], b.energies, label='${p_y}$', linewidth=5,alpha=0.5,)
                            line2= ax.plot(c.densities[Spin.up], c.energies, label='${p_z}$', linewidth=5,alpha=0.5,)
                            #plt.xlabel('Density of states' ,font2)
                            plt.ylabel('E-${E_f}$  /  eV' ,font2)
                            ax.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                            plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1) 
                            ax.set_facecolor('none') 
                            #存储为
                            fig.savefig(str(isite+1)+str(site)+'p_up.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                            plt.show() 

                        if 'd' in orbi_1:
                            fig, ax = plt.subplots()
                            a = complete_dos.get_site_orbital_dos(site, Orbital.dx2 )
                            b = complete_dos.get_site_orbital_dos(site, Orbital.dxy )
                            c = complete_dos.get_site_orbital_dos(site, Orbital.dxz )
                            d = complete_dos.get_site_orbital_dos(site, Orbital.dyz )
                            e = complete_dos.get_site_orbital_dos(site, Orbital.dz2 )
                            line0= ax.plot(a.densities[Spin.up], a.energies, label='$d_{x^2}$', linewidth=5,alpha=0.5,)
                            line1= ax.plot(b.densities[Spin.up], b.energies, label='$d_{xy}$', linewidth=5,alpha=0.5,)
                            line2= ax.plot(c.densities[Spin.up], c.energies, label='$d_{xz}$', linewidth=5,alpha=0.5,)
                            line3= ax.plot(d.densities[Spin.up], d.energies, label='$d_{yz}$', linewidth=5,alpha=0.5,)
                            line4= ax.plot(e.densities[Spin.up], e.energies, label='$d_{z^2}$', linewidth=5,alpha=0.5,)
                            #plt.xlabel('Density of states' ,font2)
                            plt.ylabel('E-${E_f}$  /  eV' ,font2)
                            ax.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                            plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1) 
                            ax.set_facecolor('none') 
                            #存储为
                            fig.savefig(str(isite+1)+str(site)+'d_up.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                            plt.show() 

                      


                        if 'f' in orbi_1:
                            fig, ax = plt.subplots()
                            a = complete_dos.get_site_orbital_dos(site, Orbital.f0 )
                            b = complete_dos.get_site_orbital_dos(site, Orbital.f1 )
                            c = complete_dos.get_site_orbital_dos(site, Orbital.f2 )
                            d = complete_dos.get_site_orbital_dos(site, Orbital.f3 )
                            f = complete_dos.get_site_orbital_dos(site, Orbital.f_1 )
                            g = complete_dos.get_site_orbital_dos(site, Orbital.f_2 )
                            h = complete_dos.get_site_orbital_dos(site, Orbital.f_3 )
                            line0= ax.plot(a.densities[Spin.up], a.energies, label='${f_0}$', linewidth=5,alpha=0.5,)
                            line1= ax.plot(b.densities[Spin.up], b.energies, label='${f_1}$', linewidth=5,alpha=0.5,)
                            line2= ax.plot(c.densities[Spin.up], c.energies, label='${f_2}$', linewidth=5,alpha=0.5,)
                            line3= ax.plot(d.densities[Spin.up], d.energies, label='${f_3}$', linewidth=5,alpha=0.5,)
                            line4= ax.plot(f.densities[Spin.up], f.energies, label='${f_5}$', linewidth=5,alpha=0.5,)
                            line5= ax.plot(g.densities[Spin.up], g.energies, label='${f_6}$', linewidth=5,alpha=0.5,)
                            line6= ax.plot(h.densities[Spin.up], h.energies, label='${P_z}$', linewidth=5,alpha=0.5,)
                            #plt.xlabel('Density of states' ,font2)
                            plt.ylabel('E-${E_f}$  /  eV' ,font2)
                            ax.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                            plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1) 
                            ax.set_facecolor('none') 
                            #存储为
                            fig.savefig(str(isite+1)+str(site)+'f_up.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                            plt.show() 

                else:
                    for isite,site in enumerate(structure[site_number_inital:site_number_final]):
                        if 's' in orbi_1:
                            fig, ax = plt.subplots()
                            a = complete_dos.get_site_orbital_dos(site, Orbital.s )

                            line0= ax.plot(a.densities[Spin.down], a.energies, label='S', linewidth=5,alpha=0.5,)
                            #plt.xlabel('Density of states' ,font2)
                            plt.ylabel('E-${E_f}$  /  eV' ,font2)
                            ax.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                            plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1) 
                            ax.set_facecolor('none') 
                            #存储为
                            fig.savefig(str(isite+1)+str(site)+'s_down.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                            plt.show()            
                        if 'p' in orbi_1:
                            fig, ax = plt.subplots()
                            a = complete_dos.get_site_orbital_dos(site, Orbital.px )
                            b = complete_dos.get_site_orbital_dos(site, Orbital.py )
                            c = complete_dos.get_site_orbital_dos(site, Orbital.pz )
                            line0= ax.plot(a.densities[Spin.down], a.energies, label='${p_x}$', linewidth=5,alpha=0.5,)
                            line1= ax.plot(b.densities[Spin.down], b.energies, label='${p_y}$', linewidth=5,alpha=0.5,)
                            line2= ax.plot(c.densities[Spin.down], c.energies, label='${p_z}$', linewidth=5,alpha=0.5,)
                            #plt.xlabel('Density of states' ,font2)
                            plt.ylabel('E-${E_f}$  /  eV' ,font2)
                            ax.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                            plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1) 
                            ax.set_facecolor('none') 
                            #存储为
                            fig.savefig(str(isite+1)+str(site)+'p_down.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                            plt.show() 

                        if 'd' in orbi_1:
                            fig, ax = plt.subplots()
                            a = complete_dos.get_site_orbital_dos(site, Orbital.dx2 )
                            b = complete_dos.get_site_orbital_dos(site, Orbital.dxy )
                            c = complete_dos.get_site_orbital_dos(site, Orbital.dxz )
                            d = complete_dos.get_site_orbital_dos(site, Orbital.dyz )
                            e = complete_dos.get_site_orbital_dos(site, Orbital.dz2 )
                            line0= ax.plot(a.densities[Spin.down], a.energies, label='$d_{x^2}$', linewidth=5,alpha=0.5,)
                            line1= ax.plot(b.densities[Spin.down], b.energies, label='$d_{xy}$', linewidth=5,alpha=0.5,)
                            line2= ax.plot(c.densities[Spin.down], c.energies, label='$d_{xz}$', linewidth=5,alpha=0.5,)
                            line3= ax.plot(d.densities[Spin.down], d.energies, label='$d_{yz}$', linewidth=5,alpha=0.5,)
                            line4= ax.plot(e.densities[Spin.down], e.energies, label='$d_{z^2}$', linewidth=5,alpha=0.5,)
                            #plt.xlabel('Density of states' ,font2)
                            plt.ylabel('E-${E_f}$  /  eV' ,font2)
                            ax.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                            plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1) 
                            ax.set_facecolor('none') 
                            #存储为
                            fig.savefig(str(isite+1)+str(site)+'d_down.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                            plt.show() 

                        if 'f' in orbi_1:
                            fig, ax = plt.subplots()
                            a = complete_dos.get_site_orbital_dos(site, Orbital.f0 )
                            b = complete_dos.get_site_orbital_dos(site, Orbital.f1 )
                            c = complete_dos.get_site_orbital_dos(site, Orbital.f2 )
                            d = complete_dos.get_site_orbital_dos(site, Orbital.f3 )
                            f = complete_dos.get_site_orbital_dos(site, Orbital.f_1 )
                            g = complete_dos.get_site_orbital_dos(site, Orbital.f_2 )
                            h = complete_dos.get_site_orbital_dos(site, Orbital.f_3 )
                            line0= ax.plot(a.densities[Spin.down], a.energies, label='${f_0}$', linewidth=5,alpha=0.5,)
                            line1= ax.plot(b.densities[Spin.down], b.energies, label='${f_1}$', linewidth=5,alpha=0.5,)
                            line2= ax.plot(c.densities[Spin.down], c.energies, label='${f_2}$', linewidth=5,alpha=0.5,)
                            line3= ax.plot(d.densities[Spin.down], d.energies, label='${f_3}$', linewidth=5,alpha=0.5,)
                            line4= ax.plot(f.densities[Spin.down], f.energies, label='${f_5}$', linewidth=5,alpha=0.5,)
                            line5= ax.plot(g.densities[Spin.down], g.energies, label='${f_6}$', linewidth=5,alpha=0.5,)
                            line6= ax.plot(h.densities[Spin.down], h.energies, label='${P_z}$', linewidth=5,alpha=0.5,)
                            #plt.xlabel('Density of states' ,font2)
                            plt.ylabel('E-${E_f}$  /  eV' ,font2)
                            ax.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                            plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1) 
                            ax.set_facecolor('none') 
                            #存储为
                            fig.savefig(str(isite+1)+str(site)+'f_down.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                            plt.show()






    def site_spd_dos(self,site_number_inital = 0,site_number_final = 30):
        import os
        from pymatgen import Element
        from pymatgen.io.vasp import Vasprun  # 读取vasp作业(vasprun.xml)
        from pymatgen.io.vasp import Vasprun, BSVasprun
        from pymatgen.electronic_structure.plotter import DosPlotter
        from pymatgen.electronic_structure.core import Spin, OrbitalType,Orbital
        import matplotlib.pyplot as plt
        import numpy as np
        for dirpath, dirnames, filenames in os.walk(self.dire):
            # print(dirpath)
            for name in dirnames:
                path = os.path.join(self.dire, name)
                os.chdir(path)
                print (os.getcwd())
        

        
        # read vasprun.xml，get band and dos information
                dosrun=Vasprun("./vasprun.xml")
                spd_dos = dosrun.complete_dos.get_spd_dos()
                

                complete_dos = dosrun.complete_dos
                # print(complete_dos)
                structure=complete_dos.structure
                for isite,site in enumerate(structure[site_number_inital:site_number_final]):
                    fig, ax = plt.subplots()
                    c = complete_dos.get_site_spd_dos(site)
                    tatal = c[OrbitalType.s].densities[Spin.up] + c[OrbitalType.p].densities[Spin.up] + c[OrbitalType.d].densities[Spin.up]
                    line = ax.plot(tatal, dosrun.tdos.energies - dosrun.efermi, label='Total DOS',linewidth=8,alpha=0.5,)
                    line0 = ax.plot(c[OrbitalType.s].densities[Spin.up], dosrun.tdos.energies- dosrun.efermi , label=(str(isite+1)+str(site)+ '(s)'))
                    line1 = ax.plot(c[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies - dosrun.efermi, label=(str(isite+1)+str(site)+ '(p)'))
                    # line2 = ax.plot(c[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies - dosrun.efermi, label=(str(isite+1)+str(site)+ '(d)'))# Plotter.get_plot(ylim = [0,1.2]).show()
                    

                    # plt.ylim(-15,5)
                    
                    ax.set_xlabel('Density of states of Silicon')
                    ax.set_ylabel('voltage (mV)')
                    font2 = {'family' : 'Times New Roman',
                    'weight' : 'bold',
                    }
                    #plt.xlabel('Density of states' ,font2)
                    plt.ylabel('E-${E_f}$  /  eV' ,font2)

                    font1 = {'family' : 'Times New Roman',
                    'weight' : 'bold',
                    }
                    ax.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)

                    plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                    # plt.set_facecolor('none') 
                    ax.set_facecolor('none') 

                    #存储为
                    fig.savefig(str(isite+1)+str(site)+".png",bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                    plt.show()
                print(structure[site_number_inital:site_number_final])





    def site_orbital_dos_mirror(self, site_number_inital = 0,site_number_final = 30,orbi_1 = 'ps',spin = 'up'):
        import os
        from pymatgen import Element
        from pymatgen.io.vasp import Vasprun  # 读取vasp作业(vasprun.xml)
        from pymatgen.io.vasp import Vasprun, BSVasprun
        from pymatgen.electronic_structure.plotter import DosPlotter
        from pymatgen.electronic_structure.core import Spin, OrbitalType,Orbital
        import matplotlib.pyplot as plt
        import numpy as np
        import shutil

        os.chdir(self.dire)
        for dirpath, dirnames, filenames in os.walk(self.dire):
            # print(dirpath)
            for name in dirnames:
                path = os.path.join(self.dire, name)
                os.chdir(path)
                print (os.getcwd())

                font2 = {'family' : 'Times New Roman','fontsize':'20' , 'weight' : 'bold',} 
                font1 = {'family' : 'Times New Roman',
                'weight' : 'bold',
                }              
                # read vasprun.xml，get band and dos information
                dosrun=Vasprun("./vasprun.xml")
                complete_dos = dosrun.complete_dos
                structure=complete_dos.structure
                
                if 'up' in spin:

                    for isite,site in enumerate(structure[site_number_inital:site_number_final]):
                        if 's' in orbi_1:
                            fig, ax0 = plt.subplots()
                            a = complete_dos.get_site_orbital_dos(site, Orbital.s )

                            line0,= ax0.plot(-a.densities[Spin.up], a.energies, label='S : α', color = 'g', linewidth=1,alpha=0.5)
                            line00= ax0.plot(a.densities[Spin.down], a.energies, label='S : β',color = 'g', linewidth=1,alpha=0.5)
                            print(dosrun.efermi)
                            linef = plt.axhline(y=dosrun.efermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                            linef.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                            # plt.axhline(0, 0, 0.5,linestyles = "dashed", alpha=0.5)
                            ax0 = plt.gca()                                            # get current ax0is 获得坐标轴对象

                            ax0.spines['right'].set_color('none') 
                            ax0.spines['top'].set_color('none')   
                            # ax0.spines['bottom'].set_position(('data', -20))      # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                            ax0.spines['bottom'].set_color('none') 
                            ax0.spines['left'].set_position(('data', 0))
                            plt.xticks([])
                            plt.yticks([])
                            #plt.xlabel('Density of states' ,font2)
                            # plt.ylabel('E-${E_f}$  /  eV' ,font2,160)
                            # ax0.annotate("Energy  /  eV", xy=(-0.05, 0.3), rotation=90,xycoords=ax0.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                            ax0.legend([line0],['s'], frameon=True, edgecolor='none', facecolor='none', prop=font1)
                            # ax0.annotate("α", xy=(0.43, 0.95), xycoords=ax0.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                            # ax0.annotate("β", xy=(0.55, 0.95), xycoords=ax0.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                            
                            # plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1) 
                            ax0.set_facecolor('none') 
                            #存储为
                            fig.savefig(str(isite+1)+str(site)+'s.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                            plt.show()            
                        if 'p' in orbi_1:
                            fig, ax1 = plt.subplots()
                            a = complete_dos.get_site_orbital_dos(site, Orbital.px )
                            b = complete_dos.get_site_orbital_dos(site, Orbital.py )
                            c = complete_dos.get_site_orbital_dos(site, Orbital.pz )
                            a0 = complete_dos.get_site_orbital_dos(site, Orbital.px )
                            b0 = complete_dos.get_site_orbital_dos(site, Orbital.py )
                            c0 = complete_dos.get_site_orbital_dos(site, Orbital.pz )
                            line0,= ax1.plot(-a.densities[Spin.up], a.energies, label='${p_x} : α$', color = 'r', linewidth=1,alpha=0.5,)
                            line1,= ax1.plot(-b.densities[Spin.up], b.energies, label='${p_y} : α$', color = 'g',linewidth=1,alpha=0.5,)
                            line2,= ax1.plot(-c.densities[Spin.up], c.energies, label='${p_z} : α$', color = 'blue',linewidth=1,alpha=0.5,)
                            line00= ax1.plot(a0.densities[Spin.down], a0.energies, label='${p_x}: β$', color = 'r',linewidth=1,alpha=0.5,)
                            line10= ax1.plot(b0.densities[Spin.down], b0.energies, label='${p_y}: β$', color = 'g',linewidth=1,alpha=0.5,)
                            line20= ax1.plot(c0.densities[Spin.down], c0.energies, label='${p_z}: β$', color = 'blue',linewidth=1,alpha=0.5,)
                            print(dosrun.efermi)
                            linef = plt.axhline(y=dosrun.efermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                            linef.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                            # plt.axhline(0, 0, 0.5,linestyles = "dashed", alpha=0.5)



                            ax1 = plt.gca()                                            # get current ax1is 获得坐标轴对象

                            ax1.spines['right'].set_color('none') 
                            ax1.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                            ax1.spines['bottom'].set_color('none') 
                            # ax1.spines['bottom'].set_position(('data', -20))
                            ax1.spines['left'].set_position(('data', 0))
                            plt.xticks([])
                            plt.yticks([])
                            #plt.xlabel('Density of states' ,font2)
                            # plt.ylabel('E-${E_f}$  /  eV' ,font2,160)
                            # ax1.annotate("Energy  /  eV", xy=(-0.05, 0.3), rotation=90,xycoords=ax1.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                            ax1.legend([line0, line1,line2],['${p_x}$','${p_y}$','${p_z}$'],  frameon=True, edgecolor='none', facecolor='none', prop=font1)
                            # plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                            # ax1.annotate("α", xy=(0.43, 0.95), xycoords=ax1.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                            # ax1.annotate("β", xy=((0.55, 0.95)), xycoords=ax1.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                            ax1.set_facecolor('none') 
                            #存储为
                            fig.savefig(str(isite+1)+str(site)+'p.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                            plt.show() 

                        if 'd' in orbi_1:
                            fig, ax2 = plt.subplots()
                            a = complete_dos.get_site_orbital_dos(site, Orbital.dx2 )
                            b = complete_dos.get_site_orbital_dos(site, Orbital.dxy )
                            c = complete_dos.get_site_orbital_dos(site, Orbital.dxz )
                            d = complete_dos.get_site_orbital_dos(site, Orbital.dyz )
                            e = complete_dos.get_site_orbital_dos(site, Orbital.dz2 )
                            a0 = complete_dos.get_site_orbital_dos(site, Orbital.dx2 )
                            b0 = complete_dos.get_site_orbital_dos(site, Orbital.dxy )
                            c0 = complete_dos.get_site_orbital_dos(site, Orbital.dxz )
                            d0 = complete_dos.get_site_orbital_dos(site, Orbital.dyz )
                            e0 = complete_dos.get_site_orbital_dos(site, Orbital.dz2 )
                            line0,= ax2.plot(-a.densities[Spin.up], a.energies, color = 'r',label='$d_{x^2}$', linewidth=1,alpha=0.5,)
                            line1,= ax2.plot(-b.densities[Spin.up], b.energies, color = 'g',label='$d_{xy}$', linewidth=1,alpha=0.5,)
                            line2,= ax2.plot(-c.densities[Spin.up], c.energies, color = 'blue',label='$d_{xz}$', linewidth=1,alpha=0.5,)
                            line3,= ax2.plot(-d.densities[Spin.up], d.energies, color = 'orange',label='$d_{yz}$', linewidth=1,alpha=0.5,)
                            line4,= ax2.plot(-e.densities[Spin.up], e.energies, color = 'grey',label='$d_{z^2}$', linewidth=1,alpha=0.5,)
                            line00= ax2.plot(a0.densities[Spin.down], a0.energies, color = 'r',label='$d_{x^2}$', linewidth=1,alpha=0.5,)
                            line10= ax2.plot(b0.densities[Spin.down], b0.energies, color = 'g',label='$d_{xy}$', linewidth=1,alpha=0.5,)
                            line20= ax2.plot(c0.densities[Spin.down], c0.energies, color = 'blue',label='$d_{xz}$', linewidth=1,alpha=0.5,)
                            line30= ax2.plot(d0.densities[Spin.down], d0.energies, color = 'grey',label='$d_{yz}$', linewidth=1,alpha=0.5,)
                            line40= ax2.plot(e0.densities[Spin.down], e0.energies, color = 'orange',label='$d_{z^2}$', linewidth=1,alpha=0.5,)
                            print(dosrun.efermi)
                            linef = plt.axhline(y=dosrun.efermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                            linef.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                            # plt.axhline(0, 0, 0.5,linestyles = "dashed", alpha=0.5)
                            ax2 = plt.gca()                                            # get current ax2is 获得坐标轴对象

                            ax2.spines['right'].set_color('none') 
                            ax2.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                            ax2.spines['bottom'].set_color('none') 
                            # ax2.spines['bottom'].set_position(('data', -20))
                            ax2.spines['left'].set_position(('data', 0))
                            plt.xticks([])
                            plt.yticks([])
                            #plt.xlabel('Density of states' ,font2)
                            # plt.ylabel('E-${E_f}$  /  eV' ,font2,160)
                            # ax2.annotate("Energy  /  eV", xy=(-0.05, 0.3), rotation=90,xycoords=ax2.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                            ax2.legend([line0,line1,line2,line3,line4],['$d_{x^2}$','$d_{xy}$','$d_{xz}$','$d_{yz}$','$d_{z^2}$',],  frameon=True, edgecolor='none', facecolor='none', prop=font1)
                            # plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                            # ax2.annotate("α", xy=(0.43, 0.95), xycoords=ax2.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                            # ax2.annotate("β", xy=((0.55, 0.95)), xycoords=ax2.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                            ax2.set_facecolor('none') 
                            #存储为
                            fig.savefig(str(isite+1)+str(site)+'d.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                            plt.show() 

              


                        if 'f' in orbi_1:
                            fig, ax3 = plt.subplots()
                            a = complete_dos.get_site_orbital_dos(site, Orbital.f0 )
                            b = complete_dos.get_site_orbital_dos(site, Orbital.f1 )
                            c = complete_dos.get_site_orbital_dos(site, Orbital.f2 )
                            d = complete_dos.get_site_orbital_dos(site, Orbital.f3 )
                            f = complete_dos.get_site_orbital_dos(site, Orbital.f_1 )
                            g = complete_dos.get_site_orbital_dos(site, Orbital.f_2 )
                            h = complete_dos.get_site_orbital_dos(site, Orbital.f_3 )
                            a0 = complete_dos.get_site_orbital_dos(site, Orbital.f0 )
                            b0 = complete_dos.get_site_orbital_dos(site, Orbital.f1 )
                            c0 = complete_dos.get_site_orbital_dos(site, Orbital.f2 )
                            d0 = complete_dos.get_site_orbital_dos(site, Orbital.f3 )
                            f0 = complete_dos.get_site_orbital_dos(site, Orbital.f_1 )
                            g0 = complete_dos.get_site_orbital_dos(site, Orbital.f_2 )
                            h0 = complete_dos.get_site_orbital_dos(site, Orbital.f_3 )
                            line00,= ax3.plot(a0.densities[Spin.down], a0.energies, color = 'r',label='${f_0}$', linewidth=1,alpha=0.5,)
                            line10,= ax3.plot(b0.densities[Spin.down], b0.energies, color = 'g',label='${f_1}$', linewidth=1,alpha=0.5,)
                            line20,= ax3.plot(c0.densities[Spin.down], c0.energies, color = 'blue',label='${f_2}$', linewidth=1,alpha=0.5,)
                            line30,= ax3.plot(d0.densities[Spin.down], d0.energies, color = 'grey',label='${f_3}$', linewidth=1,alpha=0.5,)
                            line40,= ax3.plot(f0.densities[Spin.down], f0.energies, color = 'orange',label='${f_5}$', linewidth=1,alpha=0.5,)
                            line50,= ax3.plot(g0.densities[Spin.down], g0.energies, color = 'darkviolet',label='${f_6}$', linewidth=1,alpha=0.5,)
                            line60,= ax3.plot(h0.densities[Spin.down], h0.energies, color = 'olive',label='${f_7}$', linewidth=1,alpha=0.5,)
                            line0,= ax3.plot(a.densities[Spin.up], a.energies, color = 'r',label='${f_0}$', linewidth=1,alpha=0.5,)
                            line1,= ax3.plot(b.densities[Spin.up], b.energies, color = 'g',label='${f_1}$', linewidth=1,alpha=0.5,)
                            line2,= ax3.plot(c.densities[Spin.up], c.energies, color = 'b',label='${f_2}$', linewidth=1,alpha=0.5,)
                            line3,= ax3.plot(d.densities[Spin.up], d.energies, color = 'grey',label='${f_3}$', linewidth=1,alpha=0.5,)
                            line4,= ax3.plot(f.densities[Spin.up], f.energies, color = 'orange',label='${f_5}$', linewidth=1,alpha=0.5,)
                            line5,= ax3.plot(g.densities[Spin.up], g.energies, color = 'darkviolet',label='${f_6}$', linewidth=1,alpha=0.5,)
                            line6,= ax3.plot(h.densities[Spin.up], h.energies, color = 'olive',label='${f_7}$', linewidth=1,alpha=0.5,)
                            print(dosrun.efermi)
                            linef = plt.axhline(y=dosrun.efermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                            linef.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                            # plt.axhline(0, 0, 0.5,linestyles = "dashed", alpha=0.5)
                            ax3 = plt.gca()                                            # get current ax3is 获得坐标轴对象

                            ax3.spines['right'].set_color('none') 
                            ax3.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                            ax3.spines['bottom'].set_color('none') 
                            # ax3.spines['bottom'].set_position(('data', -20))
                            ax3.spines['left'].set_position(('data', 0)) 
                            plt.xticks([])
                            plt.yticks([])
                            #plt.xlabel('Density of states' ,font2)
                            # plt.ylabel('E-${E_f}$  /  eV' ,font2,160)
                            # ax3.annotate("Energy  /  eV", xy=(-0.05, 0.3), rotation=90,xycoords=ax3.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                            ax3.legend([line0,line1,line2,line3,line4,line5,line6],['${f_0}$','${f_1}$','${f_2}$','${f_3}$','${f_4}$','${f_5}$','${f_6}$','${f_7}$',],  frameon=True, edgecolor='none', facecolor='none', prop=font1)
                            # plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                            # ax3.annotate("α", xy=(0.43, 0.95), xycoords=ax3.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                            # ax3.annotate("β", xy=((0.55, 0.95)), xycoords=ax3.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                            ax3.set_facecolor('none') 
                            #存储为
                            fig.savefig(str(isite+1)+str(site)+'f.png',bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                            plt.show() 
                        print (structure)



    def site_spd_dos_mirror(self,site_number_inital = 0,site_number_final = 30,orbi_1 = 'spd'):
        import os
        from pymatgen import Element
        from pymatgen.io.vasp import Vasprun  # 读取vasp作业(vasprun.xml)
        from pymatgen.io.vasp import Vasprun, BSVasprun
        from pymatgen.electronic_structure.plotter import DosPlotter
        from pymatgen.electronic_structure.core import Spin, OrbitalType,Orbital
        import matplotlib.pyplot as plt
        import numpy as np
        for dirpath, dirnames, filenames in os.walk(self.dire):
            # print(dirpath)
            for name in dirnames:
                path = os.path.join(self.dire, name)
                os.chdir(path)
                print (os.getcwd())

                font2 = {'family' : 'Times New Roman','fontsize':'20' , 'weight' : 'bold',} 
                font1 = {'family' : 'Times New Roman',
                'weight' : 'bold',
                }              
                # read vasprun.xml，get band and dos information
                dosrun=Vasprun("./vasprun.xml")
                complete_dos = dosrun.complete_dos
                structure=complete_dos.structure
                spd_dos = dosrun.complete_dos.get_spd_dos()
                complete_dos = dosrun.complete_dos
                # print(complete_dos)
                structure=complete_dos.structure
                for isite,site in enumerate(structure[site_number_inital:site_number_final]):
                    fig, ax6 = plt.subplots()
                    c = complete_dos.get_site_spd_dos(site)
                    tatal0 = c[OrbitalType.s].densities[Spin.down] + c[OrbitalType.p].densities[Spin.down] + c[OrbitalType.d].densities[Spin.down]
                    tatal = c[OrbitalType.s].densities[Spin.up] + c[OrbitalType.p].densities[Spin.up] + c[OrbitalType.d].densities[Spin.up]
                    line_1, = ax4.plot(-tatal, dosrun.tdos.energies , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    line_2, = ax4.plot(tatal0, dosrun.tdos.energies , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)


                    if 'd' in str(orbi_1):


                        line00, = ax4.plot(-c[OrbitalType.s].densities[Spin.up], dosrun.tdos.energies , linewidth=1,color = 'r',label=(str(isite+1)+str(site)+ '(s)'))
                        line0 = ax4.plot(c[OrbitalType.s].densities[Spin.down], dosrun.tdos.energies , linewidth=1,color = 'r',label=(str(isite+1)+str(site)+ '(s)'))




                        line10, = ax4.plot(-c[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies , linewidth=1,color = 'g',label=(str(isite+1)+str(site)+ '(p)'))
                        line1 = ax4.plot(c[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies , linewidth=1,color = 'g',label=(str(isite+1)+str(site)+ '(p)'))


                        line20, = ax4.plot(-c[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies , linewidth=1,color = 'orange',label=(str(isite+1)+str(site)+ '(d)'))
                        line2 = ax4.plot(c[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies , linewidth=1,color = 'orange',label=(str(isite+1)+str(site)+ '(d)'))#
                        ax4.legend([line_1, line00, line10, line20],['Total DOS','s','p','d'],   frameon=True, edgecolor='none', facecolor='none', prop=font1)

                    else:
                        line00, = ax4.plot(-c[OrbitalType.s].densities[Spin.up], dosrun.tdos.energies , linewidth=1,color = 'r',label=(str(isite+1)+str(site)+ '(s)'))
                        line0 = ax4.plot(c[OrbitalType.s].densities[Spin.down], dosrun.tdos.energies , linewidth=1,color = 'r',label=(str(isite+1)+str(site)+ '(s)'))




                        line10, = ax4.plot(-c[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies , linewidth=1,color = 'g',label=(str(isite+1)+str(site)+ '(p)'))
                        line1 = ax4.plot(c[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies , linewidth=1,color = 'g',label=(str(isite+1)+str(site)+ '(p)'))
                        ax4.legend([line_1, line00, line10],['Total DOS','s','p'],   frameon=True, edgecolor='none', facecolor='none', prop=font1)
                    linef = plt.axhline(y=dosrun.efermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    linef.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    # plt.ax4hline(0, 0, 0.5,linestyles = "dashed", alpha=0.5)



                    ax4 = plt.gca()                                            # get current ax4is 获得坐标轴对象

                    ax4.spines['right'].set_color('none') 
                    ax4.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax4.spines['bottom'].set_color('none') 
                    # ax4.spines['bottom'].set_position(('data', -20))
                    ax4.spines['left'].set_position(('data', 0))
                    plt.xticks([])
                    plt.yticks([])
                    #plt.xlabel('Density of states' ,font2)
                    # plt.ylabel('E-${E_f}$  /  eV' ,font2,160)
                    # plt.ylabel('Energy  /  eV' ,font2,x = 0.1,xycoords=ax4.transAxes,)
                    # ax4.annotate("Energy  /  eV", xy=(-0.05, 0.3), rotation=90,xycoords=ax4.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                    # plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                    # ax4.annotate("α", xy=(0.43, 0.95), xycoords=ax4.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                    # ax4.annotate("β", xy=((0.55, 0.95)), xycoords=ax4.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                    ax4.set_facecolor('none')  

                    #存储为
                    fig.savefig(str(isite+1)+str(site)+".png",bbox_inches='tight', transparent=True,dpi=300,format='png')#指定分辨率,边界紧，背景透明
                    plt.show()
                print(structure[site_number_inital:site_number_final])



    def absorbed_plot(self,miller_index_1, num='1234567890',min_slab_size_1=8.0,  min_vacuum_size_1=15):
        from pymatgen import Structure, Lattice, MPRester, Molecule
        import pymatgen.core.structure
        from pymatgen.core.surface import Slab, SlabGenerator, generate_all_slabs, Structure, Lattice, ReconstructionGenerator
        import pymatgen.core.sites
        from pymatgen.analysis.adsorption import AdsorbateSiteFinder, reorient_z, plot_slab
        from pymatgen.core.surface import generate_all_slabs
        from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
        from matplotlib import pyplot as plt
        from pymatgen.ext.matproj import MPRester
        from pymatgen.io.vasp.inputs import Poscar
        from pymatgen.io.vasp.sets import MPRelaxSet
        from pymatgen.io.cif import CifWriter
        import os
        import shutil
        from pymatgen.io.vasp import Poscar

        os.chdir(self.dire)
        print (os.getcwd())
        poscar = Poscar.from_file("POSCAR")
        struct = poscar.structure
        need_miller_index = miller_index_1#通过米勒指数，确定要切的晶面
        font2 = {'family' : 'Times New Roman','fontsize':'20' , 'weight' : 'bold',} 
        slab = SlabGenerator(struct, miller_index=need_miller_index, min_slab_size=min_slab_size_1,\
                             min_vacuum_size=min_vacuum_size_1, center_slab=True)
        #晶面生成器参数
        gh = str(miller_index_1).replace(" ", "")
        for n, slabs in enumerate(slab.get_slabs()):
            if str(n) in str(num):
                fig = plt.figure()#绘图--确立画布
                ax = plt.subplot(111)#绘图--确立位置                
                slabs_bak = slabs.copy()#可能的晶面
                # slabs.make_supercell(self.supercell)
                plot_slab(slabs, ax, adsorption_sites=False,draw_unit_cell = False,scale = 0.6,repeat = 5,window =1)#绘图
                dire =str(n)
                ax.spines['right'].set_color('none') 
                ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                ax.spines['bottom'].set_color('none')
                ax.spines['left'].set_color('none')  
                # ax4.spines['bottom'].set_position(('data', -20))
                # plt.spines['left'].set_position(('data', 0))
                plt.xticks([])
                plt.yticks([])
                # plt.xlabel('FeS (001)' ,font2)
                # plt.ylabel('E-${E_f}$  /  eV' ,font2,160)
                # plt.ylabel('Energy  /  eV' ,font2,x = 0.1,xycoords=ax4.transAxes,)
                # ax4.annotate("Energy  /  eV", xy=(-0.05, 0.3), rotation=90,xycoords=ax4.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                # plt.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                # ax4.annotate("α", xy=(0.43, 0.95), xycoords=ax4.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                # ax4.annotate("β", xy=((0.55, 0.95)), xycoords=ax4.transAxes,fontsize=20,family='Times New Roman',weight='bold')
                ax.set_facecolor('none')                
                #设置一个用作存储输入文件的名称
                plt.savefig(str(dire)+".png",bbox_inches='tight', transparent=True,dpi=400,format='png')
                
                               





    def absorb_site_spd_dos_mirror(self,miller_index_1,num1,b_atomnum1 =1,b_atomnum2 =2,b_atomnum3 =3,m_atomnum =1,a_atomnum1 = 1,a_atomnum2 = 1,a_atomnum3 = 1,am_atomnum1 = 1,am_atomnum2 = 1):
        import os
        from pymatgen import Element
        from pymatgen.io.vasp import Vasprun  # 读取vasp作业(vasprun.xml)
        from pymatgen.io.vasp import Vasprun, BSVasprun
        from pymatgen.electronic_structure.plotter import DosPlotter
        from pymatgen.electronic_structure.core import Spin, OrbitalType,Orbital
        import matplotlib.pyplot as plt
        from pymatgen.io.vasp.inputs import Poscar
        from pymatgen.io.vasp.sets import MPRelaxSet
        from pymatgen.io.cif import CifWriter
        from pymatgen.analysis.adsorption import AdsorbateSiteFinder, reorient_z, plot_slab
        from pymatgen.core.surface import Slab, SlabGenerator, generate_all_slabs, Structure, Lattice, ReconstructionGenerator
        import os
        import shutil
        from pymatgen.io.vasp import Poscar
        import numpy as np
        import cv2
        font2 = {'family' : 'Times New Roman','fontsize':'20' , 'weight' : 'bold',}
        font1 = {'family' : 'Times New Roman','weight' : 'bold',} 
        # fig= plt.subplots()
        fig=plt.figure(figsize=(16, 13))
        
        for dirpath, dirnames, filenames in os.walk(self.dire):
            

            for name in dirnames:
                if'note0' in str(name):  
                    path = os.path.join(self.dire, name)
                    os.chdir(path)
                    print (os.getcwd())
                    img = cv2.imread(num1)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # 注意这行。
                    # rect1 = [-0.1, 0.45, 0.85, 0.4]#[左, 下, 宽, 高] 规定的矩形区域 （全部是0~1之间的数，表示比例）
                    ax0=fig.add_subplot(2,2,1)
                    # ax0= plt.axes(rect1)
                    plt.imshow(img)
                    ax0.spines['right'].set_color('none') 
                    ax0.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax0.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax0.spines['left'].set_color('none')
                    arrowprops = dict(arrowstyle = "->",connectionstyle = "angle,angleA=0,angleB=90,rad=10")
                    bbox = dict(boxstyle="round", fc="0.8")
                    x1 = 610
                    y1 = 600
                    ax0.annotate("Fe$_{(1)}$", xy=(x1, y1),xytext=(x1+200, y1-200), bbox=bbox, arrowprops=arrowprops,fontsize=30,family='Times New Roman',weight='bold')
                    x2 = 520
                    y2 = 695
                    ax0.annotate("Fe$_{(2)}$", xy=(x2, y2),xytext=(x2-400, y2-100), bbox=bbox, arrowprops=arrowprops ,fontsize=30,family='Times New Roman',weight='bold')
                    x3 = 605
                    y3 = 780
                    ax0.annotate("Fe$_{(3)}$", xy=(x3, y3),xytext=(x3+200, y3+200), bbox=bbox, arrowprops=arrowprops,fontsize=30,family='Times New Roman',weight='bold')
                    x4 = 610
                    y4 = 680
                    ax0.annotate("O$_{(1)}$", xy=(x4, y4),xytext=(x4+200, y4-60), bbox=bbox, arrowprops=arrowprops,fontsize=30,family='Times New Roman',weight='bold')
                    x5 = 580
                    y5 = 720
                    ax0.annotate("O$_{(2)}$", xy=(x5, y5),xytext=(x5-400, y5+200),bbox=bbox, arrowprops=arrowprops, fontsize=30,family='Times New Roman',weight='bold')
                    # plt.subplots_adjust(left=1, bottom=1, right=1, wspace=1.0,hspace =0)
                    plt.xticks([]),plt.yticks([])
                    plt.gca().xaxis.set_major_locator(plt.NullLocator())
                    plt.gca().yaxis.set_major_locator(plt.NullLocator())
                    ax0.set_facecolor('none')
                    # plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
                    # #plt.xlim((-3.5, 3.5))3))
                    # plt.ylim((-10, 
                    ax0.set_title('FeS (001)',font2,y = -0.1)   




                if 'befor' in name:
                    path = os.path.join(self.dire, name)
                    os.chdir(path)
                    print (os.getcwd())
                    dosrun=Vasprun("./vasprun.xml")
                    complete_dos = dosrun.complete_dos
                    structure=complete_dos.structure
                    spd_dos = dosrun.complete_dos.get_spd_dos()
                    complete_dos = dosrun.complete_dos
                    # print(complete_dos)
                    structure=complete_dos.structure

                    site1 = structure[b_atomnum1-1] 
                    print (site1)
                    ax1=fig.add_subplot(2,9,6)
                    c1 = complete_dos.get_site_spd_dos(site1)
                    total10 = c1[OrbitalType.s].densities[Spin.down] + c1[OrbitalType.p].densities[Spin.down] + c1[OrbitalType.d].densities[Spin.down]
                    tatal = c1[OrbitalType.s].densities[Spin.up] + c1[OrbitalType.p].densities[Spin.up] + c1[OrbitalType.d].densities[Spin.up]
                    line0, = ax1.plot(-tatal, dosrun.tdos.energies , color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    line1, = ax1.plot(total10, dosrun.tdos.energies , color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    line2, = ax1.plot(-c1[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies , linewidth=1,color = 'orange')
                    line3, = ax1.plot(c1[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies , linewidth=1,color = 'orange')#
                    linef1 = plt.axhline(y=dosrun.efermi,xmin=0.2, xmax=1, color = 'grey',linewidth=1,alpha=0.7)
                    linef1.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break

                    ax1.spines['right'].set_color('none') 
                    ax1.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax1.spines['bottom'].set_color('none')
                    ax1.set_facecolor('none') 
                    # ax1.spines['bottom'].set_position(('data', -20))
                    ax1.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([]) 
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-10, 3))
                    
                    ax1.set_title('FeS',font2,x=0.6, y = -0.1)


                    site2 = structure[b_atomnum2-1]
                    print (site2)
                    ax2 = plt.subplot(2,9,10)
                    c2 = complete_dos.get_site_spd_dos(site2)
                    total20 = c2[OrbitalType.s].densities[Spin.down] + c2[OrbitalType.p].densities[Spin.down] + c2[OrbitalType.d].densities[Spin.down]
                    tatal2 = c2[OrbitalType.s].densities[Spin.up] + c2[OrbitalType.p].densities[Spin.up] + c2[OrbitalType.d].densities[Spin.up]
                    line4, = ax2.plot(-tatal2, dosrun.tdos.energies , color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    line5, = ax2.plot(total20, dosrun.tdos.energies , color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    line6, = ax2.plot(-c2[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies , linewidth=1,color = 'orange')
                    line7, = ax2.plot(c2[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies , linewidth=1,color = 'orange')
                    linef2 = plt.axhline(y=dosrun.efermi,xmin=0.2, xmax=1, color = 'grey',linewidth=1,alpha=0.7)
                    linef2.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax2.spines['right'].set_color('none') 
                    ax2.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax2.spines['bottom'].set_color('none')
                    ax2.set_facecolor('none') 
                    # ax1.spines['bottom'].set_position(('data', -20))
                    ax2.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-10, 3))
                    ax2.set_title('FeS',font2,x=0.6, y = -0.1)



                    site3 = structure[b_atomnum3-1]
                    ax3 = plt.subplot(2,9,15)
                    c3 = complete_dos.get_site_spd_dos(site3)
                    total30 = c3[OrbitalType.s].densities[Spin.down] + c3[OrbitalType.p].densities[Spin.down] + c3[OrbitalType.d].densities[Spin.down]
                    tatal3 = c3[OrbitalType.s].densities[Spin.up] + c3[OrbitalType.p].densities[Spin.up] + c3[OrbitalType.d].densities[Spin.up]
                    line8, = ax3.plot(-tatal3, dosrun.tdos.energies , color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    line9, = ax3.plot(total30, dosrun.tdos.energies , color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    line10, = ax3.plot(-c3[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies , linewidth=1,color = 'orange')
                    line11, = ax3.plot(c3[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies , linewidth=1,color = 'orange')
                    linef3 = plt.axhline(y=dosrun.efermi,xmin=0.2, xmax=1, color = 'grey',linewidth=1,alpha=0.7)
                    Fefemi = dosrun.efermi
                    linef3.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax3.spines['right'].set_color('none') 
                    ax3.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax3.spines['bottom'].set_color('none')
                    ax3.set_facecolor('none') 
                    # ax1.spines['bottom'].set_position(('data', -20))
                    ax3.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-10, 3))
                    ax3.set_title('FeS',font2,x=0.6, y = -0.1)
                bFefemi = Fefemi
                


                    # plt.xlabel('Density of states' ,font2)
                    # ax1.ylabel('E-${E_f}$  /  eV' ,font2,160)
                    # ax1.ylabel('Energy  /  eV' ,font2,x = 0.1,xycoords=ax1.transax1es,)
                    # ax1.annotate("Energy  /  eV", xy=(-0.05, 0.3), rotation=90,xycoords=ax1.transax1es,fontsize=20,family='Times New Roman',weight='bold')
                    # ax1.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                    # ax1.annotate("α", xy=(0.43, 0.95), xycoords=ax1.transax1es,fontsize=20,family='Times New Roman',weight='bold')
                    # ax1.annotate("β", xy=((0.55, 0.95)), xycoords=ax1.transax1es,fontsize=20,family='Times New Roman',weight='bold')
                                  
                if 'mol' in name:
                    path = os.path.join(self.dire, name)
                    os.chdir(path)
                    print (os.getcwd())
                    dosrun=Vasprun("./vasprun.xml")
                    complete_dos = dosrun.complete_dos
                    structure=complete_dos.structure
                    spd_dos = dosrun.complete_dos.get_spd_dos()
                    complete_dos = dosrun.complete_dos
                    # print(complete_dos)
                    structure=complete_dos.structure
                         
                    site4 = structure[m_atomnum-1]
                    ax4 = plt.subplot(2,9,9)
                    c4 = complete_dos.get_site_spd_dos(site4)
                    mefermi = bFefemi - dosrun.efermi
                    print (mefermi)
                    mtatal0 = c4[OrbitalType.s].densities[Spin.down] + c4[OrbitalType.p].densities[Spin.down] + c4[OrbitalType.d].densities[Spin.down]
                    mtatal = c4[OrbitalType.s].densities[Spin.up] + c4[OrbitalType.p].densities[Spin.up] + c4[OrbitalType.d].densities[Spin.up]
                    mline1, = ax4.plot(-mtatal, dosrun.tdos.energies+mefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    mline2, = ax4.plot(mtatal0, dosrun.tdos.energies +mefermi, label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    mline3, = ax4.plot(-c4[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies +mefermi, linewidth=1,color = 'g')
                    mline4, = ax4.plot(c4[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies +mefermi, linewidth=1,color = 'g')
                    mlinef1 = plt.axhline(y=dosrun.efermi+mefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)

                    mlinef1.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax4.spines['right'].set_color('none') 
                    ax4.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax4.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax4.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-10, 3))
                    ax4.set_title('O$_2$',font2,x=0.6, y = -0.1)


                    ax5 = plt.subplot(2,9,13)
                    mline5, = ax5.plot(-mtatal, dosrun.tdos.energies+mefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    mline6, = ax5.plot(mtatal0, dosrun.tdos.energies +mefermi, label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    mline7, = ax5.plot(-c4[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies+mefermi , linewidth=1,color = 'g')
                    mline8, = ax5.plot(c4[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies +mefermi, linewidth=1,color = 'g')
                    mlinef2 = plt.axhline(y=dosrun.efermi+mefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    mlinef2.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax5.spines['right'].set_color('none') 
                    ax5.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax5.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax5.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-10, 3))
                    ax5.set_title('O$_2$',font2,x=0.6, y = -0.1)

                    ax6 = plt.subplot(2,9,18)
                    mline5, = ax6.plot(-mtatal, dosrun.tdos.energies+mefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    mline6, = ax6.plot(mtatal0, dosrun.tdos.energies+mefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    mline7, = ax6.plot(-c4[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies+mefermi , linewidth=1,color = 'g')
                    mline8, = ax6.plot(c4[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies +mefermi, linewidth=1,color = 'g')
                    mlinef3 = plt.axhline(y=dosrun.efermi+mefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    mlinef3.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax6.spines['right'].set_color('none') 
                    ax6.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax6.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax6.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-10, 3))
                    ax6.set_title('O$_2$',font2,x=0.6, y = -0.1)
                   
                #                 #plt.xlabel('Density of states' ,font2)
                #                 # ax2.ylabel('E-${E_f}$  /  eV' ,font2,160)
                #                 # ax2.ylabel('Energy  /  eV' ,font2,x = 0.1,xycoords=ax2.transax2es,)
                #                 # ax2.annotate("Energy  /  eV", xy=(-0.05, 0.3), rotation=90,xycoords=ax2.transax2es,fontsize=20,family='Times New Roman',weight='bold')
                #                 # ax2.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                #                 # ax2.annotate("α", xy=(0.43, 0.95), xycoords=ax2.transax2es,fontsize=20,family='Times New Roman',weight='bold')
                #                 # ax2.annotate("β", xy=((0.55, 0.95)), xycoords=ax2.transax2es,fontsize=20,family='Times New Roman',weight='bold')
                #                 ax2.set_facecolor('none')
                #                 #空的氧气重复1

                            
                if 'after' in name:
                    path = os.path.join(self.dire, name)
                    os.chdir(path)
                    print (os.getcwd())
                    dosrun=Vasprun("./vasprun.xml")
                    complete_dos = dosrun.complete_dos
                    structure=complete_dos.structure
                    spd_dos = dosrun.complete_dos.get_spd_dos()
                    complete_dos = dosrun.complete_dos
                    # print(complete_dos)
                    structure=complete_dos.structure
                    bmefermi = bFefemi - dosrun.efermi
                    print (mefermi)
                    

                    ax7 = plt.subplot(2,9,7)
                    site5 = structure[a_atomnum1-1]
                    c5 = complete_dos.get_site_spd_dos(site5)
                    site6 = structure[am_atomnum1-1]
                    c6 = complete_dos.get_site_spd_dos(site6)
                    amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    atatal0 = c5[OrbitalType.s].densities[Spin.down] + c5[OrbitalType.p].densities[Spin.down] + c5[OrbitalType.d].densities[Spin.down]
                    atatal = c5[OrbitalType.s].densities[Spin.up] + c5[OrbitalType.p].densities[Spin.up] + c5[OrbitalType.d].densities[Spin.up]
                    aline0, = ax7.plot(-atatal-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    aline1, = ax7.plot(atatal0+amotatal0, dosrun.tdos.energies +bmefermi, label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    aline2, = ax7.plot(-c5[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')
                    aline3 = ax7.plot(c5[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')#
                    # site6 = structure[am_atomnum1-1]
                    # c6 = complete_dos.get_site_spd_dos(site6)
                    # # amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    # # amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    # amline0, = ax7.plot(-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    # amline1, = ax7.plot(amotatal0, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    amline2, = ax7.plot(-c6[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g')
                    amline3 = ax7.plot(c6[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g') 
                    alinef3 = plt.axhline(y=dosrun.efermi+bmefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    alinef3.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax7.spines['right'].set_color('none') 
                    ax7.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax7.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax7.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-10, 3))
                    ax7.set_title('O$_{(1)}$\nFeS/O$_2$',font2,y = -0.15)



                    ax8 = plt.subplot(2,9,8)
                    site5 = structure[a_atomnum1-1]
                    c5 = complete_dos.get_site_spd_dos(site5)
                    site7 = structure[am_atomnum2-1]
                    c7 = complete_dos.get_site_spd_dos(site7)
                    amotatal0 = c7[OrbitalType.s].densities[Spin.down] + c7[OrbitalType.p].densities[Spin.down] + c7[OrbitalType.d].densities[Spin.down]
                    amotatal = c7[OrbitalType.s].densities[Spin.up] + c7[OrbitalType.p].densities[Spin.up] + c7[OrbitalType.d].densities[Spin.up]
                    atata20 = c5[OrbitalType.s].densities[Spin.down] + c5[OrbitalType.p].densities[Spin.down] + c5[OrbitalType.d].densities[Spin.down]
                    atata2 = c5[OrbitalType.s].densities[Spin.up] + c5[OrbitalType.p].densities[Spin.up] + c5[OrbitalType.d].densities[Spin.up]
                    aline7, = ax8.plot(-atata2-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    aline4, = ax8.plot(atata20+amotatal0, dosrun.tdos.energies +bmefermi, label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    aline5, = ax8.plot(-c5[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')
                    aline6 = ax8.plot(c5[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')#
                    # site7 = structure[am_atomnum2-1]
                    # c7 = complete_dos.get_site_spd_dos(site7)
                    # # amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    # # amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    # amline0, = ax8.plot(-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    # amline1, = ax8.plot(amotatal0, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    amline4, = ax8.plot(-c7[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g')
                    amline5 = ax8.plot(c7[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g') 
                    alinef3 = plt.axhline(y=dosrun.efermi+bmefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    alinef3.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax8.spines['right'].set_color('none') 
                    ax8.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax8.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax8.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-10, 3))
                    ax8.set_title('O$_{(2)}$\nFeS/O$_2$',font2,y = -0.15)


                    ax7 = plt.subplot(2,9,11)
                    site5 = structure[a_atomnum2-1]
                    c5 = complete_dos.get_site_spd_dos(site5)
                    site6 = structure[am_atomnum1-1]
                    c6 = complete_dos.get_site_spd_dos(site6)
                    amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    atatal0 = c5[OrbitalType.s].densities[Spin.down] + c5[OrbitalType.p].densities[Spin.down] + c5[OrbitalType.d].densities[Spin.down]
                    atatal = c5[OrbitalType.s].densities[Spin.up] + c5[OrbitalType.p].densities[Spin.up] + c5[OrbitalType.d].densities[Spin.up]
                    aline0, = ax7.plot(-atatal-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    aline1, = ax7.plot(atatal0+amotatal0, dosrun.tdos.energies +bmefermi, label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    aline2, = ax7.plot(-c5[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')
                    aline3 = ax7.plot(c5[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')#
                    # site6 = structure[am_atomnum1-1]
                    # c6 = complete_dos.get_site_spd_dos(site6)
                    # # amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    # # amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    # amline0, = ax7.plot(-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    # amline1, = ax7.plot(amotatal0, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    amline2, = ax7.plot(-c6[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g')
                    amline3 = ax7.plot(c6[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g') 
                    alinef3 = plt.axhline(y=dosrun.efermi+bmefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    alinef3.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax7.spines['right'].set_color('none') 
                    ax7.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax7.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax7.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-10, 3))
                    ax7.set_title('O$_{(1)}$\nFeS/O$_2$',font2,y = -0.15)

                    ax8 = plt.subplot(2,9,12)
                    site5 = structure[a_atomnum2-1]
                    c5 = complete_dos.get_site_spd_dos(site5)
                    site7 = structure[am_atomnum2-1]
                    c7 = complete_dos.get_site_spd_dos(site7)
                    amotatal0 = c7[OrbitalType.s].densities[Spin.down] + c7[OrbitalType.p].densities[Spin.down] + c7[OrbitalType.d].densities[Spin.down]
                    amotatal = c7[OrbitalType.s].densities[Spin.up] + c7[OrbitalType.p].densities[Spin.up] + c7[OrbitalType.d].densities[Spin.up]
                    atata20 = c5[OrbitalType.s].densities[Spin.down] + c5[OrbitalType.p].densities[Spin.down] + c5[OrbitalType.d].densities[Spin.down]
                    atata2 = c5[OrbitalType.s].densities[Spin.up] + c5[OrbitalType.p].densities[Spin.up] + c5[OrbitalType.d].densities[Spin.up]
                    aline7, = ax8.plot(-atata2-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    aline4, = ax8.plot(atata20+amotatal0, dosrun.tdos.energies +bmefermi, label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    aline5, = ax8.plot(-c5[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')
                    aline6 = ax8.plot(c5[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')#
                    # site7 = structure[am_atomnum2-1]
                    # c7 = complete_dos.get_site_spd_dos(site7)
                    # # amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    # # amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    # amline0, = ax8.plot(-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    # amline1, = ax8.plot(amotatal0, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    amline4, = ax8.plot(-c7[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g')
                    amline5 = ax8.plot(c7[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g') 
                    alinef3 = plt.axhline(y=dosrun.efermi+bmefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    alinef3.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax8.spines['right'].set_color('none') 
                    ax8.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax8.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax8.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-10, 3))
                    ax8.set_title('O$_{(2)}$\nFeS/O$_2$',font2,y = -0.15)


                    ax7 = plt.subplot(2,9,16)
                    site5 = structure[a_atomnum3-1]
                    c5 = complete_dos.get_site_spd_dos(site5)
                    site6 = structure[am_atomnum1-1]
                    c6 = complete_dos.get_site_spd_dos(site6)
                    amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    atatal0 = c5[OrbitalType.s].densities[Spin.down] + c5[OrbitalType.p].densities[Spin.down] + c5[OrbitalType.d].densities[Spin.down]
                    atatal = c5[OrbitalType.s].densities[Spin.up] + c5[OrbitalType.p].densities[Spin.up] + c5[OrbitalType.d].densities[Spin.up]
                    aline0, = ax7.plot(-atatal-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    aline1, = ax7.plot(atatal0+amotatal0, dosrun.tdos.energies +bmefermi, label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    aline2, = ax7.plot(-c5[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')
                    aline3 = ax7.plot(c5[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')#
                    # site6 = structure[am_atomnum1-1]
                    # c6 = complete_dos.get_site_spd_dos(site6)
                    # # amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    # # amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    # amline0, = ax7.plot(-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    # amline1, = ax7.plot(amotatal0, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    amline2, = ax7.plot(-c6[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g')
                    amline3 = ax7.plot(c6[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g') 
                    alinef3 = plt.axhline(y=dosrun.efermi+bmefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    alinef3.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax7.spines['right'].set_color('none') 
                    ax7.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax7.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax7.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-10, 3))
                    ax7.set_title('O$_{(1)}$\nFeS/O$_2$',font2,y = -0.15)

                    ax8 = plt.subplot(2,9,17)
                    site5 = structure[a_atomnum3-1]
                    c5 = complete_dos.get_site_spd_dos(site5)
                    site7 = structure[am_atomnum2-1]
                    c7 = complete_dos.get_site_spd_dos(site7)
                    amotatal0 = c7[OrbitalType.s].densities[Spin.down] + c7[OrbitalType.p].densities[Spin.down] + c7[OrbitalType.d].densities[Spin.down]
                    amotatal = c7[OrbitalType.s].densities[Spin.up] + c7[OrbitalType.p].densities[Spin.up] + c7[OrbitalType.d].densities[Spin.up]
                    atata20 = c5[OrbitalType.s].densities[Spin.down] + c5[OrbitalType.p].densities[Spin.down] + c5[OrbitalType.d].densities[Spin.down]
                    atata2 = c5[OrbitalType.s].densities[Spin.up] + c5[OrbitalType.p].densities[Spin.up] + c5[OrbitalType.d].densities[Spin.up]
                    aline7, = ax8.plot(-atata2-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    aline4, = ax8.plot(atata20+amotatal0, dosrun.tdos.energies +bmefermi, label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    aline5, = ax8.plot(-c5[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')
                    aline6 = ax8.plot(c5[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')#
                    # site7 = structure[am_atomnum2-1]
                    # c7 = complete_dos.get_site_spd_dos(site7)
                    # amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    # amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    # amline0, = ax8.plot(-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    # amline1, = ax8.plot(amotatal0, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    amline4, = ax8.plot(-c7[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g')
                    amline5 = ax8.plot(c7[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g') 
                    alinef3 = plt.axhline(y=dosrun.efermi+bmefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    alinef3.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax8.spines['right'].set_color('none') 
                    ax8.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax8.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax8.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-10, 3))
                    ax8.set_title('O$_{(2)}$\nFeS/O$_2$',font2,y = -0.15)
        fig.legend([aline0, mline3, line11],['Total DOS','O$_{2p}$','Fe$_{3d}$'], loc='upper right', bbox_to_anchor=(0.49, 0.5),frameon=True, edgecolor='none', fontsize=20,facecolor='none')

        fig.text(0.54, 0.85, "Fe$_{(1)}$:", fontsize=25,family='Times New Roman',weight='bold')
        fig.text(0.1, 0.45, "Fe$_{(2)}$:", fontsize=25,family='Times New Roman',weight='bold')
        fig.text(0.54, 0.45, "Fe$_{(3)}$:", fontsize=25,family='Times New Roman',weight='bold')
        os.chdir(self.dire)
        print (os.getcwd())
        plt.savefig('1.png',bbox_inches='tight', transparent=True,dpi=500,format='png')
        plt.show()            #设置一个用作存储输入文件的名称


    def absorb_site_spd_dos_mirror_1(self,miller_index_1,num1,b_atomnum1 =1,b_atomnum2 =2,b_atomnum3 =3,m_atomnum =1,a_atomnum1 = 1,a_atomnum2 = 1,a_atomnum3 = 1,am_atomnum1 = 1,am_atomnum2 = 1):
        import os
        from pymatgen import Element
        from pymatgen.io.vasp import Vasprun  # 读取vasp作业(vasprun.xml)
        from pymatgen.io.vasp import Vasprun, BSVasprun
        from pymatgen.electronic_structure.plotter import DosPlotter
        from pymatgen.electronic_structure.core import Spin, OrbitalType,Orbital
        import matplotlib.pyplot as plt
        from pymatgen.io.vasp.inputs import Poscar
        from pymatgen.io.vasp.sets import MPRelaxSet
        from pymatgen.io.cif import CifWriter
        from pymatgen.analysis.adsorption import AdsorbateSiteFinder, reorient_z, plot_slab
        from pymatgen.core.surface import Slab, SlabGenerator, generate_all_slabs, Structure, Lattice, ReconstructionGenerator
        import os
        import shutil
        from pymatgen.io.vasp import Poscar
        import numpy as np
        import cv2
        font2 = {'family' : 'Times New Roman','fontsize':'20' , 'weight' : 'bold',}
        font1 = {'family' : 'Times New Roman','weight' : 'bold',} 
        # fig= plt.subplots()
        fig=plt.figure(figsize=(16, 13))
        
        for dirpath, dirnames, filenames in os.walk(self.dire):
            

            for name in dirnames:
                if'note0' in str(name):  
                    path = os.path.join(self.dire, name)
                    os.chdir(path)
                    print (os.getcwd())
                    img = cv2.imread(num1)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # 注意这行。
                    # rect1 = [-0.1, 0.45, 0.85, 0.4]#[左, 下, 宽, 高] 规定的矩形区域 （全部是0~1之间的数，表示比例）
                    ax0=fig.add_subplot(2,2,1)
                    # ax0= plt.axes(rect1)
                    plt.imshow(img)
                    ax0.spines['right'].set_color('none') 
                    ax0.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax0.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax0.spines['left'].set_color('none')
                    arrowprops = dict(arrowstyle = "->",connectionstyle = "angle,angleA=0,angleB=90,rad=10")
                    bbox = dict(boxstyle="round", fc="0.8")
                    x1 = 620
                    y1 = 700
                    ax0.annotate("Fe$_{(1)}$", xy=(x1, y1),xytext=(x1-400, y1-400), bbox=bbox, arrowprops=arrowprops,fontsize=30,family='Times New Roman',weight='bold')
                    x2 = 700
                    y2 = 750
                    ax0.annotate("Fe$_{(2)}$", xy=(x2, y2),xytext=(x2-100, y2+350), bbox=bbox, arrowprops=arrowprops ,fontsize=30,family='Times New Roman',weight='bold')
                    x3 = 785
                    y3 = 680
                    ax0.annotate("Fe$_{(3)}$", xy=(x3, y3),xytext=(x3+200, y3+200), bbox=bbox, arrowprops=arrowprops,fontsize=30,family='Times New Roman',weight='bold')
                    x4 = 700
                    y4 = 680
                    ax0.annotate("O$_{(1)}$", xy=(x4, y4),xytext=(x4+200, y4-60), bbox=bbox, arrowprops=arrowprops,fontsize=30,family='Times New Roman',weight='bold')
                    x5 = 700
                    y5 = 685
                    ax0.annotate("O$_{(2)}$", xy=(x5, y5),xytext=(x5-400, y5+100),bbox=bbox, arrowprops=arrowprops, fontsize=30,family='Times New Roman',weight='bold')
                    # plt.subplots_adjust(left=1, bottom=1, right=1, wspace=1.0,hspace =0)
                    plt.xticks([]),plt.yticks([]) 
                    # #plt.xlim((-3.5, 3.5))3))
                    # plt.ylim((-10, 3))
                    ax0.set_facecolor('none')
                    ax0.set_title('SFeS (001)',font2,y = -0.1)   




                if 'dos0' in name:
                    path = os.path.join(self.dire, name)
                    os.chdir(path)
                    print (os.getcwd())
                    dosrun=Vasprun("./vasprun.xml")
                    complete_dos = dosrun.complete_dos
                    structure=complete_dos.structure
                    spd_dos = dosrun.complete_dos.get_spd_dos()
                    complete_dos = dosrun.complete_dos
                    # print(complete_dos)
                    structure=complete_dos.structure

                    site1 = structure[b_atomnum1-1] 
                    print (site1)
                    ax1=fig.add_subplot(2,9,6)
                    c1 = complete_dos.get_site_spd_dos(site1)
                    total10 = c1[OrbitalType.s].densities[Spin.down] + c1[OrbitalType.p].densities[Spin.down] + c1[OrbitalType.d].densities[Spin.down]
                    tatal = c1[OrbitalType.s].densities[Spin.up] + c1[OrbitalType.p].densities[Spin.up] + c1[OrbitalType.d].densities[Spin.up]
                    line0, = ax1.plot(-tatal, dosrun.tdos.energies , color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    line1, = ax1.plot(total10, dosrun.tdos.energies , color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    line2, = ax1.plot(-c1[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies , linewidth=1,color = 'orange')
                    line3, = ax1.plot(c1[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies , linewidth=1,color = 'orange')#
                    linef1 = plt.axhline(y=dosrun.efermi,xmin=0.2, xmax=1, color = 'grey',linewidth=1,alpha=0.7)
                    linef1.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break

                    ax1.spines['right'].set_color('none') 
                    ax1.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax1.spines['bottom'].set_color('none')
                    ax1.set_facecolor('none') 
                    # ax1.spines['bottom'].set_position(('data', -20))
                    ax1.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([]) 
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-12,1))
                    
                    ax1.set_title('SFeS',font2,x=0.6, y = -0.1)


                    site2 = structure[b_atomnum2-1]
                    print (site2)
                    ax2 = plt.subplot(2,9,10)
                    c2 = complete_dos.get_site_spd_dos(site2)
                    total20 = c2[OrbitalType.s].densities[Spin.down] + c2[OrbitalType.p].densities[Spin.down] + c2[OrbitalType.d].densities[Spin.down]
                    tatal2 = c2[OrbitalType.s].densities[Spin.up] + c2[OrbitalType.p].densities[Spin.up] + c2[OrbitalType.d].densities[Spin.up]
                    line4, = ax2.plot(-tatal2, dosrun.tdos.energies , color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    line5, = ax2.plot(total20, dosrun.tdos.energies , color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    line6, = ax2.plot(-c2[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies , linewidth=1,color = 'orange')
                    line7, = ax2.plot(c2[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies , linewidth=1,color = 'orange')
                    linef2 = plt.axhline(y=dosrun.efermi,xmin=0.2, xmax=1, color = 'grey',linewidth=1,alpha=0.7)
                    linef2.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax2.spines['right'].set_color('none') 
                    ax2.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax2.spines['bottom'].set_color('none')
                    ax2.set_facecolor('none') 
                    # ax1.spines['bottom'].set_position(('data', -20))
                    ax2.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-12,1))
                    ax2.set_title('SFeS',font2,x=0.6, y = -0.1)



                    site3 = structure[b_atomnum3-1]
                    ax3 = plt.subplot(2,9,15)
                    c3 = complete_dos.get_site_spd_dos(site3)
                    total30 = c3[OrbitalType.s].densities[Spin.down] + c3[OrbitalType.p].densities[Spin.down] + c3[OrbitalType.d].densities[Spin.down]
                    tatal3 = c3[OrbitalType.s].densities[Spin.up] + c3[OrbitalType.p].densities[Spin.up] + c3[OrbitalType.d].densities[Spin.up]
                    line8, = ax3.plot(-tatal3, dosrun.tdos.energies , color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    line9, = ax3.plot(total30, dosrun.tdos.energies , color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    line10, = ax3.plot(-c3[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies , linewidth=1,color = 'orange')
                    line11, = ax3.plot(c3[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies , linewidth=1,color = 'orange')
                    linef3 = plt.axhline(y=dosrun.efermi,xmin=0.2, xmax=1, color = 'grey',linewidth=1,alpha=0.7)
                    Fefemi = dosrun.efermi
                    linef3.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax3.spines['right'].set_color('none') 
                    ax3.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax3.spines['bottom'].set_color('none')
                    ax3.set_facecolor('none') 
                    # ax1.spines['bottom'].set_position(('data', -20))
                    ax3.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-12,1))
                    ax3.set_title('SFeS',font2,x=0.6, y = -0.1)
                bFefemi = Fefemi
                


                    # plt.xlabel('Density of states' ,font2)
                    # ax1.ylabel('E-${E_f}$  /  eV' ,font2,160)
                    # ax1.ylabel('Energy  /  eV' ,font2,x = 0.1,xycoords=ax1.transax1es,)
                    # ax1.annotate("Energy  /  eV", xy=(-0.05, 0.3), rotation=90,xycoords=ax1.transax1es,fontsize=20,family='Times New Roman',weight='bold')
                    # ax1.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                    # ax1.annotate("α", xy=(0.43, 0.95), xycoords=ax1.transax1es,fontsize=20,family='Times New Roman',weight='bold')
                    # ax1.annotate("β", xy=((0.55, 0.95)), xycoords=ax1.transax1es,fontsize=20,family='Times New Roman',weight='bold')
                                  
                if 'mol' in name:
                    path = os.path.join(self.dire, name)
                    os.chdir(path)
                    print (os.getcwd())
                    dosrun=Vasprun("./vasprun.xml")
                    complete_dos = dosrun.complete_dos
                    structure=complete_dos.structure
                    spd_dos = dosrun.complete_dos.get_spd_dos()
                    complete_dos = dosrun.complete_dos
                    # print(complete_dos)
                    structure=complete_dos.structure
                         
                    site4 = structure[m_atomnum-1]
                    ax4 = plt.subplot(2,9,9)
                    c4 = complete_dos.get_site_spd_dos(site4)
                    mefermi = bFefemi - dosrun.efermi
                    print (mefermi)
                    mtatal0 = c4[OrbitalType.s].densities[Spin.down] + c4[OrbitalType.p].densities[Spin.down] + c4[OrbitalType.d].densities[Spin.down]
                    mtatal = c4[OrbitalType.s].densities[Spin.up] + c4[OrbitalType.p].densities[Spin.up] + c4[OrbitalType.d].densities[Spin.up]
                    mline1, = ax4.plot(-mtatal, dosrun.tdos.energies+mefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    mline2, = ax4.plot(mtatal0, dosrun.tdos.energies +mefermi, label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    mline3, = ax4.plot(-c4[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies +mefermi, linewidth=1,color = 'g')
                    mline4, = ax4.plot(c4[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies +mefermi, linewidth=1,color = 'g')
                    mlinef1 = plt.axhline(y=dosrun.efermi+mefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)

                    mlinef1.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax4.spines['right'].set_color('none') 
                    ax4.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax4.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax4.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-12,1))
                    ax4.set_title('O$_2$',font2,x=0.6, y = -0.1)


                    ax5 = plt.subplot(2,9,13)
                    mline5, = ax5.plot(-mtatal, dosrun.tdos.energies+mefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    mline6, = ax5.plot(mtatal0, dosrun.tdos.energies +mefermi, label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    mline7, = ax5.plot(-c4[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies+mefermi , linewidth=1,color = 'g')
                    mline8, = ax5.plot(c4[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies +mefermi, linewidth=1,color = 'g')
                    mlinef2 = plt.axhline(y=dosrun.efermi+mefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    mlinef2.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax5.spines['right'].set_color('none') 
                    ax5.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax5.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax5.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-12,1))
                    ax5.set_title('O$_2$',font2,x=0.6, y = -0.1)

                    ax6 = plt.subplot(2,9,18)
                    mline5, = ax6.plot(-mtatal, dosrun.tdos.energies+mefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    mline6, = ax6.plot(mtatal0, dosrun.tdos.energies+mefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    mline7, = ax6.plot(-c4[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies+mefermi , linewidth=1,color = 'g')
                    mline8, = ax6.plot(c4[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies +mefermi, linewidth=1,color = 'g')
                    mlinef3 = plt.axhline(y=dosrun.efermi+mefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    mlinef3.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax6.spines['right'].set_color('none') 
                    ax6.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax6.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax6.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-12,1))
                    ax6.set_title('O$_2$',font2,x=0.6, y = -0.1)
                   
                #                 #plt.xlabel('Density of states' ,font2)
                #                 # ax2.ylabel('E-${E_f}$  /  eV' ,font2,160)
                #                 # ax2.ylabel('Energy  /  eV' ,font2,x = 0.1,xycoords=ax2.transax2es,)
                #                 # ax2.annotate("Energy  /  eV", xy=(-0.05, 0.3), rotation=90,xycoords=ax2.transax2es,fontsize=20,family='Times New Roman',weight='bold')
                #                 # ax2.legend(frameon=True, edgecolor='none', facecolor='none', prop=font1)
                #                 # ax2.annotate("α", xy=(0.43, 0.95), xycoords=ax2.transax2es,fontsize=20,family='Times New Roman',weight='bold')
                #                 # ax2.annotate("β", xy=((0.55, 0.95)), xycoords=ax2.transax2es,fontsize=20,family='Times New Roman',weight='bold')
                #                 ax2.set_facecolor('none')
                #                 #空的氧气重复1

                            
                if 'dos1' in name:
                    path = os.path.join(self.dire, name)
                    os.chdir(path)
                    print (os.getcwd())
                    dosrun=Vasprun("./vasprun.xml")
                    complete_dos = dosrun.complete_dos
                    structure=complete_dos.structure
                    spd_dos = dosrun.complete_dos.get_spd_dos()
                    complete_dos = dosrun.complete_dos
                    # print(complete_dos)
                    structure=complete_dos.structure
                    bmefermi = bFefemi - dosrun.efermi
                    print (mefermi)
                    

                    ax7 = plt.subplot(2,9,7)
                    site5 = structure[a_atomnum1-1]
                    site6 = structure[am_atomnum1-1]
                    c5 = complete_dos.get_site_spd_dos(site5)
                    c6 = complete_dos.get_site_spd_dos(site6)
                    amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    atatal0 = c5[OrbitalType.s].densities[Spin.down] + c5[OrbitalType.p].densities[Spin.down] + c5[OrbitalType.d].densities[Spin.down]
                    atatal = c5[OrbitalType.s].densities[Spin.up] + c5[OrbitalType.p].densities[Spin.up] + c5[OrbitalType.d].densities[Spin.up]
                    aline0, = ax7.plot(-atatal-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    aline1, = ax7.plot(atatal0+amotatal0, dosrun.tdos.energies +bmefermi, label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    aline2, = ax7.plot(-c5[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')
                    aline3 = ax7.plot(c5[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')#
                    
                    
                    # amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    # amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    # amline0, = ax7.plot(-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    # amline1, = ax7.plot(amotatal0, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    amline2, = ax7.plot(-c6[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g')
                    amline3 = ax7.plot(c6[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g') 
                    alinef3 = plt.axhline(y=dosrun.efermi+bmefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    alinef3.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax7.spines['right'].set_color('none') 
                    ax7.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax7.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax7.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-12,1))
                    ax7.set_title('O$_{(1)}$\nSFeS/O$_2$',font2,y = -0.15)



                    ax8 = plt.subplot(2,9,8)
                    site5 = structure[a_atomnum1-1]
                    site7 = structure[am_atomnum2-1]
                    c5 = complete_dos.get_site_spd_dos(site5)
                    c7 = complete_dos.get_site_spd_dos(site7)
                    amotatal0 = c7[OrbitalType.s].densities[Spin.down] + c7[OrbitalType.p].densities[Spin.down] + c7[OrbitalType.d].densities[Spin.down]
                    amotatal = c7[OrbitalType.s].densities[Spin.up] + c7[OrbitalType.p].densities[Spin.up] + c7[OrbitalType.d].densities[Spin.up]
                    atatal20 = c5[OrbitalType.s].densities[Spin.down] + c5[OrbitalType.p].densities[Spin.down] + c5[OrbitalType.d].densities[Spin.down]
                    atatal2 = c5[OrbitalType.s].densities[Spin.up] + c5[OrbitalType.p].densities[Spin.up] + c5[OrbitalType.d].densities[Spin.up]
                    aline7, = ax8.plot(-atatal2-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    aline4, = ax8.plot(atatal20+amotatal0, dosrun.tdos.energies +bmefermi, label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    aline5, = ax8.plot(-c5[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')
                    aline6 = ax8.plot(c5[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')#
                    
                    # c7 = complete_dos.get_site_spd_dos(site7)
                    # amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    # amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    # amline0, = ax8.plot(-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    # amline1, = ax8.plot(amotatal0, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    amline4, = ax8.plot(-c7[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g')
                    amline5 = ax8.plot(c7[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g') 
                    alinef3 = plt.axhline(y=dosrun.efermi+bmefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    alinef3.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax8.spines['right'].set_color('none') 
                    ax8.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax8.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax8.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-12,1))
                    ax8.set_title('O$_{(2)}$\nSFeS/O$_2$',font2,y = -0.15)


                    ax7 = plt.subplot(2,9,11)
                    site5 = structure[a_atomnum2-1]
                    site6 = structure[am_atomnum1-1]
                    c5 = complete_dos.get_site_spd_dos(site5)
                    c6 = complete_dos.get_site_spd_dos(site6)
                    amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    atatal0 = c5[OrbitalType.s].densities[Spin.down] + c5[OrbitalType.p].densities[Spin.down] + c5[OrbitalType.d].densities[Spin.down]
                    atatal = c5[OrbitalType.s].densities[Spin.up] + c5[OrbitalType.p].densities[Spin.up] + c5[OrbitalType.d].densities[Spin.up]
                    aline0, = ax7.plot(-atatal-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    aline1, = ax7.plot(atatal0+amotatal0, dosrun.tdos.energies +bmefermi, label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    aline2, = ax7.plot(-c5[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')
                    aline3 = ax7.plot(c5[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')#
                    
                    
                    # amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    # amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    # amline0, = ax7.plot(-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    # amline1, = ax7.plot(amotatal0, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    amline2, = ax7.plot(-c6[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g')
                    amline3 = ax7.plot(c6[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g') 
                    alinef3 = plt.axhline(y=dosrun.efermi+bmefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    alinef3.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax7.spines['right'].set_color('none') 
                    ax7.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax7.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax7.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-12,1))
                    ax7.set_title('O$_{(1)}$\nSFeS/O$_2$',font2,y = -0.15)

                    ax8 = plt.subplot(2,9,12)
                    site5 = structure[a_atomnum2-1]
                    site7 = structure[am_atomnum2-1]
                    c5 = complete_dos.get_site_spd_dos(site5)
                    c7 = complete_dos.get_site_spd_dos(site7)
                    amotatal0 = c7[OrbitalType.s].densities[Spin.down] + c7[OrbitalType.p].densities[Spin.down] + c7[OrbitalType.d].densities[Spin.down]
                    amotatal = c7[OrbitalType.s].densities[Spin.up] + c7[OrbitalType.p].densities[Spin.up] + c7[OrbitalType.d].densities[Spin.up]
                    atata20 = c5[OrbitalType.s].densities[Spin.down] + c5[OrbitalType.p].densities[Spin.down] + c5[OrbitalType.d].densities[Spin.down]
                    atata2 = c5[OrbitalType.s].densities[Spin.up] + c5[OrbitalType.p].densities[Spin.up] + c5[OrbitalType.d].densities[Spin.up]
                    aline7, = ax8.plot(-atata2-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    aline4, = ax8.plot(atata20+amotatal0, dosrun.tdos.energies +bmefermi, label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    aline5, = ax8.plot(-c5[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')
                    aline6 = ax8.plot(c5[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')#
                    
                    
                    # 
                    # amline0, = ax8.plot(-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    # amline1, = ax8.plot(amotatal0, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    amline4, = ax8.plot(-c7[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g')
                    amline5 = ax8.plot(c7[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g') 
                    alinef3 = plt.axhline(y=dosrun.efermi+bmefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    alinef3.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax8.spines['right'].set_color('none') 
                    ax8.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax8.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax8.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-12,1))
                    ax8.set_title('O$_{(2)}$\nSFeS/O$_2$',font2,y = -0.15)


                    ax7 = plt.subplot(2,9,16)
                    site5 = structure[a_atomnum3-1]
                    site6 = structure[am_atomnum1-1]
                    c5 = complete_dos.get_site_spd_dos(site5)
                    c6 = complete_dos.get_site_spd_dos(site6)
                    amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    atatal0 = c5[OrbitalType.s].densities[Spin.down] + c5[OrbitalType.p].densities[Spin.down] + c5[OrbitalType.d].densities[Spin.down]
                    atatal = c5[OrbitalType.s].densities[Spin.up] + c5[OrbitalType.p].densities[Spin.up] + c5[OrbitalType.d].densities[Spin.up]
                    aline0, = ax7.plot(-atatal-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    aline1, = ax7.plot(atatal0+amotatal0, dosrun.tdos.energies +bmefermi, label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    aline2, = ax7.plot(-c5[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')
                    aline3 = ax7.plot(c5[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')#
                    
                    # c6 = complete_dos.get_site_spd_dos(site6)
                    # amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    # amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    # amline0, = ax7.plot(-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    # amline1, = ax7.plot(amotatal0, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    amline2, = ax7.plot(-c6[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g')
                    amline3 = ax7.plot(c6[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g') 
                    alinef3 = plt.axhline(y=dosrun.efermi+bmefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    alinef3.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax7.spines['right'].set_color('none') 
                    ax7.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax7.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax7.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-12,1))
                    ax7.set_title('O$_{(1)}$\nSFeS/O$_2$',font2,y = -0.15)

                    ax8 = plt.subplot(2,9,17)
                    site5 = structure[a_atomnum3-1]
                    site7 = structure[am_atomnum2-1]
                    c5 = complete_dos.get_site_spd_dos(site5)
                    c7 = complete_dos.get_site_spd_dos(site7)
                    amotatal0 = c7[OrbitalType.s].densities[Spin.down] + c7[OrbitalType.p].densities[Spin.down] + c7[OrbitalType.d].densities[Spin.down]
                    amotatal = c7[OrbitalType.s].densities[Spin.up] + c7[OrbitalType.p].densities[Spin.up] + c7[OrbitalType.d].densities[Spin.up]
                    atata20 = c5[OrbitalType.s].densities[Spin.down] + c5[OrbitalType.p].densities[Spin.down] + c5[OrbitalType.d].densities[Spin.down]
                    atata2 = c5[OrbitalType.s].densities[Spin.up] + c5[OrbitalType.p].densities[Spin.up] + c5[OrbitalType.d].densities[Spin.up]
                    aline7, = ax8.plot(-atata2-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    aline4, = ax8.plot(atata20+amotatal0, dosrun.tdos.energies +bmefermi, label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    aline5, = ax8.plot(-c5[OrbitalType.d].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')
                    aline6 = ax8.plot(c5[OrbitalType.d].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'orange')#
                    
                    # c7 = complete_dos.get_site_spd_dos(site7)
                    # amotatal0 = c6[OrbitalType.s].densities[Spin.down] + c6[OrbitalType.p].densities[Spin.down] + c6[OrbitalType.d].densities[Spin.down]
                    # amotatal = c6[OrbitalType.s].densities[Spin.up] + c6[OrbitalType.p].densities[Spin.up] + c6[OrbitalType.d].densities[Spin.up]
                    # amline0, = ax8.plot(-amotatal, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3)
                    # amline1, = ax8.plot(amotatal0, dosrun.tdos.energies+bmefermi , label='Total DOS',color = 'cornflowerblue',linewidth=8,alpha=0.3,)
                    amline4, = ax8.plot(-c7[OrbitalType.p].densities[Spin.up], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g')
                    amline5 = ax8.plot(c7[OrbitalType.p].densities[Spin.down], dosrun.tdos.energies+bmefermi , linewidth=1,color = 'g') 
                    alinef3 = plt.axhline(y=dosrun.efermi+bmefermi,xmin=0.1, xmax=0.9, color = 'grey',linewidth=1,alpha=0.7)
                    alinef3.set_dashes([5, 5, 5, 5]) # 2pt line, 2pt break, 10pt line, 2pt break
                    ax8.spines['right'].set_color('none') 
                    ax8.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
                    ax8.spines['bottom'].set_color('none') 
                    # ax2.spines['bottom'].set_position(('data', -20))
                    ax8.spines['left'].set_position(('data', 0))
                    plt.xticks([]),plt.yticks([])
                    #plt.xlim((-3.5, 3.5))
                    plt.ylim((-12,1))
                    ax8.set_title('O$_{(2)}$\nSFeS/O$_2$',font2,y = -0.15)
        fig.legend([aline0, mline3, line11],['Total DOS','O$_{2p}$','Fe$_{3d}$'], loc='upper right', bbox_to_anchor=(0.49, 0.5),frameon=True, edgecolor='none', fontsize=20,facecolor='none')

        fig.text(0.54, 0.85, "Fe$_{(1)}$:", fontsize=25,family='Times New Roman',weight='bold')
        fig.text(0.1, 0.45, "Fe$_{(2)}$:", fontsize=25,family='Times New Roman',weight='bold')
        fig.text(0.54, 0.45, "Fe$_{(3)}$:", fontsize=25,family='Times New Roman',weight='bold')
        os.chdir(self.dire)
        print (os.getcwd())
        plt.savefig('1.png',bbox_inches='tight', transparent=True,dpi=500,format='png')
        plt.show()            #设置一个用作存储输入文件的名称
