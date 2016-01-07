import time
import numpy as np
import matplotlib.pyplot as plt

rootdir='C:\documents'
fileNameTemplate = "C:\documents\Plot-" + "_".join(os.path.split(os.path.join(subdir,file))) + ".png"
fig = plt.figure(2)
ax = fig.add_subplot(111)
plt.axis([0, 1000, 0, 1])
plt.ion()
plt.show()

for i in range(5):
    y = np.random.random()
    ax.scatter(i, y)
    plt.draw()
    time.sleep(0.05)
    for subdir,dirs,files in os.walk(rootdir):
    for count, file in enumerate(files):
        # Generate a plot in `pl`
        pl.savefig(fileNameTemplate.format(count), format='png')
        pl.clf()  # Clear the figure for the next loop
    f.close()
# raw_input()