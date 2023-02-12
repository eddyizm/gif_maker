# gif_maker
convert still images to gif using Pillow

# Install   


```
python -m venv env
# activate environment
source env/Scripts/activate
# install requirements
pip install -r requirements.txt
```

# Usage  

```  
$ py gif_maker.py -h
usage: gif_maker.py [-h] [-c] [-d DIRECTORY] [-L]

Resizes and creates gif out of png files in specified directory

options:
  -h, --help            show this help message and exit
  -c, --config          pass in -c or --config to use a config.
  -d DIRECTORY, --directory DIRECTORY
                        directory where files are located.
  -L, --leave           leave processed files, default app removes all files except gif output.

And then there was gif...   
```

Current state needs the directory flag and path. 

`python gif_maker.py -d /path_to_files `

Several variables need to be changed to suit your images. 

Future state will be a config file.

# TODO  

Dockerize a gui app? 
Desktop or Terminal app? 
API ? 