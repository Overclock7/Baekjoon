import numpy as np
from math import *


buff = (map(str,input().split(";")))
a = []

for b in buff:
    temp = []
    for k in b.split(",") :
        temp.append(int(k))
    a.append(temp)

for c in a:
    print(c)