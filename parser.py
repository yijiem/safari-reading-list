#!/usr/bin/env python3

from xml.dom.minidom import parse

# encountered a ReadingList text node?
reading_list = False
# encountered a URLString text node?
url_string = False
# encountered a title text node?
title = False

title_s = ''
urls = []

def goParse(node):
  global reading_list
  global urls
  global url_string
  global title
  global title_s
  if node is None:
    return
  if node.nodeValue == "ReadingList":
    reading_list = True
  elif reading_list is True and node.nodeValue == "title":
    title = True
  elif title is True and node.nodeType == node.ELEMENT_NODE:
    if node.firstChild is not None:
      title_s = ''.join(node.firstChild.nodeValue)
      title = False
  elif reading_list is True and node.nodeValue == "URLString":
    url_string = True
  elif url_string is True and node.nodeType == node.ELEMENT_NODE:
    # well this is fun
    urls.append((title_s, ''.join(node.firstChild.nodeValue)))
    reading_list = False
    url_string = False
    title = False
  for child in node.childNodes:
    goParse(child)

document = parse("Bookmarks.plist.xml")

goParse(document)

with open('ReadingList.md', 'w') as f:
  for u in urls:
    f.write(u[0])
    f.write('\n\n')
    f.write(u[1])
    f.write('\n\n')

