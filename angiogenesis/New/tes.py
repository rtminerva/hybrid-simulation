import numpy as np
a = []
a.append(np.array([1,2,3,4]))
a.append(np.array([1,2,3,4,5]))
a.append(np.array([1,2,3,4,5,6]))
a.append(np.array([1,2,3,4,5,6,7]))
a.append(np.array([1,2,3,4,5,6,7,8]))
a.append(np.array([1,2,3,4,5,6,7]))
a.append(np.array([1,2,3,4,5,6]))
a.append(np.array([1,2,3,4,5]))
a.append(np.array([1,2,3,4]))

Q = np.array([1,2,3,4,5,6,7,8])
s = (len(a)-1)/2 #s=2 #index vector diagonal 
                 #number of pivot for each process
                 #number of elimination
s1 = len(a[s])-1 #s1=3 number of process
j = 0
ii = 0
jk = False


for i in range(0,s1): #range sampai (Nx/2)**2-Nx/2
    if jk == True: #kalau pivot sudah masuk vector akhir
        print 'proses ke', i
        ii += 1
        for j in range(0,s-ii):
            print
            print 'pivot ke', j, 'diambil dari element', s+j+1, i, 'dibagi', s,i
            p = a[s+j+1][i]/a[s][i]
            a[s+j+1][i] = 0
            print 'Q eliminasi untuk element', i+j+1, 'dikurang p*elemen',i
            Q[i+j+1] = Q[i+j+1]-p*Q[i]
            for u in range(1,s+1-ii):
                if j+1-u < 0: #untuk lebih dari diagonal 
                    print 'elmininasI ke', u, 'untuk element', s+j+1-u, jj, 'dikurang p*elemen', s-u, i
                    a[s+j+1-u][jj] = a[s+j+1-u][jj]-p*a[s-u][i]
                else:
                    jj = i+u
                    print 'elmininasi ke', u, 'untuk element', s+j+1-u, i+u, 'dikurang p*elemen', s-u, i
                    a[s+j+1-u][i+u] = a[s+j+1-u][i+u]-p*a[s-u][i]
        print
    else: #normal process
        print 'proses ke', i
        for j in range(0,s):
            print
            print 'pivot ke', j, 'diambil dari element', s+j+1, i, 'dibagi', s,i
            p = a[s+j+1][i]/a[s][i]
            a[s+j+1][i] = 0
            print 'Q eliminasi untuk element', i+j+1, 'dikurang p*elemen',i
            Q[i+j+1] = Q[i+j+1]-p*Q[i]
            for u in range(1,s+1):
                if j+1-u < 0: #untuk lebih dari diagonal 
                    print 'elmininasI ke', u, 'untuk element', s+j+1-u, jj, 'dikurang p*elemen', s-u, i
                    a[s+j+1-u][jj] = a[s+j+1-u][jj]-p*a[s-u][i]
                else:
                    jj = i+u
                    print 'elmininasi ke', u, 'untuk element', s+j+1-u, i+u, 'dikurang p*elemen', s-u, i
                    a[s+j+1-u][i+u] = a[s+j+1-u][i+u]-p*a[s-u][i]
        print   
        if s+j+1 == len(a)-1 and i == len(a[-1])-1:
            jk = True


#     for i in range(Nx/2,(Nx/2)**2-Nx/2): # 5 - 19
#         if i%5 == 0: # 5,10,15
#             vector_left.append(numpy.zeros(Nx+1))
#             vector_left[-1][0] = D_left[i-Nx/2]
#             vector_left[-1][Nx/2] = B_left[i]
#             vector_left[-1][Nx/2+1] = C_left[i]
#             vector_left[-1][Nx] = E_left[i]
#         elif (i+1)%5 == 0: #9,14,19
#             vector_left.append(numpy.zeros(Nx+1))
#             vector_left[-1][0] = D_left[i-Nx/2]
#             vector_left[-1][Nx/2-1] = A_left[i-1]
#             vector_left[-1][Nx/2] = B_left[i]
#             vector_left[-1][Nx] = E_left[i]
#         else: #6,7,8,  11,12,13,  16,17,18
#             vector_left.append(numpy.zeros(Nx+1))
#             vector_left[-1][0] = D_left[i-Nx/2]
#             vector_left[-1][Nx/2-1] = A_left[i-1]
#             vector_left[-1][Nx/2] = B_left[i]
#             vector_left[-1][Nx/2+1] = C_left[i]
#             vector_left[-1][Nx] = E_left[i]

