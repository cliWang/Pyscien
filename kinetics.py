class Kinetics():
    def __init__(self,dire):

        self.dire = dire

    def Firstorderreaction(self,dirr):
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
    
        def func(t,k,n):
            # u=np.exp(k*t)

            # return np.exp(1-1/(t*k+1))
            return ((1/(1+(n-1)*k*t))**(n-1))
            # return np.exp(k*t)
        # def func(t,k):
        #     # u=np.exp(k*t)

        #     # return np.exp(1-1/(t*k+1))
        #     return ((1/(1+(2-1)*k*t))**(2-1))
        #     # return np.exp(k*t)    
        popt, pcov = curve_fit(func, xa, yb)
        k=popt[0]
        n=popt[1] # popt里面是拟合系数，读者可以自己help其用法
        yvals=func(xa,k,n)
        # yvals=func(xa,k)  
        print(k)  
        print('n= '+str(n))
        # x_smooth = np.linspace(x.min(), a.max(), 300)
        # y_smooth = make_interp_spline(a, yvals)(x_smooth)
        li = 0.07
        plot1=plt.plot(xa, yvals, alpha=0.7,linestyle="--",label='k = '+str('%.2f' %li)+' h$^{-1}$ ')

        def func(t,k):
            # u=np.exp(k*t)

            # return np.exp(1-1/(t*k+1))
            return ((1/(1+(3-1)*k*t))**(3-1))
            # return np.exp(k*t)
        popt, pcov = curve_fit(func, a, d)
        k=popt[0]
        # n=popt[1] # popt里面是拟合系数，读者可以自己help其用法
        yvals=func(a,k)  
        print(k) 
        # print('n= '+str(n))     
        x_smooth = np.linspace(a.min(), a.max(), 300)
        y_smooth = make_interp_spline(a, yvals)(x_smooth)
        li = 0.23
        plot2=plt.plot(x_smooth, y_smooth, alpha=0.7,linestyle="--",label='k = '+str('%.2f' %li)+' h$^{-1}$ ')

        # plot2=plt.plot(a, yvals, alpha=0.7,linestyle="--",label='k = '+str('%.2f' %li)+' h$^{-1}$ ')






        # 以下是图片的格式设置
        # 设置横纵坐标的名称以及对应字体格式
        font2 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'x-large'
        }
        plt.xlabel('Time (min)' ,font2)
        plt.ylabel(r'C/C$_0$' ,font2)

        #不显示Y轴的刻度
        # plt.yticks([])

        #设置图例对应格式和字体
        font1 = {'family' : 'Times New Roman',
        'weight' : 'normal','size':'large'
        }
        ax.legend(edgecolor='none', prop=font1,)

        plt.legend(edgecolor='none', prop=font1)

        #存储为
        fig.savefig(dirr+'fit.png',bbox_inches='tight', transparent=True,dpi=600,format='png')#指定分辨率,边界紧，背景透明
        plt.show()
