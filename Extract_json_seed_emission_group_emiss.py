# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 17:24:05 2021

@author: Huang
"""

import json
from copy import deepcopy

with open('via_project_6Jul2020_22h54m_coco.json','r') as f:
        input_json = json.load(f)

new_json = deepcopy(input_json)

annotations = input_json['annotations']  #  a list
image= input_json['images']
categories = input_json['categories']
categorielist=[]
for b in range(len(categories)):
    categorielist.append(categories[b]['id']) #get the categories list

annotation_temp=[]
for c in range(len(annotations)):
    if annotations[c]['category_id'] == categorielist[0] or annotations[c]['category_id'] == categorielist[3] or annotations[c]['category_id'] == categorielist[4]: #Seed, emission, group emission id
        annotation_temp.append(annotations[c]) #append seed, emission and group emiss to annotation list

new_json['annotations']=annotation_temp # put the annotation list into the new_json dict
new_annotations= new_json['annotations']
annotations_idlist = []
image_idlist= []
for k in range(len(image)):
    for i in range(len(new_annotations)):
        if new_annotations[i]['image_id'] == image[k]['id']:
            image_idlist.append(image[k]['id']) #The the image name match whats on the json file then extract those name to the new list
            
#print(image_idlist)
imgfinal=[]
[imgfinal.append(x) for x in image_idlist if x not in imgfinal] #Eliminate duplicates in the image_idlist.- since one image could have different label

#print(imgfinal)
new_image=[]
for a in imgfinal:
    img_temp=deepcopy(image[a])
    new_image.append(img_temp) #put the image info to a new list base on its id we got from imgfinal

# image_temp = deepcopy(image[k])
new_json['images'] = new_image #put the new_image information list into new_json dict

with open("emiss_seed_group_emiss.json","w") as f: #Creat a new json file and write into it
      json.dump(new_json,f)
