#!/c/Users/zachd/AppData/Local/Microsoft/WindowsApps/python
import os
from pathlib import Path

os.system("rm -rf content/*")
os.system("cp -r /c/Users/zachd/Documents/aemora/* ./content")

for root, subdirs, files in os.walk('./content'):
  for file in files:
    fullPath = os.path.join(root, file)
    content = open(fullPath).read()
    if ".md" in file and """
tags:
  - publish
""" not in content:
      os.remove(fullPath)
    else:
      separator = "# Private"
      if len(content.split(separator)) > 1:
        print(content.split(separator)[1])
