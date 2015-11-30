import continuous_run as cont
import discrete_run as disc

t = 0
k = 0
T = 2
Nt = 10000
tau = 0.001


while t <= T and k < Nt:
    k += 1
    t += tau
    r = cont.???(iter = k) #sudah ada plot
    q = disc.???(???) #sudah ada plot