import os
from pathlib import Path

import fire

from qgoferdoc import __version__
from qgoferdoc.search import initialize_config, index_folders



def init(home_dir: Path = Path.home(), root_dir: Path = Path.home(), path: Path = Path.home()):
    initialize_config(home_dir, root_dir)
    index_folders(path)


def version():
    try:
        username = os.getlogin()
    except FileNotFoundError:
        username = "You"
    print(f"Hello {username}, my version number is: '{__version__}'\n")


def main():
    fire.Fire({
        "version": version,
        "init": init
    })


if __name__ == '__main__':
    main()