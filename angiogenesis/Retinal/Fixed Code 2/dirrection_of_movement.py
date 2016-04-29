def p_ijx(coef,set,sol,xb,yb):
    f = coef['Ki_n']/(1+coef['Al_n']*sol['c'][xb,yb])*(sol['c'][xb,yb]-sol['c'][xb-1,yb])/set['h'] +coef['Ro']*(sol['f'][xb,yb]-sol['f'][xb-1,yb])/set['h']
    return f

def p_ijy(coef,set,sol,xb,yb):
    f = coef['Ki_n']/(1+coef['Al_n']*sol['c'][xb,yb])*(sol['c'][xb,yb]-sol['c'][xb,yb-1])/set['h'] +coef['Ro']*(sol['f'][xb,yb]-sol['f'][xb,yb-1])/set['h']
    return f

def p_iplus1jx(coef,set,sol,xb,yb):
    f = coef['Ki_n']/(1+coef['Al_n']*sol['c'][xb+1,yb])*(sol['c'][xb+1,yb]-sol['c'][xb,yb])/set['h'] +coef['Ro']*(sol['f'][xb+1,yb]-sol['f'][xb,yb])/set['h']
    return f

def p_ijplus1y(coef,set,sol,xb,yb):
    f = coef['Ki_n']/(1+coef['Al_n']*sol['c'][xb,yb+1])*(sol['c'][xb,yb+1]-sol['c'][xb,yb])/set['h'] +coef['Ro']*(sol['f'][xb,yb+1]-sol['f'][xb,yb])/set['h']
    return f

def movement_dir(coef, set, sol, xb, yb, nom, n_dir = True):
    ml = 'f'
    mr = 'f'
    md = 'f'
    mu = 'f'
    la = sol['tp']/set['h']
    
    '''
    Area2|Area1
    -----------
    Area3|Area4
    
    '''
    
    if n_dir == True:
        if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
            aa = coef['Al_n']
            coef['Al_n'] = coef['Al_n']/(1+coef['Mic']*sol['m'][xb,yb])
            bb = coef['Ro']
            coef['Ro'] = coef['Ro'] + coef['Kappa']*sol['m'][xb,yb]
        
        r_f = (xb*set['h']-set['O_x'])**2 + (yb*set['h']-set['O_y'])**2
        if r_f <= (set['R_min']**2 + set['error']):
            if xb >= sol['matrix_tip'][2][0][0] and yb >= sol['matrix_tip'][0][0][1]: #area 1 
                P_1 = 0
                P_3 = 0
                P_2 = la*coef['D_n']/set['h']+la*max(0,p_iplus1jx(coef,set,sol,xb,yb))
                P_4 = la*coef['D_n']/set['h']+la*max(0,p_ijplus1y(coef,set,sol,xb,yb))
                
            elif xb < sol['matrix_tip'][2][0][0] and yb > sol['matrix_tip'][0][0][1]: #area 2
                P_2 = 0
                P_3 = 0
                P_1 = la*coef['D_n']/set['h']+la*max(0,-p_ijx(coef,set,sol,xb,yb))
                P_4 = la*coef['D_n']/set['h']+la*max(0,p_ijplus1y(coef,set,sol,xb,yb))
        
            elif xb <= sol['matrix_tip'][2][0][0] and yb <= sol['matrix_tip'][0][0][1]: #area 3
                P_2 = 0
                P_4 = 0
                P_1 = la*coef['D_n']/set['h']+la*max(0,-p_ijx(coef,set,sol,xb,yb))       
                P_3 = la*coef['D_n']/set['h']+la*max(0,-p_ijy(coef,set,sol,xb,yb))
                
            elif xb > sol['matrix_tip'][2][0][0] and yb < sol['matrix_tip'][0][0][1]: #area 4
                P_1 = 0
                P_4 = 0
                P_2 = la*coef['D_n']/set['h']+la*max(0,p_iplus1jx(coef,set,sol,xb,yb))
                P_3 = la*coef['D_n']/set['h']+la*max(0,-p_ijy(coef,set,sol,xb,yb))
                
                                    
        elif yb == 0: #diluar lingkaran kecil
            if xb == 0:
                P_1 = 0
                P_3 = 0
                P_2 = la*coef['D_n']/set['h']+la*max(0,p_iplus1jx(coef,set,sol,xb,yb))
                P_4 = la*coef['D_n']/set['h']+la*max(0,p_ijplus1y(coef,set,sol,xb,yb))
                
            elif xb == set['Nx']:
                P_2 = 0
                P_3 = 0
                P_1 = la*coef['D_n']/set['h']+la*max(0,-p_ijx(coef,set,sol,xb,yb))
                P_4 = la*coef['D_n']/set['h']+la*max(0,p_ijplus1y(coef,set,sol,xb,yb))
                
            else:
                P_3 = 0
                P_1 = la*coef['D_n']/set['h']+la*max(0,-p_ijx(coef,set,sol,xb,yb))
                P_2 = la*coef['D_n']/set['h']+la*max(0,p_iplus1jx(coef,set,sol,xb,yb))
                P_4 = la*coef['D_n']/set['h']+la*max(0,p_ijplus1y(coef,set,sol,xb,yb))
                
        elif yb == set['Ny']:
            if xb == 0:
                P_1 = 0
                P_4 = 0
                P_2 = la*coef['D_n']/set['h']+la*max(0,p_iplus1jx(coef,set,sol,xb,yb))
                P_3 = la*coef['D_n']/set['h']+la*max(0,-p_ijy(coef,set,sol,xb,yb))
                
            elif xb == set['Nx']:
                P_2 = 0
                P_4 = 0
                P_1 = la*coef['D_n']/set['h']+la*max(0,-p_ijx(coef,set,sol,xb,yb))       
                P_3 = la*coef['D_n']/set['h']+la*max(0,-p_ijy(coef,set,sol,xb,yb))
                
            else:
                P_4 = 0
                P_1 = la*coef['D_n']/set['h']+la*max(0,-p_ijx(coef,set,sol,xb,yb)) 
                P_2 = la*coef['D_n']/set['h']+la*max(0,p_iplus1jx(coef,set,sol,xb,yb))      
                P_3 = la*coef['D_n']/set['h']+la*max(0,-p_ijy(coef,set,sol,xb,yb))
                
        else:
            if xb == 0:
                P_1 = 0
                P_2 = la*coef['D_n']/set['h']+la*max(0,p_iplus1jx(coef,set,sol,xb,yb))      
                P_3 = la*coef['D_n']/set['h']+la*max(0,-p_ijy(coef,set,sol,xb,yb))
                P_4 = la*coef['D_n']/set['h']+la*max(0,p_ijplus1y(coef,set,sol,xb,yb))
                
            elif xb == set['Nx']:
                P_2 = 0
                P_1 = la*coef['D_n']/set['h']+la*max(0,-p_ijx(coef,set,sol,xb,yb)) 
                P_3 = la*coef['D_n']/set['h']+la*max(0,-p_ijy(coef,set,sol,xb,yb))
                P_4 = la*coef['D_n']/set['h']+la*max(0,p_ijplus1y(coef,set,sol,xb,yb))
                
            else:
                P_1 = la*coef['D_n']/set['h']+la*max(0,-p_ijx(coef,set,sol,xb,yb)) 
                P_2 = la*coef['D_n']/set['h']+la*max(0,p_iplus1jx(coef,set,sol,xb,yb))
                P_3 = la*coef['D_n']/set['h']+la*max(0,-p_ijy(coef,set,sol,xb,yb))
                P_4 = la*coef['D_n']/set['h']+la*max(0,p_ijplus1y(coef,set,sol,xb,yb))
        
        P_0 = 1-(P_1 + P_2 + P_3 + P_4)
        if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
            coef['Al_n'] = aa
            coef['Ro'] = bb
    else:
        aa = 0
    
    if P_1 < 0 or P_2 < 0 or P_3 < 0 or P_4 < 0:
        print 'ADA P yang Negative'
