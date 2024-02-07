#!/usr/bin/env python3
"""Fabric test file"""

from fabric.api import *

env.user = 'ubuntu'

env.hosts = ['52.86.50.144', '52.3.250.50']

env.key_filename = '~/.ssh/id_rsa'

def create_dir():
    'Creates directory'
    run('sudo mkdir -p test_ping')
