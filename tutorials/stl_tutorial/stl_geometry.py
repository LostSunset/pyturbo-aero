'''
    This tutorial shows how you can export a geometry to STL
'''

import numpy as np
from pyturbo.aero import Airfoil2D
from pyturbo.helper import exp_ratio
from pyturbo.aero import Airfoil3D, StackType
import matplotlib.pyplot as plt

stator2D = Airfoil2D(alpha1=0,alpha2=72,axial_chord=0.038,stagger=58) # This creates the camberline

# Building Leading Edge
stator2D.add_le_thickness(0.04)
# Building the Pressure side
ps_height = [0.0500,0.0200,-0.0100] # These are thicknesses
stator2D.add_ps_thickness(thicknessArray=ps_height,expansion_ratio=1.2)

ss_height=[0.2400, 0.2000, 0.1600, 0.1400]
stator2D.add_ss_thickness(thicknessArray=ss_height,camberPercent=0.8,expansion_ratio=1.2)
stator2D.match_le_thickness()
stator2D.te_create(radius=0.001,wedge_ss=2.5,wedge_ps=2.4)

stator2D.add_ss_flow_guidance_2(s_c=0.8, n=10)


stator3D = Airfoil3D(profileArray=[stator2D,stator2D,stator2D],profile_loc=[0.0,0.5,1.0], height = 0.02)
stator3D.stack(StackType.leading_edge) # Stators are typically stacked with leading edge; rotors with centroid or trailing edge
# You can also use StackType.centroid or StackType.trailing_edge
stator3D.build(nProfiles=20, num_points=50, trailing_edge_points=10)
# stator3D.center_le() # Centers the leading edge at (0,0); use this only if you are simulating a single blade. Makes creating planes for data extraction easier.
# stator3D.plot3D()
stator3D.export_stl()
