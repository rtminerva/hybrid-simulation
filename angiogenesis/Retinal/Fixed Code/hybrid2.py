def hybrid_tech_m(coef, set, sol, h2):
    mo = sol['m'][:]
    for yb in range(1,set['Ny'],2):
        for xb in range(1,set['Nx'],2):
            #print mo[xb,yb]
            if mo[xb,yb] == 1 and not [xb,yb] in sol['index_mn']:
                #print mo[xb,yb]
                dirr = movement_dir(x_pos = xb, y_pos = yb, cc = p_o, mm = m, #ff = fake,
                                    tep = tp, h1 = h2, R_min = r_min, error = Error,
                                    d_n1 = d_m, ki_n1 = ki_m, al_n1 = al_m, #ro1 = ro_m, 
                                    n_x = set['Nx'], n_y = set['Ny'], Matrix_tip = matrix_tip, n_dir = False)
                dirr_m = [dirr[0],dirr[0]+dirr[1],dirr[0]+dirr[1]+dirr[2],dirr[0]+dirr[1]+dirr[2]+dirr[3],1]
                #print dirr
                trial = random.uniform(0,1)
                if trial <= dirr_sol['m'][0]: #stay
                    lop = 1
                    #print 'STAY'
                    #do nothing
                elif trial <= dirr_sol['m'][1]: #left
                    #print 'LEFT'
                    #print sol['m'][xb,yb]
                    #index_sol['m'][dot][0] = xb - 2
                    sol['m'][xb - 2, yb] = 1
                    sol['m'][xb,yb] = 0
                    #print sol['m'][xb,yb]
                    #print sol['m'][xb - 2, yb]
                elif trial <= dirr_sol['m'][2]: #right
                    #print 'RIGHT'
                    #print sol['m'][xb,yb]
                    #index_sol['m'][dot][0] = xb + 2
                    sol['m'][xb + 2, yb] = 1
                    sol['m'][xb,yb] = 0
                    #print sol['m'][xb,yb]
                    #print sol['m'][xb + 2, yb]
                elif trial <= dirr_sol['m'][3]: #down
                    #print 'DOWN'
                    #print sol['m'][xb,yb]
                    #index_sol['m'][dot][1] = yb - 2
                    sol['m'][xb, yb - 2] = 1
                    sol['m'][xb,yb] = 0
                    #print sol['m'][xb,yb]
                   # print sol['m'][xb, yb - 2]
                else: #>dirr[3] #up
                    #print 'UP'
                    #print sol['m'][xb,yb]
                    #index_sol['m'][dot][1] = yb + 2
                    sol['m'][xb, yb + 2] = 1
                    sol['m'][xb,yb] = 0
                    #print sol['m'][xb,yb]
                    #print sol['m'][xb, yb + 2]
                for ec_i in range(0,len(matrix_tip)):
                    if (xb,yb) in matrix_tip[ec_i]:
                        index_mn.append([xb,yb])
