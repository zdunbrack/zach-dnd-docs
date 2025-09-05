#!/c/Users/zachd/AppData/Local/Microsoft/WindowsApps/python
import os
from pathlib import Path

os.system("rm -rf content/*")
os.system("cp -r /c/Users/zachd/Documents/aemora/* ./content")

for root, subdirs, files in os.walk('./content'):
  for file in files:
    fullPath = os.path.join(root, file)
    print(fullPath)
    if ".md" in fullPath and "not campaign" not in fullPath:
      with open(fullPath, 'r', encoding='utf-8') as file:
        content = open(fullPath).read()
    if """
tags:
- publish
""" not in content:
      try:
        os.remove(fullPath)
      except Exception:
        print(f"failed to remove {fullPath}")
        pass
    else:
      separator = "# Private"
      if len(content.split(separator)) > 1:
        print(str(content.split(separator)))
        # print(content.split(separator)[1])
