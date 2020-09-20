from vaspy.electro import ElfCar

import matplotlib.pyplot as plt
import os
from vaspy.electro import ChgCar

os.chdir(r"D:\Desktop\合作计算数据\4月-王春雳\4月发送-王春雳\2-ELF\ELF\ele")
print (os.getcwd())


elfcar = ElfCar("ELFCARs5")
elfcar.plot_contour(axis_cut='y',distance=0.5,widths=(1, 1, 1),show_mode='save')
elfcar.plot_contour3d()
from vaspy.electro import ElfCar

import matplotlib.pyplot as plt
import os
from vaspy.electro import ChgCar

os.chdir(r"D:\Desktop\合作计算数据\4月-王春雳\4月发送-王春雳\2-ELF\ELF\ele")
print (os.getcwd())


elfcar = ElfCar("ELFCARs5")
elfcar.plot_contour(axis_cut='y',distance=0.5,widths=(1, 1, 1),show_mode='save')
elfcar.plot_contour3d()
