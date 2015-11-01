if y_pos == 1: #batas bawah
        v4y = 0.5/h*(c[x_pos+1,y_pos+3,k]+c[x_pos-1,y_pos+3,k]-c[x_pos+1,y_pos+1,k]-c[x_pos-1,y_pos+1,k])
        w4y = 0.5/h*(f[x_pos+1,y_pos+3,k]+f[x_pos-1,y_pos+3,k]-f[x_pos+1,y_pos+1,k]-f[x_pos-1,y_pos+1,k])
        v4y = max(0,v4y)
        w4y = max(0,w4y)
        P_4 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v4y + la*h*ro*w4y
        if x_pos == 1: #pojok kiri bawah
            P_1 = 0
            P_3 = 0
            v2x = 0.5/h*(c[x_pos+3,y_pos+1,k]-c[x_pos+1,y_pos+1,k]+c[x_pos+3,y_pos-1,k]-c[x_pos+1,y_pos-1,k])
            w2x = 0.5/h*(f[x_pos+3,y_pos+1,k]-f[x_pos+1,y_pos+1,k]+f[x_pos+3,y_pos-1,k]-f[x_pos+1,y_pos-1,k])
            v2x = max(0,v2x)
            w2x = max(0,w2x)
            P_2 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v2x + la*h*ro*w2x
        elif x_pos == Nx-1: #pojok kanan bawah
            P_2 = 0
            P_3 = 0
            v1x = 0.5/h*(c[x_pos-3,y_pos+1,k]-c[x_pos-1,y_pos+1,k]+c[x_pos-3,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
            w1x = 0.5/h*(f[x_pos-3,y_pos+1,k]-f[x_pos-1,y_pos+1,k]+f[x_pos-3,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
            v1x = max(0,v1x)
            w1x = max(0,w1x)
            P_1 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v1x + la*h*ro*w1x
        else: #batas bawah selain pojok
            P_3 = 0
            v2x = 0.5/h*(c[x_pos+3,y_pos+1,k]-c[x_pos+1,y_pos+1,k]+c[x_pos+3,y_pos-1,k]-c[x_pos+1,y_pos-1,k])
            w2x = 0.5/h*(f[x_pos+3,y_pos+1,k]-f[x_pos+1,y_pos+1,k]+f[x_pos+3,y_pos-1,k]-f[x_pos+1,y_pos-1,k])
            v2x = max(0,v2x)
            w2x = max(0,w2x)
            P_2 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v2x + la*h*ro*w2x
            v1x = 0.5/h*(c[x_pos-3,y_pos+1,k]-c[x_pos-1,y_pos+1,k]+c[x_pos-3,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
            w1x = 0.5/h*(f[x_pos-3,y_pos+1,k]-f[x_pos-1,y_pos+1,k]+f[x_pos-3,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
            v1x = max(0,v1x)
            w1x = max(0,w1x)
            P_1 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v1x + la*h*ro*w1x
    elif y_pos == Ny-1: #batas atas
        v3y = 0.5/h*(c[x_pos+1,y_pos-3,k]+c[x_pos-1,y_pos-3,k]-c[x_pos+1,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
        w3y = 0.5/h*(f[x_pos+1,y_pos-3,k]+f[x_pos-1,y_pos-3,k]-f[x_pos+1,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
        v3y = max(0,v3y)
        w3y = max(0,w3y)
        P_3 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v3y + la*h*ro*w3y
        if x_pos == 1: #pojok kiri atas
            P_1 = 0
            P_4 = 0
            v2x = 0.5/h*(c[x_pos+3,y_pos+1,k]-c[x_pos+1,y_pos+1,k]+c[x_pos+3,y_pos-1,k]-c[x_pos+1,y_pos-1,k])
            w2x = 0.5/h*(f[x_pos+3,y_pos+1,k]-f[x_pos+1,y_pos+1,k]+f[x_pos+3,y_pos-1,k]-f[x_pos+1,y_pos-1,k])
            v2x = max(0,v2x)
            w2x = max(0,w2x)
            P_2 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v2x + la*h*ro*w2x
        elif x_pos == Nx-1: #pojok kanan atas
            P_2 = 0
            P_4 = 0
            v1x = 0.5/h*(c[x_pos-3,y_pos+1,k]-c[x_pos-1,y_pos+1,k]+c[x_pos-3,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
            w1x = 0.5/h*(f[x_pos-3,y_pos+1,k]-f[x_pos-1,y_pos+1,k]+f[x_pos-3,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
            v1x = max(0,v1x)
            w1x = max(0,w1x)
            P_1 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v1x + la*h*ro*w1x
        else: #batas atas selain pojok
            P_4 = 0
            v1x = 0.5/h*(c[x_pos-3,y_pos+1,k]-c[x_pos-1,y_pos+1,k]+c[x_pos-3,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
            w1x = 0.5/h*(f[x_pos-3,y_pos+1,k]-f[x_pos-1,y_pos+1,k]+f[x_pos-3,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
            v1x = max(0,v1x)
            w1x = max(0,w1x)
            P_1 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v1x + la*h*ro*w1x
            v2x = 0.5/h*(c[x_pos+3,y_pos+1,k]-c[x_pos+1,y_pos+1,k]+c[x_pos+3,y_pos-1,k]-c[x_pos+1,y_pos-1,k])
            w2x = 0.5/h*(f[x_pos+3,y_pos+1,k]-f[x_pos+1,y_pos+1,k]+f[x_pos+3,y_pos-1,k]-f[x_pos+1,y_pos-1,k])
            v2x = max(0,v2x)
            w2x = max(0,w2x)
            P_2 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v2x + la*h*ro*w2x
    else: #selain batas bawah dan atas
        v3y = 0.5/h*(c[x_pos+1,y_pos-3,k]+c[x_pos-1,y_pos-3,k]-c[x_pos+1,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
        w3y = 0.5/h*(f[x_pos+1,y_pos-3,k]+f[x_pos-1,y_pos-3,k]-f[x_pos+1,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
        v3y = max(0,v3y)
        w3y = max(0,w3y)
        P_3 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v3y + la*h*ro*w3y
        v4y = 0.5/h*(c[x_pos+1,y_pos+3,k]+c[x_pos-1,y_pos+3,k]-c[x_pos+1,y_pos+1,k]-c[x_pos-1,y_pos+1,k])
        w4y = 0.5/h*(f[x_pos+1,y_pos+3,k]+f[x_pos-1,y_pos+3,k]-f[x_pos+1,y_pos+1,k]-f[x_pos-1,y_pos+1,k])
        v4y = max(0,v4y)
        w4y = max(0,w4y)
        P_4 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v4y + la*h*ro*w4y
        if x_pos == 1: #batas kiri selain pojok
            P_1 = 0
            v2x = 0.5/h*(c[x_pos+3,y_pos+1,k]-c[x_pos+1,y_pos+1,k]+c[x_pos+3,y_pos-1,k]-c[x_pos+1,y_pos-1,k])
            w2x = 0.5/h*(f[x_pos+3,y_pos+1,k]-f[x_pos+1,y_pos+1,k]+f[x_pos+3,y_pos-1,k]-f[x_pos+1,y_pos-1,k])
            v2x = max(0,v2x)
            w2x = max(0,w2x)
            P_2 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v2x + la*h*ro*w2x
        elif x_pos == Nx-1: #batas kanan selain pojok
            P_2 = 0
            v1x = 0.5/h*(c[x_pos-3,y_pos+1,k]-c[x_pos-1,y_pos+1,k]+c[x_pos-3,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
            w1x = 0.5/h*(f[x_pos-3,y_pos+1,k]-f[x_pos-1,y_pos+1,k]+f[x_pos-3,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
            v1x = max(0,v1x)
            w1x = max(0,w1x)
            P_1 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v1x + la*h*ro*w1x
        #selain batas2, tetap pada nilai P_1 ~ P_4 awal saja
        else:
            v1x = 0.5/h*(c[x_pos-3,y_pos+1,k]-c[x_pos-1,y_pos+1,k]+c[x_pos-3,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
            w1x = 0.5/h*(f[x_pos-3,y_pos+1,k]-f[x_pos-1,y_pos+1,k]+f[x_pos-3,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
            v1x = max(0,v1x)
            w1x = max(0,w1x)
            P_1 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v1x + la*h*ro*w1x
            v2x = 0.5/h*(c[x_pos+3,y_pos+1,k]-c[x_pos+1,y_pos+1,k]+c[x_pos+3,y_pos-1,k]-c[x_pos+1,y_pos-1,k])
            w2x = 0.5/h*(f[x_pos+3,y_pos+1,k]-f[x_pos+1,y_pos+1,k]+f[x_pos+3,y_pos-1,k]-f[x_pos+1,y_pos-1,k])
            v2x = max(0,v2x)
            w2x = max(0,w2x)
            P_2 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v2x + la*h*ro*w2x
            v3y = 0.5/h*(c[x_pos+1,y_pos-3,k]+c[x_pos-1,y_pos-3,k]-c[x_pos+1,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
            w3y = 0.5/h*(f[x_pos+1,y_pos-3,k]+f[x_pos-1,y_pos-3,k]-f[x_pos+1,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
            v3y = max(0,v3y)
            w3y = max(0,w3y)
            P_3 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v3y + la*h*ro*w3y
            v4y = 0.5/h*(c[x_pos+1,y_pos+3,k]+c[x_pos-1,y_pos+3,k]-c[x_pos+1,y_pos+1,k]-c[x_pos-1,y_pos+1,k])
            w4y = 0.5/h*(f[x_pos+1,y_pos+3,k]+f[x_pos-1,y_pos+3,k]-f[x_pos+1,y_pos+1,k]-f[x_pos-1,y_pos+1,k])
            v4y = max(0,v4y)
            w4y = max(0,w4y)
            P_4 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v4y + la*h*ro*w4y