# -*- coding: utf-8 -*

import os;
arr = os.listdir('.')
for a in arr:
    if a.find("ic_fun_filter")>=0:
        na = "ic_"+ a[a.find("filter"):]
        print na
        os.rename(a,na)