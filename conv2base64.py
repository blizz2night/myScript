#!/usr/bin/python
# -*- coding: utf-8 -*

import base64
import sys
import os.path

def conv2base64(path):
    with open(path, 'rb') as f :
       s = base64.b64encode(f.read())
    return s

def main():
    print sys.argv
    argv = sys.argv
    sz =len(argv)
    if sz<2 :
        print 'usage %s <inputfile> [outputfile]' %(os.path.basename(argv[0]))
        return
    str64 = conv2base64(argv[1])
    if sz>2 :
        of = argv[2]
    else :
        of = argv[1]+'.base64'
    with open(of, 'w') as f :
        f.write(str64)

if __name__ == '__main__':
    main()
