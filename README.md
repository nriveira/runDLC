FUNCTIONAL, and now includes deeplabcutcore to simplify graphics card hassle.

Applications needed: 
SSH client - I use PuTTY, it has a simple interface with all the features needed
Recommended: WinSCP - A GUI for transferring files to Maverick2 (could also just use scp command)

Installation and Accessing DeepLabCut:
Log on the Maverick2 computer system with both PuTTY [and WinSCP] and type:

	cdw2

This will change directory to the work directory, and make directory with the specified name. The work directory is used because we will need to write into the directory, which is not able to be done in the home directory. Feel free to make a project folder for all of the contents, which can be done using 

	mkdir [name of directory]

To download the contents needed for DLC, use:

	git clone https://github.com/nriveira/runDLC.git

This will import the folder runDLC, which has all of the contents to run DLC on TACC.
Change your current directory to the new folder by typing: 

	cd runDLC
	
Note that you can go back in a directory by typing

	cd ..

Using WinSCP [or equivalent], upload the project file from your computer to your current directory.
BE SURE TO KEEP A BACKUP PROJECT FILE ON YOUR LOCAL COMPUTER SINCE DLC WILL OVERWRITE THINGS TO CONVERT TO UNIX (Windows/Linux do not use the same character for the end of lines, which becomes an issue when switching between systems.)
I have had many issues with this if I mess up a step, but it can be reverted by reuploading the file and redoing the steps.

Since it is not permitted to run executables on the login nodes, we will also need to create an interactive development environment. This can be done by typing:

	idev -L work2
	./init.sh
	./container.sh

-L specifies that you will be interacting with the contents of the work directory. When running the application, also consider adding

	-m [number_of_minutes] 

to the idev line to specify how long before the system will return you back to the login node. The default is 30 minutes. (e.x if you plan to train the module for 10 hours, use -m 600)
Another issue I ran into was not having permission to access the files. The workaround for this is to first run 

	chmod 770 [name of file]
This will grant you execute permission for the file specified. https://en.wikipedia.org/wiki/Chmod has more details on the different permission settings you can use.
To get back to this step when working on your project, run:

	./container.sh

To get back to the environment.

Integrating Maverick2 into DeepLabCut workflow
Detailed instructions for running DLC “normally” can be found at https://github.com/DeepLabCut/DeepLabCut/blob/master/docs/UseOverviewGuide.md
Here is an overview of the steps:
The first step is creating a new project and labeling datasets on your local computer, as you would normally if you planned to create and train a dataset. Then, the project file is imported to TACC to create a training dataset and train the model. After, the project can be moved back to your local computer or left on TACC to analyze video. I find the video uploads to TACC to be somewhat slow, so there is a tradeoff between running DLC on your computer and spending time uploading lots of videos to TACC.

Importing Project to TACC:
DeepLabCut finds the project by following the path directory specified in the config file in your Project folder. Since you are changing computers, change the config file’s path to match your project directory on Maverick2 inside of the config.yaml file. Your current directory can be found by typing

	pwd

Once this step is done, you are able to move the files to the same directory that your project is on and continue on from the Maverick2 computer through WinSCP. I would recommend zipping the file first to save time. From here, get back into the DLC container by running:
 		
	./conatiner.sh

Training the Model:
Once inside of the container, run 

	python3 runDLC.py <full file_path_to_config_file>

This step will take several hours. It will tell display when a message every 1000 iterations and every 50,000 iterations will produce a more refined model that can be used. (Try and run for as many iterations as possible.) The runDLC.py program will create a training dataset and train the model. The model is now ready to be exported back to your computer to analyze videos. 

Analyzing Video Using TACC:
You can also continue the analysis using TACC, this can be done in the interactive mode of python, found by running

	ipython
	import deeplabcutcore as deeplabcut
	deeplabcut.analyze_videos(config_path, [‘path of video 1’,‘path of video2’, ...], videotype='.mp4',save_as_csv=True)
	<ANY OTHER PYTHON LINES FOR DLC>
	
Hopefully this helps, and feel free to email me at nickriveira@utexas.edu for questions.
