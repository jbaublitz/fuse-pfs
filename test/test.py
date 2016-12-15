#!/usr/bin/python

import os
import sys
import subprocess

from lib import filename, stringcontents
from lib.fileutils import read_file

def main():
    p = subprocess.Popen(['./bin/pfs', os.path.join(os.environ['PWD'], 'test',
            'exec.py')], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = p.communicate()
    print(stdout)

    f = filename(p.pid)
    print('Checking file {0} cannot be read outside of sandbox...'.format(f))
    try:
        filecontents = open(f).read()
        if filecontents == stringcontents:
            print('FAILURE')
    except IOError as e:
        print('SUCCESS')

if __name__ == '__main__':
    main()
