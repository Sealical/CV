import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from LucasKanade import LucasKanade
import cv2
import math

# write your script here, we recommend the above libraries for making your animation

parser = argparse.ArgumentParser()
parser.add_argument('--num_iters', type=int, default=1e4, help='number of iterations of Lucas-Kanade')
parser.add_argument('--threshold', type=float, default=5e-2, help='dp threshold of Lucas-Kanade for terminating optimization')
args = parser.parse_args()
num_iters = args.num_iters
threshold = args.threshold

seq = np.load("../data/carseq.npy")
rect = [59, 116, 145, 151]
carseqrects = np.zeros((seq.shape[2],4))
# frame_0 = seq[:,:,0]

fig = plt.figure()
for i in range (1,seq.shape[2]):
    # print(i)
    frame_0 = seq[:,:,i-1]
    frame_1 = seq[:,:,i]

    result = LucasKanade(frame_0,frame_1,rect,threshold,num_iters, p0 = np.zeros(2))
    #plot the result
    rect = [rect[0] + result[0], rect[1] + result[1], rect[2] + result[0], rect[3] + result[1]]
    plt.imshow(frame_1,cmap = 'gray')
    plt.axis('off')
    plt.axis('tight')
    patch = patches.Rectangle((rect[0], rect[1]), rect[2] - rect[0] , rect[3] - rect[1] ,linewidth=1,edgecolor='r',facecolor='none')
    ax = plt.gca()
    ax.add_patch(patch)
    #visualizing the result
    plt.show(block=False)
    plt.pause(0.2)

    # plt.close()
    # if i == 1 or i==100 or i==200 or i ==300 or i ==400:
    #     fig.savefig('../result/carseq_frame' + str(i) + '.png',bbox_inches = 'tight')

    #save a .npy file storing a N(frame no.) x 4 matrix
    # carseqrects[i,:] = np.array([rect[0], rect[1], rect[2], rect[3]])
    ax.clear()
np.save('../result/carseqrects.npy',carseqrects)
