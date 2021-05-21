singularity exec --nv --env DLClight=True --home $PWD \
		  -B local_models/:/usr/local/lib/python3.6/dist-packages/deeplabcut/pose_estimation_tensorflow/models/pretrained/ \
		  colginlab_latest.sif python3 runDLC.py
