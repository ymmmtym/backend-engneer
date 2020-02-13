# -*- coding: utf-8 -*-

import os
import glob
import re
import sys
import io
import yaml
from jinja2 import Template, Environment, FileSystemLoader


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
data = yaml.safe_load(open("./templates/mkdocs.yml.base", "r+"))
title = os.getcwd().split('/')[-1].replace('-',' ').title()
docs_path = './docs/'
index = 'index.md'
html = r"\.html$|\.css$|\.js$"
pattern = r"\.md$"
doc_dict = {}
os.chdir(docs_path)


def is_html(path):
  dir_list = os.listdir(path)
  if 'index.html' in dir_list:
    return True
    
def in_html(path):
  split_path = path.split('/')
  parent_path = '/'.join(split_path[:-1])
  grand_path = '/'.join(split_path[:-2])
  if len(split_path) > 1 and is_html(parent_path):
    return True
  elif len(grand_path) > 2 and is_html(grand_path):
    return True
  return re.match(html, split_path[-1])

def create_dict(path):
  l = path.split('/')
  name = re.sub(pattern, "", l[-1]).title()
  key = l[-2].title()
  doc_dict[key].append({name: path})

for i in sorted(glob.glob('**', recursive=True)):
  if i == index:
    pass
  elif in_html(i):
    pass
  elif os.path.isfile(i) or is_html(i):
    create_dict(i)
  elif os.path.isdir(i):
    doc_dict[i.title()] = []

for k,v in doc_dict.items():
  data["nav"].append({k: v})

with open("../mkdocs.yml", "w") as wf:
  yaml.dump(data, wf)