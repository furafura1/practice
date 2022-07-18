from ctypes import * 
import numpy as np
a = np.arange(0,1000,1)
liveadd = CDLL("./liveadd.so")
size = c_int(1000)
array = (c_double*1000) (*a.tolist())
result = (c_double*1) ()
liveadd.add(size,array,result)
print(result[0])