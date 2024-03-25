
**Build the ComfyUI environment with one click and test related workflows.**

**This ComfyUI is the official version maintained by ComfyFlowApp. Workflows created in this version can also be published to [ComfyFlowApp](https://comfyflow.app) online**

# ComfyUI for ComfyFlowApp

The ComfyUI for ComfyFlowApp is the official version maintained by ComfyFlowApp, which includes several commonly used ComfyUI custom nodes. The online platform of ComfyFlowApp also utilizes this version, ensuring that workflow applications developed with it can operate seamlessly on ComfyFlowApp.

Instead of using ComfyUI-Manager to install missing nodes, the project carefully picks the custom nodes and verifies that there are no conflicts between them.

- [ComfyUI Segment Anything](https://github.com/storyicon/comfyui_segment_anything)
- [ComfyUI TiledKSampler](https://github.com/BlenderNeko/ComfyUI_TiledKSampler)
- [ComfyUI UltimateSDUpscale](https://github.com/ssitu/ComfyUI_UltimateSDUpscale)
- [ComfyUI InstantID](https://github.com/cubiq/ComfyUI_InstantID)
- [ComfyUI AnimateDiff Evolved](https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved)
- [ComfyUI Inpaint Nodes](https://github.com/Acly/comfyui-inpaint-nodes)
- [ComfyUI VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)
- [Rgthree Comfy](https://github.com/rgthree/rgthree-comfy)
- [ComfyUI FizzNodes](https://github.com/FizzleDorf/ComfyUI_FizzNodes)
- [ComfyUI Essentials](https://github.com/cubiq/ComfyUI_essentials)
- [ComfyUI Custom Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)
- [Efficiency Nodes ComfyUI](https://github.com/jags111/efficiency-nodes-comfyui)
- [ComfyUI Impact Pack](https://github.com/xingren23/ComfyUI-Impact-Pack)
- [ComfyUI-Inspire-Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack)
- [ComfyUI Advanced ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)
- [ComfyUi PromptStylers](https://github.com/wolfden/ComfyUi_PromptStylers)
- [OneButtonPrompt](https://github.com/AIrjen/OneButtonPrompt)
- [ComfyUi NNLatentUpscale](https://github.com/Ttl/ComfyUi_NNLatentUpscale)
- [ComfyUI WD14 Tagger](https://github.com/pythongosssss/ComfyUI-WD14-Tagger)
- [CG Use Everywhere](https://github.com/chrisgoringe/cg-use-everywhere)
- [ComfyUI DynamicPrompts](https://github.com/adieyal/comfyui-dynamicprompts)
- [WAS Node Suite ComfyUI](https://github.com/WASasquatch/was-node-suite-comfyui)
- [SDXL Prompt Styler](https://github.com/twri/sdxl_prompt_styler)
- [ControlNet LLLite ComfyUI](https://github.com/kohya-ss/ControlNet-LLLite-ComfyUI)
- [ComfyUI Layerdiffuse](https://github.com/huchenlei/ComfyUI-layerdiffuse)
- [ComfyUI Noise](https://github.com/BlenderNeko/ComfyUI_Noise)
- [ComfyUI IPAdapter Plus](https://github.com/cubiq/ComfyUI_IPAdapter_plus)
- [ComfyUI LayerStyle](https://github.com/chflame163/ComfyUI_LayerStyle)
- [ComfyUI ControlNet Aux](https://github.com/Fannovel16/comfyui_controlnet_aux)



## How to use

we only test comfyui-for-comfyflowapp on ubuntu(wsl) with NVIDIA GPUs

* install, use conda to manage python env
```
conda create -n comfyui
conda activate comfyui
git clone https://github.com/xingren23/ComfyUI-for-ComfyFlowApp
cd ComfyUI-for-ComfyFlowApp
pip install -r requirements.txt
```

* install comfyui and custom nodes , and then install packages required, default install path: /workspace/comfyui, you could change it with env COMFYUI_PATH
```python
python script/install_comfyui.py
```

* start comfyui, http://localhost:8888 , check the log in /workspace/comfyui/comfyui.log
```bash
sh bin/start_comfyui.sh
```

* stop comfyui
```bash
sh bin/stop_comfyui.sh
```

* run workflow, the project contains some commonly used workflows, as well as some workflows provided by custom nodes for everyone to learn and study.
```
sh run_workflow.sh
```

## Docker

Building images manually
You can build a docker image with the Dockerfile in this repo.

Specify PYTORCH_INSTALL_ARGS build arg with one of the PyTorch commands above to build for AMD or NVIDIA GPUs.

docker buildx --build-arg PYTORCH_INSTALL_ARGS="--index-url https://download.pytorch.org/whl/cu121" .

docker buildx --build-arg PYTORCH_INSTALL_ARGS="--index-url https://download.pytorch.org/whl/rocm5.6" .

docker buildx --build-arg PYTORCH_INSTALL_ARGS="--pre --index-url https://download.pytorch.org/whl/nightly/rocm5.7" .

This dockerfile requires BuildKit to be enabled. If your docker does not support the buildx command, you can enable BuildKit by setting the DOCKER_BUILDKIT environment variable.

DOCKER_BUILDKIT=1 docker build --build-arg PYTORCH_INSTALL_ARGS="--index-url https://download.pytorch.org/whl/cu121" .

NOTE: For building the CPU-only image, it is recommended that you add the --cpu flag to the EXTRA_ARGS build arg:

docker buildx --build-arg PYTORCH_INSTALL_ARGS="--index-url https://download.pytorch.org/whl/cpu" --build-arg EXTRA_ARGS=--cpu .


## Models
before start, start_comfyui.sh will create symlink of models with the env "COMFYUI_MODELS_PATH"

## Workflows 

* ComfyUI Example
https://github.com/comfyanonymous/ComfyUI_examples

* Custom_nodes

```custom_nodes/
├── ComfyUI-Advanced-ControlNet
├── ComfyUI-AnimateDiff-Evolved
├── ComfyUI-Custom-Scripts
├── ComfyUI-Image-Filters
├── ComfyUI-Impact-Pack
├── ComfyUI-Inspire-Pack
├── ComfyUI-VideoHelperSuite
├── ComfyUI-WD14-Tagger
├── ComfyUI-layerdiffuse
├── ComfyUI_FizzNodes
├── ComfyUI_IPAdapter_plus
├── ComfyUI_InstantID
├── ComfyUI_LayerStyle
├── ComfyUI_Noise
├── ComfyUI_TiledKSampler
├── ComfyUI_UltimateSDUpscale
├── ComfyUI_essentials
├── ComfyUi_NNLatentUpscale
├── ComfyUi_PromptStylers
├── ControlNet-LLLite-ComfyUI
├── OneButtonPrompt
├── cg-use-everywhere
├── comfyui-dynamicprompts
├── comfyui-inpaint-nodes
├── comfyui_controlnet_aux
├── comfyui_segment_anything
├── efficiency-nodes-comfyui
├── rgthree-comfy
├── sdxl_prompt_styler
└── was-node-suite-comfyui
```

* sdxl-lighting workflow

https://huggingface.co/ByteDance/SDXL-Lightning
https://huggingface.co/ByteDance/AnimateDiff-Lightning


## Credits

[ComfyUI](https://github.com/comfyanonymous/ComfyUI)
