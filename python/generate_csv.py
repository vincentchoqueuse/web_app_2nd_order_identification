from ENIB_lib import *
import numpy as np

system_list=[]
freq_list=[]

# system1
sys = LP(2,0.2,1000)
w, mag, phase = sys.bode(w=np.logspace(2,4,1000))
export_bode("../data/data0.csv",w,mag,phase)

#system2
sys = LP(-10,2,100)
w, mag, phase = sys.bode(w=np.logspace(1,4,1000))
export_bode("../data/data1.csv",w,mag,phase)

#system3
sys = LP(1,0.8,500)
w, mag, phase = sys.bode(w=np.logspace(1,5,1000))
export_bode("../data/data2.csv",w,mag,phase)

#system4
sys = HP(10,2,100)
w, mag, phase = sys.bode(w=np.logspace(1,4,1000))
export_bode("../data/data3.csv",w,mag,phase)

#system5
sys = HP(-4,0.1,100)
w, mag, phase = sys.bode(w=np.logspace(0,5,1000))
export_bode("../data/data4.csv",w,mag,phase)

#system6
sys = BP(-0.5,0.25,2000)
w, mag, phase = sys.bode(w=np.logspace(2,5,1000))
export_bode("../data/data5.csv",w,mag,phase)

#system7
sys = BP(5,1,100)
w, mag, phase = sys.bode(w=np.logspace(0,4,1000))
export_bode("../data/data6.csv",w,mag,phase)

#system7
sys = BP(5,4,200)
w, mag, phase = sys.bode(w=np.logspace(2,5,1000))
export_bode("../data/data7.csv",w,mag,phase)


#system7
sys = Notch(-10,5,100)
w, mag, phase = sys.bode(w=np.logspace(1,4,1000))
export_bode("../data/data8.csv",w,mag,phase)

#system7
sys = Notch(1,0.05,1000)
w, mag, phase = sys.bode(w=np.logspace(2,4,1000))
export_bode("../data/data9.csv",w,mag,phase)

#system7
sys = Notch(-2,0.9,100)
w, mag, phase = sys.bode(w=np.logspace(1,4,1000))
export_bode("../data/data10.csv",w,mag,phase)


#system11
sys = HP(4,0.1,530)
w, mag, phase = sys.bode(w=np.logspace(1,4,1000))
export_bode("../data/data11.csv",w, mag, phase)
