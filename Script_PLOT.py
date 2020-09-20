import sys
sys.path.append(r"D:\Desktop\VASP practical\Pymatgen")
from PLOT import Plot




my_Plot =Plot(r'D:\Desktop\fullprof\GYP')
# my_Plot.Plotterfill(dir1='RDF OO',dir2='RDF OH',dir3='RDF HH',dir4='RDF Ha')
my_Plot.Barchart()
# my_Plot.XRDrefinement()
# my_Plot.FTIR()
# my_Plot.XRD(name="pvp.xlsx")