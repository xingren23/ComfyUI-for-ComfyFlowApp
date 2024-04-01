#This is an example that uses the websockets api to know when a prompt execution is done
#Once the prompt execution is done it downloads the images using the /history endpoint

import websocket #NOTE: websocket-client (https://github.com/websocket-client/websocket-client)
import uuid
import json
import urllib.request
import urllib.parse
import os
import time
import shutil
import argparse

COMFYUI_PATH = os.environ.get("COMFYUI_PATH", "comfyui")
COMFYUI_SERVER_ADDRESS = os.environ.get("COMFYUI_SERVER_ADDRESS", "127.0.0.1:8188")
client_id = str(uuid.uuid4())

def queue_prompt(prompt):
    p = {"prompt": prompt, "client_id": client_id}
    data = json.dumps(p).encode('utf-8')
    req =  urllib.request.Request("http://{}/prompt".format(COMFYUI_SERVER_ADDRESS), data=data)
    return json.loads(urllib.request.urlopen(req).read())

def get_image(filename, subfolder, folder_type):
    data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
    url_values = urllib.parse.urlencode(data)
    with urllib.request.urlopen("http://{}/view?{}".format(COMFYUI_SERVER_ADDRESS, url_values)) as response:
        return response.read()

def get_history(prompt_id):
    with urllib.request.urlopen("http://{}/history/{}".format(COMFYUI_SERVER_ADDRESS, prompt_id)) as response:
        return json.loads(response.read())

def run_workflow_api(file):
    try:
      start = time.time()
      print(f"Run workflow {file}")
      with open(file, "r") as f:
        prompt = json.load(f)
        prompt_id = queue_prompt(prompt)['prompt_id']
        output_images = {}

        ws = websocket.WebSocket()
        ws.connect("ws://{}/ws?clientId={}".format(COMFYUI_SERVER_ADDRESS, client_id))
        while True:
          out = ws.recv()
          if isinstance(out, str):
            message = json.loads(out)
            print("recv ", message)
            if message['type'] == 'executing':
              data = message['data']
              if data['node'] is None and data['prompt_id'] == prompt_id:
                end = time.time()
                print(f"websocket_api|{file}|{round(end-start, 2)}|Success|{prompt_id}")
                break #Execution is done
          else:
            continue #previews are binary data

        history = get_history(prompt_id)[prompt_id]
        for o in history['outputs']:
          for node_id in history['outputs']:
            node_output = history['outputs'][node_id]
            if 'images' in node_output:
              images_output = []
              for image in node_output['images']:
                image_data = get_image(image['filename'], image['subfolder'], image['type'])
                images_output.append(image_data)
              output_images[node_id] = images_output

        return output_images
    except Exception as e:
      end = time.time()
      # 保留2为小数
      print(f"websocket_api|{file}|{round((end-start), 2)}|Error|{e}")

def run_path_workflow_api(path):
  # loop dir to run all api file
  print(f"Run all workflow in {path}")
  for file in os.listdir(path):
    # check is file
    if os.path.isfile(os.path.join(path, file)):
      if file.endswith("_api.json"):
        run_workflow_api(os.path.join(path, file))
      if file.index("disable") > 0:
        print(f"Skip {file}")
      else:
        print(f"Skip {file}")
    
    # chedck is dir
    elif os.path.isdir(os.path.join(path, file)):
      run_path_workflow_api(os.path.join(path, file))
  print(f"Run all workflow in {path} done")

def run_files_workflow_api(workflow_files):
  print(f"Run workflow {workflow_files}")
  for line in workflow_files:
    file = line.strip()
    print(f"Run workflow {file}")
    if file.endswith("_api.json"):
      run_workflow_api(file)
  print(f"Run workflow {workflow_files} done")

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description='Run workflow')
  parser.add_argument('--files', type=str, help='files, workflow file separated by comma')
  parser.add_argument('--path', type=str, help='path, run all workflow api json in the path')
  args = parser.parse_args()

  if args.files:
    workflow_files = args.files.split(",")
    run_files_workflow_api(workflow_files)

  if args.path:
    run_path_workflow_api(args.path)


