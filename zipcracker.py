#!/usr/bin/env python
# -*- coding: utf-8 -*-

__autor__ = "@xcod3"
__contributor__ = "@codeshard"
__copyright__ = "Copyright 2017, Xc0d3"
__license__ = "GPLv3"
__version__ = "1.3.1"

import optparse
from zipfile import ZipFile
import string
import itertools
import random
import time
from threading import Thread

# Banner
print(
    """
 ______        ____                _
|__  (_)_ __  / ___|_ __ __ _  ___| | _____ _ __
  / /| | '_ \| |   | '__/ _` |/ __| |/ / _ \ '__|
 / /_| | |_) | |___| | | (_| | (__|   <  __/ |
/____|_| .__/ \____|_|  \__,_|\___|_|\_\___|_|
       |_|

         	   By XC0D3
	   https://cs-academy.org/
"""
)


def extract_zip(zFile, dictionary):
    t0 = time.time()
    password = None
    zip_file = ZipFile(zFile)
    alphabet = string.ascii_letters + string.digits + string.punctuation
    with open(dictionary, "r") as f:
        for line in f.readlines():
            password_string = line.rstrip()
            try:
                password = bytes(password_string, "utf-8")
                zip_file.extractall(pwd=password)
                t1 = time.time()
                total = t1 - t0
                print("Password found : %s" % password_string)
                print("Time spent : %f seconds" % total)
                return
            except:
                pass

    nbcharmax = 255

    for i in range(1, nbcharmax):
        print("Testing length = %i" % i)
        for j in itertools.product(alphabet, repeat=i):
            try:
                password_string = "".join(j)
                password = bytes(password_string, "utf-8")
                zip_file.extractall(pwd=password)
                t1 = time.time()
                total = t1 - t0
                print("Password found : %s" % password_string)
                print("Time spent : %f seconds" % total)
                return
            except:
                pass


if __name__ == "__main__":
    parser = optparse.OptionParser("usage python zipcracker.py -f <zipfile> -d <dictionary>")
    parser.add_option("-f", dest="zname", type="string", help="specify zip file")
    parser.add_option("-d", dest="dname", type="string", help="specify dictionary file")
    (options, arg) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = str(zname)
    passFile = open(dname)
    t = Thread(target=extract_zip, args=(zFile, dname))
    t.start()
