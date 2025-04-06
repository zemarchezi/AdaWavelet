"""
AdaWavelet: Adaptive Wavelet Analysis with Gap Handling
======================================================

A Python package for wavelet analysis of signals with gaps.

Main Features
------------
- Gap-aware wavelet transform
- Multiple mother wavelets: Morlet, Paul, DOG
- Numba-accelerated computations
"""

__version__ = "0.1.0"
__author__ = "Jose P. Marchezi"

# Import the main class to make it available at the top level
from .core import AdaptativeWaveletTransform

__all__ = ['AdaptativeWaveletTransform']