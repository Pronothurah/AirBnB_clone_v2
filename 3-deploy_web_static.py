#!/usr/bin/python3
"""
Distributes an archive to your web servers, using the function do_deploy
"""
import os
from datetime import datetime
from fabric.api import *

env.user = "ubuntu"
env.hosts = ["52.86.50.144", "52.3.250.50"]


@runs_once
def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    cur_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cur_time.year,
        cur_time.month,
        cur_time.day,
        cur_time.hour,
        cur_time.minute,
        cur_time.second
    )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        archize_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archize_size))
    except Exception:
        output = None
    return output


def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload archive to /tmp directory on remote server
        put(archive_path, "/tmp")

        folder_name = os.path.basename(archive_path).split('.')[0]
        folder_path = f"/data/web_static/releases/{folder_name}"
        run(f"mkdir -p {folder_path}")
        run(f"tar -xzf /tmp/{os.path.basename(archive_path)} -C {folder_path}")

        # Remove archive from /tmp directory
        run(f"rm /tmp/{os.path.basename(archive_path)}")

        # Move contents of extracted folder to current release directory
        run(f"mv {folder_path}/web_static/* {folder_path}/")

        # Remove empty web_static directory
        run(f"rm -rf {folder_path}/web_static")

        # Remove current symbolic link
        run("rm -rf /data/web_static/current")

        # Create new symbolic link
        run(f"ln -s {folder_path} /data/web_static/current")

        print('New version deployed!')
        return True
    except Exception as e:
        print(f"Failed to deploy: {e}")
        return False


def deploy():
    """
    Full deployment based on do_pack & do_deploy (task 2)
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
