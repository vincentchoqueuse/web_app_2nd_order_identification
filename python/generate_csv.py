import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

system_list=[]
freq_list=[]

# system1
w0=2*np.pi*10000
m=0.5
system1 = signal.lti([2*m*1/w0,0], [(1/(w0**2)),2*m/w0,1])
system_list.append(system1)
freq_list.append({"min":3,"max":5})

#system2
w0=1640
system2 = signal.lti([4], [(1/(w0**2)),2*0.2/w0,1])
system_list.append(system2)
freq_list.append({"min":1,"max":4})

#system3
tau=1.06*(10**-5)
system3 = signal.lti([-tau,1], [tau,1])
system_list.append(system3)
freq_list.append({"min":1,"max":5})

#system4
w0=2*np.pi*1000
system4 = signal.lti([1/(w0**2),0,0], [(1/(w0**2)),2*0.714/w0,1])
system_list.append(system4)
freq_list.append({"min":2,"max":5})

#system5
w0=2*np.pi*100
system5 = signal.lti([2,0], [(1/(w0**2)),2*0.1/w0,1])
system_list.append(system5)
freq_list.append({"min":1,"max":4})

#system6
w0=2*np.pi*10
system6 = signal.lti([5], [(1/(w0**2)),2*1.2/w0,1])
system_list.append(system6)
freq_list.append({"min":0,"max":4})

#system7
w0=2*np.pi*20
system7 = signal.lti([3], [1/w0,1])
system_list.append(system7)
freq_list.append({"min":-1,"max":4})

for indice in range(len(system_list)):
    system=system_list[indice]
    freq=freq_list[indice]
    f=np.logspace(freq["min"],freq["max"],1000)
    w,T=system.freqresp(2*np.pi*f)
    filename="../data/data{}.csv".format(indice)
    header="f, module, argument"
    data=np.transpose([w,np.abs(T),np.angle(T)])
    np.savetxt(filename,data,header=header, delimiter=",",comments="")
