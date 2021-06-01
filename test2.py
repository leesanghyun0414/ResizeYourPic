import os
import pandas as pd

d1 = {"Memory": {
    "Name": "G.Skill Ripjaws V Series 16 GB (2 x 8 GB) DDR4-3200 CL14",
    "Price": 1
}}

d2 = {}
for k, v in d1.items():
    d2[k] = pd.Series(v)

df = pd.DataFrame(d2)
print(d2['Memory']['Price'])
