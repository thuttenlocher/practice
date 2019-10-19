# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import control
tf=control.tf([1,2,4,8], [1,2,-15])
[x,y]=control.root_locus(tf)
