import fipy
nx = 10
Lx = 1.
dx = Lx/nx
mesh = fipy.Grid1D(nx=nx, Lx=Lx)
n = fipy.CellVariable(name="density of EC", mesh=mesh, hasOld=True)
c = fipy.CellVariable(name="concentration of TAF", mesh=mesh, hasOld=True)

"""Initial Value"""
n.value[nx-1] = 1
for i in range(nx):
    c.value[i] = 1-i*dx

"""Boundary Conditions"""
n.constrain(1, where=mesh.facesRight)
n.constrain(0, where=mesh.facesLeft)

c.constrain(0, where=mesh.facesRight)
c.constrain(1, where=mesh.facesLeft)

si = fipy.Viewer((n, c))
si.plot()

"""equation"""
D = 0.00035
Ki = 0.38
A = 0.1
eqn0 = fipy.TransientTerm(var=n)==fipy.DiffusionTerm(D,var=n)+fipy.DiffusionTerm(1,var=c)
print eqn0
quit()

eqn0 = fipy.TransientTerm(var=n)==fipy.DiffusionTerm(D,var=n)-(Ki/(1+A+c))*fipy.ConvectionTerm(1,var=c)*fipy.ConvectionTerm(1,var=n)+(Ki*(Ki-A)/(1+A*c)**2)*fipy.Diffusionterm(1,var=c)
print eqn0