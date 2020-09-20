# Import the neccesary tools to generate surfaces
from pymatgen.core.surface import SlabGenerator, generate_all_slabs, Structure, Lattice
# Import the neccesary tools for making a Wulff shape
from pymatgen.analysis.wulff import WulffShape
from pymatgen.ext.matproj import MPRester
from pymatgen.io.cif import CifParser
import os
os.chdir(r"D:\Desktop\VASP practical\Cif library")  
print (os.getcwd())   
struct = CifParser(ass)
structure = struct.get_structures()[0]
mpr = MPRester()
# Let's start with fcc Ni
# lattice = Lattice.cubic(3.508)
# Ni = Structure(lattice, ["Ni", "Ni", "Ni", "Ni"],
#                 [[0,0,0], [0,0.5,0], 
#                 [0.5,0,0], [0,0,0.5]
#                 ])
mp_id = "mp-698074"
struct = mpr.get_structure_by_material_id(mp_id)

# We'll use the SlabGenerator class to get a single slab. We'll start with the 
# (111) slab of Ni. Plug in the CONVENTIONAL unit cell of your structure, the 
# maximum Miller index value to generate the different slab orientations along 
# with the minimum slab and vacuum size in Angstroms
# slabgen = SlabGenerator(Ni, (1,1,1), 10, 10)

# # If we want to find all terminations for a particular Miller index orientation, 
# # we use the get_slabs() method. This returns a LIST of slabs rather than a single
# # slab. When generating a slab for a particular orientation, there are sometimes 
# # more than one location we can terminate or cut the structure to create a slab. The
# # simplest example of this would be the Si(Fd-3m) (111) slab which can be cut or 
# # terminated in two different locations along the vector of the Miller index. For a
# # fcc structure such as Ni however, there should only be one way to cut a (111) slab.
# all_slabs = slabgen.get_slabs() 
# print("The Ni(111) slab only has %s termination." %(len(all_slabs)))

# Now let's assume that we then calculated the surface energies for these slabs

# Surface energy values in J/m^2
surface_energies_Ni = {(0, 0, 1): 2.3869, (2, 0, 1): 2.2862, 
                       (1, -1, 0): 2.3964, (0, 2, 0): 2.0944,  
                       (-2, -2, 1): 0.9353,  (2, -2, 0): 2.3183,  
                       (-1, 1, 1): 2.2288, (0, 2, 2): 1.9235}
miller_list = surface_energies_Ni.keys()
e_surf_list = surface_energies_Ni.values()

# We can now construct a Wulff shape with an accuracy up to a max Miller index of 3
wulffshape = WulffShape(struct.lattice, miller_list, e_surf_list)

# Let's get some useful information from our wulffshape object
# print("shape factor: %.3f, anisotropy: \
# %.3f, weighted surface energy: %.3f J/m^2" %(wulffshape.shape_factor, 
#                                        wulffshape.anisotropy,
#                                        wulffshape.weighted_surface_energy))


# If we want to see what our Wulff shape looks like
wulffshape.show()






