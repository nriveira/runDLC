import deeplabcutcore as deeplabcut
import tensorflow

config = "/path/to/config.yaml"
vidPath = ["path/to/first/folder","path/to/second/folder", "path/to/third/folder"]

import os
import sys

for vid in vidPath:
    listVids = []
    path = os.walk(vid)
    for root, directories, files in path:
        for file in files:       
            if file.endswith('.avi'):
                currentVid = root+'\\'+file
                listVids.append(currentVid)
                
    deeplabcut.analyze_videos(config, listVids, videotype='.avi', save_as_csv = True)
