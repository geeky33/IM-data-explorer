import h5py
import numpy as np
from pathlib import Path

class EmbeddingStorage:
    def __init__(self, hdf5_path="embeddings.h5"):
        self.hdf5_path = Path(hdf5_path)

    def save_embedding(self, emb_type, emb_id, embedding):
        """
        emb_type: 'image' or 'text'
        emb_id: a unique string ID (e.g., filename or caption hash)
        embedding: numpy array
        """
        with h5py.File(self.hdf5_path, "a") as f:
            group = f.require_group(emb_type)
            group.create_dataset(emb_id, data=embedding)

    def load_embedding(self, emb_type, emb_id):
        with h5py.File(self.hdf5_path, "r") as f:
            return f[emb_type][emb_id][...]

    def list_ids(self, emb_type):
        with h5py.File(self.hdf5_path, "r") as f:
            return list(f[emb_type].keys())
