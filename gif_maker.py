import glob
import os
import sys
from datetime import datetime
from PIL import Image
from rich import print
from rich.progress import track


def scale_image(input_image_path,
                output_image_path,
                width=None,
                height=None
                ):
    """
        resize images before making gif. 
    """
    original_image = Image.open(input_image_path)
    w, h = original_image.size
    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        raise RuntimeError('Width or height required!')
    original_image.thumbnail(max_size, Image.ANTIALIAS)
    original_image.save(output_image_path)


def resize_images(image_path, glob_regex):
    print('Resizing images...')
    search = os.path.join(image_path, glob_regex)
    for image in track(glob.glob(search)):
        out = image + '.resized.png'
        scale_image(image, out, width=800)
    print('resizing done')

def make_gif(image_path, glob_regex,  gif_name = None):
    print('making gif!')
    gif_name = gif_name or f'{datetime.now().strftime("%Y%m%d%H%M")}_gif_maker.gif'
    search = os.path.join(image_path, glob_regex)
    outfile = os.path.join(image_path, gif_name)
    frames = [Image.open(image) for image in glob.glob(search)]
    frame_one = frames[0]
    frame_one.save(outfile, format="GIF", append_images=frames,
               save_all=True, duration=100, loop=0)
    print(f'gif created: {gif_name}')


def main():
    # TODO flag to clean up original files
    # TODO flag to scale down
    # TODO flag to specify scale down size
    # TODO add arg parser
    if len(sys.argv) < 2:
        print('[bold red]Please enter a path to image files.[/bold red]')
        return
    fp_in = sys.argv[1]
    resize_images(fp_in, 'vlcsnap*.png')
    make_gif(fp_in, 'vlcsnap*.resized.png')
    


if __name__ == "__main__":
    main()    
