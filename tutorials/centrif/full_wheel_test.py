"""Full Wheel Test for Centrifugal Compressor

Demonstrates building a full wheel with and without a splitter blade
using the current Centrif API.
"""
from pyturbo.aero import Centrif, CentrifProfile, TrailingEdgeProperties
from pyturbo.aero.centrif import PatternPairCentrif
from pyturbo.helper import bezier
import numpy as np


def create_passage_compressor():
    """Creates the hub and shroud curves for the compressor.

    Returns:
        Tuple of (xhub, rhub, xshroud, rshroud) arrays.
    """
    xhub_ctrl_pts = np.array([0.0, 0.02, 0.08, 0.11, 0.12, 0.12])
    rhub_ctrl_pts = np.array([0.0, 0.0, 0.004, 0.06, 0.09, 0.10]) + 0.02
    hub = bezier(xhub_ctrl_pts, rhub_ctrl_pts)

    xshroud_ctrl_pts = np.array([0.0, 0.02, 0.05, 0.09, 0.11, 0.11])
    rshroud_ctrl_pts = np.array([0.03, 0.03, 0.04, 0.055, 0.09, 0.10]) + 0.02
    shroud = bezier(xshroud_ctrl_pts, rshroud_ctrl_pts)

    xhub, rhub = hub.get_point(np.linspace(0, 1, 100))
    xshroud, rshroud = shroud.get_point(np.linspace(0, 1, 100))

    return xhub, rhub, xshroud, rshroud


def build_rounded_te_blade():
    """Build a centrifugal compressor blade with rounded trailing edge.

    Returns:
        Centrif: The built blade.
    """
    xhub, rhub, xshroud, rshroud = create_passage_compressor()

    te_props = TrailingEdgeProperties(TE_Cut=False, TE_Radius=0.05)

    hub_profile = CentrifProfile(
        percent_span=0, LE_Thickness=0.02,
        trailing_edge_properties=te_props,
        LE_Metal_Angle=30, TE_Metal_Angle=50,
        LE_Metal_Angle_Loc=0.15, TE_Metal_Angle_Loc=0.9,
        ss_thickness=[0.02, 0.03, 0.02, 0.02],
        ps_thickness=[0.02, 0.03, 0.02, 0.02],
        wrap_angle=-45,
    )

    mid_profile = CentrifProfile(
        percent_span=0.5, LE_Thickness=0.02,
        trailing_edge_properties=te_props,
        LE_Metal_Angle=15, TE_Metal_Angle=40,
        LE_Metal_Angle_Loc=0.1, TE_Metal_Angle_Loc=0.98,
        ss_thickness=[0.02, 0.03, 0.02, 0.02],
        ps_thickness=[0.02, 0.03, 0.02, 0.02],
        wrap_angle=-45,
    )

    tip_profile = CentrifProfile(
        percent_span=1, LE_Thickness=0.02,
        trailing_edge_properties=te_props,
        LE_Metal_Angle=10, TE_Metal_Angle=0,
        LE_Metal_Angle_Loc=0.1, TE_Metal_Angle_Loc=0.98,
        ss_thickness=[0.02, 0.03, 0.02, 0.02],
        ps_thickness=[0.02, 0.03, 0.02, 0.02],
        wrap_angle=-45,
    )

    comp = Centrif(blade_position=(0.01, 0.95), use_mid_wrap_angle=True)
    comp.add_hub(xhub, rhub)
    comp.add_shroud(xshroud, rshroud)
    comp.add_profile(hub_profile)
    comp.add_profile(mid_profile)
    comp.add_profile(tip_profile)

    return comp


