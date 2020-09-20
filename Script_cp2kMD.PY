import sys
sys.path.append(r"D:\Desktop\VASP practical\Pymatgen")
from cp2kMD import cp2kMD



my_cp2kMD = cp2kMD(r'F:\cp2k practical\useful\bassanite\300cal\mdcal')
# my_cp2kMD.POSTAIMD(filename='run-NH2O-MD-T300.xyz',rdf_fir='type O',rdf_sec='type H')


my_cp2kMD.Energychek()

my_cp2kMD.Energy()

'''
cp2k输入文件生成码，两步需分开操作
'''


'''
第一步
# '''
# my_cp2kMD.PREAIMD(para='matflow cp2k -r 10 --cif aimd.cif --cutoff 300 --kpoints-scheme NONE -d mdcal --md-steps 100')
'''
第二步
'''
# my_cp2kMD.rewrite()