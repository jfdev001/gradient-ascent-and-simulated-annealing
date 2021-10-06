#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:12:37 2019

@author: Joshua L. Phillips
Department of Computer Science
Middle Tennessee State University
Illustration of how to sample
from the SoG function.

Portions based on Python code provided by
Scott P. Morton
Center for Computational Science
Middle Tennessee State University
"""
import SumofGaussians as SG
import numpy as np, sys

seed = int(sys.argv[1])
dims = int(sys.argv[2])
ncenters = int(sys.argv[3])

np.random.seed(seed)

sog = SG.SumofGaussians(dims,ncenters)

epsilon = 1e-8

# Data
data_input = np.loadtxt(sys.stdin)

for i in data_input:
    print("%.8f"%(sog.Eval(i)),end=' ')
    print(" ".join(["%.8f"%(x) for x in sog.Deriv(i)]))
    
sys.exit(0)