def build_splitter_blade():
    """Build a centrifugal compressor blade with a splitter.

    Returns:
        Centrif: The built blade with splitter.
    """
    xhub, rhub, xshroud, rshroud = create_passage_compressor()

    te_props = TrailingEdgeProperties(TE_Cut=False, TE_Radius=0.05)

    # Main blade profiles
    hub_profile = CentrifProfile(
        percent_span=0, LE_Thickness=0.02,
        trailing_edge_properties=te_props,
        LE_Metal_Angle=0, TE_Metal_Angle=70,
        LE_Metal_Angle_Loc=0.1, TE_Metal_Angle_Loc=0.98,
        ss_thickness=[0.02, 0.03, 0.02, 0.02],
        ps_thickness=[0.02, 0.02, 0.02, 0.02],
        wrap_angle=-35,
    )

    mid_profile = CentrifProfile(
        percent_span=0.5, LE_Thickness=0.02,
        trailing_edge_properties=te_props,
        LE_Metal_Angle=0, TE_Metal_Angle=70,
        LE_Metal_Angle_Loc=0.1, TE_Metal_Angle_Loc=0.98,
        ss_thickness=[0.02, 0.03, 0.02, 0.02],
        ps_thickness=[0.02, 0.02, 0.02, 0.02],
        wrap_angle=-35,
    )

    tip_profile = CentrifProfile(
        percent_span=1, LE_Thickness=0.02,
        trailing_edge_properties=te_props,
        LE_Metal_Angle=0, TE_Metal_Angle=70,
        LE_Metal_Angle_Loc=0.1, TE_Metal_Angle_Loc=0.98,
        ss_thickness=[0.02, 0.03, 0.02, 0.02],
        ps_thickness=[0.02, 0.02, 0.02, 0.02],
        wrap_angle=-35,
    )

    # Splitter profiles
    splitter_hub = CentrifProfile(
        percent_span=0, LE_Thickness=0.02,
        trailing_edge_properties=te_props,
        LE_Metal_Angle=0, TE_Metal_Angle=70,
        LE_Metal_Angle_Loc=0.1, TE_Metal_Angle_Loc=0.98,
        ss_thickness=[0.02, 0.03, 0.02, 0.02],
        ps_thickness=[0.02, 0.03, 0.02, 0.02],
        wrap_angle=-35,
    )

    splitter_mid = CentrifProfile(
        percent_span=0.5, LE_Thickness=0.02,
        trailing_edge_properties=te_props,
        LE_Metal_Angle=0, TE_Metal_Angle=70,
        LE_Metal_Angle_Loc=0.1, TE_Metal_Angle_Loc=0.98,
        ss_thickness=[0.02, 0.03, 0.02, 0.02],
        ps_thickness=[0.02, 0.03, 0.02, 0.02],
        wrap_angle=-35,
    )

    splitter_tip = CentrifProfile(
        percent_span=1, LE_Thickness=0.02,
        trailing_edge_properties=te_props,
        LE_Metal_Angle=0, TE_Metal_Angle=70,
        LE_Metal_Angle_Loc=0.1, TE_Metal_Angle_Loc=0.98,
        ss_thickness=[0.02, 0.03, 0.02, 0.02],
        ps_thickness=[0.02, 0.03, 0.02, 0.02],
        wrap_angle=-35,
    )

    comp = Centrif(blade_position=(0.01, 0.95), use_mid_wrap_angle=True)
    comp.add_hub(xhub, rhub)
    comp.add_shroud(xshroud, rshroud)
    comp.add_profile(hub_profile)
    comp.add_profile(mid_profile)
    comp.add_profile(tip_profile)
    comp.add_splitter([splitter_hub, splitter_mid, splitter_tip], splitter_start=0.4)

    return comp


def fullwheel_no_fillet():
    comp = build_rounded_te_blade()

    comp.add_pattern_pair(PatternPairCentrif(0.96, 0.5))
    comp.add_pattern_pair(PatternPairCentrif(0.96, -0.5))
    comp.add_pattern_pair(PatternPairCentrif(1, -0.5))
    comp.add_pattern_pair(PatternPairCentrif(1, 0.5))

    comp.build(npts_span=10, npts_chord=100, nblades=12)
    comp.plot_fullwheel()


def fullwheel_splitter():
    comp = build_splitter_blade()

    comp.add_pattern_pair(PatternPairCentrif(0.96, 0.5))
    comp.add_pattern_pair(PatternPairCentrif(0.96, -0.5))
    comp.add_pattern_pair(PatternPairCentrif(1, -0.5))
    comp.add_pattern_pair(PatternPairCentrif(1, 0.5))

    comp.build(npts_span=10, npts_chord=100, nblades=12)
    comp.plot_fullwheel()


if __name__ == '__main__':
    # fullwheel_no_fillet()
    fullwheel_splitter()
