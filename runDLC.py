import sys
import deeplabcut

print(sys.argv[1])
config_path = sys.argv[1]
deeplabcut.create_training_dataset(config_path)
deeplabcut.train_model(config_path)
