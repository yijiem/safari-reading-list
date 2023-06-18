#!/usr/bin/env python3

from xml.dom.minidom import parse

# encountered a ReadingList text node?
reading_list = False
# encountered a URLString text node?
url_string = False

urls = []

def goParse(node):
  global reading_list
  global urls
  global url_string
  if node is None:
    return
  if node.nodeValue == "ReadingList":
    reading_list = True
  elif reading_list is True and node.nodeValue == "URLString":
    url_string = True
  elif url_string is True and node.nodeType == node.ELEMENT_NODE:
    # well this is fun
    urls.append(''.join(node.firstChild.nodeValue))
    reading_list = False
    url_string = False
  for child in node.childNodes:
    goParse(child)

document = parse("Bookmarks.plist.xml")

goParse(document)

with open('ReadingList.md', 'w') as f:
  for u in urls:
    f.write(u)
    f.write('\n\n')

