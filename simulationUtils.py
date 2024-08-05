from matplotlib import pyplot as plt
import scipy.stats
from scipy.sparse import spmatrix, issparse, csr_matrix
from scipy.stats import multivariate_normal
from anndata import AnnData
from typing import Optional, Union
from shapely.geometry import Point, MultiPoint
from numpy.linalg import svd, solve, lstsq
from numpy.random import randn
import plotly.graph_objects as go
from scipy.spatial.transform import Rotation as R
from cytocraft.craft import *
from cytocraft.model import BasisShapeModel


def overided_generate_random_rotation_matrices(n, num_angles=16000):
    if n % 8 != 0:
        raise ValueError("n must be a multiple of 8.")

    # Generate rotation angles phi and theta
    phi = np.arccos(2 * np.random.rand(num_angles) - 1)
    theta = 2 * np.pi * np.random.rand(num_angles)
    # Convert to Cartesian coordinates
    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi)
    # Convert to rotation vectors
    rotation_vectors = np.stack((x, y, z), axis=-1)
    # Generate rotation matrices from rotation vectors
    rotations = R.from_rotvec(rotation_vectors)
    matrices = rotations.as_matrix()
    # Split matrices into 8 octants
    octants = [[] for _ in range(8)]
    for matrix, rotation_vector in zip(matrices, rotation_vectors):
        octant_index = (rotation_vector > 0).astype(int).dot(1 << np.arange(3))
        octants[octant_index].append(matrix)
    # Randomly sample matrices from each octant
    selected_matrices = []
    matrices_per_octant = n // 8
    for octant in octants:
        if len(octant) < matrices_per_octant:
            raise ValueError("Not enough matrices in one or more octants.")
        octant_matrices = np.array(octant)
        indices = np.random.choice(len(octant_matrices), matrices_per_octant, replace=True)
        selected_matrices.extend(octant_matrices[indices])
    return np.array(selected_matrices)





def add_salt_and_pepper_noise(simW, noise_ratio):
    noisy_simW = np.copy(simW)
    total_pixels = simW.size
    num_salt = np.ceil(noise_ratio * total_pixels * 0.5)
    num_pepper = np.ceil(noise_ratio * total_pixels * 0.5)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in simW.shape]
    noisy_simW[tuple(coords)] = np.max(simW)
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in simW.shape]
    noisy_simW[tuple(coords)] = np.min(simW)
    return noisy_simW
