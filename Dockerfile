ARG BASE_IMAGE="ubuntu:22.04"

FROM ${BASE_IMAGE}

ARG PYTORCH_INSTALL_ARGS=""
ARG EXTRA_ARGS=""
ARG USERNAME="comfyui"
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

# Prevents prompts from packages asking for user input during installation
ENV DEBIAN_FRONTEND=noninteractive
# Prefer binary wheels over source distributions for faster pip installations
ENV PIP_PREFER_BINARY=1
# Ensures output from python is printed immediately to the terminal without buffering
ENV PYTHONUNBUFFERED=1 

RUN \
	--mount=target=/var/lib/apt/lists,type=cache,sharing=locked \
	--mount=target=/var/cache/apt,type=cache,sharing=locked \
	set -eux; \
		apt-get update; \
		apt-get install -y --no-install-recommends \
			python3.10 \
			python3-dev \
			python3-pip \
			python3-venv \
			git \
			wget \
			git-lfs \
 			rsync \
			ffmpeg \
			libsm6 \
			libxext6 \
			build-essential

# Clean up to reduce image size
RUN apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

RUN set -eux; \
	groupadd --gid ${USER_GID} ${USERNAME}; \
	useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME}

# run instructions as user
USER ${USER_UID}:${USER_GID}

WORKDIR /workspace/comfyui

ENV PIP_CACHE_DIR="/cache/pip"
ENV VIRTUAL_ENV=/workspace/comfyui/venv
ENV VIRTUAL_ENV_CUSTOM=/workspace/comfyui/custom_venv
ENV TRANSFORMERS_CACHE="/workspace/comfyui/.cache/transformers"

# create cache directory
RUN mkdir -p ${TRANSFORMERS_CACHE}

# create virtual environment to manage packages
RUN python3 -m venv ${VIRTUAL_ENV}

# run python from venv
ENV PATH="${VIRTUAL_ENV_CUSTOM}/bin:${VIRTUAL_ENV}/bin:${PATH}"

RUN --mount=type=cache,target=/cache/,uid=${USER_UID},gid=${USER_GID} \
	pip install torch torchvision torchaudio ${PYTORCH_INSTALL_ARGS}

# copy requirements files first so packages can be cached separately
COPY --chown=${USER_UID}:${USER_GID} requirements.txt .
RUN --mount=type=cache,target=/cache/,uid=${USER_UID},gid=${USER_GID} \
	pip install -r requirements.txt


COPY --chown=${USER_UID}:${USER_GID} . .
RUN pip install -r custom_nodes/custom_nodes_requirements.txt

# default environment variables
ENV COMFYUI_ADDRESS=0.0.0.0
ENV COMFYUI_PORT=8188
ENV COMFYUI_EXTRA_BUILD_ARGS="${EXTRA_ARGS}"
ENV COMFYUI_EXTRA_ARGS=""
# default start command
CMD if [ -d "${VIRTUAL_ENV_CUSTOM}" ]; then rsync -aP "${VIRTUAL_ENV}/" "${VIRTUAL_ENV_CUSTOM}/"; fi;\
  python3 -u main.py --listen ${COMFYUI_ADDRESS} --port ${COMFYUI_PORT} ${COMFYUI_EXTRA_BUILD_ARGS} ${COMFYUI_EXTRA_ARGS}