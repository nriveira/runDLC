import sys
import deeplabcutcore as deeplabcut

config_path = sys.argv[1]
deeplabcut.create_training_dataset(config_path)
deeplabcut.train_network(config_path)
