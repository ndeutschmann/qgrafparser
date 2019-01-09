"""A collection of standard Feynman rules for propagators"""
from .algebra_tools import *

def standard_denominator(momentum,mass):
    """The common 1/(p^2-m^2) denominator in all Lorentz-invariant QFTs.

    Parameters
    ----------
    momentum : str
    mass : .abstract_objects.Parameters

    Returns
    -------
    str
    """
    return "Den({},{})".format(momentum,mass)

def scalar_propagator(momentum,mass):
    """Propagator for a scalar field i*Den(p,m)

    Parameters
    ----------
    momentum : str
    mass : .abstract_objects.Parameters

    Returns
    -------
    str
    """
    return times(i_,standard_denominator(momentum,mass))

def fermionic_propagator(from_field,to_field,momentum,mass):
    """Kinematic part of a standard fermionic propagator

    Parameters
    ----------
    from_field : qgraf_parser.diagram_elements.DiagramField
    to_field : qgraf_parser.diagram_elements.DiagramField
    momentum : str
    mass : .abstract_objects.Parameters

    Returns
    -------
    str
    """
    spinhalf_numerator = "g({p},x{psi},x{psibar}) + {m}*g(x{psi},x{psibar})".format(p=momentum,psi=from_field.id,psibar=to_field.id,m=mass)
    propagator = times(i_,spinhalf_numerator,standard_denominator(momentum,mass))
    return propagator

def quark_propagator(from_field,to_field,momentum,mass):
    """Kinematic part of a standard fermionic propagator

    Parameters
    ----------
    from_field : qgraf_parser.diagram_elements.DiagramField
    to_field : qgraf_parser.diagram_elements.DiagramField
    momentum : str
    mass : .abstract_objects.Parameters

    Returns
    -------
    str
    """
    return times(fermionic_propagator(from_field,to_field,momentum,mass),"d_(i{psi},i{psibar})".format(psi=from_field.id,psibar=to_field.id))