#     RR = P_0 + P_1 + P_2 + P_3 + P_4
#     
#     P_0 = P_0/RR
#     P_1 = P_1/RR
#     P_2 = P_2/RR
#     P_3 = P_3/RR
#     P_4 = P_4/RR
    
    '''Boundary on the inner circle'''
    
    '''Checking space for n'''
    lx = xb - 1
    rx = xb + 1
        
    dy = yb - 1
    uy = yb + 1
    if n_dir == True:
        for tep in range(0,len(sol['matrix_tip'])):
            if not tep == nom:
               # if (lx,yb) in sol['matrix_tip'][tep] and (rx,yb) in sol['matrix_tip'][tep] and (xb,dy) in sol['matrix_tip'][tep] and (xb,uy) in sol['matrix_tip'][tep]:
               #     move = 'stop'
                if (lx,yb) in sol['matrix_tip'][tep]:
                    ml = 'stop'
                if (rx,yb) in sol['matrix_tip'][tep]:
                    mr = 'stop'
                if (xb,dy) in sol['matrix_tip'][tep]:
                    md = 'stop'
                if (xb,uy) in sol['matrix_tip'][tep]:
                    mu = 'stop'
        
    if not n_dir == True:
        '''Checking space for m'''
        if not P_1 == 0:
            if sol['m'][lx,yb] == 1:
                P_1 = 0
        if not P_2 == 0:
            if sol['m'][rx,yb] == 1:
                P_2 = 0
        if not P_3 == 0:
            if sol['m'][xb,dy] == 1:
                P_3 = 0
        if not P_4 == 0:
            if sol['m'][xb,uy] == 1:
                P_4 = 0          
    
    prob_range = [P_0,P_1,P_2,P_3,P_4,ml,mr,md,mu]
#     print 'probability P', P_0, ',',P_1,',',P_2,',',P_3,',',P_4
    return prob_range;
