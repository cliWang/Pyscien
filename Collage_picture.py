class Coll_pic():
    def __init__(self,dire):

        self.dire = dire

    def transparent_back(self,content):
        import PIL.Image as Image
        import os
        os.chdir(self.dire)
        print (os.getcwd())
        tem=content.replace('(','').replace(')','')
        
        vun=list([str(i) for i in tem.split(',')])
        print(vun)
        for site in vun[0:100]:
            img=Image.open(str(site)+'.png')
            img = img.convert('RGBA')
            datas = img.getdata()
            # print(datas)
            newData = list()
            for item in datas:
                if item[0] >220 and item[1] > 220 and item[2] > 220:
                    newData.append(( 255, 255, 255, 0))
                else:
                    newData.append(item)
    
            img.putdata(newData)
            img.save(str(site)+".png")


    def m_collage_pic(self, content='(a,b,c,d,e,f)',rows= 0, columns= 1):
        import cv2
        import os
        import matplotlib.pyplot as plt # plt 用于显示图片
        import matplotlib.image as mpimg # mpimg 用于读取图片
        import numpy as np
        from matplotlib.gridspec import GridSpec
        from PIL import Image, ImageDraw, ImageFont
        os.chdir(self.dire)
        filePath = self.dire 
        font2 = {'family' : 'Times New Roman','fontsize':'16' , 'weight' : 'bold'} 
        tem=content.replace('(','').replace(')','')
        vun=list([str(i) for i in tem.split(',')])

        fig = plt.figure(figsize = (6,12),dpi=600)
        
        for isite,site in enumerate(vun):
            i0 = int(rows)
            i1 = int(columns)
            i2 = int(isite+1)
            img = cv2.imread(str(site )+".png",1)
            # lena = mpimg.imread(str(site )+'.tif') 
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.subplot(i0,i1,i2)
            # gs = GridSpec(2, 3)
            # gs.new_subplotspec((i0,i1),rowspan = 1,colspan = 1)
            print (i0,i1,i2)
            plt.imshow(img)
            plt.title(str(site),font2,loc = 'left',x = -0.1,y=0.95)#loc = 'left',
            plt.axis('off')

        os.chdir(self.dire)
        print (os.getcwd()) 
        # auto_adjust_subplotpars(fig, renderer,(2,3) , [1,1,1,1,1,1], (2,3,1), ax_bbox_list=None, pad=1.08, h_pad=None, w_pad=None, rect=None)
        # fig.tight_layout()
        plt.subplots_adjust(wspace =0.1,hspace =-0.1 )
        fig.savefig(str(vun[0])+'to'+str(vun[-1])+'.png',bbox_inches='tight', transparent=True,)#指定分辨率,边界紧，背景透明
        plt.show()


    def em_collage_pic(self, content='(a,b,c,d,e,f)',grid = (1,1),a="(1,1,1)",b="(1,1,1)",c="(1,1,1)",d="(1,1,1)",e="(1,1,1)",f="(1,1,1)",g="(1,1,1)",h="(1,1,1)",i="(1,1,1)",j="(1,1,1)",k="(1,1,1)"):
        import cv2
        import os
        import matplotlib.pyplot as plt # plt 用于显示图片
        import matplotlib.image as mpimg # mpimg 用于读取图片
        import numpy as np
        from matplotlib.gridspec import GridSpec
        from PIL import Image, ImageDraw, ImageFont
        os.chdir(self.dire)
        filePath = self.dire
        # pic=[]
        font2 = {'family' : 'Times New Roman','fontsize':'20' , 'weight' : 'bold',"color":"white"}  
        tem=content.replace('(','').replace(')','')
        vun=list([str(i) for i in tem.split(',')])
        

        par = [a,b,c,d,e,f,g,h,i,j,k]
        fig = plt.figure()
        # figsize = (16,12)
        for isite,site in enumerate(vun):

            temp=par[isite].replace('(','').replace(')','')
            r=list([int(i) for i in temp.split(',')])
            i0 = r[0]
            i1 = r[1]
            i2 = r[2]
            img = cv2.imread(str(site )+".png",1)
            # lena = mpimg.imread(str(site )+'.tif') 
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.subplot(i0,i1,i2)
            # gs = GridSpec(2, 3)
            # gs.new_subplotspec((i0,i1),rowspan = 1,colspan = 1)
            print (i0,i1,i2)
            plt.imshow(img)
            plt.title(str(site),font2,loc = 'left',x= 0.03,y=0.75)#loc = 'left',
            plt.axis('off')

        

        os.chdir(self.dire)
        print (os.getcwd()) 
        # auto_adjust_subplotpars(fig, renderer,(2,3) , [1,1,1,1,1,1], (2,3,1), ax_bbox_list=None, pad=1.08, h_pad=None, w_pad=None, rect=None)
        fig.tight_layout()
        plt.subplots_adjust(wspace =-0.73,hspace = 0.03)
        fig.savefig('./1.png',bbox_inches='tight', transparent=True,dpi=1000)#指定分辨率,边界紧，背景透明
        plt.show()
        os.chdir(r"D:\Desktop\VASP practical\workdir")
        print ('finished')





        #grid = (1,1),a="(1,1,1)",b="(1,1,1)",c="(1,1,1)",d="(1,1,1)",e="(1,1,1)",f="(1,1,1)",g="(1,1,1)",
                    #h="(1,1,1)",i="(1,1,1)",j="(1,1,1)",k="(1,1,1)",l='',m='',n='',o='',p='',q='',r='',s='',t='',u='',v='',w='',x='',y='',z=''):