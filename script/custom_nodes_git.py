import os
import subprocess

def git_remote_v(folder_path):
    for item in os.listdir(folder_path):
        dir_path = os.path.join(folder_path, item)
        if os.path.isdir(dir_path) and '.git' in os.listdir(dir_path):  # Check if the item is a directory and a Git repository
            print(f"Executing 'git remote -v' in {dir_path}")
            subprocess.run(["git", "remote", "-v"], cwd=dir_path)

# Replace '/path/to/MyProjects' with the path to your folder
git_remote_v('/workspace/comfyui/custom_nodes/')