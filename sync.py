#!/c/Users/zachd/AppData/Local/Microsoft/WindowsApps/python
import os
from pathlib import Path

os.system("rm -rf content/*")
os.system("cp -r /c/Users/zachd/Documents/aemora/* ./content")

for root, subdirs, files in os.walk('./content'):
  for file in files:
    fullPath = os.path.join(root, file)
    if ".md" in file and """
tags:
  - publish
""" not in open(fullPath).read():
      os.remove(fullPath)
    else:
      print(f"reading {fullPath}")
      print(open(fullPath).read())
