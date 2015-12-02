import continuous_run as cont
# import discrete_run as disc

t = 0
k = 0
T = 2
Nt = 5
tau = 0.001

r = [0, 0, 0, 0,0,0]
while t <= T and k < Nt:
    k += 1
    t += tau
    r = cont.contiuous_1_iter(iter = k, n_o = r[0], c_o = r[1], f_o = r[2], n = r[3], c = r[4], f = r[5]) #sudah ada plot
    print k
#     q = disc.???(???) #sudah ada plot
print 'done'