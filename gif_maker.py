import argparse
import glob
import os
from datetime import datetime

from PIL import Image
from rich import print
from rich.progress import track
from rich.console import Console



parser = argparse.ArgumentParser(description="Resizes and creates gif out of png files in specified directory"
    ,epilog="And then there was gif..."
)    
parser.add_argument('-c', '--config', help="pass in -c or --config to use a config.", action='store_false', required=False)
parser.add_argument('-d', '--directory', help="directory where files are located.", required=False)
parser.add_argument('-L', '--leave', help='leave processed files, default app removes all files except gif output.', action='store_false')
args=parser.parse_args()

CLEAN = args.leave


def scale_image(input_image_path, output_image_path, width=400):
    """
        resize images before making gif. 
    """
    original_image = Image.open(input_image_path)
    w, h = original_image.size
    max_size = (width, h)
    original_image.thumbnail(max_size, Image.Resampling.LANCZOS)
    original_image.save(output_image_path)
    if CLEAN:
        print('[bold yellow]removing source image[/bold yellow]')
        os.remove(input_image_path)


def resize_images(image_path, glob_regex):
    print('Resizing images...')
    search = os.path.join(image_path, glob_regex)
    for image in track(glob.glob(search)):
        out = image + '.resized.png'
        scale_image(image, out)
    print('resizing done')


def clean_up(search):
    if CLEAN:
        for image in track(glob.glob(search), description=f'cleaning up files {search}'):
            os.remove(image)


def make_gif(image_path, glob_regex,  gif_name = None):
    gif_name = gif_name or f'{datetime.now().strftime("%Y%m%d%H%M")}_gif_maker.gif'
    search = os.path.join(image_path, glob_regex)
    outfile = os.path.join(image_path, gif_name)
    console = Console()
    with console.status("[bold green]generating the gif... ") as status:
        frames = [Image.open(image) for image in glob.glob(search)]
        frame_one = frames[0]
        frame_one.save(outfile, format="GIF", append_images=frames,
                save_all=True, duration=100, loop=0)
        print(f'gif created: {gif_name}')
    clean_up(search)


def main():
    # TODO flag to scale down
    # TODO flag to specify scale down size
    if not args.config:
        # check_config()
        # TODO check if config exists and use it.
        pass        
    
    if not args.directory:
        print('[bold red]Please enter a path to image files.[/bold red]')
        return
    fp_in = args.directory
    file_filter_to_resize = 'vlcsnap*.png'
    print(f'[yellow]{file_filter_to_resize[0:-4]}[/yellow]')
    resize_images(fp_in, file_filter_to_resize)
    resized_files = f'{file_filter_to_resize[0:-4]}.resized.png' 
    make_gif(fp_in, resized_files)


if __name__ == "__main__":
    main()