#     '''Matrix Kiri dibuat vector per baris saja'''
#     vector_left = [] #(Nx/2)**2
#     for i in range(0,Nx/2): # 0 - 4
#         if i == 0:
#             vector_left.append(numpy.zeros(Nx/2+1))
#             vector_left[0][0] = B_left[0]
#             vector_left[0][1] = C_left[0]
#             vector_left[0][Nx/2] = E_left[0]        
#         else: #i > 0 and i <= Nx/2-1
#             vector_left.append(numpy.zeros(Nx/2+2))
#             vector_left[-1][0] = A_left[i-1]
#             vector_left[-1][1] = B_left[i]
#             vector_left[-1][2] = C_left[i]
#             vector_left[-1][Nx/2+1] = E_left[i]
#     
#     
#     for i in range(Nx/2,(Nx/2)**2-Nx/2): # 5 - 19
#         vector_left.append(numpy.zeros(Nx+1))
#         vector_left[-1][0] = D_left[i-Nx/2]
#         vector_left[-1][Nx/2-1] = A_left[i-1]
#         vector_left[-1][Nx/2] = B_left[i]
#         vector_left[-1][Nx/2+1] = C_left[i]
#         vector_left[-1][Nx] = E_left[i]
#     
#     for i in range((Nx/2)**2-Nx/2,(Nx/2)**2-1): # 20 - 24
#         vector_left.append(numpy.zeros((i-(Nx/2)**2+Nx/2)*(-1)+Nx))
#         vector_left[-1][0] = D_left[i-Nx/2]
#         vector_left[-1][Nx/2-1] = A_left[i-1]
#         vector_left[-1][Nx/2] = B_left[i]
#         vector_left[-1][Nx/2+1] = C_left[i]
#     i = (Nx/2)**2-1
#     vector_left.append(numpy.zeros((i-(Nx/2)**2+Nx/2)*(-1)+Nx))
#     vector_left[-1][0] = D_left[i-Nx/2]
#     vector_left[-1][Nx/2-1] = A_left[i-1]
#     vector_left[-1][Nx/2] = B_left[i]
# 
#     '''Algoritma Untuk Menjadikan Matrix Segitiga Atas'''
#     for i in range(0, Nx/2):
#         if i == 0:
#             pivot_1 = vector_left[i+1][0]/vector_left[i][0]
#             for j in range(0,len(vector_left[i])):
#                 vector_left[i+1][j] = vector_left[i+1][j] - vector_left[i][j]*pivot_1
#             pivot_1 = vector_left[i+Nx/2][0]/vector_left[i][0]
#             for j in range(0,len(vector_left[i])):
#                 vector_left[i+Nx/2][j] = vector_left[i+Nx/2][j] - vector_left[i][j]*pivot_1
#         else:
#             pivot_1 = vector_left[i+1][0]/vector_left[i][1]
#             for j in range(0,len(vector_left[i])-1):
#                 vector_left[i+1][j] = vector_left[i+1][j] - vector_left[i][j+1]*pivot_1
#             
#             pivot_1 = vector_left[i+Nx/2][0]/vector_left[i][1]
#             for j in range(0,len(vector_left[i])-1):
#                 vector_left[i+Nx/2][j] = vector_left[i+Nx/2][j] - vector_left[i][j+1]*pivot_1
#     '''Algoritma Untuk Menjadikan Matrix Segitiga Atas''' #unfinished because too complicated        
               
    