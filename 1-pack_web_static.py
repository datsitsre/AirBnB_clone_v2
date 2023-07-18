#!/usr/bin/python3
""" Fabric  to create an archive """

# import libraries
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """ the Archive code """
    current_time = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(current_time.year,
                                                         current_time.month,
                                                         current_time.day,
                                                         current_time.hour,
                                                         current_time.minute,
                                                         current_time.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
