#!/c/Users/zachd/AppData/Local/Microsoft/WindowsApps/python
import os
from pathlib import Path

os.system("rm -rf content/*")
os.system("cp -r /c/Users/zachd/Documents/aemora/* ./content")


def removePrivateContent(fileText):
  HIDE_TEXT_AFTER_KEY = "# Private"
  return fileText

def filterIfMetadataOnly(fileText):
  return fileText

for root, subdirs, files in os.walk('./content'):
  for file in files:
    fullPath = os.path.join(root, file)
    print(fullPath)
    # only try to read markdown files, otherwise encoding can fail
    if ".md" in fullPath:
      with open(fullPath, 'r', encoding='utf-8') as file:
        content = open(fullPath).read()
      # filter out anything not supposed to be published
      if """
tags:
  - publish
""" not in content:
        os.remove(fullPath)
      else:
        print(f"not removing {fullPath}")
      # for stuff that's published, only keep the content that's supposed to be published
      # elif len(content.split(HIDE_TEXT_AFTER_KEY)) < 2:
      #   print(str(content.split(HIDE_TEXT_AFTER_KEY)[0]))
      #   # print(content.split(separator)[1])
    
