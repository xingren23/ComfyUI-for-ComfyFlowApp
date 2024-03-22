from git import Repo
import shutil
import subprocess
import os

COMFYUI_PATH = os.environ.get("COMFYUI_PATH", "ComfyUI")

comfyui_repo = "https://github.com/comfyanonymous/ComfyUI"

def clone_comfyui(repo, clean=True):
  # clone comfyui
  branch = repo.split(" ")[1] if len(repo.split(" ")) > 1 else "master"

  if clean:
    print(f"remove path {COMFYUI_PATH}")
    shutil.rmtree(f"{COMFYUI_PATH}", ignore_errors=True)

  try:
    print(f"Cloning {comfyui_repo} to {COMFYUI_PATH}")
    Repo.clone_from(comfyui_repo, COMFYUI_PATH, branch=branch)
  except:
    print(f"Repo {comfyui_repo} already cloned")

  return

# custom nodes repo
custom_nodes_repos = [
  "https://github.com/spacepxl/ComfyUI-Image-Filters",
  "https://github.com/storyicon/comfyui_segment_anything",
  "https://github.com/BlenderNeko/ComfyUI_TiledKSampler master",
  "https://github.com/ssitu/ComfyUI_UltimateSDUpscale",
  "https://github.com/cubiq/ComfyUI_InstantID",
  "https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved",
  "https://github.com/Acly/comfyui-inpaint-nodes",
  "https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite",
  "https://github.com/rgthree/rgthree-comfy",
  "https://github.com/FizzleDorf/ComfyUI_FizzNodes",
  "https://github.com/cubiq/ComfyUI_essentials",
  "https://github.com/pythongosssss/ComfyUI-Custom-Scripts",
  "https://github.com/jags111/efficiency-nodes-comfyui",
  "https://github.com/xingren23/ComfyUI-Impact-Pack Main",
  "https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet",
  "https://github.com/wolfden/ComfyUi_PromptStylers",
  "https://github.com/AIrjen/OneButtonPrompt",
  "https://github.com/Ttl/ComfyUi_NNLatentUpscale master",
  "https://github.com/pythongosssss/ComfyUI-WD14-Tagger",
  "https://github.com/chrisgoringe/cg-use-everywhere",
  "https://github.com/adieyal/comfyui-dynamicprompts",
  "https://github.com/WASasquatch/was-node-suite-comfyui",
  "https://github.com/twri/sdxl_prompt_styler",
  "https://github.com/kohya-ss/ControlNet-LLLite-ComfyUI",
  "https://github.com/huchenlei/ComfyUI-layerdiffuse",
  "https://github.com/BlenderNeko/ComfyUI_Noise master",
  "https://github.com/cubiq/ComfyUI_IPAdapter_plus",
  "https://github.com/chflame163/ComfyUI_LayerStyle",
  "https://github.com/Fannovel16/comfyui_controlnet_aux",
]

# clone or update repos
def clone_repos(repos, clean=True):

  for item in repos:
    repo = item.split(" ")[0]
    branch = item.split(" ")[1] if len(item.split(" ")) > 1 else "main"
    path_to_clone = f"{COMFYUI_PATH}/custom_nodes/{repo.split('/')[-1]}"

    # remove COMFYUI_PATH/custom_nodes
    if clean and os.path.exists(path_to_clone):
      print(f"remove path {path_to_clone}")
      shutil.rmtree(f"{path_to_clone}")

    # check if the repo is already cloned
    try:
      print(f"Cloning {repo} {branch} to ComfyUI/custom_nodes/{repo.split('/')[-1]}")
      Repo.clone_from(repo, f"{COMFYUI_PATH}/custom_nodes/{repo.split('/')[-1]}", single_branch=True, branch=branch, recursive=True)
    except:
      print(f"Clone {item} error")
    
  return

def install_requirements(requirements_file):
  # pip install -r requirements.txt
  print(f"Installing requirements from {requirements_file}")
  installed_packages = subprocess.run(["pip", "install", "-r", requirements_file])
  print(f"Installed package {installed_packages}")
  return installed_packages

def install_package(args):
  # pip install package  
  pip_install_args = args.split(" ")
  print(f"Installing package {pip_install_args}")
  subprocess.run(pip_install_args)
  return

def install_comfyui(clean=True):
  # pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121
  # pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121
  install_package("pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121 --upgrade")

  clone_comfyui(comfyui_repo, clean)
  comfyui_requirements = f"{COMFYUI_PATH}/requirements.txt"
  install_requirements(comfyui_requirements)
  return

def install_custom_nodes(clean=True):
  clone_repos(custom_nodes_repos, clean)
  custom_nodes_requirements = f"script/custom_nodes_requirements.txt"
  install_requirements(custom_nodes_requirements)

if __name__ == "__main__":
  
  install_comfyui()
  install_custom_nodes()

  print("Done")