#!/usr/bin/env python

import json
import sys
import re

for line in sys.stdin:
    line = line.strip()
    
    try:
        serial_json = json.loads(line)
    except:
        continue
    
    try:
        time_json = serial_json['node']['taken_at_timestamp'] 
        id_json = serial_json['node']['owner']['id'] 
        like_json = serial_json['node']['edge_liked_by']['count'] 
        text_json = serial_json['node']['edge_media_to_caption']['edges'][0]['node']['text'].encode('utf-8').strip() 
    except IndexError:
        continue
    
    if re.search( 'graduat', text_json, re.I):
        if re.search( '(commenc|ceremo)', text_json, re.I):
            if re.search( 'uga', text_json, re.I):
                print('%s\t%s\t%s' % (id_json, like_json, time_json)) 

