#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Permet de tracer les graphes avec les critères du collège.

'''

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

def format_ax(ax):
    # Move the left and bottom spines to x = 0 and y = 0, respectively.
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    # Hide the top and right spines.
    ax.spines[["top", "right"]].set_visible(False)
    # Deal with negatives values of x and y by shifting 0 tick labels
    xlim = np.array(ax.get_xlim())
    ylim = np.array(ax.get_ylim())
    if not (ylim < 0).any():
        ax.spines.left.set_bounds((0, ax.get_ylim()[-1]))
    else:
        ticklabels = ax.get_xticklabels()
        tick_pos = ax.get_xticks()
        ticklabels[np.argwhere(tick_pos==0)[0][0]].set_ha("left")
    if not (xlim < 0).any():
        ax.spines.bottom.set_bounds((0, ax.get_xlim()[-1]))
    else:
        ticklabels = ax.get_yticklabels()
        tick_pos = ax.get_yticks()

        ticklabels[np.argwhere(tick_pos==0)[0][0]].set_va("bottom")
    #
    # Draw arrows (as black triangles: ">k"/"^k") at the end of the axes.  In each
    # case, one of the coordinates (0) is a data coordinate (i.e., y = 0 or x = 0,
    # respectively) and the other one (1) is an axes coordinate (i.e., at the very
    # right/top of the axes).  Also, disable clipping (clip_on=False) as the marker
    # actually spills out of the axes.
    #
    # Use 'markersize=' to change the arrow size.
    # You can also customized markers if you want to change the arrow shape: https://stackoverflow.com/questions/14324270/matplotlib-custom-marker-symbol
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    #
    # Shift axis labels to the tip of spines arrows
    pad = 0.02 # pad as a proportion ox the axis length
    ax.text(0, 1 + pad, ax.get_ylabel(), transform=ax.get_xaxis_transform(), ha='center', va='bottom')
    ax.text(1 + pad, 0, ax.get_xlabel(), transform=ax.get_yaxis_transform(), rotation=0, ha='left', va='center')
    ax.set_xlabel('')
    ax.set_ylabel('')

if __name__ == '__main__' :
    x = np.linspace(-10, 10, 100)
    y = pl.cos(x)

    for i in range(3):
        fix, ax = plt.subplots(1, 1, constrained_layout=True)
        ax.plot(x, y)
        ax.set_xlabel('Position [cm]')
        ax.set_ylabel('Vitesse [cm/s]')
        if i == 1:
            ax.set_xlim(left=0)
        if i ==2:
            ax.set_ylim(bottom=0)
        format_ax(ax)
    plt.show()
