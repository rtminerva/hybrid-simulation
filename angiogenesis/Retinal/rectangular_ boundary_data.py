elif y_pos == 1: #batas bawah
        P_3 = 0
        if x_pos == 1: #pojok kiri bawah
            P_1 = 0
        elif x_pos == n_x-1: #pojok kanan bawah
            P_2 = 0
    elif y_pos == n_x-1: #batas atas
        P_4 = 0
        if x_pos == 1: #pojok kiri atas
            P_1 = 0
        elif x_pos == n_x-1: #pojok kanan atas
            P_2 = 0
    else: #selain batas bawah dan atas
        if x_pos == 1: #batas kiri selain pojok
            P_1 = 0
        elif x_pos == n_x-1: #batas kanan selain pojok
            P_2 = 0
        #selain batas2, tetap pada nilai P_1 ~ P_4 awal saja





***********************************************************




            elif y == 0:
                if x == 0:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[1,1])
                    f[x,y] = f_o[x,y] + tp*be*n[1,1] - tp*ga*f_o[x,y]*mm_o[x,y]
                elif x == Nx:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[Nx-1,1])
                    f[x,y] = f_o[x,y] + tp*be*n[Nx-1,1] - tp*ga*f_o[x,y]*mm_o[x,y]
                else:
                    if n[x+1,1] == 1 or n[x-1,1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*mm_o[x,y]
            elif y == Ny:
                if x == 0:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[1,Ny-1])
                    f[x,y] = f_o[x,y] + tp*be*n[1,Ny-1] - tp*ga*f_o[x,y]*mm_o[x,y]
                elif x == Nx:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[Nx-1,Ny-1])
                    f[x,y] = f_o[x,y] + tp*be*n[Nx-1,Ny-1] - tp*ga*f_o[x,y]*mm_o[x,y] 
                else:
                    if n[x+1,Ny-1] == 1 or n[x-1,Ny-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*mm_o[x,y]
            else:
                if x == 0:
                    if n[x+1,y+1] == 1 or n[x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*mm_o[x,y]
                elif x == Nx:
                    if n[x-1,y+1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*mm_o[x,y]
                else:
                    if n[x+1,y+1] == 1 or n[x-1,y+1] == 1 or n[x+1,y-1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*mm_o[x,y]