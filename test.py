#!/c/Users/zachd/AppData/Local/Microsoft/WindowsApps/python
import os

os.system("cp -r /c/Users/zachd/Documents/aemora ./content")
for root, subdirs, files in os.walk("."):
  for file in files:
    print(file)
