import tes_run as tt
import numpy 
w = 1
r = [0,0]
while w <=3:
 r = tt.ff(iter = w, q = r[0], qr = r[1])
 w +=1