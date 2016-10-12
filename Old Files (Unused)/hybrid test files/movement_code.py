def movement_dir():
    la = tp/(h**2)
    x_pos = xb
    y_pos = yb
    
    '''Way of Reflection on The Boundary'''
    vvx = 0.5/h*(c[x_pos+1,y_pos+1,k]-c[x_pos-1,y_pos+1,k]+c[x_pos+1,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
    vvy = 0.5/h*(c[x_pos+1,y_pos+1,k]+c[x_pos-1,y_pos+1,k]-c[x_pos+1,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
    
    wwx = 0.5/h*(f[x_pos+1,y_pos+1,k]-f[x_pos-1,y_pos+1,k]+f[x_pos+1,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
    wwy = 0.5/h*(f[x_pos+1,y_pos+1,k]+f[x_pos-1,y_pos+1,k]-f[x_pos+1,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
    
    vvx_p = max(0,vvx)
    vvx_n = max(0,-vvx)
    vvy_p = max(0,vvy)
    vvy_n = max(0,-vvy)
    
    wwx_p = max(0,wwx)
    wwx_n = max(0,-wwx)
    wwy_p = max(0,wwy)
    wwy_n = max(0,-wwy)
    
    P_1 = la*d+la*h*ki/(1+al*0.5*(c[x_pos-1,y_pos+1,k]+c[x_pos-1,y_pos-1,k]))*vvx_n + la*h*ro*wwx_n
    P_2 = la*d+la*h*ki/(1+al*0.5*(c[x_pos+1,y_pos+1,k]+c[x_pos+1,y_pos-1,k]))*vvx_p + la*h*ro*wwx_p
    
    P_3 = la*d+la*h*ki/(1+al*0.5*(c[x_pos+1,y_pos+1,k]+c[x_pos-1,y_pos+1,k]))*vvy_n + la*h*ro*wwy_n
    P_4 = la*d+la*h*ki/(1+al*0.5*(c[x_pos+1,y_pos-1,k]+c[x_pos-1,y_pos-1,k]))*vvy_p + la*h*ro*wwy_p
    
    '''Boundary'''
    '''Using reflection on the boundary'''
    if y_pos == 1: #batas bawah
        P_4 +=P_3
        if x_pos == 1: #pojok kiri bawah
            P_2 += P_1
            P_1 = 0
            P_3 = 0
        elif x_pos == Nx-1: #pojok kanan bawah
            P_1 += P_2
            P_2 = 0
            P_3 = 0
        else: #batas bawah selain pojok
            P_3 = 0
    elif y_pos == Ny-1: #batas atas
        P_3 += P_4
        if x_pos == 1: #pojok kiri atas
            P_2 += P_1
            P_1 = 0
            P_4 = 0
        elif x_pos == Nx-1: #pojok kanan atas
            P_1 += P_2
            P_2 = 0
            P_4 = 0
        else: #batas atas selain pojok
            P_4 = 0
    else: #selain batas bawah dan atas
        if x_pos == 1: #batas kiri selain pojok
            P_2 += P_1
            P_1 = 0
        elif x_pos == Nx-1: #batas kanan selain pojok
            P_1 += P_2
            P_2 = 0
        #selain batas2, tetap pada nilai P_1 ~ P_4 awal saja
    '''Way of Reflection on The Boundary'''
    
#     '''Other way'''
#     if y_pos == 1: #batas bawah
#         v4y = 0.5/h*(c[x_pos+1,y_pos+3,k]+c[x_pos-1,y_pos+3,k]-c[x_pos+1,y_pos+1,k]-c[x_pos-1,y_pos+1,k])
#         w4y = 0.5/h*(f[x_pos+1,y_pos+3,k]+f[x_pos-1,y_pos+3,k]-f[x_pos+1,y_pos+1,k]-f[x_pos-1,y_pos+1,k])
#         v4y = max(0,v4y)
#         w4y = max(0,w4y)
#         P_4 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v4y + la*h*ro*w4y
#         if x_pos == 1: #pojok kiri bawah
#             P_1 = 0
#             P_3 = 0
#             v2x = 0.5/h*(c[x_pos+3,y_pos+1,k]-c[x_pos+1,y_pos+1,k]+c[x_pos+3,y_pos-1,k]-c[x_pos+1,y_pos-1,k])
#             w2x = 0.5/h*(f[x_pos+3,y_pos+1,k]-f[x_pos+1,y_pos+1,k]+f[x_pos+3,y_pos-1,k]-f[x_pos+1,y_pos-1,k])
#             v2x = max(0,v2x)
#             w2x = max(0,w2x)
#             P_2 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v2x + la*h*ro*w2x
#         elif x_pos == Nx-1: #pojok kanan bawah
#             P_2 = 0
#             P_3 = 0
#             v1x = 0.5/h*(c[x_pos-3,y_pos+1,k]-c[x_pos-1,y_pos+1,k]+c[x_pos-3,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
#             w1x = 0.5/h*(f[x_pos-3,y_pos+1,k]-f[x_pos-1,y_pos+1,k]+f[x_pos-3,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
#             v1x = max(0,v1x)
#             w1x = max(0,w1x)
#             P_1 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v1x + la*h*ro*w1x
#         else: #batas bawah selain pojok
#             P_3 = 0
#             v2x = 0.5/h*(c[x_pos+3,y_pos+1,k]-c[x_pos+1,y_pos+1,k]+c[x_pos+3,y_pos-1,k]-c[x_pos+1,y_pos-1,k])
#             w2x = 0.5/h*(f[x_pos+3,y_pos+1,k]-f[x_pos+1,y_pos+1,k]+f[x_pos+3,y_pos-1,k]-f[x_pos+1,y_pos-1,k])
#             v2x = max(0,v2x)
#             w2x = max(0,w2x)
#             P_2 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v2x + la*h*ro*w2x
#             v1x = 0.5/h*(c[x_pos-3,y_pos+1,k]-c[x_pos-1,y_pos+1,k]+c[x_pos-3,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
#             w1x = 0.5/h*(f[x_pos-3,y_pos+1,k]-f[x_pos-1,y_pos+1,k]+f[x_pos-3,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
#             v1x = max(0,v1x)
#             w1x = max(0,w1x)
#             P_1 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v1x + la*h*ro*w1x
#     elif y_pos == Ny-1: #batas atas
#         v3y = 0.5/h*(c[x_pos+1,y_pos-3,k]+c[x_pos-1,y_pos-3,k]-c[x_pos+1,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
#         w3y = 0.5/h*(f[x_pos+1,y_pos-3,k]+f[x_pos-1,y_pos-3,k]-f[x_pos+1,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
#         v3y = max(0,v3y)
#         w3y = max(0,w3y)
#         P_3 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v3y + la*h*ro*w3y
#         if x_pos == 1: #pojok kiri atas
#             P_1 = 0
#             P_4 = 0
#             v2x = 0.5/h*(c[x_pos+3,y_pos+1,k]-c[x_pos+1,y_pos+1,k]+c[x_pos+3,y_pos-1,k]-c[x_pos+1,y_pos-1,k])
#             w2x = 0.5/h*(f[x_pos+3,y_pos+1,k]-f[x_pos+1,y_pos+1,k]+f[x_pos+3,y_pos-1,k]-f[x_pos+1,y_pos-1,k])
#             v2x = max(0,v2x)
#             w2x = max(0,w2x)
#             P_2 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v2x + la*h*ro*w2x
#         elif x_pos == Nx-1: #pojok kanan atas
#             P_2 = 0
#             P_4 = 0
#             v1x = 0.5/h*(c[x_pos-3,y_pos+1,k]-c[x_pos-1,y_pos+1,k]+c[x_pos-3,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
#             w1x = 0.5/h*(f[x_pos-3,y_pos+1,k]-f[x_pos-1,y_pos+1,k]+f[x_pos-3,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
#             v1x = max(0,v1x)
#             w1x = max(0,w1x)
#             P_1 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v1x + la*h*ro*w1x
#         else: #batas atas selain pojok
#             P_4 = 0
#             v1x = 0.5/h*(c[x_pos-3,y_pos+1,k]-c[x_pos-1,y_pos+1,k]+c[x_pos-3,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
#             w1x = 0.5/h*(f[x_pos-3,y_pos+1,k]-f[x_pos-1,y_pos+1,k]+f[x_pos-3,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
#             v1x = max(0,v1x)
#             w1x = max(0,w1x)
#             P_1 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v1x + la*h*ro*w1x
#             v2x = 0.5/h*(c[x_pos+3,y_pos+1,k]-c[x_pos+1,y_pos+1,k]+c[x_pos+3,y_pos-1,k]-c[x_pos+1,y_pos-1,k])
#             w2x = 0.5/h*(f[x_pos+3,y_pos+1,k]-f[x_pos+1,y_pos+1,k]+f[x_pos+3,y_pos-1,k]-f[x_pos+1,y_pos-1,k])
#             v2x = max(0,v2x)
#             w2x = max(0,w2x)
#             P_2 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v2x + la*h*ro*w2x
#     else: #selain batas bawah dan atas
#         v3y = 0.5/h*(c[x_pos+1,y_pos-3,k]+c[x_pos-1,y_pos-3,k]-c[x_pos+1,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
#         w3y = 0.5/h*(f[x_pos+1,y_pos-3,k]+f[x_pos-1,y_pos-3,k]-f[x_pos+1,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
#         v3y = max(0,v3y)
#         w3y = max(0,w3y)
#         P_3 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v3y + la*h*ro*w3y
#         v4y = 0.5/h*(c[x_pos+1,y_pos+3,k]+c[x_pos-1,y_pos+3,k]-c[x_pos+1,y_pos+1,k]-c[x_pos-1,y_pos+1,k])
#         w4y = 0.5/h*(f[x_pos+1,y_pos+3,k]+f[x_pos-1,y_pos+3,k]-f[x_pos+1,y_pos+1,k]-f[x_pos-1,y_pos+1,k])
#         v4y = max(0,v4y)
#         w4y = max(0,w4y)
#         P_4 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v4y + la*h*ro*w4y
#         if x_pos == 1: #batas kiri selain pojok
#             P_1 = 0
#             v2x = 0.5/h*(c[x_pos+3,y_pos+1,k]-c[x_pos+1,y_pos+1,k]+c[x_pos+3,y_pos-1,k]-c[x_pos+1,y_pos-1,k])
#             w2x = 0.5/h*(f[x_pos+3,y_pos+1,k]-f[x_pos+1,y_pos+1,k]+f[x_pos+3,y_pos-1,k]-f[x_pos+1,y_pos-1,k])
#             v2x = max(0,v2x)
#             w2x = max(0,w2x)
#             P_2 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v2x + la*h*ro*w2x
#         elif x_pos == Nx-1: #batas kanan selain pojok
#             P_2 = 0
#             v1x = 0.5/h*(c[x_pos-3,y_pos+1,k]-c[x_pos-1,y_pos+1,k]+c[x_pos-3,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
#             w1x = 0.5/h*(f[x_pos-3,y_pos+1,k]-f[x_pos-1,y_pos+1,k]+f[x_pos-3,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
#             v1x = max(0,v1x)
#             w1x = max(0,w1x)
#             P_1 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v1x + la*h*ro*w1x
#         #selain batas2, tetap pada nilai P_1 ~ P_4 awal saja
#         else:
#             v1x = 0.5/h*(c[x_pos-3,y_pos+1,k]-c[x_pos-1,y_pos+1,k]+c[x_pos-3,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
#             w1x = 0.5/h*(f[x_pos-3,y_pos+1,k]-f[x_pos-1,y_pos+1,k]+f[x_pos-3,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
#             v1x = max(0,v1x)
#             w1x = max(0,w1x)
#             P_1 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v1x + la*h*ro*w1x
#             v2x = 0.5/h*(c[x_pos+3,y_pos+1,k]-c[x_pos+1,y_pos+1,k]+c[x_pos+3,y_pos-1,k]-c[x_pos+1,y_pos-1,k])
#             w2x = 0.5/h*(f[x_pos+3,y_pos+1,k]-f[x_pos+1,y_pos+1,k]+f[x_pos+3,y_pos-1,k]-f[x_pos+1,y_pos-1,k])
#             v2x = max(0,v2x)
#             w2x = max(0,w2x)
#             P_2 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v2x + la*h*ro*w2x
#             v3y = 0.5/h*(c[x_pos+1,y_pos-3,k]+c[x_pos-1,y_pos-3,k]-c[x_pos+1,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
#             w3y = 0.5/h*(f[x_pos+1,y_pos-3,k]+f[x_pos-1,y_pos-3,k]-f[x_pos+1,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
#             v3y = max(0,v3y)
#             w3y = max(0,w3y)
#             P_3 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v3y + la*h*ro*w3y
#             v4y = 0.5/h*(c[x_pos+1,y_pos+3,k]+c[x_pos-1,y_pos+3,k]-c[x_pos+1,y_pos+1,k]-c[x_pos-1,y_pos+1,k])
#             w4y = 0.5/h*(f[x_pos+1,y_pos+3,k]+f[x_pos-1,y_pos+3,k]-f[x_pos+1,y_pos+1,k]-f[x_pos-1,y_pos+1,k])
#             v4y = max(0,v4y)
#             w4y = max(0,w4y)
#             P_4 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*v4y + la*h*ro*w4y
#     '''Other way'''
    
#     '''tes saja'''
#     P_1 = 0.15# P_1#*100
#     P_2 = 0.15#P_2#*100
#     P_3 = 0.15#P_3#*100
#     P_4 = 0.15#P_4#*100
#     if y_pos == 1: #batas bawah
#         if x_pos == 1: #pojok kiri bawah
#             P_1 = 0
#             P_3 = 0
#         elif x_pos == Nx-1: #pojok kanan bawah
#             P_2 = 0
#             P_3 = 0
#         else: #batas bawah selain pojok
#             P_3 = 0
#     elif y_pos == Ny-1: #batas atas
#         if x_pos == 1: #pojok kiri atas
#             P_1 = 0
#             P_4 = 0
#         elif x_pos == Nx-1: #pojok kanan atas
#             P_2 = 0
#             P_4 = 0
#         else: #batas atas selain pojok
#             P_4 = 0
#     else: #selain batas bawah dan atas
#         if x_pos == 1: #batas kiri selain pojok
#             P_1 = 0
#         elif x_pos == Nx-1: #batas kanan selain pojok
#             P_2 = 0
#         #selain batas2, tetap pada nilai P_1 ~ P_4 awal saja
#         else:
#             lop = 1
#     '''tes saja'''
    
    P_0 = 1-(P_1+P_2+P_3+P_4)
    R_0 = P_0
    R_1 = P_0+P_1
    R_2 = P_0+P_1+P_2
    R_3 = P_0+P_1+P_2+P_3
    R_4 = 1
    
    prob_range = [R_0,R_1,R_2,R_3,R_4]
#     print P_0, ',',P_1,',',P_2,',',P_3,',',P_4
    return prob_range;