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
$ python gif_maker.py --help
usage: Gif Maker [-h] [-c] [-d DIRECTORY] [-p PREFIX] [-s SCALE] [-e EXTENSION] [--clean] [-L] [-o OUTPUT] [--version]

Resizes and creates gif out of png files in specified directory

options:
  -h, --help            show this help message and exit
  -c, --config          pass in -c or --config to use a config.
  -d DIRECTORY, --directory DIRECTORY
                        directory where files are located.
  -p PREFIX, --prefix PREFIX
                        prefix to filter files.
  -s SCALE, --scale SCALE
                        width value to scale final output, defaults to 400
  -e EXTENSION, --extension EXTENSION
                        file extenstion to filter by.
  --clean               clean up resized images, default
  -L, --leave           leave original and processed files, default app removes all files except gif output.
  -o OUTPUT, --output OUTPUT
                        directory to output gif.
  --version             show program's version number and exit

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