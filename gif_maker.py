import argparse
import glob
import os
from datetime import datetime

from PIL import Image
from rich import print
from rich.progress import track
from rich.console import Console
from config import check_config


parser = argparse.ArgumentParser(description="Resizes and creates gif out of png files in specified directory"
    ,epilog="And then there was gif..."
    ,prog='Gif Maker'
)    
parser.add_argument('-c', '--config', help="pass in -c or --config to use a config.", action='store_true', required=False)
parser.add_argument('-d', '--directory', help="directory where files are located.", required=False)
parser.add_argument('-p', '--prefix', help="prefix to filter files.", required=False)
parser.add_argument('-s', '--scale', help="width value to scale final output, defaults to 400", required=False)
parser.add_argument('-e', '--extension', help="file extenstion to filter by.", required=False)
parser.add_argument('-L', '--leave', help='leave original and processed files, default app removes all files except gif output.', action='store_false')
parser.add_argument('--version', action='version', version='%(prog)s 0.2')
args=parser.parse_args()

CLEAN = args.leave


def scale_image(input_image_path, output_image_path, width):
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


def resize_images(image_path, glob_regex, width) -> int:
    file_count = 0
    print(f'Resizing images in directory: {image_path}')
    search = os.path.join(image_path, glob_regex)
    for image in track(glob.glob(search)):
        out = image + '.resized.png'
        export_folder = os.path.join(image_path, out)
        scale_image(image, export_folder, width)
        file_count += 1
    print(f'resized {file_count} images')
    return file_count


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


def generate_filter(args):
    if (args.prefix and args.extension):
        return f'{args.prefix}*.{args.extension}'  
    if (args.prefix or args.extension):
        return f'{args.prefix}*' if args.prefix else f'*.{args.extension}'
    return 'vlcsnap*.png' # TODO default will be set in config 


def main():
    if args.config:
        check_config()
        # parser.print_help()
        return    
    
    if not args.directory:
        print('[bold red]Please enter a path to image files with -d flag.[/bold red]')
        return
    fp_in = args.directory
    arg_width = int(args.scale) if args.scale else 400
    file_filter_to_resize = generate_filter(args)
    print(f'file filter: [yellow]{file_filter_to_resize}[/yellow]')
    count = resize_images(fp_in, file_filter_to_resize, arg_width)
    if count >= 1:
        resized_files = f'{file_filter_to_resize[0:-4]}.resized.png' 
        make_gif(fp_in, resized_files)
    else:
        print('[yellow]No files found. Check file path/filters and ry again bob[/yellow]')


if __name__ == "__main__":
    main()
