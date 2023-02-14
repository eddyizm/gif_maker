import os
from rich import print

conf = os.path.join(os.path.expanduser('~'), '.gif_maker')
# os.system(f'touch {conf}')

def check_config():
    # print(os.path.isfile(conf))
    print('[bold yellow]Config does not exist![/bold yellow]')


def create_config():
    pass


def edit_config():
    pass


def remove_config():
    pass


def return_config():
    pass
