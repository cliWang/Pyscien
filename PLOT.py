class Plot():
    def __init__(self,dire):

        self.dire = dire

    def Plotterfill(self,dir1,dir2,dir3,dir4):
        import os
        import matplotlib.pyplot as plt
        import pandas as pd
        from scipy.optimize import curve_fit
        import numpy as np
        from scipy.signal import savgol_filter
        from scipy.interpolate import make_interp_spline
        from scipy.interpolate import interp1d

        # from scipy.interpolate import spline
        font1 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'30'
        }

        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        os.chdir(self.dire)

        df1 = pd.read_excel('phase.xlsx')
        a1=df1['wt% water']
        # b1=df1[dir1]


        # df2 = pd.read_excel(dir2+'.xlsx')
        a2=df1['wt% bassanite']
        # b2=df2[dir2]

        # df3 = pd.read_excel(dir3+'.xlsx')
        # a3=df3['Distance']
        # b3=df3[dir3]

        # df4 = pd.read_excel(dir4+'.xlsx')
        # a4=df4['Distance']
        # b4=df4[dir4]
        f = interp1d(a1, a2)
        f2 = interp1d(a1, a2, kind='cubic')
        xnew = np.linspace(a1.min(),a1.max(), num=200, endpoint=True)


        fig,ax = plt.subplots(figsize=(12,9),dpi=300)
        ax.scatter(a1, a2, alpha=0.85, marker='o',color='', s=80,edgecolors='red',label='Experiment',linewidth=2)
        ax.plot(xnew, f2(xnew), alpha=0.85,linestyle="-",linewidth=2,label='Fitting curve')
        # plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
        ax.fill_between(xnew, f2(xnew), alpha=.15,ec="none",lw=.1,zorder=2) 
        # plt.plot(a2, b2, alpha=0.85,linestyle="-",label='O - H',linewidth=2)
        # plt.fill_between(a2, b2, alpha=.15,ec="none",lw=.1,zorder=2)
        # plt.plot(a3, b3, alpha=0.85,linestyle="-",label='H - H',linewidth=2)
        # plt.fill_between(a3, b3, alpha=.15,ec="none",lw=.1,zorder=2)
        # # plt.plot(a4, b4, alpha=0.85,linestyle="-",label='Ca - H',linewidth=2)
        # # plt.fill_between(a4, b4, alpha=.15,ec="none",lw=.1,zorder=2)
        ax.tick_params(labelsize=24)

        ax.set_xlabel(r"wt% water",fontsize=36,family='Times New Roman')
        ax.set_ylabel(r'wt% bassanite',fontsize=36,family='Times New Roman')
        # 
        

        # ax.invert_xaxis() 
        # ax.spines['top'].set_visible(False) #去掉上边框
        # # ax.spines['bottom'].set_visible(False) #去掉下边框
        # ax.spines['left'].set_visible(False) #去掉左边框
        # ax.spines['right'].set_visible(False) #去掉右边框

        # ax.xlim((5,80))
        # 以下是图片的格式设置
        # 设置横纵坐标的名称以及对应字体格式
        font2 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'x-large'
        }

        # ax.xlim((0,12))
        ax.set_ylim((-3,103))
        ax.set_xlim((0,30))
        #不显示Y轴的刻度
        # ax.set_yticks([])
        ax.legend(prop=font1,frameon=False)
        #设置图例对应格式和字体
        # auto_adjust_subplotpars(fig, renderer,(2,3) , [1,1,1,1,1,1], (2,3,1), ax_bbox_list=None, pad=1.08, h_pad=None, w_pad=None, rect=None)
        # plt.subplots_adjust(wspace =0.3,hspace =0.3 )
        #存储为
        plt.savefig('phase.png', transparent=True,format='png')#指定分辨率,边界紧，背景透明
        plt.show()
        print ('congratulate！！！')




    def Plotterfitting(self,dirr):
        import os
        import matplotlib.pyplot as plt
        import pandas as pd
        from scipy.optimize import curve_fit
        import numpy as np
        from scipy.signal import savgol_filter
        from scipy.interpolate import make_interp_spline

        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        os.chdir(self.dire)
        df = pd.read_excel(dirr)

        a=df['time'].astype("float")
        b=df['FeSvalue']
        c=df['FeSerror']
        d=df['SFeSvalue']
        f=df['SFeSerror']

        fig, ax = plt.subplots()
        # ax.scatter(a, b,label='FeS')
  # 2pt line, 2pt break, 10pt line, 2pt break

        

        ax.errorbar(a, b, elinewidth=2,yerr=c, ecolor='r', fmt='o',c='y',label='FeS')
        ax.errorbar(a, d, elinewidth=2,yerr=f, fmt='^',ecolor='r',c='b',label='SFeS')




        xa = np.linspace(a.min(), a.max(), 300)
        yb = make_interp_spline(a, b)(xa)
        def func(x,k):
            return np.exp(-x*k)
        popt, pcov = curve_fit(func, xa, yb)
        k=popt[0] # popt里面是拟合系数，读者可以自己help其用法
        yvals=func(xa,k)  
        print(k)  
        # x_smooth = np.linspace(x.min(), a.max(), 300)
        # y_smooth = make_interp_spline(a, yvals)(x_smooth)
        li = k*60
        plot1=plt.plot(xa, yvals, alpha=0.7,linestyle="--",label='k = '+str('%.2f' %li)+' h$^{-1}$ ')


        popt, pcov = curve_fit(func, a, d)
        k=popt[0] # popt里面是拟合系数，读者可以自己help其用法
        yvals=func(a,k)  
        print(k)      
        x_smooth = np.linspace(a.min(), a.max(), 300)
        y_smooth = make_interp_spline(a, yvals)(x_smooth)
        li = k*60
        plot2=plt.plot(x_smooth, y_smooth, alpha=0.7,linestyle="--",label='k = '+str('%.2f' %li)+' h$^{-1}$ ')






    def Barchart(self):
        import os
        import matplotlib.pyplot as plt
        import pandas as pd
        from scipy.optimize import curve_fit
        import numpy as np
        from scipy.signal import savgol_filter
        from scipy.interpolate import make_interp_spline

        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        font1 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'30'
        }
        os.chdir(self.dire)
        # df = pd.read_excel(dirr)
        #构造数据
        labels = ['1', '2', '3', '4', '5', '6']
        data_a = [100, 80, 60, 40, 20,0 ]
        data_b = [100, 74, 57,41,22,0]
        # data_c = [12, 20, 24, 17, 16]

        x = np.arange(len(labels))
        width = .25

        plt.rcParams['font.family'] = "Times New Roman"
        #plots
        fig,ax = plt.subplots(figsize=(12,9),dpi=300)
        plt.grid(axis="y",ls='--',lw=0.6,alpha=0.5)
        ax.set_axisbelow(True)
        bar_a = ax.bar(x-width/2, data_a,width,label='True value',color='#130074',ec='black',lw=.5)
        bar_b = ax.bar(x+width/2, data_b, width,label='Refinement',color='#CB181B',ec='black',lw=.5)
        plt.ylim((-1,105))
        # bar_c = ax.bar(x+width*3/2, data_c,width,label='category_C',color='white',ec='black',lw=.5)

        #定制化设计
        ax.tick_params(axis='x',direction='in',labelsize=24,bottom=False)
        ax.tick_params(axis='y',direction='out',labelsize=24,length=3)
        ax.set_xticks(x)
        ax.set_xticklabels(labels,fontsize=36,family='Times New Roman')
        ax.set_ylabel(r"Bassanite content (%)",fontsize=36,family='Times New Roman')
        ax.set_xlabel(r'Sample index',fontsize=36,family='Times New Roman')
        # ax.set_ylim(bottom=0,top=30)
        # ax.set_yticks(np.arange(0, 50, step=5))

        

        for spine in ['top','right']:
            ax.spines[spine].set_color('none')
            
        # ax.legend(prop=font1,frameon=False)

        text_font = {'size':'14','weight':'bold','color':'black'}
        # ax.text(.03,.93,"(a)",transform = ax.transAxes,fontdict=text_font,zorder=4)
        # ax.text(.87,-.08,'\nVisualization by DataCharm',transform = ax.transAxes,
                # ha='center', va='center',fontsize = 5,color='black',fontweight='bold',family='Times New Roman')
        plt.savefig('bar.png',bbox_inches='tight', transparent=True,dpi=600,format='png')
        plt.show()





    def XRDrefinement(self):
        import os
        import matplotlib.pyplot as plt
        import pandas as pd
        from scipy.optimize import curve_fit
        import numpy as np
        from scipy.signal import savgol_filter
        from scipy.interpolate import make_interp_spline
        import re


        os.chdir(self.dire)

        font1 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'30'
        }


        f=open('bassanite.prf','r')
        alllines=f.readlines()
        f.close()
        a1=[]
        a2=[]
        a3=[]
        a4=[]
        a5=[]
        a6=[]
        for i, eachline in enumerate(alllines):
            if i>2 and '('not in eachline:
                a=eachline
                r=a.split('\t')#分隔符
                rr1=r[0].lstrip().rstrip()
                rr2=r[1].lstrip().rstrip()
                rr3=r[2].lstrip().rstrip()
                rr4=r[3].lstrip().rstrip()
                a1.append(float(rr1))
                a2.append(float(rr2))  
                a3.append(float(rr3))
                a4.append(float(rr4))             

            if '(' in eachline and 'hkl' not in eachline:
                b=eachline
                c=b.split('\t')#分隔符
                cc1=c[0].lstrip().rstrip()
                cc2=c[-3].lstrip().rstrip()
                if float(cc1)<max(a1):
                    a5.append(float(cc1))
                    a6.append(float(cc2))
        

        fig = plt.figure(figsize=(12,9),dpi=300)

        plt.scatter(a1, a2, alpha=0.85, marker='o',color='', s=40,edgecolors='red',label='Yobs',linewidth=2)



        plt.plot(a1, a3, alpha=0.85, label='Ycal',linewidth=2,c='black')



 
        plt.plot(a1, a4, alpha=0.85, label='Yobs-Ycal',linewidth=3,c='blue')
        ve=(min(a2)-max(a4))/3
        if max(a6)+ve >min(a2):
            a6[:] = [x - ve for x in a6] 
            plt.scatter(a5, a6, alpha=0.85, marker="|",s=150,label='Standard',linewidth=2,c='forestgreen')
        else:
            plt.scatter(a5, a6, alpha=0.85, marker="|",s=150,label='Standard',linewidth=2,c='forestgreen')





        plt.xlabel(r"2Theta (Degree)",fontsize=36,family='Times New Roman')
        plt.ylabel(r'Intensity (a.u)',fontsize=36,family='Times New Roman')
        # 
        plt.legend(edgecolor='none', prop=font1,)
        plt.tick_params(labelsize=24)






        dm = pd.DataFrame({'2Theta':a1,'Yobs':a2,'Ycal':a3,'Yobs-Ycal':a4})

        dm.to_excel("Refinement.xlsx")
        de=pd.DataFrame({'2Theta':a5,'(hkl)':a6})
        de.to_excel("Pdf.xlsx")

        # plt.xlim((5,80))
        # 以下是图片的格式设置
        # 设置横纵坐标的名称以及对应字体格式
        font2 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'x-large'
        }

        # plt.xlim((0,12))
        # plt.ylim((0))
        #不显示Y轴的刻度
        plt.yticks([])

        #设置图例对应格式和字体
        # auto_adjust_subplotpars(fig, renderer,(2,3) , [1,1,1,1,1,1], (2,3,1), ax_bbox_list=None, pad=1.08, h_pad=None, w_pad=None, rect=None)
        # plt.subplots_adjust(wspace =0.3,hspace =0.3 )
        #存储为
        plt.savefig('refinement.png', transparent=True,format='png')#指定分辨率,边界紧，背景透明
        plt.show()
        print ('congratulate！！！')



    def FTIR(self):
        import os
        import matplotlib.pyplot as plt
        import pandas as pd
        from scipy.optimize import curve_fit
        import numpy as np
        from scipy.signal import savgol_filter
        from scipy.interpolate import make_interp_spline
        import re


        os.chdir(self.dire)

        font1 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'30'
        }

        a1=pd.read_csv('bassanite.csv',sep=',',usecols = [0],skipinitialspace=True,engine='python')
        a2=pd.read_csv('bassanite.csv',sep=',',usecols = [1],skipinitialspace=True,engine='python')
        a3=pd.read_csv('gypsum.csv',sep=',',usecols = [0],skipinitialspace=True,engine='python')
        a4=pd.read_csv('gypsum.csv',sep=',',usecols = [1],skipinitialspace=True,engine='python')
        

        fig,ax = plt.subplots(figsize=(12,9),dpi=300)
        # ss=float(min(a1))
        # bb=float(max(a3))
        # print(bb)

        ax.hlines(1.1, 500,4000,colors = "grey",alpha=0.6)
        ax.tick_params(labelsize=24)
        ax.plot(a1, a2+1.15, alpha=0.85,label='Bassanite',linewidth=4,c='red')
        axins = ax.inset_axes([0.3, 0.65, 0.3, 0.3])
        axins.plot(a1, a2+1.15, alpha=0.85,linewidth=4,c='red')
        axins.invert_xaxis() 
        axins.set_yticks([])
        axins.spines['top'].set_visible(False) #去掉上边框
        # axins.spines['bottom'].set_visible(False) #去掉下边框
        axins.spines['left'].set_visible(False) #去掉左边框
        axins.spines['right'].set_visible(False) #去掉右边框
        axins.tick_params(labelsize=24)
        # sub region of the original image
        # x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9
        axins.set_xlim(700, 500)
        # axins.set_ylim(y1, y2)
        # axins.set_xticklabels('')
        # axins.set_yticklabels('')
        
        
        
        ax.plot(a3, a4+0.05, alpha=0.65,label='gypsum',linestyle=(0,(3,1.5)), linewidth=2,c='blue')
        

        axins0 = ax.inset_axes([0.3, 0.15, 0.3, 0.3])
        axins0.plot(a3, a4+0.05, alpha=0.65,linewidth=2,linestyle=(0,(3,1.5)),c='blue')
        axins0.invert_xaxis() 
        axins0.set_yticks([])
        axins0.spines['top'].set_visible(False) #去掉上边框
        # axins.spines['bottom'].set_visible(False) #去掉下边框
        axins0.spines['left'].set_visible(False) #去掉左边框
        axins0.spines['right'].set_visible(False) #去掉右边框
        axins0.tick_params(labelsize=24)
        # sub region of the original image
        # x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9
        axins0.set_xlim(700, 500)
        # axins.set_ylim(y1, y2)
        # xticks=np.arange(550,700,50)
        # print(xticks)
        # axins.set_xticks([700,650,600,550])
        # axins.set_yticklabels('')






        ax.set_xlabel(r"Wavenumber (cm$^{-1}$)",fontsize=36,family='Times New Roman')
        ax.set_ylabel(r'Intensity (a.u)',fontsize=36,family='Times New Roman')
        # 
        

        ax.invert_xaxis() 
        ax.spines['top'].set_visible(False) #去掉上边框
        # ax.spines['bottom'].set_visible(False) #去掉下边框
        ax.spines['left'].set_visible(False) #去掉左边框
        ax.spines['right'].set_visible(False) #去掉右边框

        # ax.xlim((5,80))
        # 以下是图片的格式设置
        # 设置横纵坐标的名称以及对应字体格式
        font2 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'x-large'
        }

        # ax.xlim((0,12))
        ax.set_ylim((0,2.2))
        #不显示Y轴的刻度
        ax.set_yticks([])
        ax.legend(prop=font1,frameon=False)
        #设置图例对应格式和字体
        # auto_adjust_subplotpars(fig, renderer,(2,3) , [1,1,1,1,1,1], (2,3,1), ax_bbox_list=None, pad=1.08, h_pad=None, w_pad=None, rect=None)
        # plt.subplots_adjust(wspace =0.3,hspace =0.3 )
        #存储为
        plt.savefig('FTIR.png', transparent=True,format='png')#指定分辨率,边界紧，背景透明
        plt.show()
        print ('congratulate！！！')




    def XRD(self,name="xrd.xlsx"):
        import os
        import matplotlib.pyplot as plt
        import pandas as pd
        from scipy.optimize import curve_fit
        import numpy as np
        from scipy.signal import savgol_filter
        from scipy.interpolate import make_interp_spline
        import re


        font1 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'30'
        }

        os.chdir(self.dire)

        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        df = pd.read_excel(name)




        a=df['2θ']
        b=df['Intensity']
        # c=df['2θB']
        # e=df['Bassanite']
        # f=df['2θG']
        # g=df['gypsum']
        # eee=[]
        # for i, element in enumerate(e):
        #     if element<b[i]:
        #         ee=
        # ee=[]
        # for i in b:

        fig,ax = plt.subplots(figsize=(12,9),dpi=300)

        # k=min(b)/max(e)
        line1= ax.scatter(a, b, alpha=0.85, marker='o',color='', s=40,edgecolors='red',label='PVP',linewidth=2)
        # ax.plot(a, b, alpha=0.65,label='Bassanite',linestyle=(0,(1,0.3)), linewidth=5,c='red')

        # bar_a = ax.bar(c, e*k,label='Bassanite',color='blue',width=0.2,ec='black',lw=.2)

        ax.set_xlim([5, 60])


        # 以下是XRD图片的格式设置
        #设置横纵坐标的名称以及对应字体格式
        ax.set_xlabel(r"2Theta (Degree)",fontsize=36,family='Times New Roman')
        ax.set_ylabel(r'Intensity (a.u)',fontsize=36,family='Times New Roman')
        # ax.set_xlabel(r"Size (nm)",fontsize=36,family='Times New Roman')
        # ax.set_ylabel(r'Concentration (particles × 10$^6$/ml)',fontsize=36,family='Times New Roman')


        #不显示Y轴的刻度
        ax.set_yticks([])

        ax.legend(prop=font1,frameon=False)
        ax.tick_params(labelsize=24)
        #存储为
        plt.savefig(name+'.png', transparent=True,format='png')#指定分辨率,边界紧，背景透明
        plt.show()
        print ('congratulate！！！')