import numpy as np
import matplotlib.pyplot as plt
x,y = np.loadtxt('xy.txt', delimiter='\t', dtype=None, unpack=True)

print x[0:10]



# a = (f.read())
# xcoord = []
# ycoord = []
# n = len(a)
# for i in range(1,n):
#     coord = a[i].split()
#     print coord
#     if(i%2==0):
#         ycoord.insert(coord[2])
#     else:
#         xcoord.insert(coord[1])
# xcoord.insert('fin')
# ycoord.insert('end')

# print xcoord
# print ycoord

plt.plot(x, y)

plt.show()
