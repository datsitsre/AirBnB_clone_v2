#!/usr/bin/python3
""" Fabric  to create an archive """
import os
from fabric.api import  env, put, run


env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
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
        return True
