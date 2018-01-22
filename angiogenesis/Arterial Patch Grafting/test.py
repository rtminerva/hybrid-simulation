import numpy as np
# cc = np. zeros((2,2,2))
cc = np.array([[[ 13,0,5],[5,0,7],[1,0,8]],[[99,0,1],[10,0,2],[11,0,16]],[[53,0,1],[3,0,55],[56,0,8]]])
cd = np.array([[[ 1,0,4],[44,0,77],[5,0,34]],[[99,0,1],[67,0,232],[11,0,13]],[[4,0,1],[4,0,6],[6,0,81]]])
# a = np.array([[1,2,3], [4,5,6]])
cc_1 = np.reshape(cc, 3**3) 
cd_1 = np.reshape(cd, 3**3)
cd_2 = np.diag(cd_1)
result = np.dot(cc_1,cd_2)

y = result * 100

g = cc_1 - y

g_1 = np.reshape(g,(3,3,3))


# c = np.reshape(b,(3,3,3))
# c = size(a)
# c = np.reshape(b,(2,-1))

# even_list = [e for x,e in enumerate(b) if e%2 != 0]
# d = np.asarray(even_list)
# d = np.reshape(even_list,(1,2,2))
print 'cc',cc
print
print 'cc_1',cc_1
print
print 'cd',cd
print 
print 'cd_1',cd_1
print
print 'cd_2',cd_2
print
print 'result',result
print
print 'y', y
print
print 'g', g
print
print 'g_1', g_1