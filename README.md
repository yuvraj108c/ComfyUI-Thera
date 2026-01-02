<div align="center">

# ComfyUI Thera
[![Paper](https://img.shields.io/badge/arXiv-PDF-b31b1b)](https://arxiv.org/abs/2311.17643)
[![Page](https://img.shields.io/badge/Project-Page-green)](https://therasr.github.io)
[![License](https://img.shields.io/badge/License-Apache--2.0-929292)](https://www.apache.org/licenses/LICENSE-2.0)

This project is an unofficial ComfyUI implementation of [Thera](https://github.com/prs-eth/thera) (Aliasing-Free Arbitrary-Scale Super-Resolution with Neural Heat Fields)

**Last tested**: 2 January 2026 (ComfyUI v0.7.0@f2fda02 | Torch 2.9.1 | Python 3.10.12 | RTX4090 | CUDA 13.0 | Debian 12)

<img height="350" src="https://github.com/user-attachments/assets/956de75b-c331-49b7-87d0-aad482734a25" />

</div>

## ⭐ Support
If you like my projects and wish to see updates and new features, please consider supporting me. It helps a lot! 

[![ComfyUI-Depth-Anything-Tensorrt](https://img.shields.io/badge/ComfyUI--Depth--Anything--Tensorrt-blue?style=flat-square)](https://github.com/yuvraj108c/ComfyUI-Depth-Anything-Tensorrt)
[![ComfyUI-Upscaler-Tensorrt](https://img.shields.io/badge/ComfyUI--Upscaler--Tensorrt-blue?style=flat-square)](https://github.com/yuvraj108c/ComfyUI-Upscaler-Tensorrt)
[![ComfyUI-Dwpose-Tensorrt](https://img.shields.io/badge/ComfyUI--Dwpose--Tensorrt-blue?style=flat-square)](https://github.com/yuvraj108c/ComfyUI-Dwpose-Tensorrt)
[![ComfyUI-Rife-Tensorrt](https://img.shields.io/badge/ComfyUI--Rife--Tensorrt-blue?style=flat-square)](https://github.com/yuvraj108c/ComfyUI-Rife-Tensorrt)

[![ComfyUI-Whisper](https://img.shields.io/badge/ComfyUI--Whisper-gray?style=flat-square)](https://github.com/yuvraj108c/ComfyUI-Whisper)
[![ComfyUI_InvSR](https://img.shields.io/badge/ComfyUI__InvSR-gray?style=flat-square)](https://github.com/yuvraj108c/ComfyUI_InvSR)
[![ComfyUI-Thera](https://img.shields.io/badge/ComfyUI--Thera-gray?style=flat-square)](https://github.com/yuvraj108c/ComfyUI-Thera)
[![ComfyUI-Video-Depth-Anything](https://img.shields.io/badge/ComfyUI--Video--Depth--Anything-gray?style=flat-square)](https://github.com/yuvraj108c/ComfyUI-Video-Depth-Anything)
[![ComfyUI-PiperTTS](https://img.shields.io/badge/ComfyUI--PiperTTS-gray?style=flat-square)](https://github.com/yuvraj108c/ComfyUI-PiperTTS)

[![buy-me-coffees](https://i.imgur.com/3MDbAtw.png)](https://www.buymeacoffee.com/yuvraj108cZ)
[![paypal-donation](https://i.imgur.com/w5jjubk.png)](https://paypal.me/yuvraj108c)
---

## Installation
Navigate to `/ComfyUI/custom_nodes` directory
```bash
git clone https://github.com/yuvraj108c/ComfyUI-Thera
cd ComfyUI-Thera
pip install -r requirements.txt
```

## Usage
- Load [example workflow](workflows/thera_workflow.json) 
- Models will be autodownloaded to `/ComfyUI/models/Thera`

## Citation

```
@article{becker2025thera,
  title={Thera: Aliasing-Free Arbitrary-Scale Super-Resolution with Neural Heat Fields},
  author={Becker, Alexander and Daudt, Rodrigo Caye and Narnhofer, Dominik and Peters, Torben and Metzger, Nando and Wegner, Jan Dirk and Schindler, Konrad},
  journal={arXiv preprint arXiv:2311.17643},
  year={2025}
}
```
## Acknowledgments
Thanks to [simplepod.ai](https://simplepod.ai/) for providing GPU servers
