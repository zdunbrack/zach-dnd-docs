#!/c/Users/zachd/AppData/Local/Microsoft/WindowsApps/python
import os
from pathlib import Path

os.system("rm -rf content/*")
os.system("cp -r /c/Users/zachd/Documents/aemora/* ./content")

def removeUnpublishedFiles(fileText, fullPath):
  if "- publish" not in fileText:
    os.remove(fullPath)
    return True
  return False

def filterContent(fileText):
  # remove publish tag
  REMOVE_TAG_STRING = "  - publish"
  content = fileText.strip().replace(REMOVE_TAG_STRING, "")
  # remove 
  HIDE_TEXT_AFTER_KEY = "# Private"
    # for stuff that's published, only keep the content that's supposed to be published
  return content.split(HIDE_TEXT_AFTER_KEY)[0].strip()

for root, subdirs, files in os.walk('./content'):
  for fileName in files:
    fullPath = os.path.join(root, fileName)
    # only try to read markdown files, otherwise encoding can fail
    if ".md" in fullPath:
      # read original text
      with open(fullPath, 'r', encoding='utf-8') as file:
        fileText = file.read()
      # if it's not supposed to be published, trash it.
      # if it is supposed to be published, remove private content and #publish tag.
      if not removeUnpublishedFiles(fileText, fullPath):
        filteredFileText = filterContent(fileText)
        if filteredFileText.split("---")[2].strip():
          with open(fullPath, 'w', encoding='utf-8') as file:
            file.write(filteredFileText)
        else:
          os.remove(fullPath)
