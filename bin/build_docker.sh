# !/bin/bash

# check version parameter
if [ "$#" -ne 1 ]; then
    echo "please input 'version' parameter."
    exit 1
fi
version=$1
echo "build Version: $version"

# set comfyui path
CURRENT_PATH=${COMFYUI_PATH:-"/workspace/comfyui"}
echo "ComfyUI path: ${CURRENT_PATH}"
cd ${CURRENT_PATH}
echo "Current path: $(pwd)"
COMFYUI_PATH=${CURRENT_PATH}

# # clean .pyc 
# find . -name '*.pyc' -delete
# # clean __pycache__ 
# find . -type d -name '__pycache__' -exec rm -r {} +

# rm symlink
if [ -L "${COMFYUI_PATH}/models" ]; then
  echo "Removing symlink ${COMFYUI_PATH}/models"
  rm "${COMFYUI_PATH}/models"
fi

# docker build
echo "docker build comfyui, version: comfyui-for-comfyflowapp-cu121-${version}"
docker buildx build -t xingren23/comfyui-for-comfyflowapp:comfyui-for-comfyflowapp-cu121-${version} --build-arg PYTORCH_INSTALL_ARGS="--index-url https://download.pytorch.org/whl/cu121" .