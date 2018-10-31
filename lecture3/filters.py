"""a little helper module
"""
__author__ = "Reed Essick <reedessick@kicp.uchicago.edu>"

#-------------------------------------------------

import numpy as np

#-------------------------------------------------

DEFAULT_ALPHA = 0.1

#-------------------------------------------------

def tukey(N, alpha=DEFAULT_ALPHA):
    """
    generate a tukey window
    The Tukey window, also known as the tapered cosine window, can be regarded as a cosine lobe of width \alpha * N / 2
        that is convolved with a rectangle window of width (1 - \alpha / 2). At \alpha = 1 it becomes rectangular, and
        at \alpha = 0 it becomes a Hann window.

    """
    # Special cases
    if alpha <= 0:
        return np.ones(N) #rectangular window
    elif alpha >= 1:
        return np.hanning(N)

    # Normal case
    x = np.linspace(0, 1, N)
    w = np.ones(x.shape)

    # first condition 0 <= x < alpha/2
    first_condition = x<alpha/2
    w[first_condition] = 0.5 * (1 + np.cos(2*np.pi/alpha * (x[first_condition] - alpha/2) ))

    # second condition already taken care of

    # third condition 1 - alpha / 2 <= x <= 1
    third_condition = x>=(1 - alpha/2)
    w[third_condition] = 0.5 * (1 + np.cos(2*np.pi/alpha * (x[third_condition] - 1 + alpha/2)))

    return w

def lowpass(f, fo, m):
    """return 1./(1+(f/fo)**m)
    """
    return 1./(1+(f/fo)**m)

def highpass(f, fo, m):
    """return (f/fo)**m/(1+(f/fo)**m)
    """
    return 1. - lowpass(f, fo, m) 
