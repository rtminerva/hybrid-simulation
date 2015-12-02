

    

def gg(a = 1, b = 2, **args):
    f = [1,2,3,4,5]
    h = b
    return h

def ff(t = 0, iter = 0, q = 0, qr = 0):
    if iter == 1:
        q = [10000]
        qr = [100]
    
    q[0] += 1
    qr[0] += 1
    yy = [q,qr]
    print 'here',yy
    return yy