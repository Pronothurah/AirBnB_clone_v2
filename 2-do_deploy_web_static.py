#!/usr/bin/python3
"""
Creates and distributes an archive to your web
servers, using the function deploy
"""
import os
from datetime import datetime
from fabric.api import *

env.user = "ubuntu"
env.hosts = ["52.86.50.144", "52.3.250.50"]


def do_pack():
    """Compress files from web_static directory"""
    try:
        local('sudo mkdir -p versions')
        date = datetime.now()
        t_string = date.strftime('%Y%m%d%H%M%S')
        local(f'sudo tar -cvzf versions/web_static_{t_string}.tgz web_static')
        f_path = f"versions/web_static_{t_string}.tgz"
        f_size = os.path.getsize(f_path)
        print(f"web_static packed: {f_path} -> {f_size}Bytes")
        return f_path
    except FileNotFoundError:
        print("Error: Unable to find specified directory.")
        return None


def do_deploy(archive_path):
    """
    Deploy archive

    Args:
        - archive_path(str, optional): Path of the archive
    """
    try:
        if not os.path.isfile(archive_path):
            return False
        
        # Extract filename from the full path
        path = os.path.basename(archive_path)
        name = os.path.splitext(path)[0]

        # path = archive_path.split("/")[1]
        # name = path.split(".")[0]
        put(archive_path, "/tmp/{0}".format(path))
        run("sudo mkdir -p /data/web_static/releases/{}/".format(name))
        source = "sudo tar -xzf /tmp/{0} -C".format(path)
        dest = "/data/web_static/releases/{0}/".format(name)
        run(source + " " + dest)
        run("sudo rm /tmp/{0}".format(path))
        source = (
            "sudo mv /data/web_static/releases/{0}/web_static/*".format(name)
        )
        dest = "/data/web_static/releases/{0}/".format(name)
        run(source + " " + dest)
        run(
            "sudo rm -rf /data/web_static/releases/{0}/web_static".format(name)
        )
        run("sudo rm -rf /data/web_static/current")
        source = "sudo ln -s /data/web_static/releases/{0}/".format(name)
        dest = "/data/web_static/current"
        run(source + " " + dest)
        return True
    except Exception:
        return False
