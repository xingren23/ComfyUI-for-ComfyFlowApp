# !/bin/bash

# 设置 comfyui 路径
CURRENT_PATH=${COMFYUI_PATH:-"/workspace/comfyui"}
echo "ComfyUI path: ${CURRENT_PATH}"
cd ${CURRENT_PATH}
echo "Current path: $(pwd)"
COMFYUI_PATH=${CURRENT_PATH}

# 判断是否是链接
if [ -L "${COMFYUI_PATH}/models" ]; then
  echo "Removing symlink ${COMFYUI_PATH}/models"
  rm "${COMFYUI_PATH}/models"
else
  echo "Removing path ${COMFYUI_PATH}/models"
  rm -rf "${COMFYUI_PATH}/models"
fi

# 获取模型路径，默认为 /workspace/models
MODELS_PATH=${COMFYUI_MODELS_PATH:-"/workspace/models"}

# 创建链接
echo "Creating symlink from ${MODELS_PATH} to ${COMFYUI_PATH}/models"
ln -s "${MODELS_PATH}" "${COMFYUI_PATH}/models"

echo "Starting ComfyUI server"
nohup python -u main.py --port=8188 --preview-method auto --force-fp16 > comfyui.log 2>&1 &

