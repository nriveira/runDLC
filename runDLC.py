import deeplabcut

config_path = "PATH_TO_CONFIG_FILE"
deeplabcut.create_training_dataset(config_path, windows2linux=True)
deeplabcut.train_network(config_path)
