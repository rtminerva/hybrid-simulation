from pysb import *
import numpy as np
import pylab as pl
from pysb.integrate import odesolve

Model()
Monomer('A',['d'])
Monomer('B',['d'])
Monomer('D',['s'])

Parameter('k_A_D',0.3336)#2.417)
Parameter('k_B_D',0.3336)#2.417)
Parameter('l_A_D',1)#1.25)
Parameter('l_B_D',1)#1.25)

Rule('A_D', A(d=None) + D(s=None) <> A(d=1)%D(s=1), k_A_D, l_A_D)
Rule('B_D', B(d=None) + D(s=None) <> B(d=1)%D(s=1), k_B_D, l_B_D)

Initial(A(d=None), Parameter('A_0', 1.1))
Initial(B(d=None), Parameter('B_0', 1))
Initial(D(s=None), Parameter('D_0', 0.1))

Observable('tA', A(d=None))
Observable('tB', B(d=None))
Observable('tD', D(s=None))
Observable('tAD', A(d=1) % D(s=1))
Observable('tBD', B(d=1) % D(s=1))

t=np.linspace(0,3,10000)
z1 = odesolve(model,t)#, integrator='vode', with_jacobian=True, rtol=1e-20, atol=1e-20)
pl.figure()
pl.xlim(0,3)
pl.ylim(0,0.2)
pl.title('A_0=1.1,B_0=1,D_0=0.1')
pl.plot(t, z1['tA'], label="A")
pl.plot(t, z1['tB'], label="B")
pl.plot(t, z1['tD'], label="D")
pl.plot(t, z1['tAD'], label="AD")
pl.plot(t, z1['tBD'], label="BD")
pl.legend()
pl.xlabel("Time")
pl.ylabel("Concentrations")
pl.show()

