import deeplabcutcore as deeplabcut
import tensorflow

config = "C:\\Users\\nrive\\Research\\DLC-Models-Copy\\AnkGDLC-EnriqueV2\\config.yaml"
vidPath = ["C:\\Users\\nrive\\Research\\AnkG\\Videos\\Mouse-3", "C:\\Users\\nrive\\Research\\AnkG\\Videos\\Mouse-4", "C:\\Users\\nrive\\Research\\AnkG\\Videos\\Mouse-5"]

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