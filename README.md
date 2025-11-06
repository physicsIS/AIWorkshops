# AI Workshops

This repository contains resources and materials for AI workshops covering fundamental and advanced topics in artificial intelligence and machine learning.

## Topics Covered

- **01-Introduction_to_ML**: Foundational concepts in machine learning (PDF materials)
- **02-Markov_Chains**: Markov chain implementation with text generation and visualization
- **03-Autoencoders**: Basic autoencoders for MNIST, including latent space visualization and image denoising
- **04-Variational-Autoencoders**: Variational autoencoders (VAE) with latent space interpolation and image generation

## Requirements

The following Python libraries are required for working with the workshop materials:

```bash
pip install torch torchvision
pip install numpy matplotlib
pip install scikit-learn tqdm
pip install jupyter notebook
pip install pillow
```

### Libraries by Topic

**Markov Chains:**
- `numpy` - Numerical computing
- `matplotlib` - Visualization
- `random` - Random number generation

**Autoencoders:**
- `torch` - Deep learning framework
- `torchvision` - Computer vision datasets and utilities
- `matplotlib` - Visualization
- `numpy` - Numerical operations
- `scikit-learn` - PCA and t-SNE for dimensionality reduction
- `tqdm` - Progress bars

**Variational Autoencoders:**
- `torch` - Deep learning framework
- `torchvision` - MNIST dataset and transforms
- `matplotlib` - Visualization
- `numpy` - Array operations
- `PIL` (Pillow) - Image processing
- `tqdm` - Progress bars

## Getting Started

1. Clone this repository
2. Install the required dependencies
3. Navigate to the specific workshop folder
4. Open Jupyter notebooks or run Python scripts

## Repository Structure

```
.
├── 01-Introduction_to_ML/          # ML fundamentals (PDF)
├── 02-Markov_Chains/               # Markov chain text generation
│   └── markov_chain.py
├── 03-Autoencoders/                # Basic autoencoder implementation
│   └── ae.ipynb
└── 04-Variational-Autoencoders/    # VAE implementation and training
    ├── vae_train_mnist.ipynb
    └── vae_train_mnist_solution.ipynb
```

## Workshop Highlights

**Autoencoders:**
- Training autoencoders with different latent dimensions
- Latent space visualization using t-SNE
- Image denoising and reconstruction
- MNIST digit encoding and decoding

**Variational Autoencoders:**
- VAE architecture with encoder-decoder structure
- Training with reconstruction loss and KL divergence
- Latent space interpolation between digits
- Generating new samples from latent codes
