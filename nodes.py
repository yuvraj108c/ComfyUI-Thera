import folder_paths
import os
import numpy as np
import torch
import pickle
from comfy.utils import ProgressBar
from .utils import download_file

# Set environment variables for JAX memory management
os.environ["XLA_PYTHON_CLIENT_PREALLOCATE"] = "false"  # Disable preallocation
os.environ["XLA_PYTHON_CLIENT_ALLOCATOR"] = "platform"  # Enable dynamic allocation

class LoadTheraModel:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": (['thera-edsr-air', 'thera-edsr-plus', 'thera-edsr-pro', 'thera-rdn-air', 'thera-rdn-plus', 'thera-rdn-pro'],),
            },
        }

    RETURN_TYPES = ("THERA_PIPE",)
    RETURN_NAMES = ("thera_pipe",)
    FUNCTION = "loadmodel"
    CATEGORY = "Thera"

    def loadmodel(self, model):
        from .thera.model import build_thera

        thera_models_dir = os.path.join(folder_paths.models_dir, "thera")
        os.makedirs(thera_models_dir, exist_ok=True)
        thera_model_path = os.path.join(thera_models_dir, f"{model}.pkl")

        if not os.path.exists(thera_model_path):
            print(f"[ComfyUI-Thera] - Downloading {model}..")
            download_url = f"https://huggingface.co/prs-eth/{model}/resolve/main/model.pkl"
            download_file(url=download_url, save_path=thera_model_path)

        with open(thera_model_path, 'rb') as fh:
            check = pickle.load(fh)
            params, backbone, size = check['model'], check['backbone'], check['size']

        thera_model = build_thera(3, backbone, size)
        return ((thera_model, params),)

class TheraProcess:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "thera_pipe": ("THERA_PIPE",),
                "images": ("IMAGE",),
                "scale": ("FLOAT", {"default": 4.0, "step":0.1}),
                "patch_size": (["256", "512"], {"default": "256"}),
                "do_ensemble": ("BOOLEAN", {"default": False})
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "process"
    CATEGORY = "Thera"

    def process(self, thera_pipe, images, scale, patch_size, do_ensemble):
        print(f"[ComfyUI-Thera] - Input Shape: {images.shape}")

        from .thera.super_resolve import process as thera_process
        thera_model, params = thera_pipe
        
        images_cpu = images.cpu().numpy()
        batch_size = images_cpu.shape[0]
        pbar = ProgressBar(batch_size)
        out_batch = []
        
        for i in range(batch_size):
            source = np.clip(images_cpu[i], 0, 1)
            target_shape = (
                round(source.shape[0] * scale),
                round(source.shape[1] * scale),
            )
            out = thera_process(source, thera_model, params, target_shape, int(patch_size), do_ensemble)
            out_batch.append(np.asarray(out, dtype=np.float32).copy() / 255.0)
            pbar.update(1)
        
        result = torch.from_numpy(np.stack(out_batch, axis=0))
        print(f"[ComfyUI-Thera] - Output Shape: {result.shape}")
        return (result,)