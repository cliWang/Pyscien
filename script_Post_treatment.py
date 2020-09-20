import sys
sys.path.append(r"D:\Desktop\VASP practical\Pymatgen")
from Post_treatment import Post_treatment
sulf_ener={(0, 0, 1):0.048, (2, 0, 0):3.26, 
                       (1, 1, 0): 3.31}
my_post_treatment = Post_treatment(r'E:\VASP practical\Output\ISOTOPE\NaCl-VASPdfpt')
# my_post_treatment.Wullff("mp-505531",sulf_ener,'SFeS',directions=(3,4,4),x=0.47,y=-16)

'''
AIMD
'''


# my_post_treatment.pdb_change(para='-p -t 2  --pbc')#-t 0.5用于指定时间步为0.5 fs，--pbc用于获取基于第一帧演变的连续轨迹-b参数用于指定转换从哪一帧开始，-e参数用于指定转换到哪一帧结束。

# my_post_treatment.RMSDs(group=["type Fe","type S"])
# my_post_treatment.RDF(type1='type Fe',type2='type S')
my_post_treatment.Vibration(maxx=400)
my_post_treatment.Vibrationauto(maxx=400)
# my_post_treatment.Phonopy()
# my_post_treatment.Energy()



# my_post_treatment.Diffusion(skip=10,spaces='S',temp=[300,310,350,390])
# 
# import sys
sys.path.append(r"D:\Desktop\VASP practical\Pymatgen")
from Post_treatment import Post_treatment
sulf_ener={(0, 0, 1):9.48, (1, 0, 0):3.26, 
                       (0, 2, 2): 3.31,(2, 0, 1): 1.31,(1, 1, 1): 2.31}
my_post_treatment = Post_treatment(r'E:\VASP practical\Output\Disorder_structure\AIMD')
my_post_treatment.Wullff("mp-698074",sulf_ener,'Bassanite',directions=(3,4,4),x=0.47,y=-16)