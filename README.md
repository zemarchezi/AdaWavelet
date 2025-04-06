# 🌊 AdaWavelet 

**⚠️ UNDER CONSTRUCTION ⚠️**

This package is currently in active development. APIs may change, and features may be added or removed without notice.

---

## Overview

AdaWavelet is a Python library for advanced wavelet analysis, with special focus on handling signals with gaps or irregular sampling. It implements optimized adaptative wavelet transforms using various mother wavelets, allowing for robust spectral analysis of imperfect real-world data.

## Key Features

- **Gap-aware Wavelet Transform**: Specially designed to handle signals with missing data points
- **Multiple Wavelet Types**: Support for Morlet, Paul, and DOG (Derivative of Gaussian) wavelets
- **High Performance**: Numba-accelerated computations with parallel processing
- **Scale-Period-Frequency Conversion**: Convenient utilities to interpret results in time or frequency domains
- **Signal Reconstruction**: Reconstruct signals from their wavelet transforms, even when original data has gaps

## Installation

```bash
pip install adawavelet
```

Or install from source:

```bash
git clone https://github.com/yourusername/adawavelet.git
cd adawavelet
pip install -e .
```

## Quick Start

```python
import numpy as np
from adawavelet import AdaptativeWaveletTransform

# Create an example signal with gaps
t = np.linspace(0, 10, 1000)
signal = np.sin(2*np.pi*t) + 0.5*np.sin(8*np.pi*t)
gaps = np.ones_like(signal)  # 1 = valid data, 0 = gap
gaps[300:350] = 0  # Create a gap

# Initialize the wavelet transform
awt = AdaptativeWaveletTransform(
    mother='MORLET',
    n_scales=50,
    min_scale=10,
    max_scale=500
)

# Perform the transform
scales, periods, frequencies, std_spectrum, gap_spectrum, transforms = awt.transform(signal, gaps)

# Reconstruct the signal, filling in the gaps
reconstructed = awt.reconstruct_from_gapped_wavelet()

# The result now contains a filled-in version of the original signal
```

## Documentation

For detailed documentation, examples, and API reference, please visit our [documentation site](https://adawavelet.readthedocs.io/).

## Gallery of Examples

Below are some example outputs from AdaWavelet:

1. **Wavelet Power Spectrum**: Comparing standard wavelet transform with gap-aware transform
2. **Scalogram Visualization**: Time-scale representation of signal components
3. **Gap Filling**: Original signal with gaps vs. reconstructed continuous signal

(Note: Image links to be added once the package is more complete)

## Theoretical Background

AdaWavelet implements a gapped wavelet transform based on the following papers:

- Frick et al. (1997), "Wavelet analysis of signals with gaps"
- Torrence & Compo (1998), "A Practical Guide to Wavelet Analysis"

The key innovation is adapting the wavelet analysis to accommodate missing data points, which is particularly useful for:

- Astronomical time series
- Geological data
- Oceanographic measurements
- Any signal with intermittent sampling or data gaps

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

1. Clone the repository
2. Install development dependencies: `pip install -r requirements-dev.txt`
3. Install the package in development mode: `pip install -e .`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use AdaWavelet in your research, please cite:

```
@software{adawavelet2025,
  author = {Your Name},
  title = {AdaWavelet: Adaptive Wavelet Analysis with Gap Handling},
  year = {2025},
  url = {https://github.com/yourusername/adawavelet}
}
```

## Contact

For questions and feedback, please open an issue on GitHub or contact the maintainers directly.