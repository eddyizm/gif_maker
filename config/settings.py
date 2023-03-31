import os
import configparser
from rich import print
from rich.prompt import Confirm, Prompt

conf = os.path.join(os.path.expanduser('~'), '.gif_maker')
# os.system(f'touch {conf}')
config = configparser.ConfigParser()

def read_config(conf):
    config.read(conf)
    print(f'[bold yellow]value: {config}\n[bold yellow]')


def check_config():
    if os.path.isfile(conf):
        read_config(conf)
    create = Confirm.ask('[yellow]Config does not exist. Do you want to create one?[yellow]')
    create_config() if create else print('Have it your way boss.')


def create_config():
    print("[yellow]Let's create a config[yellow]")


def edit_config():
    pass


def remove_config():
    pass


def return_config():
    pass
