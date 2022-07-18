from ctypes import * 
import numpy as np
a = np.arange(0,100,1)
liveadd = CDLL("./liveadd.so")
size = c_int(100)
array = (c_double*100) (*a.tolist())
result = (c_double*1) ()
liveadd.add(size,array,result)
print(result[0])