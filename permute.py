#!/usr/bin/env python
# encoding: utf-8
"""
Randomizes a Difframp list 

Created by DELSUC Marc-André and Julia Asencio on 2013-12-18.
Copyright (c) 2013 IGBMC. All rights reserved.
"""

import random

N = 40   # Adapt to your system

perm = random.sample(range(N), N)

print N, "points :", perm

filelist = ['difflist',  '/opt/topspin/exp/stan/nmr/lists/gp/user/Difframp']

for fname in filelist:
    F = open(fname,'r')
    FF = open(fname+'P','w')
    ll = []
    for l in F:
       if not l.startswith('#'):
           ll.append(l) 
       elif l != '##END=':
           FF.write(l)
    F.close()
    if len(ll) != N:
        raise Exception( 'This prgm is meant for %d points'%N )
    for i in range(N):
        FF.write(ll[perm[i]])
    FF.write('##END=')
    FF.close()
