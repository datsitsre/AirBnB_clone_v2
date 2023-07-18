#!/usr/bin/python3
""" Fabric  to create an archive """

# import libraries
import os
from datetime import datetime
from fabric.api import local, runs_once


def do_deplay(archive_path):
    """
       Deplay static files on the host

       Args:
            archive_apth (str): the path of the archive
       Returns:
            If the file doesnt exit

    """
    if os.path.exists("archive_path"):
        file_name = os.path.basename(archive_apth)
        dir_name = file_name.replace(".tgz", "")
        dir_path = "/data/web_static/releases/{}/".format(dir_name)
        try:
            put(archive_path, "/tmp/{}".format(file_name))
            run("mkdir -p {}".format(dir_path))
            run("tar -xzf /tmp/{} -C {}".format(file_name, dir_path))
            run("rm -rf /tmp/{}".format(file_name))
            run("mv {}web_static/* {}".format(dir_path, dir_path))
            run("rm -rf {}web_static".format(dir_path))
            run("rm -rf /data/web_static/current")
            run("ln -s {} /data/web_static/current".format(dir_path))
            print('New version deployed!')
        except Exception:
            return False
        return False
