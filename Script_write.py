import sys
sys.path.append(r"D:\Desktop\VASP practical\Pymatgen")

from write import Write


my_write = Write(r'E:\VASP practical\Output\ZWF\zwf')
my_write.energy()
my_write.mol_energy()
my_write.muti_adsorbate_energy(unit_energy=-353.06964595, unit_number=1,mol_number=1)
# my_write.adsorbate_energy(unit_energy, unit_number,mol_energy,mol_number)

# my_write.file('vaspgam_sub','vaspstd_sub')#原始文件，目标文件

# my_write.file('INCAR_Pro','INCAR')#原始文件，目标文件INCAR_Pro,INCAR_Vib,INCAR_Mol,INCAR_AIMD,

# my_write.file('KPOINTS_Gamma','KPOINTS')#原始文件，目标文件KPOINTS_Gamma,KPOINTS_molvib

# my_write.surface_energy(-92.81078785, 3)

# my_write.molecular('Single water molecule')

# my_write.copy()参数写CONTCAR
