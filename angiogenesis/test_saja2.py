import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1)
xs = np.array([0.01, 0.02, 0.02, 0.02, 0.03])
ys = np.array([1.6, 1.6,1.59 , 1.58, 1.58])

xs1 = np.array([0.03, 0.03, 0.04, 0.04, 0.05])
ys1 = np.array([1.59, 1.60, 1.60,1.59,1.59 ])
#xs = np.cos(np.linspace(0, 8 * np.pi, 200)) * np.linspace(0, 1, 200)
#ys = np.sin(np.linspace(0, 8 * np.pi, 200)) * np.linspace(0, 1, 200)
widths = np.round(np.array([10,10,5,4,2]))
widths1 = np.round(np.array([4,4,3,2,1]))
#widths = np.round(np.linspace(1, 5, len(xs)))


def plot_widths(xs, ys, widths, ax=None, color='r', xlim=None, ylim=None,
                **kwargs):
    if not (len(xs) == len(ys) == len(widths)):
        raise ValueError('xs, ys, and widths must have identical lengths')
    fig = None
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111)
#         fig, ax = plt.subplots(1)

    segmentx, segmenty = [xs[0]], [ys[0]]
    current_width = widths[0]
    for ii, (x, y, width) in enumerate(zip(xs, ys, widths)):
        segmentx.append(x)
        segmenty.append(y)
        if (width != current_width) or (ii == (len(xs) - 1)):
            w = ax.plot(segmentx, segmenty, linewidth=current_width, color=color,
                    **kwargs)
            segmentx, segmenty = [x], [y]
            current_width = width
#     if xlim is None:
#         xlim = [min(xs), max(xs)]
#     if ylim is None:
#         ylim = [min(ys), max(ys)]
#     ax.set_xlim(xlim)
#     ax.set_ylim(ylim)

    return w if fig is None else fig
plt.xlim(0,0.3)
plt.ylim(1.4,1.7)
plot_widths(xs, ys, widths)
plot_widths(xs1, ys1, widths1)
plt.show()



# '''TRIAL'''
# from pylab import *
# for i in range(1,num_sp+1):
#     globals()['xp%s' % i] =[]
#     globals()['yp%s' % i] =[]
#     for j in range(0,len(globals()['sp%s' % i])):
#         globals()['xp%s' % i].append(globals()['sp%s' % i][j][0]*hh)
#         globals()['yp%s' % i].append(globals()['sp%s' % i][j][1]*hh)
#         print 'tes', len(globals()['xp%s' % i])
#         print 'tes2', len(globals()['xp%s' % i])
#     for j in range(0,len(globals()['width_tip%s' % i])):
#         ssx = globals()['xp%s' % i][j]
#         ssy = globals()['yp%s' % i][j]
#         ssw = globals()['width_tip%s' % i][j]
#         plot(ssx, ssy,linewidth = ssw)
# plt.show()
# '''TRIAL'''