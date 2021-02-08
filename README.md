Applications needed: 
SSH client - I use PuTTY, it has a simple interface with all the features needed
Recommended: WinSCP - A GUI for transferring files to Maverick2
runDLC file

WIP - By accessing this through TACC, you may be able run without needing to download anything.

Installation and Accessing DeepLabCut:
Log on the Maverick2 computer system with both PuTTY and WinSCP, and create a new folder for your project by typing:

	cdw
	mkdir [name_of_directory]

This will change directory to the work directory, and make directory with the specified name. The work directory is used because we will need to write into the directory, which is not able to be done in the home directory.

Change your current directory to the new folder by typing: 

	cd [name_of_directory]

to enter the newly created folder. Using WinSCP, upload the runDLC and project files from your computer to your current directory by dragging and dropping the file.  

Unzip and run the contents of the folder. Since it is not permitted to run executables on the login nodes, we will also need to create an interactive development environment this can be done by typing:

	idev -L work
	unzip runDLCv2.zip
	./init.sh
	./container.sh

-L specifies that you will be interacting with the contents of the work directory. When running the application, also consider adding -m [number_of_minutes] to the idev line to specify how long before the system will return you back to the login node. The default is 30 minutes. (e.x if you plan to train the module for 10 hours, use -m 600)
Another issue I ran into was not having permission to access the files. The workaround for this is to first run 
		chmod 777 [name of file]
This will grant you access to the file specified. 

This will bring up a shell running the DeepLabCut environment. To get back to this step when working on your project, run:

	./container.sh

To get back to the environment.

Integrating Maverick2 into DeepLabCut workflow
Detailed instructions for running DLC “normally” can be found at https://github.com/DeepLabCut/DeepLabCut/blob/master/docs/UseOverviewGuide.md

The first step is creating a new project and labeling datasets on your local computer, as you would normally if you planned to create and train a dataset. 

DeepLabCut finds the project by following the path directory specified in the config file in your Project folder. Since you are changing computers, change the config file’s path to match your project directory on Maverick2 inside of the config.yaml file. Your current directory can be found by typing

	pwd

Once this step is done, you are able to move the files to the same directory that your project is on and continue on from the Maverick2 computer through WinSCP. I would recommend zipping the file first to save time. From here, get back into the DLC container by running:
 		
	./conatiner.sh

Once inside of the container, run 

	export DLClight=True
	python3 runDLC  <full file_path_to_config_file>

This step will take several hours. It will tell display when a message every 1000 iterations and every 50,000 iterations will produce a more refined model that can be used. (Try and run for as many iterations as possible.) The runDLC program will create a training dataset and train the model. The model is now ready to be exported back to your computer to analyze videos. 
