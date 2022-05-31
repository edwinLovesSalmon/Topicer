# "Topicer"  An topic listener application for youtube trends
> This project displays the information about the top trending videos of a youtube

## Features
##### Main Functionality
> User can train a top2vec model using a functionaries/train.py file using a command
	!python train.py --dataFilePath='/content/drive/MyDrive/USvideos.csv' --columns=['title','description'] --outputFolderPath='/content'

> User can get the topic of each trending video
	-> go to the project directory from command line
	-> run this command: uvicorn main:app --reload
	-> open: http://localhost:8000/ in the browser 

##### Input
> This accepts the video as an input

### Directory Structure
        
        ├── data # contains the relevant data
        ├── templates
            ├── index.htm               #home page template
                
        ├── Functionaries
	    ├── train.py      # a python implementaion to train your own model
	    ├── youtube.py    # a python implmentation to get top trending videos
            ├── get_results.py    # a python implementation to get the topic keywords for each video
        ├── main.py   
        └── README.md
        
        
