import numpy as np
from sklearn.decomposition import PCA

def compute_pca(embeddings, n_components=2):
    """
    embeddings: numpy array of shape (N, D)
    n_components: target dimension (usually 2 or 3)

    Returns: numpy array of shape (N, n_components)
    """
    pca = PCA(n_components=n_components)
    reduced = pca.fit_transform(embeddings)
    return reduced
