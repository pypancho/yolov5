# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:54:33 2019

@author: liuchao
"""
import json
import os
from copy import deepcopy
from shutil import copyfile

print('getcwd:      ', os.getcwd())

src_dir = 'C:/Users/Huang/Desktop/imagefolder/All/'
dst_dir = 'C:/Users/Huang/Desktop/imagefolder/Output_emiss_seed_group_emiss/'

with open('emiss_seed_group_emiss.json','r') as f:
        input_json = json.load(f)

new_json = deepcopy(input_json)
image=new_json['images']
img_names = []
for i in range(len(image)):
    if image[i]['file_name']:
        img_name = image[i]['file_name']
        img_names.append(img_name)
        src = src_dir + img_name
        dst = dst_dir + img_name
        copyfile(src, dst)