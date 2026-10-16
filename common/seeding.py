import random
import numpy as np


def set_global_seed(seed: int) -> None:
    """Python ve NumPy tohumlarını ayarlar. PyTorch kuran ajanlar kendi içinde torch.manual_seed(seed) çağırmalı."""
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch
        torch.manual_seed(seed)
    except ImportError:
        pass
