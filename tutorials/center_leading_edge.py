from pyturbo.aero import Airfoil2D, plot2D_compare

# match with LPT vane 3, 50%
tauFact = 0.7
lengthFact = 42.0
betaIn = 45.
betaOut = 72.
axialChord = 0.040*lengthFact
staggerAngle = 24.
radiusTE = 0.0004*lengthFact

vane = Airfoil2D( alpha1=betaIn, alpha2=betaOut, axial_chord=axialChord, stagger=staggerAngle)
#vane.custom_camber( 0.10, 0.10 )  # 0.24, 0.22, 0.20, 0.18
vane.add_le_thickness(0.02)
vane.add_ps_thickness(thicknessArray=[ 0.050*tauFact, 0.020*tauFact,-0.010*tauFact], expansion_ratio=1.2 )
vane.add_ss_thickness(thicknessArray=[ 0.150*tauFact, 0.400*tauFact, 0.340*tauFact, 0.160*tauFact ], camberPercent=0.75, expansion_ratio=1.2 )
vane.match_le_thickness()
vane.te_create( radius=radiusTE, wedge_ss=3.5, wedge_ps=2.4 )
vane.add_ss_flow_guidance_2( s_c=0.75, n=10 )
vane.center_le()

staggerAngle2 = 50
vane2 = Airfoil2D( alpha1=betaIn, alpha2=betaOut, axial_chord=axialChord, stagger=staggerAngle2)
#vane.custom_camber( 0.10, 0.10 )  # 0.24, 0.22, 0.20, 0.18
vane2.add_le_thickness(0.02)
vane2.add_ps_thickness(thicknessArray=[ 0.050*tauFact, 0.020*tauFact,-0.010*tauFact], expansion_ratio=1.2 )
vane2.add_ss_thickness(thicknessArray=[ 0.150*tauFact, 0.400*tauFact, 0.340*tauFact, 0.160*tauFact ], camberPercent=0.75, expansion_ratio=1.2 )
vane2.match_le_thickness()
vane2.te_create( radius=radiusTE, wedge_ss=3.5, wedge_ps=2.4 )
vane2.add_ss_flow_guidance_2( s_c=0.75, n=10 )
vane2.center_le()

plot2D_compare([vane, vane2], labels=['Stagger 24°', 'Stagger 50°'])