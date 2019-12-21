#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import minmax_helpers

from gamestate import *

g = GameState()

print("calling min_value on an empty board...")
v = minmax_helpers.min_value(g)

if v == -1:
    print("sahiii")
else:
    print("galat")

