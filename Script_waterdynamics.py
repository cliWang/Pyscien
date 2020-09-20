import sys
sys.path.append(r"D:\Desktop\VASP practical\Pymatgen")
from waterdynamics import Waterdynamics
sulf_ener={(0, 0, 1):0.048, (2, 0, 0):3.26, 
                       (1, 1, 0): 3.31}
my_Waterdynamics = Waterdynamics(r'F:\cp2k practical\test\water')
# my_Waterdynamics.MSD(selects="name H",tbegin=0,tfinal=1000,filename='gyp300')#index 30,name S
# my_Waterdynamics.RMSDs(group=["type H","type S",'type O'],filename='gyp300')
# my_Waterdynamics.HBL(select1="all",select2="point 3.0 3.0 3.0 2",tbegin=0,tfinal=1000,filename='gyp300')#index 
# my_Waterdynamics.WOR(selects="all",tbegin=0,tfinal=1000,title='gyp300')#index 30,name S
# my_Waterdynamics.AD(selects="all",title='gyp300')#index 30,name
# my_Waterdynamics.RDF(rdf_fir='name S',rdf_sec='name O')#index 30,name  
my_Waterdynamics.SP(select1="name H and point 5.0 5.0 5.0 6",select2="name O and point 5.0 5.0 5.0 6",tbegin=0,tfinal=1000)#index 30,name