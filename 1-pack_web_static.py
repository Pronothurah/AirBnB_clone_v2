#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo,
using the function do_pack
"""
import os
from datetime import datetime
from fabric.api import *


def do_pack():
    """Compress files from web_static directory"""
    try:
        local('sudo mkdir -p versions')
        date = datetime.now()
        t_string = date.strftime('%Y%m%d%H%M%S')
        local(f'sudo tar -cvzf versions/web_static_{t_string}.tgz web_static')
        # return file
    except FileNotFoundError:
        print("Error: Unable to find specified directory.")
        return None
