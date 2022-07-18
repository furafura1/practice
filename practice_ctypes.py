from ctypes import * 
import numpy as np
a = np.arange(0,10,1)
liveadd = CDLL("./liveadd.so")
size = c_int(10)
array = (c_double*10) (*a.tolist())
result = (c_double*1) ()
liveadd.add(size,array,result)
print(result[0])