<div align="center">

# ComfyUI Thera
[![Paper](https://img.shields.io/badge/arXiv-PDF-b31b1b)](https://arxiv.org/abs/2311.17643)
[![Page](https://img.shields.io/badge/Project-Page-green)](https://therasr.github.io)
[![License](https://img.shields.io/badge/License-Apache--2.0-929292)](https://www.apache.org/licenses/LICENSE-2.0)

This project is an unofficial ComfyUI implementation of [Thera](https://github.com/prs-eth/thera) (Aliasing-Free Arbitrary-Scale Super-Resolution with Neural Heat Fields)

<img height="350" src="https://github.com/user-attachments/assets/956de75b-c331-49b7-87d0-aad482734a25" />

</div>


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
