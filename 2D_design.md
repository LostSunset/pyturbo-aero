# 2D Airfoil Design
There are two ways of using this code.
1. If you need to design from scratch.
2. If you already have a design

Designing from Scratch - Building the 2D geometry which will later be used to build the 3D Blade.
The code below shows how to construct a stator
```python
import numpy as np
from pyturbo.aero import Airfoil2D
from pyturbo.helper import exp_ratio

stator_hub = Airfoil2D(alpha1=0,alpha2=72,axial_chord=0.038,stagger=58) # This creates the camberline
stator_hub.add_le_thickness(0.04)
ps_height = [0.0500,0.0200,-0.0100]
stator_hub.add_ps_thickness(thicknessArray=ps_height,expansion_ratio=1.2)

ss_height=[0.2400, 0.2000, 0.1600, 0.1400]
stator_hub.add_ss_thickness(thicknessArray=ss_height,camberPercent=0.8,expansion_ratio=1.2)
stator_hub.match_thickness(location='LE')
stator_hub.te_create(radius=0.001,wedge_ss=2.5,wedge_ps=2.4)

stator_hub.add_ss_flow_guidance_2(s_c=0.75,n=10)
```

Below is the camberline plotted by calling.
`stator_hub.plot_camber()`

Subsequently the design blade geometry with control points are plotted
`stator_hub.plot2D()`

Second derivative for both suction and pressure sides
`stator_hub.plot_derivative2()`

Plot of the stator with pitch to chord of 0.75
`stator_hub.plot2D_channel(0.75)`
