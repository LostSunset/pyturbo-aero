# 3D Design

The 3D design of the blade begins by stacking 2D Designs together to form a 3D geometry.
## Useful import scripts

```python
import numpy as np
from pyturbo.aero import Airfoil2D, Airfoil3D, AirfoilWavy
from pyturbo.helper import StackType
```


## Simple 3D Blade
The code below shows an example of how to build a 3D Blade from 2D designs located at the hub and tip

```python
# Hub Geometry
stator_hub = Airfoil2D(alpha1=0,alpha2=72,axial_chord=0.038,stagger=58)
stator_hub.add_le_thickness(0.04)
ps_height = [0.0500,0.0200,-0.0100]
stator_hub.add_ps_thickness(thicknessArray=ps_height,expansion_ratio=1.2)

ss_height=[0.2400, 0.2000, 0.1600, 0.1400]
stator_hub.add_ss_thickness(thicknessArray=ss_height,camberPercent=0.8,expansion_ratio=1.2)

stator_hub.te_create(radius=0.001,wedge_ss=2.5,wedge_ps=2.4)
stator_hub.match_thickness(location='LE')
stator_hub.add_ss_flow_guidance_2(s_c=0.75,n=10)

# Tip Geometry
stator_tip = Airfoil2D(alpha1=5,alpha2=72,axial_chord=0.036,stagger=56)
stator_tip.add_le_thickness(0.04)
ps_height = [0.0500,0.0200,-0.0100]
stator_tip.add_ps_thickness(thicknessArray=ps_height,expansion_ratio=1.2)

ss_height=[0.2400, 0.2000, 0.1600, 0.1400]
stator_tip.add_ss_thickness(thicknessArray=ss_height,camberPercent=0.8,expansion_ratio=1.2)

stator_tip.te_create(radius=0.001,wedge_ss=2.5,wedge_ps=2.4)
stator_tip.match_thickness(location='LE')
stator_tip.add_ss_flow_guidance_2(s_c=0.75,n=6)

# Begin 3D design
stator3D = Airfoil3D([stator_hub,stator_tip],[0,1],0.05)
stator3D.stack(StackType.trailing_edge)
# stator3D.add_lean(leanX=[0, 0.05, 1], leanZ=[0,0.5,1])
stator3D.build(nProfiles=100,num_points=80,trailing_edge_points=20)
stator3D.plot3D()
```

## Wavy Blade
Wavy code from Paht's thesis has been included in the design tools. This allows for optimizing sinusoidal profiles on the surfaces of the blade.
The code is very similar to the 3D blade. A few lines were added to apply the waves in the spanwise direction.
Note: Variables with names LE and TE wave angle control the angle modification of the leading and trailing edges.
These modifications are done perpendicular to the leading and trailing edge angle.


### Wavy Blade with constant Trailing Edge Radius
For blade designs that require a constant trailing edge radius. The example below is useful.

```python
# Wavy Geometry
stator3D_wavy = AirfoilWavy(profileArray=[stator_hub,stator_tip],profile_loc=[0,1],height=0.05)
stator3D_wavy.stack(StackType.trailing_edge)
stator3D_wavy.build(nProfiles=100,num_points=160,trailing_edge_points=20)

t = np.linspace(0,10*np.pi,100)
ssratio = 0.05*np.sin(t)
psratio = ssratio*0
leratio = 0.05*np.cos(t/4)
teratio = 0.05*np.cos(t)
lewave_angle = 0*ssratio
tewave_angle = 0*ssratio

stator3D_wavy.stretch_thickness_chord_te(ssratio,psratio,leratio,teratio,lewave_angle,tewave_angle,TE_smooth=0.90)
stator3D_wavy.plot3D()
```

### Wavy Blade without a constant Trailing Edge Radius
If trailing edge radius is not a problem and you want to explore designs that can vary the radius.

```python
stator3D_wavy = AirfoilWavy(profileArray=[stator_hub,stator_tip],profile_loc=[0,1],height=0.05)
stator3D_wavy.stack(StackType.trailing_edge)
stator3D_wavy.add_lean(leanX=[0, 0.05, 0], leanZ=[0,0.5,1])
stator3D_wavy.build(nProfiles=100,num_points=100,trailing_edge_points=20)

t = np.linspace(0,10*np.pi,100)
ssratio = 0.05*np.sin(t)
psratio = ssratio*0
leratio = 0.05*np.cos(t/4)
teratio = 0.05*np.cos(t)
lewave_angle = 0*ssratio
tewave_angle = 0*ssratio

stator3D_wavy.stretch_thickness_chord(ssratio,psratio,leratio,teratio,lewave_angle,tewave_angle)
stator3D_wavy.plot3D()
```

### Whisker Blade
Whiskers maintain their cross sectional area along the span. Can a blade do the same thing?
By removing the suction side ratio and allowing it to vary, a whisker-like blade geometry can be created.

```python
stator3D_wavy = AirfoilWavy(profileArray=[stator_hub,stator_tip],profile_loc=[0,1],height=0.05)
stator3D_wavy.stack(StackType.trailing_edge)
stator3D_wavy.add_lean(leanX=[0, 0.05, 0], leanZ=[0,0.5,1])
stator3D_wavy.build(nProfiles=100,num_points=100,trailing_edge_points=20)

t = np.linspace(0,10*np.pi,100)
psratio = 0.05*np.sin(t)
leratio = 0.05*np.cos(t/4)
teratio = 0.05*np.cos(t)
lewave_angle = 0*psratio
tewave_angle = 0*psratio

stator3D_wavy.whisker_blade(leratio,teratio,psratio,lewave_angle,tewave_angle,TE_smooth=0.9)
stator3D_wavy.plot3D()
```

### Importing a geometry
This is an example of how to import a geometry:
```python
rotor = Airfoil3D.import_geometry(folder='import_7%',axial_chord=124,span=114,ss_ps_split=105)
rotor.rotate(cx=0,cy=0,angle=90)
rotor.spanwise_spline_fit()
rotor.plot3D()
```

When you import geometries, you can manipulate it: add lean, fit it into a row/channel etc.
