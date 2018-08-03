from PIL import Image
import random
import math


def generate_voronoi_diagram(width, height, num_cells):
    image = Image.new("RGB", (width, height))
    putpixel = image.putpixel
    imgx, imgy = image.size
    nx = []
    ny = []
    nr = []
    ng = []
    nb = []
    for i in range(num_cells):
        nx.append(random.randrange(imgx))
        ny.append(random.randrange(imgy))
        nr.append(random.randrange(256))
        ng.append(random.randrange(256))
        nb.append(random.randrange(256))
    for y in range(imgy):
        for x in range(imgx):
            dmin = math.hypot(imgx - 1, imgy - 1)
            j = -1
            for i in range(num_cells):
                d = math.hypot(nx[i] - x, ny[i] - y)
                if d < dmin:
                    dmin = d
                    j = i
            putpixel((x, y), (nr[j], ng[j], nb[j]))
    image.save("VoronoiDiagram.png", "PNG")
    image.show()


generate_voronoi_diagram(500, 500, 25)

#
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.collections import PatchCollection
# from matplotlib.patches import Rectangle
#
# # Number of data points
# n = 5
#
# # Dummy data
# np.random.seed(19680801)
# x = np.arange(0, n, 1)
# y = np.random.rand(n) * 5.
#
# # Dummy errors (above and below)
# xerr = np.random.rand(2, n) + 0.1
# yerr = np.random.rand(2, n) + 0.2
#
#
# def make_error_boxes(ax, xdata, ydata, xerror, yerror, facecolor='r',
#                      edgecolor='None', alpha=0.5):
#
#     # Create list for all the error patches
#     errorboxes = []
#
#     # Loop over data points; create box from errors at each point
#     for x, y, xe, ye in zip(xdata, ydata, xerror.T, yerror.T):
#         rect = Rectangle((x - xe[0], y - ye[0]), xe.sum(), ye.sum())
#         errorboxes.append(rect)
#
#     # Create patch collection with specified colour/alpha
#     pc = PatchCollection(errorboxes, facecolor=facecolor, alpha=alpha,
#                          edgecolor=edgecolor)
#
#     # Add collection to axes
#     ax.add_collection(pc)
#
#     # Plot errorbars
#     artists = ax.errorbar(xdata, ydata, xerr=xerror, yerr=yerror,
#                           fmt='None', ecolor='k')
#
#     return artists
#
#
# # Create figure and axes
# fig, ax = plt.subplots(1)
#
# # Call function to create error boxes
# _ = make_error_boxes(ax, x, y, xerr, yerr)
#
# plt.show()