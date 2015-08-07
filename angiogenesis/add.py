path=[[]]
path[0]=[0,0]
path.append([1,1])
path[1,0]=path[1,0]+path[0,0]
"""discrete at ix=2"""
                    if ix==2:
                        path
                        Z = P_0+P_1+P_2+P_3+P_4
                        Q_0 = P_0/Z
                        Q_1 = P_1/Z
                        Q_2 = P_2/Z
                        Q_3 = P_3/Z
                        Q_4 = P_4/Z
                        R0 = 0
                        R1 = Q_0
                        R2 = Q_0+Q_1
                        R3 = Q_0+Q_1+Q_2
                        R4 = Q_0+Q_1+Q_2+Q_3
                        R5 = Q_0+Q_1+Q_2+Q_3+Q_4
                        import random
                        w = random.randint(0, 1)
                        if w<=R1:
                            move = 4

import numpy as np
t2=np.linspace(0,5,500)
print type(t2)
print t2
quit()